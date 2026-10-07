---
name: istpetdev-revision
description: Revisión de cambios de IstpetDev antes de commit, push o pull request. Usar para redactar mensajes de commit (Conventional Commits), preparar o revisar un PR hacia develop, aplicar el checklist de calidad, pruebas, seguridad y secretos, y comprobar que documentación, contrato y hechos canónicos siguen consistentes.
---

# IstpetDev — revisión, commits y pull requests

Rutas relativas a la raíz del repositorio. Esta skill es la única definición de Conventional Commits del equipo; las demás la enlazan.

## Flujo de ramas

- Trabajo integrado en `develop`; se integra en `main` cuando está listo (`README.md`).
- Antes de empezar: `git fetch origin`, `git switch develop`, `git pull --ff-only`.
- Cambios grandes en una rama corta desde `develop`: `feat/<tema>`, `fix/<tema>`, `docs/<tema>`, `chore/<tema>`.
- PR hacia `develop` con la plantilla `.github/pull_request_template.md`. Al fusionar, **squash** para dejar un commit por tema.
- **No forzar el push** sobre `develop`, `main` ni ramas que otra persona use (`00 Inicio/Convenciones y estados.md`). Si hay divergencia, integrar conservando los cambios ajenos.
- No borrar ramas de otra persona sin su acuerdo.

## Conventional Commits

Formato:

```text
<tipo>(<alcance opcional>): <descripción en imperativo, 10 a 72 caracteres>

<cuerpo: qué cambia y por qué, con los IDs afectados>

<pie: BREAKING CHANGE, Refs, Co-authored-by>
```

| Tipo | Cuándo |
|---|---|
| `feat` | Nueva funcionalidad visible para usuarios o consumidores de la API |
| `fix` | Corrección de un defecto |
| `docs` | Solo documentación o bóveda |
| `refactor` | Cambio interno sin funcionalidad nueva ni corrección |
| `test` | Pruebas nuevas o corregidas |
| `chore` | Dependencias, configuración, skills, tareas de mantenimiento |
| `ci` | Workflows de integración y despliegue |
| `perf` | Mejora de rendimiento medida |
| `style` | Formato sin cambio de lógica |
| `revert` | Revierte un commit anterior |

No usar mensajes como «fix bug», «cambios», «WIP» o «update file». Alcances sugeridos: `boveda`, `skills`, `backend`, `web`, `movil`, `datos`, `infra`, `n8n`, `pitch`.

## Checklist antes de PR

Severidad de cada observación: 🔴 BLOCKER (no se fusiona) · 🟡 WARNING (corregir o registrar como deuda) · 🟢 SUGGESTION · ℹ️ INFO.

- [ ] `python .agents/skills/istpetdev-docs/scripts/check_vault.py` termina sin errores.
- [ ] Ningún dato inventado: cifras, versiones, rutas y comandos tienen fuente o están en `00 Inicio/Hechos canonicos.md`.
- [ ] Contradicciones nuevas reportadas y registradas, no corregidas en silencio.
- [ ] Cada cambio de comportamiento cita su RF/RNF o ADR.
- [ ] Contrato actualizado antes que la implementación (`.agents/skills/istpetdev-contrato/SKILL.md`).
- [ ] Sin secretos, tokens, IPs públicas, datos personales ni rutas personales.
- [ ] Pruebas del camino feliz y de al menos un error; pasan en la máquina local antes del push (cuando exista código).
- [ ] Si se tocó `.agents/skills/`, se ejecutó `--sync-skills` y `.claude/skills/` va en el mismo commit.
- [ ] Registro en `99 Fuentes/Fuente y control documental.md` si el cambio es relevante.

Checklist completo por categorías: [references/checklist-revision.md](references/checklist-revision.md). Principios de infraestructura y observabilidad para el piloto: [references/infra-y-observabilidad.md](references/infra-y-observabilidad.md).

## Pruebas

- Unitarias para reglas puras; integración con base real (contenedor efímero) para comandos y consultas; extremo a extremo solo para el recorrido de la demo.
- Mocks solo para dependencias externas (mapas, LLM, S3); nunca para la lógica que se prueba.
- Datos de prueba deterministas (seed); nunca datos reales.
- Todo defecto corregido deja una prueba que lo habría detectado.
- Pruebas intermitentes se arreglan o se eliminan; no se repiten hasta que pasen.

## Seguridad del repositorio

- `.env` y secretos fuera de git (ya en `.gitignore`); variables documentadas en un `.env.example` sin valores reales.
- Escaneo de secretos antes del commit cuando exista el repositorio de código (por ejemplo `detect-secrets` o `gitleaks`; herramienta PENDIENTE).
- Protección de ramas en GitHub para `main` y `develop`: PR obligatorio, checks en verde, sin push forzado. Se configura en Settings → Branches.

## Prohibido inventar

- Resultados de pruebas que no se ejecutaron o comandos que no existen en el repositorio.
- Aprobaciones: un PR no se describe como revisado si nadie lo revisó.

## Origen

Adaptada de las skills personales `code-review-assistant` (Conventional Commits, severidades, checklist), `qa-testing-engineer` (pirámide de pruebas, datos deterministas, pruebas intermitentes), `devsecops-github-guardian` (secretos, protección de ramas), `gitlab-workflow-istpet` (asunto de 10 a 72 caracteres, plantilla de MR) y `tech-writer` (plantilla de PR). Se excluyó el commit único con `amend` y `--force-with-lease`, porque contradice la regla del equipo de no forzar el push.
