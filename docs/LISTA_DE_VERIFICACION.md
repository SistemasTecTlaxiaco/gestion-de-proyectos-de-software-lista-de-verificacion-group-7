# Lista Maestra de Verificación de Calidad y Control de Cambios (Tema 2.5)

> **Asignatura:** Gestión de Proyectos de Software
> **Institución:** Instituto Tecnológico de Tlaxiaco (Sistemas Tec Tlaxiaco)
> **Equipo:** Grupo 7
> **Proyecto:** Plataforma de trazabilidad textil para vendedores-tejedores de Santo Tomás Ocotepec (TisaaSavi)
> **Referencia normativa:** MoProSoft (Operación: APE, DMS · Gerencia: GPY, GR, GP)

---

## 1. Introducción y propósito

Esta Lista de Verificación es el instrumento operativo con el que el equipo revisa el control de cambios del repositorio `gestion-de-proyectos-de-software-plantilla-plan-de-calidad-group-7`. Ningún cambio se integra a `main` sin pasar por las puertas de calidad descritas aquí.

A diferencia de una checklist genérica, cada punto de control está anclado a una de las 5 historias reales del backlog (HU-01 a HU-05) y al contexto real del proyecto: conectividad intermitente en la región Mixteca y protección de los datos bancarios (CLABE) de las tejedoras.

---

## 2. Fases de la lista de verificación

```
[Fase 1: Pre-Desarrollo] ---> [Fase 2: Construcción y Commit] ---> [Fase 3: Pre-Integración (PR)] ---> [Fase 4: Auditoría y Línea Base]
```

---

### Fase 1 — Pre-Desarrollo (definición y trazabilidad de requerimientos)

*Objetivo: asegurar que todo trabajo responde a una historia de usuario real, no a una idea suelta.*

| Código | Punto de control | Responsable | Criterio de aprobación |
|---|---|---|---|
| CK-1.1 | Existencia de Issue o historia de usuario | Desarrollador | Existe un Issue en GitHub vinculado a HU-01, HU-02, HU-03, HU-04 o HU-05 |
| CK-1.2 | Criterios de aceptación identificados | Desarrollador | Se especifica cuáles criterios de aceptación de esa historia se van a cumplir con el cambio |
| CK-1.3 | Rama temática aislada | Desarrollador | La rama parte de `main` actualizada y sigue la convención `feature/<nombre>`, `fix/<nombre>`, `docs/<nombre>` |

### Fase 2 — Construcción y Commit (disciplina de configuración local)

*Objetivo: mantener el repositorio limpio y el historial legible.*

| Código | Punto de control | Responsable | Criterio de aprobación |
|---|---|---|---|
| CK-2.1 | Respeto del `.gitignore` | Desarrollador | `git status` no muestra archivos de configuración local, claves ni carpetas temporales |
| CK-2.2 | Formato de Conventional Commits | Desarrollador | Cada commit usa un prefijo estándar: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:` |
| CK-2.3 | Atomicidad del commit | Desarrollador | Cada commit resuelve una sola unidad lógica de cambio, no varias mezcladas |
| CK-2.4 | Verificación local antes de subir | Desarrollador | El cambio se revisó manualmente (o con pruebas, si aplica) antes de hacer push |

### Fase 3 — Pre-Integración y Pull Request (revisión de pares y CI)

*Objetivo: que ningún cambio se integre sin que otra persona del equipo lo revise.*

| Código | Punto de control | Responsable | Criterio de aprobación |
|---|---|---|---|
| CK-3.1 | Plantilla de PR completa | Desarrollador | Se llenan todos los campos de `.github/PULL_REQUEST_TEMPLATE.md` |
| CK-3.2 | Pipeline automatizado en verde | CI / Actions | El workflow `audit.yml` termina en estado exitoso |
| CK-3.3 | Verificación de resiliencia offline | Revisor (par) | Se confirma que el cambio no rompe el registro offline-first de HU-02 ni depende de conexión constante |
| CK-3.4 | Protección de datos de pago (CLABE) | Revisor (par) | Se revisa que ningún log, commit o archivo exponga la CLABE de una tejedora en texto plano (HU-05) |
| CK-3.5 | Aprobación mínima de un par | Revisor (par) | Al menos un integrante distinto al autor aprueba el Pull Request |

### Fase 4 — Auditoría y línea base (liberación e insignias)

*Objetivo: certificar la madurez del repositorio y asignar la insignia real.*

| Código | Punto de control | Responsable | Criterio de aprobación |
|---|---|---|---|
| CK-4.1 | Ejecución de `audit_tool.py` | Encargado de QA | Se corre la herramienta de auditoría y se regenera `AUDITORIA_INFORME.md` |
| CK-4.2 | Umbral de insignia alcanzado | Encargado de QA | El puntaje global se mantiene dentro del rango de la insignia declarada (ver `SISTEMA_INSIGNIAS.md`) |
| CK-4.3 | Integración limpia a `main` | Encargado del repo | El merge se hace con *Squash & Merge*, manteniendo el historial legible |
| CK-4.4 | Etiquetado de versión | Encargado del repo | Se crea un tag (`v1.0.0`, etc.) que respalda la nueva línea base aprobada |

---

## 3. Matriz de aplicabilidad por nivel de insignia

| Nivel | Puntos de control obligatorios | Estado |
|---|---|---|
| 🥉 Bronce | CK-1.1 a CK-2.4 (Fases 1 y 2 completas) | Ver `AUDITORIA_INFORME.md` |
| 🥈 Plata | Todo Bronce + CK-3.1 a CK-3.5 (Fase 3 completa) | Ver `AUDITORIA_INFORME.md` |
| 🥇 Oro | Todo Plata + CK-4.1 a CK-4.4 (Fase 4 completa) | Ver `AUDITORIA_INFORME.md` |
