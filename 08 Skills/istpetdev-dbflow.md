---
tipo: skill
estado: vigente
actualizado: 2026-10-09
tags: [istpetdev, ia, skills, base-de-datos, postgresql, migraciones]
---

# IstpetDev — base de datos colaborativa y migraciones

**Cuándo usarla:** Trabajo colaborativo sobre PostgreSQL 16 y PostGIS 3.4 en Amazon RDS. Usar al crear o modificar entidades en C# (`src/Domain/Entities`), generar y aplicar migraciones de Entity Framework Core, conectarse mediante el túnel SSM con TLS VerifyFull, alternar entre el rol de aplicación (`user_dev_XX`) y el rol migrador (`migrator_dev_XX`), y resolver conflictos de concurrencia de esquema en Git.

> Documentación de la skill `istpetdev-dbflow`. El archivo `SKILL.md` no se versiona en la bóveda: quien quiera usarla con su asistente de IA copia este contenido a la carpeta de skills de su herramienta (frontmatter con `name: istpetdev-dbflow` y la descripción de arriba). Catálogo y origen en [[Catalogo y plan de skills]].

Rutas relativas a la raíz del repositorio de software `istpetdev-platform`. Leer antes [[istpetdev-contexto]] y [[istpetdev-datos]].

## Leer primero

- `04 Datos y algoritmos/Modelo de datos.md`: entidades, tipos canónicos, relaciones e invariantes ([[Modelo de datos]]).
- `00 Inicio/Hechos canonicos.md`: nombres en código, motor y convenciones canónicas ([[Hechos canonicos]]).
- `03 Arquitectura/AWS temporal para la hackathon y cierre.md`: infraestructura RDS dev, aislamiento y usuarios ([[AWS temporal para la hackathon y cierre]]).
- `docs/database-workflow.md` (en el repositorio de software): guía operativa detallada paso a paso.
- `docs/onboarding.md` (en el repositorio de software): configuración de estación de trabajo y comandos locales.
- `04 Datos y algoritmos/Esquema completo de base de datos.md`: diseño objetivo, organización/FKs/políticas RLS y migraciones de transición; `03 Arquitectura/Conexion PostgreSQL en DBeaver.md` para las dos conexiones.

## Hechos que no se cambian sin decisión

- **Motor y hosting:** PostgreSQL 16.13 con extensión PostGIS 3.4 en Amazon RDS (`istpetdev-rds-dev`). Ubicado en subredes privadas sin IP pública ni acceso directo a Internet.
- **Aislamiento en desarrollo (Bases personales):** Cada desarrollador tiene su base física dedicada (`istpetdev_dev_01` a `istpetdev_dev_05`). Ningún integrante modifica ni interfiere en la base de otro compañero.
- **Base de integración compartida:** `istpetdev_integration` refleja estrictamente el estado validado de la rama `develop`. Solo se actualiza tras aprobar e integrar un Pull Request en Git.
- **Separación DML vs DDL (Mínimo privilegio):**
  - **Rol de Aplicación (`user_dev_XX`):** Permisos DML exclusivamente (`SELECT, INSERT, UPDATE, DELETE`). Permiso DDL revocado en el esquema `public`.
  - **Rol Migrador (`migrator_dev_XX`):** Permisos DDL en el esquema `public`. Solo se utiliza puntualmente para aplicar migraciones de EF Core.
- **Conexión segura:** Túnel SSM al puerto local `15432` con verificación estricta de certificado TLS oficial de Amazon RDS (`SSL Mode=VerifyFull`) mediante mapeo en `/etc/hosts`.
- **Secretos:** Credenciales almacenadas en AWS Secrets Manager (`/istpetdev/dev/db/...`) con acceso restringido por IAM con MFA obligatorio. Nunca se escriben credenciales en Git ni en archivos públicos.

### Mapeo de Integrantes y Recursos
| Integrante | Código | Usuario IAM | Base Personal | Rol Aplicación | Rol Migrador |
|---|---|---|---|---|---|
| Bryan | `dev_01` | `istpetdev-bryan` | `istpetdev_dev_01` | `user_dev_01` | `migrator_dev_01` |
| Alexander | `dev_02` | `istpetdev-alexander` | `istpetdev_dev_02` | `user_dev_02` | `migrator_dev_02` |
| Andrés | `dev_03` | `istpetdev-andres` | `istpetdev_dev_03` | `user_dev_03` | `migrator_dev_03` |
| Anthony | `dev_04` | `istpetdev-anthony` | `istpetdev_dev_04` | `user_dev_04` | `migrator_dev_04` |
| Jorge | `dev_05` | `istpetdev-jorge` | `istpetdev_dev_05` | `user_dev_05` | `migrator_dev_05` |
| **Común** | `integration` | *(Todos)* | `istpetdev_integration` | `user_integ_dev_XX` | `migrator_integration` |

## Reglas del flujo de trabajo

1. **El código C# es la única fuente de la verdad:** La estructura de la base se gestiona exclusivamente mediante migraciones de Entity Framework Core en `src/Infrastructure/Persistence/Migrations/`. Nunca ejecutar sentencias DDL manuales (`CREATE TABLE`, `ALTER TABLE`) en clientes gráficos como pgAdmin o DBeaver.
2. **Ciclo de vida de una migración:**
   - Diseñar la entidad C# en `src/Domain/Entities/` y registrarla en `ApplicationDbContext.cs`.
   - Generar la migración con `dotnet ef migrations add <NombrePascalCase> --project src/Infrastructure --startup-project src/Api`.
   - Cargar temporalmente el rol migrador: `bash scripts/ops/load-dev-secrets.sh --profile istpetdev-dev --member dev_XX --database personal --migrator --config ~/.config/istpetdev/private/dev-access.json`.
   - Aplicar a la base personal: `dotnet ef database update --project src/Infrastructure --startup-project src/Api`.
   - Restaurar el rol de aplicación: ejecutar `load-dev-secrets.sh` sin el flag `--migrator`.
   - Validar que la API local responda `HTTP 200` en `/health/ready`.
   - Subir el cambio en una rama `feature/*` y abrir Pull Request hacia `develop`.
3. **Propagación en integración:**
   - Al fusionar el PR en `develop`, aplicar la migración en `istpetdev_integration` con el rol `migrator_integration`.
   - Los demás compañeros hacen `git pull origin develop`, cargan su rol migrador y corren `dotnet ef database update` en sus bases personales.
4. **Resolución de conflictos en Git (Snapshot de EF Core):**
   - Si dos integrantes crearon migraciones paralelas y Git detecta conflicto en `ApplicationDbContextModelSnapshot.cs`: **NUNCA resolver el snapshot a mano editando el código C#**.
   - Procedimiento de resolución:
     1. Ejecutar `git rebase develop`.
     2. Revertir la migración local no mergeada: `dotnet ef migrations remove --project src/Infrastructure --startup-project src/Api`.
     3. Resolver conflictos de código en `src/Domain/` y completar el rebase con `git rebase --continue`.
     4. Regenerar la migración sobre el snapshot limpio de develop: `dotnet ef migrations add <NombreMigracion> ...`.
     5. Aplicar la nueva migración local con `dotnet ef database update`.

## Prohibido inventar

- Nombres de tablas, columnas o entidades que no provengan de [[Hechos canonicos]] o [[Modelo de datos]] (usar nombres canónicos en inglés: `RoutePlan`, `ServicePoint`, `HandlingUnit`, etc.).
- Modificar directamente la base de datos `istpetdev_integration` desde una máquina local sin que el PR esté fusionado en `develop`.
- Desactivar la verificación TLS (`VerifyFull`) o abrir puertos de entrada en el Security Group de RDS.
- Modificar o reescribir archivos de migración ya aplicados y fusionados en ramas principales.

## Verificar

- `GET http://localhost:5000/health/ready` devuelve `HTTP 200 OK` demostrando conectividad a la base de datos.
- Tipos de datos correctos: identificadores con UUIDv7, fechas en UTC (`DateTime.UtcNow`) y dinero/cantidades en `decimal` con escala explícita.
- Comprobación de integridad con `python .github/scripts/check_vault.py` antes de fusionar documentación.

## Origen

Creada para la hackathon para coordinar los cinco desarrolladores sobre Amazon RDS sin bloqueos de esquema. Adapta principios de `data-architect-dba` (código como fuente de la verdad, migraciones reproducibles y verificadas) y los estándares de `istpet-gitflow` (rebase limpio, ramas de características y sincronización sobre rama principal).
