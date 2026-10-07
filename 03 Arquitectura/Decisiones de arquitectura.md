---
tipo: arquitectura
estado: propuesta
actualizado: 2026-10-06
tags: [arquitectura, contratos]
---

# Decisiones de arquitectura

**Estado:** propuestas consolidadas; ADR-13 (FSD web) y ADR-14 (RBAC) fueron aceptadas por instrucción del usuario el 6 de octubre de 2026. Las demás decisiones siguen pendientes. Una decisión aceptada no es evidencia de implementación.

## Registro inicial

| ID | Tema | Base solicitada | Recomendación / decisión pendiente |
|---|---|---|---|
| ADR-01 | Versión .NET | .NET 8 | Evaluar .NET 10 LTS por soporte; cerrar antes de scaffold |
| ADR-02 | Topología | Clean Architecture + CQRS | API modular, una base; separación lógica de lectura/escritura |
| ADR-03 | Motor/IDs | PostgreSQL/PostGIS + UUID v7 | Elegir motor RDS compatible; generación interoperable en API/móvil |
| ADR-04 | Stack Web/Móvil | Angular 18+, Ionic 8, Signals y Shared Core | **Aceptada, 2026-10-06**: Standalone, Signals para UI, RxJS para streaming/SignalR y monorepo `libs/shared-core`; [[Frontend y componentes]] |
| ADR-05 | Mapas | Mapbox o Google | Elegir cobertura Ecuador, cuotas/costo y condiciones de uso |
| ADR-06 | Offline | SQLite/IndexedDB | IndexedDB PWA; SQLite nativo solo con adaptador probado |
| ADR-07 | Tiempo real | SignalR + autoscaling | Redis backplane al permitir varias réplicas; afinidad probada |
| ADR-08 | IA | n8n + DeepSeek | Riesgo numérico determinista; LLM solo explicación y recomendaciones acotadas |
| ADR-09 | Cloud y hosting | Dual: EC2 Hardened (Demo) / ECS Fargate (P2) | **Aceptada, 2026-10-06**: perfil ágil económico para hackathon y elástico para escala nacional; [[AWS y Terraform]] |
| ADR-10 | Identidad | No definida | Proveedor estándar OIDC; validar experiencia móvil/offline |
| ADR-11 | Auditoría | Trazabilidad «inmutable» | Ledger append-only en aplicación; describir garantías reales |
| ADR-12 | Repo y colaboración | Bóveda en GitHub personal | Bóveda confirmada en bryancito1090/istpetdev-hackathon-2026; repositorio de software aún pendiente |
| ADR-13 | Arquitectura frontend | Feature-Sliced Design (FSD) | **Aceptada por el equipo, 2026-10-06**: capas y límites en [[Frontend con Feature-Sliced Design]] |
| ADR-14 | Autorización | Control de acceso basado en roles (RBAC) | **Aceptada por instrucción del usuario, 2026-10-06**: permisos por rol y ámbito en servidor; [[Seguridad y evidencias]] |
| ADR-15 | CI/CD y Hardening Host | Pipeline DAG + GHCR + Rollback SHA + Defensa 6 Capas | **Aceptada, 2026-10-06**: compilación en runners, rotación 3 imágenes, rollback <30s y Lynis >80/100; [[CI-CD y automatizacion de despliegue]] y [[Hardening y seguridad de servidores]] |

## ADR-01 — versión de backend

.NET 8 conserva compatibilidad con la propuesta y experiencia del equipo. Para un producto que continúe después de noviembre, .NET 10 LTS evita una actualización inmediata por fin de soporte. **No se cambia el stack automáticamente:** decidir según dependencias disponibles y tiempo. [Soporte oficial de .NET](https://dotnet.microsoft.com/en-us/platform/support/policy).

## ADR-03 — UUID v7

PostgreSQL 18 ofrece generación nativa uuidv7(); versiones previas pueden almacenar UUID v7 aunque no tengan esa función. Seleccionar versión disponible en RDS y compatible con PostGIS; si se conserva .NET 8, verificar una implementación de generación compatible, sin asumir que tiene las APIs de runtimes posteriores. [Funciones UUID de PostgreSQL 18](https://www.postgresql.org/docs/18/functions-uuid.html), [UUID de PostgreSQL 17](https://www.postgresql.org/docs/17/functions-uuid.html).

No tomar orden UUID como orden de recepción offline; conservar fechas y secuencia de aceptación separadas. Mejor localidad temporal no equivale a rendimiento máximo garantizado.

## ADR-04 — Stack Web/Móvil, Reactividad Híbrida y Monorepo Shared Core

**Aceptada, 2026-10-06.** Contexto: se requiere coherencia estricta entre la web de gestión y la app móvil, evitando reescribir contratos o lidiar con suscripciones descontroladas de RxJS en componentes.

**Elección:**
1. **Versiones fijadas:** Node.js 22, Angular 18+ (Standalone Components), Ionic 8, Capacitor 6 y Tailwind CSS 3.4+.
2. **Modelo reactivo:** Angular Signals (`signal()`, `computed()`, `input()`, `output()`) para todo el estado síncrono de UI y componentes. RxJS exclusivamente para flujos asíncronos complejos, debounce de inputs y canales WebSockets de SignalR, integrados con `toSignal()`.
3. **Monorepo Shared Core (`libs/shared-core`):** Librería compartida para tipos TypeScript de dominio, DTOs de API, validadores de esquemas y utilidades de conversión de unidades logísticas (litros, kilos, cajas), consumida por `apps/web` y `apps/mobile`.
4. **Desacoplamiento de mapas:** Componente `shared/ui/map-view` puramente visual y agnóstico a lógica de negocio, orquestado desde `widgets/route-map`.
5. **Carga ultraligera de QR:** Ruta `/trace/:id` aislada en lazy loading (< 150 KB gzip) para visualización instantánea por el jurado.

Detalles en [[Frontend y componentes]] y [[Frontend con Feature-Sliced Design]].

## ADR-05 — mapas

Comparar por matrices y geometría de ruta real. Para Google, evaluar **Routes API / Compute Route Matrix**, no asumir que un nombre antiguo de API es la opción vigente para un proyecto nuevo. Para Mapbox, revisar límites por perfil y cantidad de coordenadas. [Google Routes](https://developers.google.com/maps/documentation/routes/compute_route_matrix), [Mapbox Matrix](https://docs.mapbox.com/api/navigation/matrix/).

**Decisión pendiente:** hacer prueba con puntos de Ecuador, cobertura y presupuesto. Las matrices por carretera no resuelven por sí solas capacidad, ventanas o selección de entregas.

## Aceptar una decisión

Copiar [[Plantilla ADR]] y registrar contexto, opciones, elección, fecha y evidencia. Actualizar las notas afectadas, el contrato y el catálogo de skills. No cerrar una decisión solo por ser «más escalable» si no mejora un requisito concreto.

## Puerta de entrada para skills

Cerrar ADR-01/03/04/05/06/09/10 y validar una entrega vertical. Después las skills se basan en rutas, comandos y convenciones existentes, según [[Catalogo y plan de skills]].

## ADR-13 — FSD en Angular web

**Aceptada, 2026-10-06, por instrucción de IstpetDev.** La estructura web usa app/pages/widgets/features/entities/shared, API pública por slice y dependencias hacia capas inferiores. Standalone Components y Tailwind se conservan. Las versiones siguen pendientes; FSD no decide el modelo de estado ni cambia el backend. Referencia: [[Frontend con Feature-Sliced Design]].

## ADR-14 — RBAC en API, web, móvil y automatización

**Aceptada, 2026-10-06, por instrucción del usuario.** Contexto: ya se describían roles funcionales y autorización por recurso, pero faltaba declarar el modelo que cumple RNF-01.

**Opciones:** reglas aisladas por endpoint o un catálogo compartido de roles/acciones con restricciones por recurso. Se elige **RBAC con validación de organización, almacén, punto y asignación**, para aplicar la misma matriz en API y SignalR. El catálogo inicial usa los seis roles existentes y deniega acciones no concedidas; definición en [[Seguridad y evidencias]].

**Consecuencias:** vincular identidades a roles por organización, centralizar políticas, reflejar permisos en web/móvil y limitar n8n. Para P0, administrar accesos por configuración/seed controlado y auditado. La sincronización offline vuelve a comprobar permisos vigentes. La elección del proveedor OIDC sigue pendiente en ADR-10.

**Verificación pendiente:** B-29 en [[Backlog]]; V-13/V-24 para permisos, aislamiento y revocación; V-14 al incorporar SignalR, según [[Plan de validacion]]. La decisión documenta lo que se implementará, sin afirmar que ya funciona.

## ADR-09 — Topología dual de infraestructura cloud (Demo vs Escala Nacional)

**Aceptada, 2026-10-06.** Contexto: la propuesta inicial de ECS Fargate + RDS Multi-AZ + ALB implica costos elevados ($160-$280 USD/mes) derivados de NAT Gateways y balanceadores, además de complejidad innecesaria para un hackathon de 48 horas.

**Elección:** Se adopta formalmente una **estrategia dual**:
1. **Perfil A (Hackathon / Demo / Piloto):** Instancia AWS EC2 con Elastic IP, Docker Compose, Nginx Reverse Proxy con TLS 1.3 y estándar de blindaje Linux de 6 capas. Costo predecible ($18-$28 USD/mes) y control operativo absoluto.
2. **Perfil B (Operación Nacional Elástica P2):** ECS Fargate + RDS PostgreSQL Multi-AZ + ALB administrado con Terraform como entregable de viabilidad para producción extendida.

Detalles en [[AWS y Terraform]].

## ADR-15 — Pipeline CI/CD Multi-Etapa DAG, Rollback Instantáneo y Hardening Linux

**Aceptada, 2026-10-06.** Contexto: el despliegue no puede depender de operaciones manuales, builds en el servidor que saturen memoria o falta de recuperación ante imprevistos en vivo.

**Elección:**
1. **Pipeline CI/CD DAG en GitHub Actions:** Filtrado inteligente de rutas, pruebas unitarias aisladas en runner, compilación de contenedores con Docker Buildx, etiquetas inmutables por SHA en GHCR, despliegue atómico por SSH y reporte ejecutivo en GitHub Summary.
2. **Rollback Instantáneo en < 30s:** Retención preventiva de las últimas 3 versiones de imágenes en el host; workflow disparado manualmente con `target_sha` sin tiempos de rebuild.
3. **Defensa en Profundidad de 6 Capas:** Mitigación obligatoria de la trampa de Docker vinculando todos los contenedores a loopback `127.0.0.1`, UFW con Default Deny, Fail2ban con jail recidive, OpenSSH con Ed25519 sin passwords ni root, Nginx con TLS 1.3, rate limit y cierre TCP HTTP 444 ante evasión de CDN, particiones `noexec/nosuid` y meta de auditoría Lynis > 80/100.

Referencias: [[CI-CD y automatizacion de despliegue]], [[Hardening y seguridad de servidores]], [[AWS y Terraform]].


## Complemento de decisiones — 7 de octubre de 2026

Se conserva el registro y las decisiones del compañero del 6 de octubre. Bryan confirmó decisiones posteriores y delegó concretar las recomendaciones. Este complemento actualiza el estado para implementación; no reescribe el contenido anterior ni declara software desplegado.

| ADR | Estado actualizado | Definición vigente |
|---|---|---|
| ADR-01 | Aceptada por Bryan, 2026-10-07 | .NET 8; mantener su rama y planificar actualización antes de fin de soporte, sin sustituirlo ahora |
| ADR-03 | Diseño concretado, implementación pendiente | PostgreSQL 16/PostGIS compatible; RDS privado dev, DB aislada por integrante/integración y UUID v7 generado en aplicación con interoperabilidad probada |
| ADR-04 | Versiones concretadas por instrucción de Bryan | Angular 22, Node 22, Ionic 8 y Tailwind 3.4; Signals/RxJS/FSD/shared-core conservados. Parches y Capacitor recomendado en [[Repositorio de software y versiones]] |
| ADR-06 | Diseño concretado | PWA con IndexedDB primero; nativo posterior con Capacitor 8 y persistencia probada |
| ADR-08 | Hosting concretado | n8n existente de Bryan, workflows exportados sin credenciales; LLM explicativo y fallback conservados |
| ADR-09 | Aceptada y ampliada | Perfiles A/B conservados; cada integrante ejecuta localmente, RDS dev compartido privado, stack completo AWS encendido solo para ensayos y producción posterior |
| ADR-10 | Decisión delegada y definida, 2026-10-07 | Amazon Cognito User Pools; Authorization Code + PKCE, cliente M2M n8n y RBAC de ADR-14; [[Identidad OIDC y sesiones]] |
| ADR-12 | Repositorio creado vacío, 2026-10-07 | GitHub privado `bryancito1090/istpetdev-platform`; esqueleto exclusivamente local en `/home/bryan/Projects/ISTPETDEV` |
| ADR-15 | Conservada; implementación pendiente del compañero | DAG/GHCR/SSH/SCP/retención/rollback/hardening, con condiciones operativas en [[Entornos y operacion acordados]] |

### ADR-10 — identidad OIDC y sesiones

Se selecciona Cognito administrado para evitar operar otro servidor de identidad. Web/PWA usan clientes públicos sin secret, PKCE S256, tokens de acceso de 15 minutos y reautenticación que conserva cola offline. La API valida issuer/firma/token_use/client_id/scopes y aplica roles y organización/asignación desde PostgreSQL. n8n usa cliente confidencial separado con scopes de Automatización. Configuración completa, alternativas operativas y pruebas pendientes en [[Identidad OIDC y sesiones]].

Dominio institucional y CI/CD/Compose los profundizarán los compañeros indicados por Bryan. Mapas continúa en ADR-05 pendiente de prueba/costo/licencia. Cuenta AWS y presupuesto están disponibles; se cargan valores privados sin volver a tratar su disponibilidad como bloqueo. Ver [[Entornos y operacion acordados]].
