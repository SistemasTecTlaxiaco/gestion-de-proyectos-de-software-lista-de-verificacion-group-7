# Sistema de Insignias de Calidad

## Objetivo

Establecer un sistema de reconocimiento del estado de calidad del repositorio, basado en los resultados de la Lista de Verificación (`LISTA_DE_VERIFICACION.md`) y en la auditoría automatizada (`scripts/audit_tool.py`).

Los umbrales de porcentaje se alinean deliberadamente con las bandas de desempeño oficiales del TecNM (Excelente, Notable, Bueno/Suficiente) usadas en la rúbrica de la unidad, en vez de usar porcentajes arbitrarios:

- 🥉 Bronce
- 🥈 Plata
- 🥇 Oro

---

## 1. Insignia Bronce

El repositorio obtiene **Bronce** cuando cumple, como mínimo:

| Criterio | Requisito |
|---|---|
| Checklist | Fases 1 y 2 de `LISTA_DE_VERIFICACION.md` aplicadas |
| Documentación | Existen `README.md`, `LICENSE` y `docs/` con la documentación básica |
| Git | Se usa control de versiones con commits siguiendo Conventional Commits |
| Seguridad | No hay hallazgos críticos abiertos (ver `docs/ADAPTACION_MOPROSOFT.md`) |
| Cumplimiento | Al menos 70% de los criterios aplicables de `audit_tool.py` pasan |

### Evidencia mínima
- Checklist de Fase 1 y 2 aplicada.
- Historial de commits visible en GitHub.
- Registro de hallazgos con su severidad.

---

## 2. Insignia Plata

Además de Bronce, el repositorio obtiene **Plata** cuando cumple:

| Criterio | Requisito |
|---|---|
| Cumplimiento | Al menos 85% de los criterios aplicables pasan |
| Pull Requests | Todos los PR usan `.github/PULL_REQUEST_TEMPLATE.md` completo |
| CI | El workflow `audit.yml` corre en cada Pull Request |
| MoProSoft | Se documenta la relación entre cada práctica y su categoría MoProSoft (`docs/ADAPTACION_MOPROSOFT.md`) |
| Revisión | Cada PR fue aprobado por un integrante distinto al autor |
| Contexto Mixteca | Se verifica en cada PR que el cambio no rompe el registro offline-first (HU-02) |

### Evidencia mínima
- Resultado de `AUDITORIA_INFORME.md`.
- Relación con MoProSoft documentada.
- Historial de Pull Requests aprobados por pares.

---

## 3. Insignia Oro

Además de Plata, el repositorio obtiene **Oro** cuando cumple:

| Criterio | Requisito |
|---|---|
| Cumplimiento | Al menos 95% de los criterios aplicables pasan |
| Seguridad | Sin hallazgos críticos ni altos abiertos, incluyendo la protección de la CLABE (HU-05) |
| Auditoría | `audit_tool.py` se ejecutó de forma real sobre el repositorio, no de forma simulada |
| Trazabilidad | Existe relación clara entre Issue → rama → commits → Pull Request → auditoría |
| Contexto | Se documenta explícitamente cómo el repositorio soporta conectividad limitada y protege datos de pago de las tejedoras |
| Re-auditoría | Se ejecutó una segunda auditoría después de corregir los hallazgos de la primera |

### Evidencia mínima
- `AUDITORIA_INFORME.md` con la segunda ejecución.
- Historial de hallazgos y su corrección.
- Tags de versión (`v1.0.0`, etc.) respaldando la línea base.

---

## 4. Tabla de clasificación

| Porcentaje de cumplimiento | Insignia |
|---|---|
| Menor a 70% | Sin insignia |
| 70% – 84% | 🥉 Bronce |
| 85% – 94% | 🥈 Plata |
| 95% – 100% | 🥇 Oro |

> La insignia declarada en el README debe corresponder exactamente al resultado real de `AUDITORIA_INFORME.md`, no a una aspiración del equipo.

---

## 5. Niveles de severidad de hallazgos

| Severidad | Descripción |
|---|---|
| Crítica | Compromete la seguridad, integridad o disponibilidad del sistema (ej. CLABE expuesta en texto plano) |
| Alta | Impacto importante sobre calidad o seguridad, pero no compromete datos sensibles |
| Media | Requiere corrección para mantener la calidad del repositorio |
| Baja | Mejora recomendada que no bloquea la insignia |

Un porcentaje alto **no** otorga una insignia superior si existen hallazgos críticos o altos sin resolver.

---

## 6. Regla de cálculo

```
Porcentaje de cumplimiento = (criterios cumplidos / criterios evaluados) × 100
```

La clasificación final considera tanto el porcentaje como los hallazgos de seguridad abiertos.

---

## 7. Estado actual

**Insignia declarada:** ver `AUDITORIA_INFORME.md` (se actualiza cada vez que se ejecuta `scripts/audit_tool.py`).
