# Infraestructura y observabilidad

Principios para revisar cambios de despliegue. El diseño de infraestructura vive en `03 Arquitectura/AWS y Terraform.md`, `03 Arquitectura/CI-CD y automatizacion de despliegue.md` y `03 Arquitectura/Hardening y seguridad de servidores.md`; esos documentos son ejemplos no probados hasta que exista evidencia.

## Para la demo del hackathon

- Imágenes Docker multi-etapa: compilar en una etapa y ejecutar en otra mínima.
- El proceso principal del contenedor no corre como `root`.
- `.dockerignore` excluye `.env`, `.git` y dependencias locales.
- Servicios internos (API, PostgreSQL, Redis, n8n) publicados solo en `127.0.0.1` o en la red interna de Docker.
- Health checks que comprueban dependencias (base de datos), no solo que el proceso responde.
- Rollback probado en el ensayo, con el tiempo medido y anotado; sin medición no se afirma «menos de 30 segundos».
- Respaldo de la base antes de migrar, y que el pipeline falle si el respaldo falla.

## Para el piloto (no bloquea la demo)

- Ambientes separados de desarrollo, staging y producción, con credenciales distintas.
- Infraestructura como código revisada en PR, igual que el software.
- Secretos en un gestor (por ejemplo AWS Secrets Manager), con rotación.
- Recursos etiquetados por proyecto y ambiente; autoescalado siempre con límite máximo.
- Despliegues sin interrupción (rolling o blue-green) cuando el servicio lo requiera.

## Observabilidad

- Logs estructurados en JSON con nivel, hora, `correlationId` y `operationId`.
- Métricas de errores y latencia p95/p99; el promedio oculta los peores casos.
- Cada error con contexto suficiente para reproducirlo.
- Nunca registrar contraseñas, tokens, firmas, fotos ni datos personales, tampoco en modo depuración.
- Pregunta de cierre para cada flujo crítico: si falla en producción, ¿quién se entera y con qué contexto?

Origen: adaptado de las skills personales `infra-devops-cloud` y `observability-performance`.
