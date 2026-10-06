---
tipo: arquitectura
estado: propuesta
actualizado: 2026-10-06
tags: [arquitectura, contratos]
---

# AWS y Terraform

## Arquitectura objetivo

Conservar el diseño AWS solicitado: **ECS Fargate para API y web, ALB, RDS PostgreSQL/PostGIS, S3 y autoescalado**, gestionados con Terraform.

**Estado:** diseño; cuenta, región, presupuesto, dominio y versiones pendientes. No se han aprovisionado recursos.

| Componente | Diseño propuesto |
|---|---|
| Red | VPC y subredes en dos zonas; ALB público, datos y cómputo protegidos |
| Entrada | ALB HTTPS; /api y /hubs a API, resto a frontend |
| API/web | Imágenes Docker en ECR, servicios ECS Fargate independientes |
| Datos | RDS PostgreSQL con PostGIS y perfil Multi-AZ |
| Evidencias | S3 privado, cifrado, acceso temporal autorizado y ciclo de vida |
| Tiempo real | Redis administrado como backplane al habilitar varias réplicas |
| Automatización | n8n con PostgreSQL y clave de cifrado persistente; instancia principal única inicialmente |
| Secretos | Secrets Manager/identidades IAM; sin credenciales en imágenes |
| Observabilidad | CloudWatch, health checks, correlación y alarmas |
| DNS/TLS | Dominio y certificado ACM, una vez definidos |

RDS soporta PostGIS, pero la versión de la extensión debe verificarse para el motor y región elegidos. [PostGIS en RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.PostGIS.html).

PostGIS ayuda con cercanía y filtros; las distancias por carretera provienen del proveedor de mapas.

## Escalado

Propuesta inicial: target tracking de CPU promedio **70%**, límites explícitos y cooldowns. No es una garantía de reacción instantánea ni implica una tarea nueva exactamente por cada pico. ECS usa métricas y políticas para ajustar capacidad. [Auto Scaling de ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html).

| Parámetro | Demo acotada | Operación nacional |
|---|---|---|
| API | min 1, max 3, valores por validar | min 2 distribuidas; máximo según carga/presupuesto |
| Frontend | min 1; máximo según medición | min 2; métricas según tráfico |
| SignalR | Redis si API puede tener >1 réplica | Redis con disponibilidad y afinidad probadas |
| RDS | Multi-AZ configurable; activar si recursos lo permiten | Multi-AZ, backups y restauración probada |
| n8n | Principal única, estado durable y reinicio recuperable | Queue mode solo si carga justifica workers |
| Evidencias | S3 privado | S3 con retención y recuperación verificadas |

El perfil acotado permite desarrollo y ensayos. **La meta de alta disponibilidad solicitada es el perfil nacional**; una demo con min 1 o Single-AZ debe declararse como tal.

Autoescalar API no autoescala capacidad de escritura de PostgreSQL. Medir conexiones por réplica, pool, índices, bloqueo y consultas. SignalR necesita considerar conexiones/memoria además de CPU.

## Salida a internet

Contenedores privados necesitan egress hacia ECR, logs, secretos, mapas y DeepSeek. Comparar NAT y endpoints de VPC; la arquitectura no debe dejar dependencias sin acceso. Para alta disponibilidad, no crear una dependencia única de salida sin declarar su efecto.

## Terraform: estructura mínima propuesta

```text
infra/terraform/
  bootstrap/          estado remoto y permisos iniciales
  environments/demo/  composición y variables del entorno
  environments/prod/  cuando realmente exista ese entorno
```

Separar archivos por red, ECS, datos, IAM y observabilidad dentro de la raíz; crear módulos solo cuando exista reutilización clara.

Estado remoto S3 con versionado, cifrado y bloqueo. En Terraform compatible usar **use_lockfile = true**; el bloqueo basado en DynamoDB aparece deprecado en la documentación actual. [Backend S3 de Terraform](https://developer.hashicorp.com/terraform/language/backend/s3).

- Fijar versión de Terraform/proveedor y conservar lockfile.
- Bootstrap separado antes de usar el backend remoto.
- Variables: región, prefijo, dominio, tamaños, límites, Multi-AZ, retención y tags.
- Secrets y state quedan fuera de la bóveda y del control de versiones.
- Recordar que marcar un valor sensible no elimina su contenido del state.
- Revisar plan para reemplazos de RDS, cambios de red y permisos.

## Despliegue reproducible

1. Validar formato/configuración y generar plan.
2. Construir imágenes con tags/versiones inmutables.
3. Publicar imágenes en ECR.
4. Aplicar infraestructura y ejecutar una migración controlada.
5. Desplegar servicios con health checks y verificar recorrido.
6. Conservar versión de imagen, commit, variables sin secretos y resultado del ensayo.
7. Volver a imagen anterior si falla; las migraciones necesitan estrategia compatible.

Este flujo se documenta para implementarlo después; no constituye autorización para gastar presupuesto sin definir cuenta y límite.

## Costos y pruebas

Presupuestar Fargate, ALB, RDS Multi-AZ, Redis, NAT, logs, S3, almacenamiento de n8n y APIs. Levantar precios oficiales con región y fecha cuando se cierre la infraestructura; no asumir Free Tier.

Pruebas: reinicio de API, reconexión, dos réplicas de SignalR, persistencia de n8n y reanudación offline. Para afirmar alta disponibilidad nacional: medir failover/restauración y latencia/errores bajo carga.

Ver [[Decisiones de arquitectura]], [[Plan de validacion]] y [[Riesgos y decisiones pendientes]].
