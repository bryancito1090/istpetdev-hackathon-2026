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
| istpetdev-backend              | Casos de uso C#/inventario/custodia          | [[Backend y tiempo real]], [[Modelo de datos]], [[Contratos API y eventos]]                     | Regla transaccional, autorización e idempotencia correctas |
| istpetdev-frontend-fsd         | Páginas, slices y componentes Angular web    | [[Frontend con Feature-Sliced Design]], [[Frontend y componentes]], [[Contratos API y eventos]] | Ubicación FSD, API pública e imports válidos               |
| istpetdev-mobile-offline       | Captura Ionic, persistencia y sincronización | [[Movil offline y sincronizacion]], [[Usuarios y flujos]], [[Seguridad y evidencias]]           | Operación durable y conflictos explícitos                  |
| istpetdev-aws-terraform        | Infraestructura y despliegue AWS             | [[AWS y Terraform]], [[Decisiones de arquitectura]], [[Seguridad y evidencias]]                 | Infra reproducible, plan revisable y límites de gasto      |
| istpetdev-n8n-ia               | Workflows, webhooks y explicaciones          | [[n8n e IA]], [[Contratos API y eventos]]                                                       | Workflow exportable, secretos separados y fallback         |
| istpetdev-datos-logistica      | Modelo, inventario y rutas                   | [[Modelo de datos]], [[Inventario y prediccion]], [[Rutas y sobrecostos]]                       | Unidades/invariantes y ruta factible                       |
| istpetdev-simulacion-evidencia | Datos, KPIs y resultados                     | [[Simulador y metricas]], [[Dataset y escenarios]], [[Plan de validacion]]                      | Experimento reproducible y cifras defendibles              |

Si dos skills repiten muchas instrucciones, mover la regla común a una referencia y reducir el catálogo. No crear una skill por cada componente o endpoint.

## Convención para frontend FSD

La skill frontend incluirá la decisión **aceptada por el usuario** de usar FSD. Debe:

- Ubicar código en app/pages/widgets/features/entities/shared según responsabilidad.
- Mantener standalone y Tailwind con versiones acordadas.
- Respetar imports hacia capas inferiores y límites entre slices.
- Exponer API pública de slice, sin deep imports externos.
- Mantener shared sin reglas específicas de logística.
- No crear capas/slices vacías ni extraer una feature solo por existir una acción.
- Mantener autorización y saldos críticos en backend.
- Revisar lint/build existentes y el recorrido afectado.

Para componentes móviles no imponer automáticamente la misma decisión; aplicar primero persistencia y sincronización de la app Ionic.

## Convención para backend

Dominio independiente de infraestructura. Comandos transaccionales y consultas proyectadas. No introducir repositorios genéricos, mediadores o servicios nuevos sin una necesidad concreta.

Toda escritura reintentable comprueba permisos, idempotencia, versión y cantidades. Toda consulta con datos privados limita ámbito y volumen. La skill debe señalar qué invariantes y pruebas existentes afecta el cambio.

## Convención para Terraform

Versiones/proveedor fijados, state protegido, secretos externos, variables y límites explícitos. El resultado debe incluir un plan revisable y costos/configuración del entorno. No declarar alta disponibilidad únicamente por la existencia de archivos Terraform.

La capacidad de ejecutar apply depende de autorización, cuenta y presupuesto de la tarea concreta; una skill no sustituye ese contexto.

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
