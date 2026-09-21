# Adaptación de MoProSoft a las prácticas de GitHub

> **Referencia normativa:** MoProSoft (NMX-I-059-NYCE) — categorías Operación y Gerencia
> **Proyecto:** Plataforma de trazabilidad textil para vendedores-tejedores de Santo Tomás Ocotepec (TisaaSavi)

## Objetivo

Traducir las categorías y procesos de MoProSoft en primitivas concretas de GitHub (Issues, ramas, Pull Requests, Actions), de modo que seguir el flujo normal de trabajo en el repositorio sea, en sí mismo, aplicar el estándar — no un documento aparte que nadie consulta.

---

## 1. Categoría Operación

### 1.1 Administración de Proyectos Específicos (APE)

| Práctica MoProSoft | Implementación en GitHub |
|---|---|
| Planificación de la historia como proyecto específico | Cada historia (HU-01 a HU-05) es un Issue con criterios de aceptación explícitos (Fase 1 de la checklist) |
| Seguimiento del avance | El tablero del Project (columnas 1. Backlog → 5. Terminado) refleja el estado real de cada historia |
| Cierre formal | Una historia se cierra solo cuando su Pull Request fue aprobado y fusionado, no cuando "ya casi está" |

### 1.2 Desarrollo y Mantenimiento de Software (DMS)

| Práctica MoProSoft | Implementación en GitHub |
|---|---|
| Separación de Prevención y Corrección | Documentado historia por historia en el Plan de Calidad (Costo de la Calidad) |
| Revisión de pares antes de integrar | CK-3.5 de la checklist: aprobación mínima de un par antes del merge |
| Verificación funcional | CK-2.4: revisión local antes de subir cada commit |

---

## 2. Categoría Gerencia

### 2.1 Gestión de Proyectos (GPY)

| Práctica MoProSoft | Implementación en GitHub |
|---|---|
| Presupuesto por tramos verificables | El Costo de la Calidad por historia (Plan de Calidad, Sección 4) alimenta la planeación de cada sprint |
| Control de cambios formal | Fases 2 y 3 de la checklist: Conventional Commits + plantilla de Pull Request obligatoria |

### 2.2 Gestión de Recursos (GR)

| Práctica MoProSoft | Implementación en GitHub |
|---|---|
| Administración de infraestructura | El repositorio, sus ramas y el workflow de auditoría se gestionan como infraestructura formal del proyecto |
| Conocimiento de la organización | El cuestionario de dolores y las historias de usuario se conservan versionadas en el repositorio, no solo en la memoria del equipo |

### 2.3 Gestión de Procesos (GP)

| Práctica MoProSoft | Implementación en GitHub |
|---|---|
| Medición y mejora del proceso | `scripts/audit_tool.py` mide el cumplimiento cada vez que se ejecuta, permitiendo comparar auditorías sucesivas |
| Acción correctiva documentada | Todo hallazgo de la auditoría se registra con severidad, impacto y responsable antes de cerrarse |

---

## 3. Nota sobre el contexto Mixteca

Dos prácticas de la checklist (CK-3.3 y CK-3.4) existen específicamente porque el proyecto opera en un contexto que MoProSoft, al ser un estándar general, no contempla por sí solo:

- **Conectividad limitada:** ningún cambio debe romper el registro offline-first de HU-02, aunque técnicamente "funcione" con conexión de laboratorio.
- **Protección de datos de pago:** la CLABE de las tejedoras (HU-05) nunca debe aparecer en texto plano en el repositorio, en un log de error, ni en un mensaje de commit.

Estas dos reglas se agregan como extensión del estándar, no como sustituto de él.
