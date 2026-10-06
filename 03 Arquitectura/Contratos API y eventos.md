---
tipo: arquitectura
estado: propuesta
actualizado: 2026-10-06
tags: [arquitectura, contratos]
---

# Contratos API y eventos

**Versión inicial propuesta:** REST /api/v1 y hub /hubs/operations. Será la fuente compartida para web, móvil, n8n y backend. No son endpoints ya implementados.

## Convenciones

- JSON camelCase; fechas ISO 8601 UTC en servidor.
- UUID como texto; cantidades con precisión decimal y unidad explícita.
- Cliente siempre indica operationId en escrituras reintentables; clave enviada como Idempotency-Key.
- Actor real derivado de autenticación, nunca confiado desde el payload.
- organizationId validado contra sesión, aunque exista en una referencia.
- version/expectedVersion para cambios concurrentes.
- Paginación y filtros acotados; no devolver todo el historial nacional.
- correlationId para seguir una operación.
- Entornos de demo y sus datos están identificados.
- Generar OpenAPI desde la API y verificar clientes contra esa definición cuando exista.

## Endpoints propuestos

| Método y ruta                                | Función                                 |
| -------------------------------------------- | --------------------------------------- |
| GET /api/v1/service-points                   | Puntos y filtros                        |
| GET /api/v1/inventory                        | Saldos por ubicación/SKU/lote           |
| POST /api/v1/lots                            | Registrar lote                          |
| POST /api/v1/handling-units                  | Crear caja/unidad y líneas de lote      |
| POST /api/v1/consumptions                    | Registrar uso de insumo                 |
| GET /api/v1/risks                            | Riesgos con cálculo                     |
| POST /api/v1/replenishment-requests          | Solicitar cantidad y fecha              |
| POST /api/v1/route-plans                     | Calcular propuesta, 202 si es asíncrono |
| GET /api/v1/jobs/{id}                        | Estado y resultado de trabajo           |
| POST /api/v1/route-plans/{id}/publish        | Aprobar/publicar versión                |
| POST /api/v1/deliveries/{id}/dispatch        | Registrar salida y custodia             |
| POST /api/v1/deliveries/{id}/receipts        | Recepción por líneas, idempotente       |
| POST /api/v1/receipts/{id}/evidence-uploads  | Obtener autorización de carga           |
| POST /api/v1/evidence/{id}/confirm           | Confirmar objeto y metadatos            |
| GET /api/v1/handling-units/{id}/trace        | Historial autorizado                    |
| GET /api/v1/public/trace/{unitId}?token=...  | Resumen público deliberado              |
| POST /api/v1/incidents                       | Incidente operativo autorizado          |
| POST /api/v1/demo/incidents                  | Incidente sintético, solo demo          |
| POST/GET /api/v1/conversations/{id}/messages | Envío/historial durable                 |
| POST /api/v1/simulations                     | Iniciar escenario comparativo           |
| GET /api/v1/simulations/{id}/metrics         | Resultados y denominadores              |
| POST /api/v1/automation/risk-runs            | Solicitar cálculo programado            |
| POST /api/v1/automation/risk-explanations    | Adjuntar explicación validada           |

## Recepción offline: ejemplo de contrato

```json
{
  "operationId": "UUID_UNICO_DEL_DISPOSITIVO",
  "expectedDeliveryVersion": 4,
  "occurredAtDevice": "2026-10-17T16:05:00Z",
  "lines": [
    {
      "deliveryLineId": "UUID_LINEA",
      "lotId": "UUID_LOTE",
      "quantityReceived": "12.000",
      "unit": "L"
    }
  ],
  "evidenceLocalRefs": ["FOTO_LOCAL_1", "FIRMA_LOCAL_1"]
}
```

El ejemplo usa placeholders, no UUIDs válidos. El servidor valida unidad, cantidades restantes y lote. Las referencias locales no prueban que ya exista evidencia en S3. Respuesta: receiptId, acceptedAtServer, deliveryVersion, estado operativo y estado de evidencia.

## Idempotencia

| Situación                          | Resultado                                      |
| ---------------------------------- | ---------------------------------------------- |
| Clave nueva + operación válida     | Registrar efecto y resultado en un commit      |
| Misma clave + misma huella         | Devolver resultado previo sin nuevo movimiento |
| Misma clave + contenido distinto   | 409 con código IDEMPOTENCY_CONFLICT            |
| Clave nueva + duplicado de negocio | Rechazo/conflicto según cantidades restantes   |
| Validación fallida                 | Error claro; no registrar cambio parcial       |

Definir período de conservación que cubra reintentos offline; no expirar claves antes de la ventana de trabajo del dispositivo.

## Errores

Usar Problem Details con código estable, correlationId y errores de campos. HTTP 400 para entrada inválida, 401 sin sesión válida, 403 sin permiso, 404 para referencia inaccesible/inexistente, 409 para conflicto y 422 para restricción de negocio acordada. 429/503 son reintentables con espera; no reintentar ciegamente errores definitivos.

El conflicto devuelve información permitida para resolverlo, sin exponer datos de otra organización.

## Eventos de dominio y SignalR

Eventos iniciales: StockChanged, RiskCalculated, RoutePublished, IncidentCreated, DeliveryDispatched, ReceiptAccepted, EvidenceCompleted, MessageCreated.

Envelope: eventId, eventType, schemaVersion, aggregateId, aggregateVersion, occurredAtServer, correlationId y payload mínimo autorizado. Las notificaciones se originan después de persistir. Puede haber duplicados y reconexiones; el cliente compara versión y consulta REST.

El hub ofrece notificaciones autorizadas; el historial y las escrituras críticas siguen en API.

## Contrato n8n

La API devuelve riskId, stockSnapshotId, valores calculados y referencias de entrada. n8n devuelve riskId, runId, explicación, provider/model/promptVersion y estado. No permite que DeepSeek cambie stock, prioridad oficial calculada ni fechas de entrega.

Ver [[n8n e IA]], [[Modelo de datos]] y [[Movil offline y sincronizacion]].
