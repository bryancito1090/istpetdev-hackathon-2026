---
tipo: arquitectura
estado: propuesta
actualizado: 2026-10-06
tags: [arquitectura, implementacion]
---

# Frontend y componentes

## Panel web

Angular con **Standalone Components** y Tailwind, según propuesta del equipo. Fijar versiones de Angular, Node, Ionic y Tailwind después de verificar compatibilidad, antes de generar sus skills.

Pantallas principales:

| Pantalla | Acción de usuario | Información imprescindible |
|---|---|---|
| Resumen operativo | Identificar puntos prioritarios | Stock, cobertura, lead time, riesgo y frescura del dato |
| Planificación | Comparar y aprobar ruta | Distancia, costo, capacidad, ventanas y pendientes |
| Inventario | Consultar y registrar movimientos | SKU/unidad, lote, saldo y origen |
| Entrega | Seguir y conciliar | Estado, cantidades, custodia y evidencia pendiente |
| Incidentes/chat | Resolver situación | Asignación, mensaje, resolución y nueva versión de ruta |
| Simulador | Ejecutar y revisar comparación | Seed, supuestos, resultados y exportación |
| Consulta QR | Ver trazabilidad autorizada | Resumen permitido, sin información privada |

## Estructura de componentes

IstpetDev adoptó **Feature-Sliced Design (FSD)** para el frontend web. Capas: app → pages → widgets → features → entities → shared. La estructura, límites de imports y API pública están en [[Frontend con Feature-Sliced Design]].

Las páginas componen widgets y acciones; entidades concentran contratos propios del dominio; shared mantiene UI y capacidades genéricas. Promover piezas por reutilización real y mantener dependencias hacia capas inferiores.

Componentes iniciales justificables: tarjeta de KPI, estado con texto/icono, tabla paginada, formulario de cantidad/unidad y visor de línea temporal. El mapa recibe paradas y geometría; no decide prioridad ni costo.

Los clientes de API reflejan [[Contratos API y eventos]]. Calcular reglas críticas en backend; la web puede previsualizar, pero no autorizar stock por su cuenta.

## Convenciones iniciales

- Tipos explícitos en límites y DTOs.
- Estado de carga, vacío, error y datos desactualizados por pantalla.
- Formularios con validación y errores del servidor visibles.
- Operaciones de escritura con indicador y protección de doble envío.
- SignalR invalida/refresca datos; no aplicar movimientos contables solo desde un evento.
- Usar capacidades nativas de Angular antes de incorporar un gestor de estado.
- Tailwind para estilos; extraer componentes por comportamiento/reutilización, no por cada bloque visual.
- Separar mapa tradicional/optimizado con leyenda y controles legibles.

## Diseño para el jurado y para operación

El mapa debe responder «qué punto está en riesgo, por qué y qué acción se propone». Una ruta pintada sin restricciones o cálculos no demuestra mejora.

Cada KPI muestra valor, unidad, período, tamaño de muestra y etiqueta **simulado** cuando corresponda. El enlace al detalle abre sus datos de origen y fórmula.

Accesibilidad: no depender solo de rojo/verde; contraste, foco visible, etiquetas y navegación por teclado. En móvil, botones de captura y sincronización fáciles de pulsar; evitar acciones críticas escondidas.

## Criterios de cierre

- Mismo riesgo y saldo en web y API.
- Ruta aprobada identificada por versión.
- Entrega parcial y evidencia pendiente comprensibles.
- Error de IA no bloquea el flujo.
- Datos de simulación nunca se mezclan silenciosamente con operación.
- El recorrido de [[Guion del pitch]] puede ejecutarse sin navegar por pantallas de administración innecesarias.

Ver [[Catalogo y plan de skills]] para transformar estas convenciones en instrucciones reutilizables.
