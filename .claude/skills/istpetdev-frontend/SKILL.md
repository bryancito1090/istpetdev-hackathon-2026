---
name: istpetdev-frontend
description: Interfaz de IstpetDev. Usar al crear o revisar pantallas y componentes Angular del panel web, la app o PWA del conductor y receptor, la consulta pública por QR, mapas, estados de carga y error, captura offline, accesibilidad, tokens de diseño o textos de la interfaz.
---

# IstpetDev — frontend web y móvil

Rutas relativas a la raíz del repositorio. Leer antes `.agents/skills/istpetdev-contexto/SKILL.md` y `.agents/skills/istpetdev-contrato/SKILL.md`.

## Leer primero

- `03 Arquitectura/Frontend con Feature-Sliced Design.md`: capas, slices, API pública e imports (ADR-13, aceptada).
- `03 Arquitectura/Frontend y componentes.md`: Signals y RxJS, `libs/shared-core`, mapas, consulta QR, RBAC en cliente.
- `03 Arquitectura/Movil offline y sincronizacion.md`: persistencia, protocolo de sincronización y conflictos.
- `02 Producto/Usuarios y flujos.md`: roles, flujo central, excepciones y estados.

## Versiones y decisiones

Versiones exactas solo de `03 Arquitectura/Repositorio de software y versiones.md`; no subir ni bajar ninguna por cuenta propia:

- Angular 22 con TypeScript 6.0, Node 22, RxJS 7.8 y Tailwind 3.4 (ADR-04).
- Móvil: PWA con Ionic 8 e IndexedDB primero; Capacitor 8 solo para el empaquetado nativo posterior (ADR-06).
- Sesión: Cognito con Authorization Code + PKCE (`03 Arquitectura/Identidad OIDC y sesiones.md`); los tokens no entran en la cola offline.
- Librería de mapas: PENDIENTE (ADR-05).

## Reglas FSD

- Capas de arriba abajo: app → pages → widgets → features → entities → shared. Una capa solo importa capas inferiores.
- Cada slice expone su API pública (`index.ts`); sin imports profundos ni entre slices de la misma capa.
- Empezar en la página o entidad y extraer a `features` o `widgets` solo cuando haya reutilización real.
- Contratos y DTOs desde `libs/shared-core`; no redefinir tipos del backend.
- `shared/ui/map-view` es visual y no conoce logística; `widgets/route-map` lo orquesta.

## Reglas de interfaz

- **Cinco estados en cada pantalla o componente con datos:** normal, cargando (skeleton, no el texto «Cargando…»), vacío (mensaje y acción sugerida), error (mensaje y reintento) y sin permiso (qué ve un rol sin acceso).
- **Offline:** distinguir siempre «guardado en el teléfono», «enviando», «aceptado por el servidor», «conflicto» y «evidencia pendiente». Nunca mostrar aceptado lo que solo está en el dispositivo.
- **RBAC en cliente** solo orienta (ocultar botones, guards); la decisión real es del servidor.
- **Accesibilidad WCAG 2.2 AA:** contraste 4,5:1 en texto normal y 3:1 en texto grande; estado que no dependa solo del color; foco visible; objetivos táctiles de al menos 24×24 px (en móvil, 44–48 px); navegación completa con teclado; respetar `prefers-reduced-motion`.
- **Tokens:** ningún color, espaciado, radio o tipografía escrito directamente en un componente; todo sale de tokens semánticos.
- **Textos:** el botón nombra la acción y el resultado usa la misma palabra («Publicar ruta» → «Ruta publicada»); los errores dicen qué pasó y qué hacer.
- **Iconos** de un sistema real (por ejemplo Lucide o el de la librería de componentes elegida); nunca emojis como iconos.
- Consulta pública QR: ruta aislada y liviana, sin datos privados (firmas, teléfonos, ubicación del conductor).

Detalle de identidad visual, tokens y leyes de UX: [references/diseno-y-accesibilidad.md](references/diseno-y-accesibilidad.md).

## Prohibido inventar

- Versiones, librerías o rutas de carpetas no registradas en `00 Inicio/Hechos canonicos.md`.
- Campos o endpoints que no estén en el contrato.
- Un arquetipo visual como decisión del equipo: hasta que se registre, es PENDIENTE (recomendación en las referencias).

## Verificar

- Revisar los cinco estados y el recorrido offline (V-08, V-11 y V-12 de `07 Demo/Plan de validacion.md`).
- Límites FSD (V-23) y build/lint del repositorio cuando existan (comandos PENDIENTES en `00 Inicio/Hechos canonicos.md`).
- Probar en un teléfono real por HTTPS antes de dar por terminado un flujo móvil.

## Origen

Adaptada de las skills personales `frontend-lead-personalidad` (cinco estados, declarar arquetipo, autocrítica, iconos reales), `design-tokens-a11y` (no inventar valores, tokens en tres capas, WCAG 2.2 AA, leyes de UX) e `identidad-visual-brand` (evitar el aspecto genérico de IA, un elemento firma, textos desde el usuario). Se excluyeron, por contradecir la bóveda: preguntar el stack, la estructura Angular con NgModules, `src/components/ui/` y Tailwind v4 como valor fijo.
