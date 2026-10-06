---
tipo: ejecucion
estado: propuesta
actualizado: 2026-10-06
tags: [hackathon, istpetdev]
---

# Backlog

Backlog compartido de IstpetDev, **sin asignación fija de integrantes**. Todas las capacidades de software empiezan en pendiente; actualizar solo con evidencia de avance.

## P0 — flujo evaluable

| ID | Entrega | Depende de | Criterio de cierre | Estado |
|---|---|---|---|---|
| B-01 | Cerrar versiones y contrato | ADRs | Versiones/contrato revisados | Pendiente |
| B-02 | Fixture de 6 puntos/2 SKU | B-01 | Unidades y balance verificables | Pendiente |
| B-03 | Catálogo, lotes y saldos | B-02 | RF-01/02, concurrencia válida | Pendiente |
| B-04 | Consumo y cobertura | B-03 | RF-03, casos cero/desactualizado | Pendiente |
| B-05 | Planner inicial | B-04, mapas | RF-04, inviables explícitos | Pendiente |
| B-06 | Unidades QR y custodia | B-03 | RF-05, líneas por lote | Pendiente |
| B-07 | Despacho/recepción online | B-06 | Cantidades parciales y actor autorizado | Pendiente |
| B-08 | Persistencia y sincronización móvil | B-07 | RF-06, reinicio/reintento/duplicados | Pendiente |
| B-09 | Panel integrado | B-04/05/07 | RF-07, datos/versiones consistentes | Pendiente |
| B-10 | Baseline/comparación pequeña | B-05 | RF-08, mismos datos/recursos | Pendiente |

## P1 — sistema completo para demo

| ID | Entrega | Depende de | Criterio de cierre | Estado |
|---|---|---|---|---|
| B-11 | S3 foto/firma | B-08 | RF-09, privada y reintentable | Pendiente |
| B-12 | Consulta pública QR | B-06/11 | RF-13, datos limitados y revocación | Pendiente |
| B-13 | SignalR y chat | B-07 | RF-10, historial y reconexión | Pendiente |
| B-14 | Incidente/replanificación | B-05/13 | RF-11, lo ejecutado se conserva | Pendiente |
| B-15 | n8n riesgo/explicación | B-04 | RF-12, fallback/JSON/error | Pendiente |
| B-16 | n8n incidente demo | B-14/15 | Credencial limitada y caso etiquetado | Pendiente |
| B-17 | Dataset 80 puntos/90 días | B-02 | Escenarios, seed y hash | Pendiente |
| B-18 | Simulador/KPIs/exportaciones | B-10/17 | RF-14, balance y denominadores | Pendiente |
| B-19 | Anomalía/investigación | B-04/17 | RF-15, alerta distinta de merma | Pendiente |
| B-20 | Terraform/hosting HTTPS | B-01, recursos | RNF-06, entorno reproducible | Pendiente |
| B-21 | Prueba dos réplicas/backplane | B-13/20 | RNF-07, mensajes cruzados | Pendiente |
| B-22 | Ensayo físico y contingencias | B-08/12/14/18/20 | Recorrido completo y video | Pendiente |
| B-23 | Evidencia de usuario/mentor | B-09/22 | Validación documentada y cambios | Pendiente |
| B-24 | Paquete/pitch final | B-18/22/23 | Entregables consistentes con evidencia | Pendiente |

## P2 — operación nacional

| ID | Entrega | Criterio |
|---|---|---|
| B-25 | Multi-bodega/flota avanzada | Restricciones reales y benchmark |
| B-26 | Pronóstico calibrado | Backtesting frente a base determinista |
| B-27 | Carga/autoscaling/recuperación | Volumen y tiempos comprobados |
| B-28 | Integración empresarial/piloto | Acuerdo y resultados observados |

## Documentación y skills

- D-01: bóveda inicial creada el 6 de octubre; validación de enlaces al cierre.
- D-02: actualizar reglas tras capacitación del 8.
- D-03: completar ADRs y convenciones con la primera entrega.
- D-04: generar skills según [[Catalogo y plan de skills]].
- D-05: registrar evidencia y cambios del evento.

Una fila se marca completa cuando cumple su criterio y tiene enlace a resultado. Las pruebas se planifican en [[Plan de validacion]].

## Convención frontend FSD

B-09 implementa el panel con [[Frontend con Feature-Sliced Design]]. RF-16 y V-23 verifican estructura, dependencias y API pública; la decisión está aceptada por IstpetDev y no depende de seleccionar versiones.
