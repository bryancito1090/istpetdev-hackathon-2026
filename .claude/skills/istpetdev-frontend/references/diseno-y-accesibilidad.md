# Diseño visual, tokens y accesibilidad

Referencia de la skill `istpetdev-frontend`. Nada de esto reemplaza una decisión del equipo: lo marcado PENDIENTE se confirma y se registra en `00 Inicio/Hechos canonicos.md`.

## Arquetipo visual

Estado: **PENDIENTE de decisión del equipo.**

Recomendación: **B — técnico/minimalista** (al estilo de herramientas de operación como Linear o Vercel): función antes que decoración, espacio en blanco generoso, tipografía sans neutral y tipografía monoespaciada para cifras, color solo donde hay acción o estado. Encaja con un panel logístico denso en datos y con un jurado que debe leer cifras rápido.

Alternativa: **C — producto pulido** (redondeos generosos, paleta cálida sobria, microanimaciones sutiles) si el equipo prefiere un tono más comercial para la app del receptor.

No usar arquetipos expresivos (neumorfismo, aurora, retro) en pantallas densas en datos o críticas en accesibilidad.

## Evitar el aspecto genérico de IA

Salvo que el equipo lo pida expresamente, no usar:

- Fondo crema con acento terracota.
- Fondo negro puro con un único acento neón.
- Diseño tipo periódico con líneas finas y cero radio de borde.
- Tailwind sin tokens propios.

Gastar la audacia en **un solo elemento firma** (por ejemplo, la línea de tiempo de custodia de la caja) y mantener el resto disciplinado. Animar solo cuando informe algo (carga, cambio de estado).

## Tokens en tres capas

1. **Primitivos:** valores puros (`blue-500`).
2. **Semánticos:** propósito (`--color-action-primary`, `--color-status-risk`).
3. **Componente:** uso concreto (`--button-primary-bg`).

Ningún componente usa primitivos ni valores directos. Antes de crear un token o componente nuevo, buscar si ya existe uno equivalente.

## Estados de riesgo y entrega

El estado nunca depende solo del color: acompañarlo de texto e icono.

| Estado | Texto mínimo |
|---|---|
| Riesgo crítico | «Crítico: X días de cobertura» |
| En tránsito | «En tránsito» con hora del último evento |
| Guardado en el teléfono | «Guardado en el teléfono; pendiente de envío» |
| Aceptado | «Aceptado por el servidor» con hora del servidor |
| Conflicto | «Conflicto: requiere revisión» con el motivo |

## Leyes de UX aplicadas

- **Miller:** máximo 5–7 elementos en la navegación principal y 5–7 campos por paso de formulario.
- **Hick:** pocas opciones visibles a la vez; la acción principal explícita («Publicar ruta», no «Aceptar»).
- **Fitts:** la acción principal es la más grande y cercana al pulgar en móvil; las destructivas, lejos.
- **Tesler:** el sistema absorbe la complejidad (valores por defecto, validación en tiempo real).
- **Jakob:** no reinventar patrones estándar de navegación.

## Accesibilidad (WCAG 2.2 AA)

- Contraste 4,5:1 en texto normal y 3:1 en texto grande o en negrita.
- Foco de teclado visible y no tapado por barras fijas.
- Objetivos táctiles de al menos 24×24 px en web; en móvil seguir 44 pt (iOS) o 48 dp (Android).
- Todo arrastre tiene alternativa por clic.
- Permitir pegar contraseñas y usar gestores; no exigir pruebas cognitivas.
- Respetar `prefers-reduced-motion`.

Origen: adaptado de las skills personales `frontend-lead-personalidad`, `design-tokens-a11y` e `identidad-visual-brand`.
