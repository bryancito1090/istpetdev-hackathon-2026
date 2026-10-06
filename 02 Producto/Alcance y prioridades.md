---
tipo: especificacion-producto
estado: propuesta
actualizado: 2026-10-06
tags: [producto, reto-1]
---

# Alcance y prioridades

Diseñamos el sistema completo propuesto por el equipo. Lo construimos en entregas funcionales para llegar al 16 de octubre con el recorrido central integrado, sujeto a las reglas confirmadas.

## P0 — primera entrega completa

| Capacidad | Incluye | Termina cuando |
|---|---|---|
| Catálogo e inventario | Punto, SKU, lote, saldos y consumo | Se puede explicar el saldo de un punto |
| Riesgo | Cobertura, lead time y alerta | La alerta referencia su cálculo y datos |
| Planificación | Un almacén, un vehículo y paradas factibles | Se valida capacidad, horarios y urgencia |
| Custodia | QR de unidad, despacho y recepción por líneas | Se consulta la cadena y concilian cantidades |
| Offline | Captura persistente y reintento idempotente | Reiniciar/reintentar no pierde ni duplica entrega |
| Panel | Puntos críticos, ruta y estado de entrega | El planificador completa el flujo |
| Comparación mínima | Baseline y política propuesta sobre escenario pequeño | Se exportan métricas calculadas |

## P1 — sistema completo para la demostración

- Dataset sintético de 80 puntos y simulación de 90 días.
- Comparación visual de rutas y KPIs con denominadores.
- Evidencias S3 y consulta pública limitada por QR.
- Alertas en vivo y chat gerencia–conductor con historial.
- Incidente controlado, replanificación y explicación del cambio.
- n8n para procesos programados y DeepSeek para explicar alertas.
- Despliegue con Terraform, ECS/ALB y RDS; perfil de alta disponibilidad si presupuesto y tiempo permiten activarlo.
- Ensayo grabado y paquete final de entregables.

## P2 — madurez para operación nacional

- Múltiples vehículos, bodegas, regiones y restricciones de transporte verificadas.
- Pronósticos calibrados con consumo real, cobertura geográfica y estacionalidad.
- Pruebas de carga, autoscaling, recuperación y disponibilidad.
- Operación continua, soporte, métricas de costos y mantenimiento.
- Integraciones con sistemas reales y piloto empresarial.

La configuración Multi-AZ y de múltiples réplicas se prepara en P1; **declarar alta disponibilidad comprobada requiere pruebas de recuperación**, no solo activar opciones.

## Orden cuando hay poco tiempo

Preservar flujo P0 y datos fiables. Después cerrar simulación, despliegue y evidencia. Los extras de [[Plus para ganar]] solo entran cuando no ponen en riesgo lo anterior.

## Fuera del alcance inicial

No desarrollar cotizador del Reto 2, ERP general, marketplace, blockchain o entrenamiento de modelos propios. Las interfaces se crean para integraciones que realmente use el flujo.

## Regla de cierre

Una capacidad está terminada si cumple [[Requisitos y aceptacion]], tiene evidencia necesaria y está integrada al guion. «Funciona en mi equipo» no basta si otra app depende de su contrato.

Cada cambio de alcance se refleja en [[Backlog]] y [[Decisiones de arquitectura]].
