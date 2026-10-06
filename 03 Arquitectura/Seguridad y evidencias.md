---
tipo: arquitectura
estado: propuesta
actualizado: 2026-10-06
tags: [arquitectura, contratos]
---

# Seguridad y evidencias

## Identidad y autorización

Identidad común web/móvil mediante un proveedor estándar compatible OIDC, pendiente de elegir. No desarrollar un sistema de autenticación propio solo para el hackathon.

El servidor deriva el actor de su sesión. Valida organización, punto, asignación y permiso de acción en cada endpoint y grupo SignalR. El cliente no puede convertir un actorId enviado en autoridad.

Para captura offline: permitir solo asignaciones previamente descargadas. La aceptación en nube requiere sesión válida; una sesión expirada conserva la cola y solicita reautenticación.

## QR y consulta del jurado

Cada **unidad logística** tiene ID interno y líneas de lote. UUID v7 puede identificarla; el lote también tiene identidad propia. Si una caja lleva un único lote, la pantalla lo muestra, pero no se asume que caja y lote son siempre lo mismo.

Contenido propuesto del QR: URL de consulta con ID de unidad y token público aleatorio revocable. El UUID no es un secreto. El token público habilita solo el resumen deliberadamente compartido; escanear no autoriza una entrega.

Consulta pública:

- SKU/unidad, estado y hitos generales permitidos.
- Sin firmas, documentos personales, teléfonos, ubicación exacta del conductor o rutas de toda la empresa.
- Sin acceso a endpoints de escritura.
- Revocación del enlace si se publicó por error.
- Protección frente a consultas masivas y errores que revelen inventario privado.

Para recibir, el conductor usa su cuenta y asignación; la consulta del jurado es independiente.

## Evidencia de entrega

1. Capturar foto/firma de demostración voluntaria y cantidades.
2. Guardar archivo local durable y checksum.
3. Pedir a la API autorización de carga ligada a recepción/asignación.
4. Cargar a S3 privado con límite de tipo/tamaño y clave controlada.
5. Confirmar metadatos y validar que el objeto existe/corresponde.
6. Dar acceso temporal de lectura solo a actores autorizados.

Una URL presignada no vuelve público el bucket. No almacenar firmas como URLs públicas ni incluirlas en logs.

Registrar por archivo: evidenceId, receiptId, tipo, objectKey, checksum, tamaño, hora y estado. Conservar originales frente a sobreescrituras accidentales con versionado cuando corresponda.

## Auditoría e inmutabilidad

Movimientos y custodia se añaden; correcciones crean entradas compensatorias con motivo. Permisos de aplicación impiden modificar/borrar historial; las proyecciones actuales sí pueden actualizarse.

Esto ofrece **historial auditable de solo adición para la aplicación**, no inmutabilidad absoluta frente a un administrador de base de datos. El pitch debe decir lo que está implementado.

Plus opcional: hashes encadenados y copia de digest a almacenamiento protegido. Un hash dentro de la misma base modificable no impide que un atacante reescriba toda la cadena. Si se usa S3 Object Lock o firma externa, definir configuración y verificarla antes de prometer resistencia a manipulación.

## Datos para demo

Usar puntos, personas, fotos y firmas ficticias/autorizadas. La IA recibe únicamente métricas necesarias anonimizadas; no fotos, firmas, datos de identidad o ubicaciones sensibles por defecto.

Mantener separados:

- Inventario y eventos operativos.
- Escenarios y eventos demo.
- Datos locales del dispositivo.
- Evidencias compartibles para evaluación.

El generador de incidentes solo funciona en entorno de demo y con credencial limitada. No publicar una interfaz para inyectar incidentes a operación real.

## Verificación

Probar acceso ajeno a entrega, modificación del token QR, reutilización de URL expirada, exceso de archivo, actor falsificado y salto a grupos SignalR. Los criterios están en [[Plan de validacion]].
