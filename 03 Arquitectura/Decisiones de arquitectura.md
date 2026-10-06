---
tipo: arquitectura
estado: propuesta
actualizado: 2026-10-06
tags: [arquitectura, contratos]
---

# Decisiones de arquitectura

**Estado:** propuestas consolidadas; ADR-13 (FSD web) fue aceptada por instrucción de IstpetDev el 6 de octubre de 2026. Las demás decisiones siguen pendientes. Una preferencia inicial del equipo es la base de discusión, no evidencia de implementación.

## Registro inicial

| ID | Tema | Base solicitada | Recomendación / decisión pendiente |
|---|---|---|---|
| ADR-01 | Versión .NET | .NET 8 | Evaluar .NET 10 LTS por soporte; cerrar antes de scaffold |
| ADR-02 | Topología | Clean Architecture + CQRS | API modular, una base; separación lógica de lectura/escritura |
| ADR-03 | Motor/IDs | PostgreSQL/PostGIS + UUID v7 | Elegir motor RDS compatible; generación interoperable en API/móvil |
| ADR-04 | Web/móvil | Angular/Tailwind + Angular/Ionic | Fijar matriz Node/Angular/Ionic/Capacitor; PWA primero y nativo si se requiere |
| ADR-05 | Mapas | Mapbox o Google | Elegir cobertura Ecuador, cuotas/costo y condiciones de uso |
| ADR-06 | Offline | SQLite/IndexedDB | IndexedDB PWA; SQLite nativo solo con adaptador probado |
| ADR-07 | Tiempo real | SignalR + autoscaling | Redis backplane al permitir varias réplicas; afinidad probada |
| ADR-08 | IA | n8n + DeepSeek | Riesgo numérico determinista; LLM solo explicación y recomendaciones acotadas |
| ADR-09 | Cloud | ECS/ALB, RDS Multi-AZ, S3 | Terraform con perfiles acotado/nacional y presupuesto explícito |
| ADR-10 | Identidad | No definida | Proveedor estándar OIDC; validar experiencia móvil/offline |
| ADR-11 | Auditoría | Trazabilidad «inmutable» | Ledger append-only en aplicación; describir garantías reales |
| ADR-12 | Repo y colaboración | Bóveda en GitHub personal | Bóveda confirmada en bryancito1090/istpetdev-hackathon-2026; repositorio de software aún pendiente |
| ADR-13 | Arquitectura frontend | Feature-Sliced Design (FSD) | **Aceptada por el equipo, 2026-10-06**: capas y límites en [[Frontend con Feature-Sliced Design]] |

## ADR-01 — versión de backend

.NET 8 conserva compatibilidad con la propuesta y experiencia del equipo. Para un producto que continúe después de noviembre, .NET 10 LTS evita una actualización inmediata por fin de soporte. **No se cambia el stack automáticamente:** decidir según dependencias disponibles y tiempo. [Soporte oficial de .NET](https://dotnet.microsoft.com/en-us/platform/support/policy).

## ADR-03 — UUID v7

PostgreSQL 18 ofrece generación nativa uuidv7(); versiones previas pueden almacenar UUID v7 aunque no tengan esa función. Seleccionar versión disponible en RDS y compatible con PostGIS; si se conserva .NET 8, verificar una implementación de generación compatible, sin asumir que tiene las APIs de runtimes posteriores. [Funciones UUID de PostgreSQL 18](https://www.postgresql.org/docs/18/functions-uuid.html), [UUID de PostgreSQL 17](https://www.postgresql.org/docs/17/functions-uuid.html).

No tomar orden UUID como orden de recepción offline; conservar fechas y secuencia de aceptación separadas. Mejor localidad temporal no equivale a rendimiento máximo garantizado.

## ADR-05 — mapas

Comparar por matrices y geometría de ruta real. Para Google, evaluar **Routes API / Compute Route Matrix**, no asumir que un nombre antiguo de API es la opción vigente para un proyecto nuevo. Para Mapbox, revisar límites por perfil y cantidad de coordenadas. [Google Routes](https://developers.google.com/maps/documentation/routes/compute_route_matrix), [Mapbox Matrix](https://docs.mapbox.com/api/navigation/matrix/).

**Decisión pendiente:** hacer prueba con puntos de Ecuador, cobertura y presupuesto. Las matrices por carretera no resuelven por sí solas capacidad, ventanas o selección de entregas.

## Aceptar una decisión

Copiar [[Plantilla ADR]] y registrar contexto, opciones, elección, fecha y evidencia. Actualizar las notas afectadas, el contrato y el catálogo de skills. No cerrar una decisión solo por ser «más escalable» si no mejora un requisito concreto.

## Puerta de entrada para skills

Cerrar ADR-01/03/04/05/06/09/10 y validar una entrega vertical. Después las skills se basan en rutas, comandos y convenciones existentes, según [[Catalogo y plan de skills]].

## ADR-13 — FSD en Angular web

**Aceptada, 2026-10-06, por instrucción de IstpetDev.** La estructura web usa app/pages/widgets/features/entities/shared, API pública por slice y dependencias hacia capas inferiores. Standalone Components y Tailwind se conservan. Las versiones siguen pendientes; FSD no decide el modelo de estado ni cambia el backend. Referencia: [[Frontend con Feature-Sliced Design]].
