# RESULTADO DE AUDITORIA

_Generado automaticamente por `scripts/audit_tool.py` el 2026-09-21 18:35 UTC._

| Dato | Resultado |
| --- | --- |
| Criterios evaluados | 17 |
| Criterios cumplidos | 17 |
| Cumplimiento | 100.0% |
| Insignia obtenida | ORO |

## Detalle

| ID | Criterio | Resultado |
| --- | --- | --- |
| DOC-01 | Existe README.md | PASS |
| DOC-02 | Existe docs/LISTA_DE_VERIFICACION.md | PASS |
| DOC-03 | Existe docs/SISTEMA_INSIGNIAS.md | PASS |
| DOC-04 | Existe docs/ADAPTACION_MOPROSOFT.md | PASS |
| DOC-05 | Existe LICENSE | PASS |
| EST-01 | Existe carpeta scripts/ | PASS |
| EST-02 | Existe el auditor automatico (este mismo script) | PASS |
| EST-03 | Existe .github/PULL_REQUEST_TEMPLATE.md | PASS |
| EST-04 | Existe .github/workflows/audit.yml | PASS |
| EST-05 | Existen plantillas de Issue (.github/ISSUE_TEMPLATE) | PASS |
| SEG-01 | No se detectan patrones basicos de posibles secretos o CLABE en texto plano | PASS |
| SEG-02 | No existe archivo .env sin ignorar en el repositorio | PASS |
| GIT-01 | Git esta disponible en el sistema | PASS |
| GIT-02 | Existe repositorio Git inicializado (.git) | PASS |
| GIT-03 | Los ultimos commits siguen Conventional Commits (feat/fix/docs/test/refactor/chore) | PASS |
| MIX-01 | Se documenta la conectividad limitada / offline-first (HU-02) | PASS |
| MIX-02 | Se documenta la protección de datos de pago (CLABE, HU-05) | PASS |

## Nota metodologica

Este resultado se recalcula cada vez que se ejecuta el script. La insignia declarada en README.md debe actualizarse manualmente para reflejar siempre el ultimo resultado real, tal como lo exige `docs/SISTEMA_INSIGNIAS.md`.
