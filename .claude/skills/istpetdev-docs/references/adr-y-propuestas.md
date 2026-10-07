# ADR, propuestas y PRD breves

Plantillas para registrar decisiones y propuestas en la bóveda. La plantilla de Obsidian equivalente está en `09 Plantillas/Plantilla ADR.md`.

## Cuándo usar cada una

| Documento | Cuándo | Dónde |
|---|---|---|
| ADR | Una decisión difícil de revertir: stack, versiones, topología, datos, seguridad, repositorio | Tabla y sección en `03 Arquitectura/Decisiones de arquitectura.md` |
| Propuesta (RFC breve) | Antes de un cambio con impacto en contratos, datos o infraestructura | Nota nueva con estado `propuesta` o comentario en el PR |
| PRD breve | Una funcionalidad nueva con usuario, requisitos y aceptación | `02 Producto/Requisitos y aceptacion.md` (filas RF/RNF) y `09 Plantillas/Plantilla historia de usuario.md` |

## ADR

```markdown
## ADR-XX — Título de la decisión

**Estado:** propuesta | aceptado | reemplazado por ADR-YY
**Fecha:** AAAA-MM-DD
**Deciders:** nombres o roles (obligatorio para «aceptado»)
**Origen:** acta, mentoría o instrucción de una persona identificada
**Registrado por (commit):** usuario de git y hash

### Contexto
Situación, requisito afectado (RF/RNF) y fuerzas en juego: técnicas, de negocio, de tiempo.

### Opciones
| Opción | Ventaja | Costo o límite |
|---|---|---|
| A | | |
| B | | |

### Decisión
La elección en una frase y su motivo concreto.

### Consecuencias
Positivas, negativas aceptadas y cambios en datos, contratos, UX, infraestructura, costos o pruebas.

### Alternativas rechazadas
| Alternativa | Razón |
|---|---|

### Verificación
Evidencia que permite aceptar la decisión y límites conocidos.
```

Reglas: un ADR no se borra; si cambia, se crea otro y el anterior pasa a «reemplazado por». Al aceptar, actualizar la tabla de ADR de `00 Inicio/Hechos canonicos.md`.

## Propuesta (RFC breve)

```markdown
## Propuesta: título

**Estado:** borrador | en revisión | aceptada | rechazada
**Autor:** nombre o rol · **Fecha:** AAAA-MM-DD

- Motivación: por qué y por qué ahora.
- Alternativas: mínimo dos, con ventajas y desventajas.
- Propuesta: qué se cambia y en qué notas, contratos o archivos.
- Riesgos y mitigación.
- Criterio de éxito verificable.
```

## Priorización MoSCoW

Para decidir alcance con poco tiempo:

| Funcionalidad | Must | Should | Could | Won't |
|---|:---:|:---:|:---:|:---:|
| Descripción breve | ✓ | | | |

«Must» corresponde a P0 en `02 Producto/Alcance y prioridades.md`. Lo que se marque «Won't» se registra como fuera de alcance, no se borra.

Origen: adaptado de la skill personal `product-manager` (plantillas PRD, RFC y ADR).
