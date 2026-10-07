---
tipo: referencia
estado: vigente
actualizado: 2026-10-07
tags: [hackathon, equipo, ia]
---

# Hechos canónicos

Fuente única de los datos que el equipo y cualquier asistente de IA deben usar sin reinterpretar. Si un dato no está aquí o dice **PENDIENTE**, no se completa por suposición: se escribe `PENDIENTE` y se pregunta. Cada fila indica su fuente y su estado según [[Convenciones y estados]].

Certeza: ✅ confirmado con fuente · ⚠️ a validar (propuesta, supuesto o dato con contradicción abierta).

## Evento

| Dato | Valor | Fuente | Certeza |
|---|---|---|---|
| Evento | Hackathon Expo Clean Ecuador 2026 | Manual, p. 2 | ✅ |
| Reto | Reto 1 — Optimización y trazabilidad logística para el abastecimiento de insumos a nivel nacional | Manual, p. 19 | ✅ |
| Área | Gestión Inteligente de Procesos | Manual, p. 19 | ✅ |
| Capacitación | 8 de octubre de 2026, 09:00–13:00 | Manual, p. 27 | ✅ |
| Jornadas | 16 y 17 de octubre de 2026 | Manual, pp. 6 y 16 | ✅ |
| Zona horaria | America/Guayaquil (UTC−05:00) | Decisión del equipo en [[Cronograma oficial]] | ✅ |
| Sede | Centro de Exposiciones Quito (CEQ), según listado público de la feria; el manual solo dice «espacio definido por la organización» (p. 14) | [Listado público](https://www.cantonfair.net/event/67411-ecuador-cleaning-expo-2026) | ⚠️ confirmar en O-07 |
| Jurado | 7 personas: 3 del sector de limpieza (incluye JIMCORPSERVI/FEDELIMP), 2 expertos técnicos/tecnológicos, 1 académico, 1 de LACIF | Manual §11.3, p. 10 | ✅ |
| Pesos de evaluación | 15/15/15/15/20/10/10 (ver [[Evaluacion y entregables]]) | Manual, pp. 9 y 26 | ✅ |
| Trabajo previo permitido | PENDIENTE (consulta O-01) | [[Consultas para la organizacion]] | ⚠️ |
| Duración del pitch | PENDIENTE (consulta O-04); meta interna 3 min | [[Guion del pitch]] | ⚠️ |

## Equipo

| Dato | Valor | Fuente | Certeza |
|---|---|---|---|
| Nombre | IstpetDev | [[Informacion inicial del equipo]] | ✅ |
| Integrantes | 5, sin asignación fija de especialidades | [[Equipo y acuerdos]] | ✅ |
| Repositorio de la bóveda | bryancito1090/istpetdev-hackathon-2026 (privado) | README | ✅ |
| Rama de trabajo | `develop`; se integra en `main` | README | ✅ |
| Repositorio de código | bryancito1090/istpetdev-platform (privado), creado vacío el 7-oct-2026; esqueleto solo local en el equipo de Bryan | ADR-12; [[Repositorio de software y versiones]] | ✅ |
| Skills en el repositorio de código | PENDIENTE: cómo llegan `AGENTS.md` y `.agents/skills/` a istpetdev-platform (copia generada o referencia) | C-01 | ⚠️ |

## Escenario de demostración

Estas cifras son propuesta del equipo, no datos de una empresa ni exigencias del manual.

| Dato | Valor | Fuente | Certeza |
|---|---|---|---|
| Puntos de servicio | 80 | [[Informacion inicial del equipo]] | ⚠️ propuesta |
| Horizonte simulado | 90 días | [[Simulador y metricas]] | ⚠️ propuesta |
| Caso hospital | 60 L disponibles, 12 L/día, lead time 2 días, margen 3 días → cobertura 5 días | [[Inventario y prediccion]] | ⚠️ ilustrativo |
| Fixture inicial | 6 puntos y 2 SKU | [[Dataset y escenarios]] | ⚠️ propuesta |
| Resultados medidos | Ninguno todavía | [[Plan de validacion]] | ✅ |

## Stack y versiones

Decisiones del 7 de octubre registradas por bryancito1090 (be0b127) en [[Repositorio de software y versiones]], [[Identidad OIDC y sesiones]] y [[Entornos y operacion acordados]]. Las filas con ⚠️ siguen siendo propuesta o tienen una contradicción abierta; no elegir una opción sin decisión registrada. Versiones exactas de paquetes: solo las de [[Repositorio de software y versiones]].

| Componente | Valor vigente | Decisión | Contradicción abierta | Certeza |
|---|---|---|---|---|
| Backend | C# con Clean Architecture y CQRS lógico | ADR-02 propuesta | — | ⚠️ |
| Versión .NET | .NET 8 (EF Core/Npgsql 8.x); soporte hasta 10-nov-2026, actualización posterior al evento | ADR-01 aceptada por Bryan | — | ✅ |
| Base de datos | PostgreSQL 16 + PostGIS 3.x compatible; UUID v7 generado en la aplicación | ADR-03 concretada | — | ✅ diseño, sin aprovisionar |
| Frontend web | Angular 22 standalone + FSD; TypeScript 6.0 | ADR-13 aceptada, ADR-04 (versión por Bryan) | — | ✅ |
| Móvil | PWA con Ionic 8 e IndexedDB primero; Capacitor 8 para el empaquetado nativo posterior | ADR-06 concretada | — | ✅ diseño |
| Tailwind | 3.4 | ADR-04 | — | ✅ |
| Node.js | 22 LTS | ADR-04 | — | ✅ |
| Mapas | PENDIENTE: Mapbox o Google Routes | ADR-05 | «Frontend y componentes» lista Mapbox GL JS / Leaflet | ⚠️ |
| Tiempo real | SignalR; Redis solo con varias réplicas | ADR-07 propuesta | — | ⚠️ |
| IA | Cálculo determinista; LLM (DeepSeek) solo explica; n8n en el servidor existente de Bryan | ADR-08 | — | ⚠️ propuesta |
| Identidad | Amazon Cognito (OIDC, Authorization Code + PKCE) | ADR-10 definida | — | ✅ diseño, sin aprovisionar |
| Autorización | RBAC con 6 roles fijos | ADR-14 aceptada | — | ✅ |
| Hosting demo | Perfil A: EC2 + Docker Compose + Nginx, encendido solo para ensayos; región `us-east-1` | ADR-09 | — | ⚠️ ver Deciders |
| Desarrollo | Aplicaciones locales por integrante; RDS dev privado compartido (base por integrante + integración) | [[Entornos y operacion acordados]] | — | ✅ diseño, sin aprovisionar |
| Acceso AWS del equipo | IAM individual con MFA y `aws login` temporal, sin Organizations (escenario vigente) | [[AWS temporal para la hackathon y cierre]] | Sustituye a SSO de [[Credenciales y acceso del equipo]] durante la hackathon | ⚠️ propuesta |
| TLS | La configuración de ejemplo permite TLS 1.2 y 1.3 | [[Hardening y seguridad de servidores]] | Varias notas dicen «TLS 1.3»; solo 1.3 es PENDIENTE | ⚠️ |

## Estado de las decisiones (ADR)

«Registrado por» viene del historial de git; no prueba quién decidió. Los Deciders reales se confirman en reunión.

| Tema | ADR | Estado en la bóveda | Registrado por (commit) | Deciders |
|---|---|---|---|---|
| Versión backend | ADR-01 | Aceptada | bryancito1090 (765c532, be0b127) | Bryan |
| Topología | ADR-02 | Propuesta | bryancito1090 (765c532) | — |
| Motor e IDs | ADR-03 | Diseño concretado | bryancito1090 (765c532, be0b127) | Bryan |
| Stack web/móvil | ADR-04 | Aceptada; versiones fijadas el 7-oct | JorgeDoicela (4c3a9ef), bryancito1090 (be0b127) | Versiones: Bryan; aceptación inicial PENDIENTE |
| Mapas | ADR-05 | Pendiente | bryancito1090 (765c532) | — |
| Offline | ADR-06 | Diseño concretado | bryancito1090 (765c532, be0b127) | Bryan |
| Tiempo real | ADR-07 | Propuesta | bryancito1090 (765c532) | — |
| IA | ADR-08 | Propuesta | bryancito1090 (765c532) | — |
| Cloud y hosting | ADR-09 | Aceptada | JorgeDoicela (4c3a9ef) | PENDIENTE |
| Identidad | ADR-10 | Definida (delegada) | bryancito1090 (be0b127) | Delegada por Bryan |
| Auditoría | ADR-11 | Propuesta | bryancito1090 (765c532) | — |
| Repositorio | ADR-12 | Repositorio creado vacío | bryancito1090 (765c532, be0b127) | Bryan |
| Frontend FSD | ADR-13 | Aceptada «por el equipo» | bryancito1090 (765c532) | PENDIENTE confirmar nombres |
| RBAC | ADR-14 | Aceptada | bryancito1090 (5905073) | PENDIENTE confirmar nombres |
| CI/CD y hardening | ADR-15 | Aceptada | JorgeDoicela (4c3a9ef) | PENDIENTE |

## Nombres en código

Tomados de [[Modelo de datos]] y [[Contratos API y eventos]]. Ningún asistente debe crear sinónimos.

| Término en la bóveda | Nombre en código | Fuente |
|---|---|---|
| Organización | `Organization` | Modelo de datos |
| Cuenta | `Account` | Modelo de datos |
| Acceso por organización | `OrganizationAccess` | Modelo de datos |
| Punto de servicio | `ServicePoint` | Modelo de datos |
| Ubicación | `Location` | Modelo de datos |
| Producto / SKU | `Product` | Modelo de datos |
| Lote | `Lot` | Modelo de datos |
| Unidad logística (caja con QR) | `HandlingUnit` | Modelo de datos |
| Movimiento | `InventoryMovement` | Modelo de datos |
| Saldo | `StockBalance` | Modelo de datos |
| Reserva | `Reservation` | Modelo de datos |
| Consumo | `Consumption` | Modelo de datos |
| Solicitud de reposición | `ReplenishmentRequest` | Modelo de datos |
| Vehículo | `Vehicle` | Modelo de datos |
| Plan de ruta / parada | `RoutePlan` / `RouteStop` | Modelo de datos |
| Entrega / línea | `Delivery` / `DeliveryLine` | Modelo de datos |
| Recepción / línea | `Receipt` / `ReceiptLine` | Modelo de datos |
| Evidencia | `Evidence` | Modelo de datos |
| Evento de custodia | `CustodyEvent` | Modelo de datos |
| Snapshot de riesgo | `RiskSnapshot` | Modelo de datos |
| Incidente | `Incident` | Modelo de datos |
| Conversación / mensaje | `Conversation` / `Message` | Modelo de datos |
| Registro de idempotencia | `IdempotencyRecord` | Modelo de datos |
| Evento outbox | `OutboxEvent` | Modelo de datos |
| Ejecución de simulación | `SimulationRun` | Modelo de datos |
| API base | `/api/v1` | Contratos API y eventos |
| Hub en tiempo real | `/hubs/operations` | Contratos API y eventos |

## Rutas, puertos y comandos

| Dato | Valor | Certeza |
|---|---|---|
| Estructura del repositorio de código | `src/` (Api, Application, Domain, Infrastructure), `apps/web`, `apps/mobile`, `libs/shared-core`, `infra/`, `automation/n8n/workflows/`, `scripts/`, `tests/`; árbol completo en [[Repositorio de software y versiones]]. Los filtros de CI usan `src/**`, no `backend/**` | ✅ acordada, sin generar |
| Puertos internos (ejemplo, solo loopback) | API 5000, PostgreSQL 5432, Redis 6379, n8n 5678 | ⚠️ propuesta |
| Comando de verificación de la bóveda | `python .agents/skills/istpetdev-docs/scripts/check_vault.py` | ✅ |
| Sincronizar skills para Claude Code | `python .agents/skills/istpetdev-docs/scripts/check_vault.py --sync-skills` | ✅ |
| Comandos de build, test y despliegue del código | PENDIENTE: el repositorio de código está vacío | ⚠️ |

## Contradicciones abiertas

Cada una sigue el protocolo de [[Convenciones y estados]]: no se corrige en silencio; se decide y se registra.

| Contradicción | Opciones | Decide |
|---|---|---|
| Mapas | Mapbox o Google Routes (ADR-05); «Frontend y componentes» lista Mapbox GL JS / Leaflet | ADR-05 |
| TLS | 1.2 + 1.3 o solo 1.3 | ADR-15 |
| Acceso AWS | SSO ([[Credenciales y acceso del equipo]]) o IAM + MFA temporal ([[AWS temporal para la hackathon y cierre]], marcado como vigente) | Bryan |
| Skills en el repositorio de código | Copia generada o referencia a la bóveda | C-01 |
| Autoría de ADR-04 (aceptación inicial), 09, 13, 14 y 15 | Confirmar Deciders | Reunión del equipo |

Cerradas el 7 de octubre por be0b127: versión .NET (8), PostgreSQL (16), Angular (22) y Capacitor (8), móvil (PWA primero), identidad (Cognito), repositorio de código y rutas (`src/**`).

Para modificar esta nota: cambiar primero la nota fuente o el ADR y después esta tabla. Ver [[Mapa de la boveda]].
