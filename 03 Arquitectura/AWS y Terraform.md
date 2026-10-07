---
tipo: arquitectura
estado: propuesta
actualizado: 2026-10-06
tags: [arquitectura, infra, aws, terraform, devops]
---

# AWS y Terraform

Este documento define la arquitectura de infraestructura en la nube y el aprovisionamiento como código (IaC) con Terraform para IstpetDev en el marco del Reto 1 de la Hackathon Expo Clean 2026.

Para garantizar viabilidad económica, velocidad de ejecución en el evento y un camino realista hacia la producción a gran escala, se establece un **Modelo Dual de Infraestructura**:

1. **Perfil A (Hackathon / Demo Ágil y Piloto Operativo):** Servidor AWS EC2 Linux blindado (*hardened*) con Docker Compose, GHCR, Nginx Reverse Proxy y pipeline CI/CD con rollback instantáneo.
2. **Perfil B (Operación Nacional Elástica P2):** Clúster ECS Fargate, Application Load Balancer (ALB), Amazon RDS PostgreSQL con PostGIS Multi-AZ, Redis ElastiCache y buckets S3 privados con ciclo de vida.

```mermaid
flowchart TD
  subgraph Perfil_A [Perfil A: Hackathon y Piloto Ágil (Costo Controlado)]
    ALB_A[Elastic IP / Cloudflare CDN] --> Nginx_A[Nginx Reverse Proxy con TLS 1.3]
    Nginx_A --> API_A[API C# .NET 8 en Loopback 127.0.0.1:5000]
    Nginx_A --> Web_A[Angular Web Standalone FSD en Loopback]
    API_A --> DB_A[(PostgreSQL 16 + PostGIS en Loopback:5432)]
    API_A --> S3_A[S3 Evidencias Privadas]
    API_A --> Redis_A[Redis 7 en Loopback:6379]
  end

  subgraph Perfil_B [Perfil B: Operación Nacional Elástica (P2 Alta Disponibilidad)]
    Route53[Route 53 + ACM TLS] --> ALB_B[Application Load Balancer HTTPS]
    ALB_B --> Fargate_Web[ECS Fargate: Frontend Web]
    ALB_B --> Fargate_API[ECS Fargate: Backend API .NET 8]
    Fargate_API --> RDS_B[(Amazon RDS PostgreSQL + PostGIS Multi-AZ)]
    Fargate_API --> Redis_B[(Amazon ElastiCache Redis)]
    Fargate_API --> S3_B[S3 Evidencias + KMS + Object Lock]
  end
```

---

## 1. Comparativa Técnica y Presupuestaria de Perfiles

| Dimensión | Perfil A (Demo Hackathon / Piloto) | Perfil B (Operación Nacional P2) |
|---|---|---|
| **Cómputo** | 1x EC2 `t3.medium` (2 vCPU, 4 GB RAM, 40 GB gp3) | AWS ECS Fargate (2 a 6 réplicas elásticas) |
| **Base de Datos** | PostgreSQL 16 + PostGIS en contenedor Docker con volumen persistente y backups gzip | Amazon RDS PostgreSQL 16 Multi-AZ (`db.t4g.medium` o `db.m6g.large`) |
| **Tiempo Real** | Redis 7 en contenedor Docker con persistencia AOF | Amazon ElastiCache Redis con replicación Multi-AZ |
| **Punto de Entrada** | Nginx Reverse Proxy en host con TLS 1.3 y mTLS CDN | AWS Application Load Balancer (ALB) con AWS WAF |
| **Evidencias S3** | Bucket S3 privado con URLs presignadas y cifrado SSE-S3 | Bucket S3 privado con KMS administrado y ciclo de vida Glacier |
| **Despliegue** | GitHub Actions DAG + SSH + GHCR + Rollback SHA | GitHub Actions + ECR + ECS Service Update / Blue-Green |
| **Costo Estimado** | **$18 – $28 USD / mes** | **$160 – $280 USD / mes** (por NAT Gateways, ALB y Multi-AZ) |
| **Tiempo de Setup** | **Listo en minutos** con cloud-init o script de hardening | Requiere aprovisionamiento completo de VPC y políticas IAM |

> [!IMPORTANT]
> Para la Hackathon del 16 y 17 de octubre de 2026, **el Perfil A es la base operativa de ejecución**. Garantiza que el equipo no consuma presupuesto innecesario en pasarelas NAT ($32/mes c/u) ni sufra latencias de aprovisionamiento de Fargate durante la competencia, manteniendo una postura de seguridad y blindaje de nivel senior conforme a [[Hardening y seguridad de servidores]]. El Perfil B se formaliza en Terraform como entregable de viabilidad y arquitectura nacional (P2).

---

## 2. Red y Salida a Internet (Egress)

### 2.1 En Perfil A (EC2 Hardened)
* La instancia se ubica en una subred pública de una VPC dedicada.
* Se asocia una **Elastic IP** fija para DNS y certificados TLS.
* Los contenedores internos (API, BD, Redis, n8n) se enlazan forzosamente a la interfaz loopback `127.0.0.1`, haciendo imposible que internet acceda a ellos directamente saltándose el firewall del host.
* La salida a internet hacia GHCR, APIs de Mapas (Mapbox/Google) y DeepSeek se realiza directamente a través del Internet Gateway (IGW) sin incurrir en costos de NAT Gateway.

### 2.2 En Perfil B (ECS Fargate + RDS Multi-AZ)
* **VPC con 2 Zonas de Disponibilidad (AZs):**
  * Subredes públicas (2x): Alojan exclusivamente el Application Load Balancer.
  * Subredes privadas de aplicación (2x): Alojan las tareas ECS Fargate de API y Frontend.
  * Subredes privadas de datos (2x): Alojan el DB Subnet Group de Amazon RDS y ElastiCache.
* **Egress Seguro:** Se evalúa el uso de **VPC Endpoints** (PrivateLink) para S3, ECR, CloudWatch y Secrets Manager para reducir tráfico hacia NAT Gateway y blindar el tránsito de paquetes dentro de la red troncal de AWS.

---

## 3. Estructura Modular de Terraform

El código de infraestructura se organiza de forma desacoplada en `infra/terraform/`:

```text
infra/terraform/
  bootstrap/
    main.tf              Bucket S3 para backend remoto + KMS Key
    outputs.tf
  environments/
    demo/
      main.tf            Composición Perfil A (EC2 Hardened + S3 evidencias)
      variables.tf
      terraform.tfvars
      outputs.tf
    prod/
      main.tf            Composición Perfil B (ECS Fargate + RDS + ALB)
      variables.tf
      terraform.tfvars
      outputs.tf
  modules/
    vpc/                 VPC, subredes públicas/privadas, IGW y route tables
    security_groups/     Security Groups con política Default Deny
    ec2_hardened/        Instancia EC2 con EBS gp3 cifrado y cloud-init
    ecs_fargate/         Clúster ECS, Task Definitions y Services
    rds_postgres/        RDS PostgreSQL 16 con extensión PostGIS
    s3_storage/          Bucket S3 privado para fotos/firmas con bloqueo público
    iam/                 Roles y políticas de ejecución de tareas (Least Privilege)
```

### 3.1 Backend Remoto S3 con Bloqueo Nativo (Terraform 1.10+)

En Terraform moderno, el bloqueo de estado concurrente se gestiona nativamente mediante S3 sin requerir tablas DynamoDB:

```hcl
terraform {
  required_version = ">= 1.10.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.50"
    }
  }

  backend "s3" {
    bucket       = "istpetdev-terraform-state-2026"
    key          = "environments/demo/terraform.tfstate"
    region       = "us-east-1"
    encrypt      = true
    use_lockfile = true  # Bloqueo nativo en S3 (reemplaza DynamoDB)
  }
}
```

### 3.2 Módulo de Seguridad: Security Groups con Mínimo Privilegio

```hcl
# Security Group para Perfil A (Host EC2)
resource "aws_security_group" "ec2_host" {
  name        = "istpetdev-ec2-sg"
  description = "Reglas perimetrales estrictas para host IstpetDev"
  vpc_id      = var.vpc_id

  # Ingreso SSH solo desde IPs administrativas autorizadas
  ingress {
    description = "SSH Administrativo"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.admin_cidr]
  }

  # Tráfico HTTP para redirección y validación ACME Let's Encrypt
  ingress {
    description = "HTTP Publico"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Tráfico HTTPS público hacia Nginx Reverse Proxy
  ingress {
    description = "HTTPS Publico"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Salida permitida (egress hacia GHCR, APIs de mapas e IA)
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Project     = "IstpetDev"
    Environment = var.environment
  }
}
```

---

## 4. Almacenamiento Seguro de Evidencias (Amazon S3)

Para cumplir con la captura de firmas y fotos de entrega descrita en [[Seguridad y evidencias]]:
* Bucket con **Block Public Access** habilitado al 100%.
* Cifrado en reposo obligatorio mediante AWS KMS (`aws:kms`) o SSE-S3 (`AES256`).
* Reglas de ciclo de vida para optimizar costos:
  * Archivos de evidencia en `Standard` durante 30 días.
  * Transición a `Standard-IA` (Infrequent Access) a los 60 días.
  * Opcional: retención inmutable con **S3 Object Lock** para cumplir con no-repudio si se requiere en P2.
* Acceso de lectura temporal concedido exclusivamente mediante **URLs presignadas** generadas por la API con expiración máxima de 15 minutos para usuarios con rol autorizado.

---

## 5. Escalado y Capacidad

### 5.1 Parámetros de Escalado en Perfil B (ECS Fargate)
* **API .NET 8:** Mínimo 2 tareas, máximo 6 tareas. Política Target Tracking con umbral de CPU al **70%** y métrica personalizada de conexiones activas en SignalR.
* **Frontend Web:** Mínimo 2 tareas, máximo 4 tareas.
* **Redis ElastiCache:** Clúster con nodo primario y réplica de lectura para soportar el backplane de SignalR ante múltiples réplicas de la API.
* **RDS PostgreSQL:** Escalado vertical de computo con `db.t4g.medium` (2 vCPU, 4 GB RAM) y almacenamiento auto-expandible gp3 de 20 GB a 100 GB.

### 5.2 Capacidad en Perfil A (EC2 Hardened)
* Instancia `t3.medium` con créditos ilimitados de CPU.
* Swapfile de 2 GB con permisos `0600` para amortiguar picos de memoria.
* Rotación automatizada de imágenes reteniendo solo las últimas 3 versiones para mantener utilización de disco por debajo del 60%.

---

## 6. Procedimiento de Aprovisionamiento y Despliegue

1. **Bootstrap inicial (una sola vez):**
   ```bash
   cd infra/terraform/bootstrap
   terraform init
   terraform apply -auto-approve
   ```
2. **Plan y Validación de Infraestructura (Perfil Demo):**
   ```bash
   cd ../environments/demo
   terraform init
   terraform plan -out=tfplan
   terraform apply tfplan
   ```
3. **Obtención de IP / Host:**
   Terraform exporta la Elastic IP generada. Esta IP se registra en los secretos del repositorio de GitHub (`EC2_HOST`) para que el pipeline CI/CD descrito en [[CI-CD y automatizacion de despliegue]] proceda con el despliegue inmutable.
4. **Hardening del Servidor:**
   Ejecución del runbook de [[Hardening y seguridad de servidores]] para verificar que UFW, Fail2ban, SSH, Nginx y sysctl cumplan con el índice Lynis > 80/100.

Referencias internas: [[Hardening y seguridad de servidores]], [[CI-CD y automatizacion de despliegue]], [[Seguridad y evidencias]], [[Decisiones de arquitectura]].
