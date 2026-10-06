---
tipo: guia
estado: vigente
actualizado: 2026-10-06
tags: [hackathon, equipo]
---

# Convenciones y estados

## Organización

Usamos Markdown y enlaces internos de Obsidian. La bóveda no necesita plugins adicionales. Los nombres de archivos son únicos y sin tildes para facilitar enlaces entre sistemas; el contenido sí usa español normal.

Cada nota tiene `tipo`, `estado`, `actualizado` y `tags`. Actualizar la fecha al cambiar el contenido.

| Estado | Significado |
|---|---|
| vigente | Guía o resumen utilizable de una fuente conocida |
| propuesta | Diseño que el equipo todavía debe validar |
| pendiente | Falta información o una decisión |
| aceptado | Se registró quién decidió y cuándo |
| validado | Hay evidencia enlazada del resultado |
| reemplazado | Existe una decisión posterior enlazada |
| plantilla | Formato para copiar y completar |

Una propuesta técnica **no certifica una implementación**. Una decisión aceptada tampoco equivale a una funcionalidad terminada.

## Tipos de afirmación

| Etiqueta | Cómo usarla |
|---|---|
| Oficial | Citar página física y sección del PDF |
| Información del equipo | Citar [[Informacion inicial del equipo]] |
| Propuesta | Explicar resultado esperado y aceptación |
| Supuesto | Indicar cómo se validará y qué cambiaría si falla |
| Medido | Enlazar ejecución, dataset, parámetros y resultado |
| Pendiente | Registrar información faltante y fecha de revisión |

Las páginas del manual se cuentan desde la portada, que es la página 1. Sus cuadros fueron revisados como imágenes; extraer solo el texto omite información importante.

## Trabajo compartido

- Coordinar cambios por entregable para evitar ediciones incompatibles.
- Actualizar la nota fuente antes de repetir información en otras notas.
- Contratos compartidos: [[Contratos API y eventos]].
- Fórmulas oficiales del equipo: [[Simulador y metricas]].
- Registrar cambios relevantes en [[Fuente y control documental]] y decisiones en [[Decisiones de arquitectura]].
- Compartimos la bóveda mediante Git y GitHub en bryancito1090/istpetdev-hackathon-2026. Hacer cambios pequeños y revisar conflictos antes de publicar.
- Actualizar la copia con `git pull --ff-only` antes de editar. Si hay divergencia, integrar conservando los cambios; no forzar el push para resolverla.
- `.obsidian/workspace*.json` contiene sesiones personales y está excluido mediante `.gitignore`; la configuración común sí se versiona.

## Fuentes y evidencia

Conservar fuentes en `99 Fuentes`. Crear `99 Fuentes/Evidencias` cuando haya resultados. Mantener fuera de esta bóveda documentos de identidad, datos bancarios, credenciales, fotos de terceros y firmas reales.

Para pruebas usar [[Plantilla evidencia]]; para mentorías, [[Plantilla mentoria]]; para decisiones, [[Plantilla ADR]].
