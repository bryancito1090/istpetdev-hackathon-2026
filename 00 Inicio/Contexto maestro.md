---
tipo: guia
estado: propuesta
actualizado: 2026-10-06
tags: [hackathon, equipo]
---

# Contexto maestro

## Nuestra misión

Construir una plataforma que ayude a una empresa de limpieza a **reabastecer antes de que falten insumos, reducir el costo de transporte y demostrar cada transferencia desde bodega hasta recepción**.

**Inscripción declarada por el equipo:** Reto 1. **Área oficial:** Gestión Inteligente de Procesos. **Equipo:** IstpetDev, cinco integrantes con amplia experiencia full stack, móvil, datos y logística; trabajo flexible por entregables, sin asignación fija de especialidades. **Estado actual:** documentación y diseño inicial; no se ha implementado el sistema en esta bóveda.

## Historia que une el producto

Una empresa atiende 80 puntos del país. Hoy descubre que un hospital se quedó sin desinfectante cuando recibe la llamada. Queremos mostrar que puede anticipar el riesgo cinco días antes, explicar el cálculo, preparar una ruta viable y seguir el insumo hasta la persona que lo recibe.

**80 puntos, cinco días y 90 días simulados son escenarios propuestos por el equipo**, no datos de una empresa validada ni cantidades exigidas por el manual. El ejemplo debe concordar con el dataset y con los resultados reales del simulador.

## Lo que sí exige el manual

- Planificación de rutas eficientes.
- Predicción de reabastecimiento crítico según la demanda de cada cliente.
- Trazabilidad del almacén central a la entrega final.
- Prototipo o herramienta demostrable con evidencia de mejora disponible.
- Entregables de problema, solución, prototipo, validación, viabilidad, negocio y pitch.

Fuente: [[Reto 1 oficial]] y [[Evaluacion y entregables]].

## Decisiones de partida

| Tema | Base de trabajo | Estado |
|---|---|---|
| Backend | C#/.NET 8, Clean Architecture y separación de comandos/consultas | Propuesta del equipo; revisar versión |
| Datos | PostgreSQL/PostGIS; UUID v7 para lotes y operaciones | Propuesta del equipo; versiones pendientes |
| Web | Angular standalone, Tailwind y Feature-Sliced Design | Stack propuesto; FSD aceptado por instrucción del equipo el 6 de octubre |
| Móvil | Angular/Ionic; persistencia y operaciones offline | Propuesta del equipo |
| Nube | AWS ECS Fargate, ALB, RDS, S3 y Terraform | Propuesta del equipo |
| Comunicación | SignalR para alertas y chat de operación | Propuesta del equipo |
| Automatización | n8n y DeepSeek para explicar alertas | Propuesta del equipo |
| Diseño interno | Una API modular, una base de datos, reglas deterministas para inventario | Recomendación técnica inicial |
| Demo | QR físico, entrega offline, comparación reproducible y trazabilidad pública limitada | Propuesta consolidada |

Las decisiones y alternativas están en [[Decisiones de arquitectura]]. No crear microservicios o bases separadas solamente por usar CQRS.

## Tres niveles de alcance

1. **P0 — flujo evaluable:** riesgo → planificación → despacho QR → recepción offline → sincronización → indicadores.
2. **P1 — sistema completo para la demo:** comparación de rutas, simulador de 90 días, chat, incidentes n8n, IA explicativa, nube desplegada y evidencias.
3. **P2 — operación nacional:** endurecimiento, capacidad medida, recuperación probada, múltiples vehículos/regiones y piloto empresarial.

La arquitectura completa se diseña desde el inicio; las entregas siguen [[Alcance y prioridades]].

## Reglas para el equipo y los asistentes

- Leer el reto, el alcance y los contratos antes de implementar.
- Distinguir requisito oficial, propuesta, supuesto y resultado medido.
- Registrar decisiones que cambian interfaces, datos o infraestructura.
- Calcular riesgo y métricas con datos verificables. La IA explica; no inventa cifras.
- Etiquetar los datos sintéticos y los resultados simulados.
- No asegurar ahorro, cero quiebres, optimalidad global o inmutabilidad absoluta sin evidencia.
- Conservar autoría, licencias y cambios hechos antes y durante el evento.
- Mantener credenciales y datos personales reales fuera de la bóveda compartida.

## Primeras acciones

- [ ] Completar los acuerdos y recursos pendientes en [[Equipo y acuerdos]].
- [ ] Resolver el 8 de octubre las [[Consultas para la organizacion]].
- [ ] Cerrar versiones y proveedor de mapas en [[Decisiones de arquitectura]].
- [ ] Construir la primera entrega vertical de [[Plan de ejecucion]].
- [ ] Generar skills según [[Catalogo y plan de skills]] una vez cerradas las convenciones reales.
