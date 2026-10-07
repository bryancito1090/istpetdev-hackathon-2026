---
tipo: plan-skills
estado: propuesta
actualizado: 2026-10-06
tags: [istpetdev, documentacion]
---

# Catálogo y plan de skills

## Objetivo

Convertir convenciones reales del proyecto en instrucciones reutilizables para asistentes, de modo que cualquier integrante de IstpetDev obtenga cambios coherentes con la arquitectura y contratos.

Esta nota define **el catálogo y las especificaciones**. Todavía no se han creado ni instalado archivos SKILL.md ejecutables. Se generarán después de fijar versiones/infraestructura y verificar la primera entrega, como pidió el equipo.

## Catálogo propuesto

| Skill                          | Cuándo se activa                             | Debe leer                                                                                       | Resultado esperado                                         |
| ------------------------------ | -------------------------------------------- | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| istpetdev-contexto             | Inicio de tarea del proyecto                 | [[Contexto maestro]], [[Reto 1 oficial]], [[Alcance y prioridades]]                             | Cambio alineado al reto, sin inventar reglas/resultados    |
| istpetdev-backend              | Casos de uso C#/inventario/custodia          | [[Backend y tiempo real]], [[Modelo de datos]], [[Contratos API y eventos]], [[Seguridad y evidencias]] | Regla transaccional, RBAC por acción/recurso e idempotencia correctos |
| istpetdev-frontend-fsd         | Páginas, slices y componentes Angular web    | [[Frontend con Feature-Sliced Design]], [[Frontend y componentes]], [[Contratos API y eventos]] | Ubicación FSD, API pública e imports válidos               |
| istpetdev-mobile-offline       | Captura Ionic, persistencia y sincronización | [[Movil offline y sincronizacion]], [[Usuarios y flujos]], [[Seguridad y evidencias]]           | Operación durable y conflictos explícitos                  |
| istpetdev-aws-terraform        | Infraestructura, CI/CD y despliegue          | [[AWS y Terraform]], [[CI-CD y automatizacion de despliegue]], [[Hardening y seguridad de servidores]], [[Decisiones de arquitectura]] | Infra reproducible, pipeline DAG con rollback instantáneo y hardening verificado |
| istpetdev-n8n-ia               | Workflows, webhooks y explicaciones          | [[n8n e IA]], [[Contratos API y eventos]]                                                       | Workflow exportable, secretos separados y fallback         |
| istpetdev-datos-logistica      | Modelo, inventario y rutas                   | [[Modelo de datos]], [[Inventario y prediccion]], [[Rutas y sobrecostos]]                       | Unidades/invariantes y ruta factible                       |
| istpetdev-simulacion-evidencia | Datos, KPIs y resultados                     | [[Simulador y metricas]], [[Dataset y escenarios]], [[Plan de validacion]]                      | Experimento reproducible y cifras defendibles              |

Si dos skills repiten muchas instrucciones, mover la regla común a una referencia y reducir el catálogo. No crear una skill por cada componente o endpoint.

## Convención para frontend FSD

La skill frontend incluirá las decisiones **aceptadas** de usar FSD (ADR-13) y el stack Angular 18+ con Signals (ADR-04). Debe:

- Ubicar código en app/pages/widgets/features/entities/shared según responsabilidad, con adopción pragmática (iniciar en pages/entities y extraer a features/widgets por reutilización real).
- Consumir contratos, DTOs y modelos compartidos desde `libs/shared-core` para no duplicar código con la app móvil.
- Usar Angular Signals (`signal()`, `computed()`, `input()`, `output()`) para el estado de UI y componentes; reservar RxJS para flujos asíncronos complejos y SignalR.
- Desacoplar mapas: `shared/ui/map-view` es puramente visual y agnóstico a lógica de negocio; `widgets/route-map` inyecta las entidades.
- Mantener la consulta QR (`pages/public-trace`) en lazy loading ultra-ligero (< 150 KB gzip).
- Respetar imports hacia capas inferiores y límites entre slices, exponiendo API pública limpia sin deep imports.
- Mantener shared sin reglas específicas de logística y autorización definitiva en backend.
- Revisar lint/build existentes y el recorrido afectado.

## Convención para backend

Dominio independiente de infraestructura. Comandos transaccionales y consultas proyectadas. No introducir repositorios genéricos, mediadores o servicios nuevos sin una necesidad concreta.

Toda escritura reintentable comprueba permisos, idempotencia, versión y cantidades. Toda consulta con datos privados limita ámbito y volumen. Aplicar RBAC aceptado en ADR-14 con denegación por defecto y políticas compartidas por API/SignalR; validar organización y recurso también al sincronizar. La skill debe señalar qué invariantes y pruebas existentes afecta el cambio.

## Convención para infraestructura, CI/CD y Terraform

Topología dual: Perfil A (EC2 Hardened + Docker Compose + GHCR para demo y piloto) y Perfil B (ECS Fargate + RDS Multi-AZ para escala nacional). State S3 con `use_lockfile = true`, secretos protegidos y límites explícitos.

El pipeline CI/CD debe cumplir ADR-15: compilación en runner, imágenes por SHA, rotación de 3 versiones y rollback en < 30s. El host debe cumplir las 6 capas de hardening de [[Hardening y seguridad de servidores]] (UFW, loopback binding, Fail2ban, SSH Ed25519, Nginx TLS 1.3 / HTTP 444 y Lynis > 80/100). No declarar alta disponibilidad nacional sin pruebas de failover y recuperación efectivas.

## Convención para n8n/IA

n8n opera a través de API; DeepSeek explica snapshots existentes. Workflow idempotente, exportado sin credenciales, errores y respuesta vacía/incorrecta probados. Registrar modelo/promptVersion y executionId. No generar automatizaciones externas no solicitadas.

## Contenido mínimo de una skill real

1. Nombre, descripción y condiciones de activación claras.
2. Contexto que lee y ruta **real y portable** al proyecto/bóveda.
3. Convenciones obligatorias y excepciones aceptadas.
4. Flujo corto de lectura → cambio → verificación.
5. Comandos reales ya comprobados en el repositorio.
6. Referencias concisas y límites de alcance.
7. Ejemplo basado en una entrega existente.

No inventar comandos de build/test ni paths de un repositorio todavía no creado.

## Ubicación futura

Propuesta: versionar skills de proyecto en `.agents/skills/istpetdev-.../SKILL.md` dentro del repositorio de software, siguiendo el formato/herramientas que se acuerden. La bóveda mantiene la especificación; el archivo operativo se crea con la skill de creación disponible en ese momento.

Si la bóveda y el código viven en repositorios distintos, documentar el mecanismo de acceso a referencias sin rutas personales /home/bryan. Los enlaces de Obsidian no se resuelven automáticamente en todos los agentes.

## Orden para generarlas

1. Contexto y frontend FSD, cuya decisión de estructura está aceptada.
2. Backend y móvil tras la entrega transaccional/offline.
3. AWS/Terraform y n8n después de fijar entornos.
4. Datos/simulación cuando haya fixtures, fórmulas y comandos verificados.

## Validación de una skill

Probar con una tarea pequeña de una entrega real. Verificar que selecciona las referencias, modifica el lugar adecuado, respeta contratos y usa checks existentes. Si necesita explicar muchas reglas no relacionadas, reducir su alcance.

Puertas: [[Decisiones de arquitectura]] y [[Plan de ejecucion]].

## Fuentes complementarias para implementación — 7 de octubre de 2026

Agregar [[Repositorio de software y versiones]], [[Entornos y operacion acordados]] e [[Identidad OIDC y sesiones]] a las referencias de las futuras skills. .NET 8/Angular 22 fijados por Bryan; perfiles A/B, DAG/GHCR/SSH y FSD/Signals del compañero conservados. Aplicar la distinción host/contenedor, manifest de release/backup/rollback sin pull y n8n externo existente. No generar una skill que repita los ejemplos previos sin estos contratos posteriores. Skills, workflows y aplicaciones aún no están implementados.
