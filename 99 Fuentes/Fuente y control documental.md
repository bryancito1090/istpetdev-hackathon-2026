---
tipo: fuente
estado: vigente
actualizado: 2026-10-06
tags: [istpetdev, documentacion]
---

# Fuente y control documental

## Fuente oficial recibida

| Campo | Valor |
|---|---|
| Documento | Manual y documento operativo Hackathon Expo Clean Ecuador 2026 |
| Copia portable | [[Manual oficial.pdf]] |
| Páginas | 33, incluyendo portada |
| Ruta de origen | /home/bryan/Downloads/Manual del Hackaton-20261005T134324Z-1-001/Manual del Hackaton/Manual HACKATON EXPO CLEAN Ecuador 2026.pdf |
| Autor en metadatos | Coordinacion Jimcorpservi |
| Creación en metadatos | 23 de septiembre de 2026 |
| SHA-256 | ddcc6b738d0ee2c5c304c5b030686477fbc86f0e607442e70dfe3f55adc6672b |
| Revisión de esta bóveda | 6 de octubre de 2026 |

Se extrajo texto y se revisaron visualmente los cuadros de calendario, entregables, evaluación, jurado y premios. Las notas son resúmenes operativos, no una sustitución del manual.

La copia incluida evita depender de la ruta de Downloads de un integrante. La versión fue aportada por el usuario; no se presume que sea la última publicada.

## Fuentes internas

- [[Informacion inicial del equipo]]: propuesta tecnológica y narrativa recibida.
- Aclaración del usuario del 6 de octubre: IstpetDev, cinco integrantes, experiencia transversal y sin reparto fijo de especialidades.
- Aclaración del usuario del 6 de octubre: adoptar Feature-Sliced Design en frontend web.
- Instrucción del usuario del 6 de octubre: comprobar RBAC y agregarlo si faltaba; modelo aceptado en ADR-14, implementación pendiente.
- [[Registro de trabajo previo y del evento]]: evolución y autoría.
- [[Registro de mentorias]]: respuestas y validación futuras.

## Fuentes técnicas primarias consultadas

Verificadas el **6 de octubre de 2026**; volver a comprobar al cerrar versiones/servicios.

| Tema | Fuente | Nota que aplica |
|---|---|---|
| Soporte .NET | [Política de Microsoft](https://dotnet.microsoft.com/en-us/platform/support/policy) | [[Backend y tiempo real]] |
| SignalR/Redis | [Backplane oficial](https://learn.microsoft.com/en-us/aspnet/core/signalr/redis-backplane?view=aspnetcore-10.0) | [[Backend y tiempo real]] |
| UUID v7 | [PostgreSQL 18](https://www.postgresql.org/docs/18/functions-uuid.html), [PostgreSQL 17](https://www.postgresql.org/docs/17/functions-uuid.html) | [[Decisiones de arquitectura]] |
| Angular offline | [Service workers](https://angular.dev/ecosystem/service-workers) | [[Movil offline y sincronizacion]] |
| Sincronización de fondo | [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Background_Synchronization_API) | [[Movil offline y sincronizacion]] |
| ECS autoscaling | [AWS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html) | [[AWS y Terraform]] |
| PostGIS/RDS | [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.PostGIS.html) | [[AWS y Terraform]] |
| Estado Terraform | [Backend S3](https://developer.hashicorp.com/terraform/language/backend/s3) | [[AWS y Terraform]] |
| Mapas | [Mapbox Matrix](https://docs.mapbox.com/api/navigation/matrix/), [Google Routes](https://developers.google.com/maps/documentation/routes/compute_route_matrix) | [[Rutas y sobrecostos]] |
| n8n | [Queue mode](https://docs.n8n.io/hosting/scaling/queue-mode) | [[n8n e IA]] |
| DeepSeek | [JSON Output](https://api-docs.deepseek.com/guides/json_mode/) | [[n8n e IA]] |
| FSD | [Overview](https://feature-sliced.design/docs/get-started/overview), [capas](https://feature-sliced.design/docs/reference/layers), [slices](https://feature-sliced.design/docs/reference/slices-segments), [API pública](https://feature-sliced.design/docs/reference/public-api) | [[Frontend con Feature-Sliced Design]] |

Estas fuentes verifican límites de plataforma y convenciones; no validan el ahorro de nuestro producto.

## Registro de versiones documentales

| Fecha | Cambio | Alcance |
|---|---|---|
| 2026-10-06 | Bóveda base, manual portable, requisitos y arquitectura | Documentación inicial, sin software implementado |
| 2026-10-06 | Identificación IstpetDev y trabajo flexible | Sin asignación fija de personas |
| 2026-10-06 | Frontend FSD aceptado y plus de competencia | Contexto, frontend, ADR-13 y catálogo de skills |
| 2026-10-06 | RBAC aceptado por instrucción del usuario | Matriz de seis roles en seguridad, ADR-14, datos/contratos, RNF-01, B-29 y V-24; sin software implementado |
| 2026-10-06 | Repositorio privado GitHub creado por instrucción del usuario | bryancito1090/istpetdev-hackathon-2026; README y exclusión de sesiones personales de Obsidian |
| Pendiente | Respuestas de capacitación | Actualizar reglas/alcance al recibirlas |

## Actualizar el manual

Conservar nueva versión sin sobrescribir silenciosamente la anterior. Registrar fecha, origen y hash; revisar cambios en retos, agenda, entregables y evaluación. Enlazar las notas afectadas y marcar qué versión sustenta el pitch.

## Verificación de la bóveda inicial

Revisión del 6 de octubre de 2026: **47 notas Markdown**, **252 enlaces internos resueltos**, metadatos YAML válidos, nombres de nota únicos y bloques de código balanceados. El hash de la copia del PDF coincide con el original recibido. Verificados los enlaces y referencias de FSD en contexto, arquitectura, ADR-13, requisitos, backlog, validación y catálogo de skills.

Esta revisión valida la documentación y navegación; las pruebas de software de [[Plan de validacion]] siguen pendientes de implementación.

Actualización RBAC del 6 de octubre: enlaces internos resueltos, metadatos YAML válidos, nombres únicos, bloques de código balanceados e IDs de ADR/backlog/validación sin duplicados. Revisión de formato con `git diff --check` sin errores. Las pruebas de permisos siguen pendientes de software.

## Fuente y actualización del 7 de octubre de 2026

Fuente de decisiones: instrucción directa de Bryan en la conversación del 7 de octubre. Confirmó cuenta/presupuesto, trabajo local con DB AWS compartida, .NET 8/Angular 22, n8n propio y creación de GitHub vacío/esqueleto local; delegó recomendaciones y pidió conservar el contenido incorporado por su compañero en `4c3a9ef`.

Se agregan [[Repositorio de software y versiones]], [[Entornos y operacion acordados]] e [[Identidad OIDC y sesiones]], con fuentes técnicas primarias fechadas y estados explícitos. Las notas anteriores se conservan y reciben complementos fechados; los ejemplos originales no sustituyen las condiciones posteriores de implementación. El repositorio software remoto se verifica vacío y el esqueleto permanece local. La validación documental revisa conservación del contenido anterior, enlaces, bloques y formato; no afirma pruebas reales de aplicaciones/AWS/n8n.

## Credenciales del equipo — 7 de octubre de 2026

Bryan pide usar AWS e integraciones en equipo sin exponer valores en la bóveda ni en el repositorio de software. Se agrega [[Credenciales y acceso del equipo]], con fuentes oficiales AWS/GitHub/Microsoft enlazadas junto a las decisiones: SSO/MFA, tipos de instancia Identity Center, acceso a Secrets Manager, configuración local y OIDC de Actions. Se documenta la verificación del subject con IDs inmutables indicado por GitHub para repositorios recientes. Se amplían exclusiones de Git y se agregan B-35/V-32; sin crear cuentas cloud, leer/cargar credenciales reales ni ejecutar pruebas AWS en esta actualización.

## Guía de preparación y aprovisionamiento — 7 de octubre de 2026

Se agrega [[Puesta en marcha del workspace y AWS dev]] por solicitud de Bryan: prompt del agente limitado a instalaciones locales, proyectos, IaC/scripts y publicación en develop; luego pasos de consola/terminal para identidad/bootstrap persistente, Terraform dev, PostgreSQL y acceso del equipo. Flujo propuesto y ejecución pendiente. Versiones npm seleccionadas verificadas en el registro oficial; pasos de consola contrastados con documentación primaria AWS/GitHub. No se crearon recursos ni se ejecutó el prompt durante esta entrega.

## Créditos y cierre temporal — 7 de octubre de 2026

Bryan aclara que quiere usar los USD 100 mostrados y retirar infraestructura después de la hackathon. Se agrega [[AWS temporal para la hackathon y cierre]], con advertencia de la consola/fuentes oficiales sobre expiración al crear Organizations, alternativa IAM/MFA con `aws login` y limpieza final. Captura indica término del plan gratuito el 21 de octubre, no prueba de expiración de cada crédito. Se actualiza precedencia de guías/prompt y B-35/V-32, con B-36/V-33 para cierre. No se registra ID de cuenta, no se accede a credenciales ni se ejecuta ninguna operación cloud.
