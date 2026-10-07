# AGENTS.md — IstpetDev

Reglas comunes para cualquier asistente de IA (Claude Code, Antigravity, Gemini CLI, Codex, GitHub Copilot, Cursor u otros) que trabaje en este repositorio. Las personas del equipo siguen las mismas reglas.

## Qué es este repositorio

Bóveda de Obsidian del equipo **IstpetDev** para el **Reto 1 del Hackathon Expo Clean Ecuador 2026**: optimización y trazabilidad logística para el abastecimiento de insumos de limpieza a nivel nacional (rutas, reabastecimiento crítico y custodia desde bodega hasta recepción).

- Contiene documentación y diseño. **No hay software implementado todavía.**
- El código vivirá en `bryancito1090/istpetdev-platform` (privado, creado vacío el 7 de octubre de 2026; ADR-12). Mientras esté vacío no hay comandos de build, test ni despliegue.
- Idioma de trabajo: español. Nombres de código en inglés (tabla «Nombres en código» de los hechos canónicos).

## Orden de lectura

1. `00 Inicio/Hechos canonicos.md`: versiones, cifras, rutas, puertos, nombres en código, estado de ADR y contradicciones abiertas.
2. `00 Inicio/Contexto maestro.md`: misión, alcance P0/P1/P2 y reglas del equipo.
3. `01 Oficial/Reto 1 oficial.md`: texto literal del reto.
4. `00 Inicio/Convenciones y estados.md`: estados de nota, tipos de afirmación y reglas contra la invención.
5. La skill de `.agents/skills/` que corresponda a la tarea.

## Reglas que no se negocian

1. **No inventar.** Versiones, rutas, puertos, comandos, endpoints, tablas, cifras, costos, fechas, respuestas de la organización, entrevistas, pruebas o quién decidió algo: si no está en la bóveda con fuente, se escribe `PENDIENTE` y se hace una pregunta concreta.
2. **Hechos canónicos primero.** Si un dato aparece distinto en dos notas, vale lo que diga `00 Inicio/Hechos canonicos.md`; si allí está como contradicción abierta, no se elige una opción sin decisión registrada.
3. **Contradicciones a la vista.** No se corrigen en silencio. Se reportan como «⚠️ Contradicción detectada» (hecho nuevo, hecho establecido, impacto, opciones) y se registran en los hechos canónicos.
4. **El manual manda.** Las reglas del evento salen de `99 Fuentes/Manual oficial.pdf` y de las notas de `01 Oficial/`. Las tablas del manual son imágenes; usar las transcripciones marcadas «transcrito de imagen».
5. **El código de las notas es ejemplo no probado.** Los bloques de configuración, scripts, YAML o Terraform de la bóveda no se copian como si estuvieran validados.
6. **Propuesta no es implementación.** «Aceptado» exige Deciders; «validado» exige evidencia enlazada. No hay resultados medidos.
7. **Sin datos sensibles.** Nada de credenciales, tokens, IPs públicas, datos personales ni rutas personales de un equipo.
8. **Una sola fuente por concepto.** Antes de explicar algo, buscar la nota que ya lo explica y enlazarla.
9. **Verificar antes de publicar.** `python .agents/skills/istpetdev-docs/scripts/check_vault.py` debe terminar sin errores.

## Skills del equipo

Formato Agent Skills (`SKILL.md` con `name` y `description`). La fuente es `.agents/skills/`; `.claude/skills/` es una copia generada para Claude Code (`check_vault.py --sync-skills`).

| Skill | Usar para |
|---|---|
| `istpetdev-contexto` | Cualquier tarea: contexto, datos faltantes, contradicciones, certeza de afirmaciones |
| `istpetdev-docs` | Editar la bóveda, ADR, mentorías, evidencias, hechos canónicos; verificador |
| `istpetdev-contrato` | Endpoints, eventos SignalR, DTOs, errores, idempotencia, OpenAPI |
| `istpetdev-backend` | Código C#/.NET: comandos, consultas, inventario, custodia, RBAC, tiempo real |
| `istpetdev-datos` | Modelo de datos, migraciones, riesgo, rutas, dataset, simulador y KPIs |
| `istpetdev-frontend` | Angular web, PWA o app del conductor, QR público, estados de UI, accesibilidad |
| `istpetdev-revision` | Commits (Conventional Commits), PR, checklist, pruebas, seguridad |
| `istpetdev-producto-pitch` | Problema, usuarios, validación, negocio, privacidad, guion y jurado |

## Git

- Trabajar en `develop` (`git pull --ff-only` antes de editar); integrar en `main` cuando esté listo.
- Commits en Conventional Commits (definición en `.agents/skills/istpetdev-revision/SKILL.md`).
- PR con `.github/pull_request_template.md`. No forzar el push sobre ramas compartidas.
- Al cambiar `.agents/skills/`, ejecutar `--sync-skills` e incluir `.claude/skills/` en el mismo commit.

## Índice de notas

Rutas desde la raíz. Dentro de las notas se usan enlaces de Obsidian con doble corchete y el nombre de la nota, que coincide con el nombre del archivo sin `.md`.

| Área | Notas |
|---|---|
| Entrada | `README.md` · `Bienvenido.md` |
| 00 Inicio | `00 Inicio/Hechos canonicos.md` · `00 Inicio/Contexto maestro.md` · `00 Inicio/Convenciones y estados.md` · `00 Inicio/Glosario.md` · `00 Inicio/Mapa de la boveda.md` |
| 01 Oficial | `01 Oficial/Reto 1 oficial.md` · `01 Oficial/Evaluacion y entregables.md` · `01 Oficial/Cronograma oficial.md` · `01 Oficial/Resumen del manual.md` · `01 Oficial/Consultas para la organizacion.md` |
| 02 Producto | `02 Producto/Alcance y prioridades.md` · `02 Producto/Historia y propuesta de valor.md` · `02 Producto/Usuarios y flujos.md` · `02 Producto/Requisitos y aceptacion.md` · `02 Producto/Modelo de negocio y piloto.md` |
| 03 Arquitectura | `03 Arquitectura/Arquitectura del sistema.md` · `03 Arquitectura/Decisiones de arquitectura.md` · `03 Arquitectura/Backend y tiempo real.md` · `03 Arquitectura/Contratos API y eventos.md` · `03 Arquitectura/Frontend con Feature-Sliced Design.md` · `03 Arquitectura/Frontend y componentes.md` · `03 Arquitectura/Movil offline y sincronizacion.md` · `03 Arquitectura/Seguridad y evidencias.md` · `03 Arquitectura/AWS y Terraform.md` · `03 Arquitectura/CI-CD y automatizacion de despliegue.md` · `03 Arquitectura/Hardening y seguridad de servidores.md` · `03 Arquitectura/Repositorio de software y versiones.md` · `03 Arquitectura/Entornos y operacion acordados.md` · `03 Arquitectura/Identidad OIDC y sesiones.md` · `03 Arquitectura/Credenciales y acceso del equipo.md` · `03 Arquitectura/Puesta en marcha del workspace y AWS dev.md` · `03 Arquitectura/AWS temporal para la hackathon y cierre.md` |
| 04 Datos y algoritmos | `04 Datos y algoritmos/Modelo de datos.md` · `04 Datos y algoritmos/Inventario y prediccion.md` · `04 Datos y algoritmos/Rutas y sobrecostos.md` · `04 Datos y algoritmos/Dataset y escenarios.md` · `04 Datos y algoritmos/Simulador y metricas.md` |
| 05 Automatización | `05 Automatizacion/n8n e IA.md` |
| 06 Equipo | `06 Equipo/Backlog.md` · `06 Equipo/Equipo y acuerdos.md` · `06 Equipo/Plan de ejecucion.md` · `06 Equipo/Riesgos y decisiones pendientes.md` · `06 Equipo/Registro de mentorias.md` · `06 Equipo/Registro de trabajo previo y del evento.md` |
| 07 Demo | `07 Demo/Guion del pitch.md` · `07 Demo/Plan de validacion.md` · `07 Demo/Checklist y contingencias.md` · `07 Demo/Plus para ganar.md` |
| 08 Skills | `08 Skills/Catalogo y plan de skills.md` |
| 09 Plantillas | `09 Plantillas/Plantilla ADR.md` · `09 Plantillas/Plantilla evidencia.md` · `09 Plantillas/Plantilla historia de usuario.md` · `09 Plantillas/Plantilla mentoria.md` |
| 99 Fuentes | `99 Fuentes/Fuente y control documental.md` · `99 Fuentes/Informacion inicial del equipo.md` · `99 Fuentes/Manual oficial.pdf` |

## Decisiones pendientes que afectan a los asistentes

Ver la tabla «Contradicciones abiertas» de `00 Inicio/Hechos canonicos.md`. Las principales: proveedor de mapas (ADR-05), TLS solo 1.3 (ADR-15), modo de acceso AWS (SSO o IAM + MFA temporal), cómo llegan las skills al repositorio de código (C-01) y Deciders de ADR-04, 09, 13, 14 y 15. Versiones, identidad y estructura del repositorio ya están cerradas: usar las de `03 Arquitectura/Repositorio de software y versiones.md`, sin elegir otras.
