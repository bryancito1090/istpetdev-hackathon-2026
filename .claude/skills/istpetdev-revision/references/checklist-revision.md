# Checklist de revisión por categorías

Marcar cada ítem con ✅, ❌ o ⚠️. Un ❌ en trazabilidad, seguridad o datos inventados es BLOCKER.

**PR:** número y título · **Autor:** · **Revisor:** · **Requisitos o ADR:** · **Fecha:**

## 1. Trazabilidad y veracidad

| Ítem | Estado |
|---|:---:|
| Cada cambio de comportamiento cita RF/RNF o ADR | |
| Ninguna cifra, versión, ruta o comando sin fuente o fuera de los hechos canónicos | |
| Datos sintéticos y resultados simulados etiquetados | |
| Contradicciones nuevas reportadas y registradas | |

## 2. Arquitectura

| Ítem | Estado |
|---|:---:|
| Dominio sin dependencias de infraestructura | |
| Comandos y consultas separados | |
| Sin lógica de negocio en controladores ni componentes de UI | |
| DTOs en la API; entidades de dominio no expuestas | |
| Imports FSD hacia capas inferiores y por API pública | |

## 3. Datos e invariantes

| Ítem | Estado |
|---|:---:|
| Movimiento, saldo e idempotencia en una transacción | |
| Sin saldo negativo ni recepción mayor a lo despachado | |
| Migración reversible o riesgo documentado; ninguna migración aplicada fue editada | |
| Cantidades con unidad base | |

## 4. Calidad de código

| Ítem | Estado |
|---|:---:|
| Sin duplicación entre archivos del cambio | |
| Nombres en el lenguaje del dominio (tabla de nombres en código) | |
| Errores con tipos explícitos | |
| Sin código comentado ni código de depuración | |
| `TODO` y `PENDIENTE` con motivo | |

## 5. Pruebas

| Ítem | Estado |
|---|:---:|
| Camino feliz y al menos un error cubiertos | |
| Integración con base real si hay transacciones | |
| Pasan en la máquina local antes del push | |

## 6. Seguridad

| Ítem | Estado |
|---|:---:|
| Autenticación y autorización RBAC en cada endpoint o acción SignalR | |
| Entradas validadas | |
| Sin secretos, tokens, IPs públicas ni datos personales | |
| Logs sin datos sensibles | |

## 7. Rendimiento

| Ítem | Estado |
|---|:---:|
| Sin consultas N+1 | |
| Listados paginados | |
| E/S asíncrona | |

## 8. Documentación

| Ítem | Estado |
|---|:---:|
| Mensaje en Conventional Commits | |
| Contrato y bóveda actualizados si cambió la interfaz o un dato | |
| `check_vault.py` sin errores | |
| Skills sincronizadas si se tocaron | |

## Decisión

- [ ] Aprobado
- [ ] Aprobado con observaciones (WARNING documentados)
- [ ] Requiere cambios (hay al menos un BLOCKER)

Origen: adaptado de la skill personal `code-review-assistant` (checklist de code review).
