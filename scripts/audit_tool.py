#!/usr/bin/env python3
"""
audit_tool.py
Motor de auditoria automatizada del repositorio (Tema 2.5).
Revisa documentacion, estructura, control de versiones y patrones
basicos de seguridad, y genera AUDITORIA_INFORME.md con el resultado real.

Uso:
    python scripts/audit_tool.py
"""

import os
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# patrones basicos de posibles secretos / datos sensibles expuestos
SECRET_PATTERNS = [
    r"AKIA[0-9A-Z]{16}",                       # AWS access key
    r"-----BEGIN (RSA|EC|DSA|OPENSSH) PRIVATE KEY-----",
    r"(?i)password\s*=\s*[\"'][^\"']{4,}[\"']",
    r"(?i)clabe\s*[:=]\s*[\"']?\d{10,18}[\"']?",  # CLABE en texto plano (18 digitos en Mexico)
]

CHECKS = []


def check(id_, description, applicable=True):
    def decorator(fn):
        CHECKS.append({"id": id_, "description": description, "fn": fn, "applicable": applicable})
        return fn
    return decorator


def exists(*parts):
    return os.path.isfile(os.path.join(ROOT, *parts)) or os.path.isdir(os.path.join(ROOT, *parts))


# ---------------------------------------------------------------------------
# DOC-xx: documentacion
# ---------------------------------------------------------------------------
@check("DOC-01", "Existe README.md")
def doc01():
    return exists("README.md")


@check("DOC-02", "Existe docs/LISTA_DE_VERIFICACION.md")
def doc02():
    return exists("docs", "LISTA_DE_VERIFICACION.md")


@check("DOC-03", "Existe docs/SISTEMA_INSIGNIAS.md")
def doc03():
    return exists("docs", "SISTEMA_INSIGNIAS.md")


@check("DOC-04", "Existe docs/ADAPTACION_MOPROSOFT.md")
def doc04():
    return exists("docs", "ADAPTACION_MOPROSOFT.md")


@check("DOC-05", "Existe LICENSE")
def doc05():
    return exists("LICENSE")


# ---------------------------------------------------------------------------
# EST-xx: estructura del repositorio
# ---------------------------------------------------------------------------
@check("EST-01", "Existe carpeta scripts/")
def est01():
    return exists("scripts")


@check("EST-02", "Existe el auditor automatico (este mismo script)")
def est02():
    return exists("scripts", "audit_tool.py")


@check("EST-03", "Existe .github/PULL_REQUEST_TEMPLATE.md")
def est03():
    return exists(".github", "PULL_REQUEST_TEMPLATE.md")


@check("EST-04", "Existe .github/workflows/audit.yml")
def est04():
    return exists(".github", "workflows", "audit.yml")


@check("EST-05", "Existen plantillas de Issue (.github/ISSUE_TEMPLATE)")
def est05():
    return exists(".github", "ISSUE_TEMPLATE")


# ---------------------------------------------------------------------------
# SEG-xx: seguridad basica
# ---------------------------------------------------------------------------
def _iter_text_files():
    skip_dirs = {".git", "node_modules", ".venv", "__pycache__"}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]
        for fn in filenames:
            if fn.endswith((".md", ".py", ".yml", ".yaml", ".json", ".js", ".env", ".txt")):
                yield os.path.join(dirpath, fn)


@check("SEG-01", "No se detectan patrones basicos de posibles secretos o CLABE en texto plano")
def seg01():
    for path in _iter_text_files():
        if os.path.abspath(path) == os.path.abspath(__file__):
            continue
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except OSError:
            continue
        for pattern in SECRET_PATTERNS:
            if re.search(pattern, content):
                return False
    return True


@check("SEG-02", "No existe archivo .env sin ignorar en el repositorio")
def seg02():
    gitignore_path = os.path.join(ROOT, ".gitignore")
    if not os.path.isfile(gitignore_path):
        return not exists(".env")
    with open(gitignore_path, "r", encoding="utf-8", errors="ignore") as f:
        gitignore = f.read()
    if exists(".env") and ".env" not in gitignore:
        return False
    return True


# ---------------------------------------------------------------------------
# GIT-xx: control de versiones
# ---------------------------------------------------------------------------
@check("GIT-01", "Git esta disponible en el sistema")
def git01():
    try:
        subprocess.run(["git", "--version"], cwd=ROOT, capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


@check("GIT-02", "Existe repositorio Git inicializado (.git)")
def git02():
    return exists(".git")


@check("GIT-03", "Los ultimos commits siguen Conventional Commits (feat/fix/docs/test/refactor/chore)")
def git03():
    try:
        result = subprocess.run(
            ["git", "log", "-15", "--pretty=%s"], cwd=ROOT, capture_output=True, text=True, check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
    messages = [m for m in result.stdout.splitlines() if m.strip()]
    if not messages:
        return False
    pattern = re.compile(r"^(feat|fix|docs|test|refactor|chore)(\(.+\))?:\s")
    matching = [m for m in messages if pattern.match(m)]
    return len(matching) / len(messages) >= 0.7


# ---------------------------------------------------------------------------
# MIX-xx: contexto Mixteca / TisaaSavi
# ---------------------------------------------------------------------------
@check("MIX-01", "Se documenta la conectividad limitada / offline-first (HU-02)")
def mix01():
    return _grep_any(["offline-first", "offline first", "conectividad limitada", "conectividad intermitente"])


@check("MIX-02", "Se documenta la protección de datos de pago (CLABE, HU-05)")
def mix02():
    return _grep_any(["clabe cifrada", "clabe se guarda cifrada", "protección de la clabe", "proteccion de la clabe"])


def _grep_any(phrases):
    for path in _iter_text_files():
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read().lower()
        except OSError:
            continue
        for phrase in phrases:
            if phrase.lower() in content:
                return True
    return False


# ---------------------------------------------------------------------------
# Ejecucion y reporte
# ---------------------------------------------------------------------------
def run():
    results = []
    for c in CHECKS:
        try:
            passed = c["fn"]() if c["applicable"] else None
        except Exception as exc:  # nunca tronar la auditoria por un check individual
            passed = False
            print(f"[WARN] {c['id']} lanzo un error: {exc}", file=sys.stderr)
        results.append({**c, "passed": passed})

    applicable = [r for r in results if r["applicable"]]
    total = len(applicable)
    passed_count = sum(1 for r in applicable if r["passed"])
    pct = round((passed_count / total) * 100, 1) if total else 0.0

    if pct >= 95:
        badge = "ORO"
    elif pct >= 85:
        badge = "PLATA"
    elif pct >= 70:
        badge = "BRONCE"
    else:
        badge = "SIN INSIGNIA"

    write_report(results, total, passed_count, pct, badge)
    print(f"Auditoria completada: {passed_count}/{total} ({pct}%) -> {badge}")
    print("Reporte escrito en AUDITORIA_INFORME.md")


def write_report(results, total, passed_count, pct, badge):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = []
    lines.append("# RESULTADO DE AUDITORIA\n")
    lines.append(f"_Generado automaticamente por `scripts/audit_tool.py` el {now}._\n")
    lines.append("| Dato | Resultado |")
    lines.append("| --- | --- |")
    lines.append(f"| Criterios evaluados | {total} |")
    lines.append(f"| Criterios cumplidos | {passed_count} |")
    lines.append(f"| Cumplimiento | {pct}% |")
    lines.append(f"| Insignia obtenida | {badge} |")
    lines.append("")
    lines.append("## Detalle\n")
    lines.append("| ID | Criterio | Resultado |")
    lines.append("| --- | --- | --- |")
    for r in results:
        if not r["applicable"]:
            estado = "N/A"
        else:
            estado = "PASS" if r["passed"] else "FAIL"
        lines.append(f"| {r['id']} | {r['description']} | {estado} |")
    lines.append("")
    lines.append("## Nota metodologica\n")
    lines.append(
        "Este resultado se recalcula cada vez que se ejecuta el script. La insignia declarada "
        "en README.md debe actualizarse manualmente para reflejar siempre el ultimo resultado real, "
        "tal como lo exige `docs/SISTEMA_INSIGNIAS.md`."
    )

    with open(os.path.join(ROOT, "AUDITORIA_INFORME.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    run()
