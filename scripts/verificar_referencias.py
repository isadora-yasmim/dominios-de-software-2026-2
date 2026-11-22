#!/usr/bin/env python3
"""Confere se as referências citadas nos documentos estão na lista consolidada.

Lê a seção "Referências" de cada arquivo .md em docs/ e procura cada item na
lista consolidada (docs/entrega/Referencias.md). Um item é considerado
presente quando:
  - algum link http(s) dele aparece na lista consolidada; ou
  - pelo menos 70% das suas palavras significativas aparecem em uma mesma
    entrada da lista (o comentário <!-- alias: ... --> de uma entrada conta
    como parte dela).

Itens que só têm links internos (.md) e os grupos "Fontes internas do
projeto" e "Artefatos do projeto" são ignorados.

Também confere o uso de IA:
  - nenhuma referência pode ficar com "Seção II.x" (prompt não registrado);
  - toda "Seção II.n" citada deve existir no Apêndice II.

Uso:
  python3 scripts/verificar_referencias.py              # todos os documentos
  python3 scripts/verificar_referencias.py ARQ.md ...   # só os arquivos dados
  python3 scripts/verificar_referencias.py --hook post  # hook PostToolUse
  python3 scripts/verificar_referencias.py --hook stop  # hook Stop

Saída 0 quando está tudo certo e 1 quando há pendências (modo normal).
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"
CONSOLIDADA = DOCS / "entrega" / "Referencias.md"
APENDICE = DOCS / "entrega" / "apendices" / "Apendice_II_Prompts_IA.md"
IGNORAR = {CONSOLIDADA.resolve(), APENDICE.resolve()}
GRUPOS_INTERNOS = ("internas", "artefatos do projeto")
LIMIAR = 0.7

RE_TITULO = re.compile(r"^(#{1,6})\s+(.*)$")
RE_URL = re.compile(r"https?://[^\s)>\]]+")
RE_LINK_MD = re.compile(r"\]\(([^)]+)\)")
RE_SECAO_II = re.compile(r"Se[cç][aã]o\s+II\.(\w+)", re.IGNORECASE)
PALAVRAS_VAZIAS = {
    "de", "da", "do", "das", "dos", "e", "em", "para", "por", "com", "the",
    "and", "for", "of", "a", "o", "as", "os", "no", "na", "ao", "um", "uma",
    "disponivel", "acesso", "cap", "caps", "ed", "secao", "secoes", "usado",
    "usada", "consulta",
}


def normalizar(texto: str) -> str:
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", texto.lower()).strip()


def palavras(texto: str) -> set[str]:
    texto = RE_URL.sub(" ", texto)
    texto = RE_LINK_MD.sub("]", texto)
    return {
        p for p in normalizar(texto).split()
        if p not in PALAVRAS_VAZIAS and (len(p) >= 3 or p.isdigit())
    }


def secao_referencias(linhas: list[str]) -> list[str]:
    """Devolve as linhas da(s) seção(ões) cujo título contém "Referências"."""
    saida: list[str] = []
    nivel = None
    for linha in linhas:
        m = RE_TITULO.match(linha)
        if m:
            n = len(m.group(1))
            if nivel is not None and n <= nivel:
                nivel = None
            if nivel is None and "referencias" in normalizar(m.group(2)):
                nivel = n
                continue
        if nivel is not None:
            saida.append(linha)
    return saida


def itens_referencia(caminho: Path) -> list[tuple[str, str]]:
    """Lista (grupo, item) de cada referência do documento."""
    linhas = caminho.read_text(encoding="utf-8").splitlines()
    grupo = ""
    itens = []
    for linha in secao_referencias(linhas):
        s = linha.strip()
        m = re.match(r"^\*\*(.+?)\*\*", s)
        if m and not s.startswith(("- ", "* ", "|")):
            grupo = normalizar(m.group(1))
            continue
        if any(g in grupo for g in GRUPOS_INTERNOS):
            continue
        if s.startswith(("- ", "* ")):
            item = s[2:].strip()
        elif s.startswith("|") and not re.match(r"^\|[\s:|-]+\|?$", s):
            celula = s.strip("|").split("|")[0].strip()
            if normalizar(celula) in ("referencia", "detalhe", "item"):
                continue
            item = celula
        else:
            continue
        links = RE_LINK_MD.findall(item)
        if not RE_URL.search(item) and links and all(".md" in l for l in links):
            continue  # só aponta para artefatos do próprio projeto
        itens.append((grupo, item))
    return itens


def entradas_consolidadas() -> tuple[str, list[set[str]]]:
    if not CONSOLIDADA.exists():
        return "", []
    texto = CONSOLIDADA.read_text(encoding="utf-8")
    entradas = []
    for linha in texto.splitlines():
        s = linha.strip()
        if s.startswith(("- ", "* ", "|")) or re.match(r"^\d+\.\s", s):
            alias = " ".join(re.findall(r"<!--\s*alias:(.*?)-->", s))
            entradas.append(palavras(s + " " + alias))
    return texto, entradas


def presente(item: str, texto: str, entradas: list[set[str]]) -> bool:
    urls = [u.rstrip(".,;") for u in RE_URL.findall(item)]
    if any(u in texto for u in urls):
        return True
    alvo = palavras(item)
    if not alvo:
        return True
    return any(len(alvo & e) / len(alvo) >= LIMIAR for e in entradas)


def documentos(args: list[str]) -> list[Path]:
    if args:
        lista = [Path(a).resolve() for a in args]
    else:
        lista = sorted(DOCS.rglob("*.md"))
    return [
        p for p in lista
        if p.suffix == ".md" and p.exists() and p.resolve() not in IGNORAR
        and DOCS in p.resolve().parents
    ]


def secoes_apendice() -> set[str]:
    if not APENDICE.exists():
        return set()
    return set(re.findall(r"^#+\s+II\.(\w+)", APENDICE.read_text(encoding="utf-8"), re.M))


def verificar(arquivos: list[Path]) -> list[str]:
    texto, entradas = entradas_consolidadas()
    secoes = secoes_apendice()
    pendencias = []
    if not texto:
        return [f"Lista consolidada não encontrada: {CONSOLIDADA.relative_to(RAIZ)}"]
    for arq in arquivos:
        rel = arq.relative_to(RAIZ)
        for _grupo, item in itens_referencia(arq):
            if not presente(item, texto, entradas):
                pendencias.append(f"{rel}: referência ausente da lista consolidada → {item[:180]}")
        conteudo = arq.read_text(encoding="utf-8")
        for sec in RE_SECAO_II.findall(conteudo):
            if sec.lower() == "x":
                pendencias.append(f"{rel}: uso de IA com prompt não registrado (\"Seção II.x\")")
            elif sec not in secoes:
                pendencias.append(f"{rel}: cita a Seção II.{sec}, que não existe no Apêndice II")
    return pendencias


INSTRUCAO = (
    "Atualize docs/entrega/Referencias.md com a referência completa (copie os dados "
    "do documento de origem, sem inventar autor, ano ou URL) e acrescente o documento "
    "em 'Usada em'. Uso de IA: registre os prompts literais no Apêndice II "
    "(docs/entrega/apendices/Apendice_II_Prompts_IA.md) e troque 'II.x' pela seção criada. "
    "Se a referência já estiver na lista com outra grafia, acrescente "
    "<!-- alias: ... --> na entrada."
)


def sessao_editou_docs(transcricao: str | None) -> bool:
    """Indica se a sessão alterou algum .md em docs/ (Edit/Write)."""
    if not transcricao or not Path(transcricao).exists():
        return False
    for linha in Path(transcricao).read_text(encoding="utf-8", errors="ignore").splitlines():
        if '"tool_use"' not in linha or "docs/" not in linha:
            continue
        try:
            msg = json.loads(linha).get("message", {})
        except json.JSONDecodeError:
            continue
        for bloco in msg.get("content", []) if isinstance(msg.get("content"), list) else []:
            if (isinstance(bloco, dict) and bloco.get("type") == "tool_use"
                    and bloco.get("name") in ("Edit", "Write", "MultiEdit")):
                caminho = str(bloco.get("input", {}).get("file_path", ""))
                if "/docs/" in caminho and caminho.endswith(".md"):
                    return True
    return False


def modo_hook(evento: str) -> int:
    try:
        entrada = json.load(sys.stdin)
    except json.JSONDecodeError:
        entrada = {}

    if evento == "post":
        caminho = (entrada.get("tool_input") or {}).get("file_path", "")
        arqs = documentos([caminho]) if caminho else []
        if not arqs:
            return 0
        pend = verificar(arqs)
        if pend:
            print(json.dumps({"hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": "Referências pendentes:\n- " + "\n- ".join(pend) + "\n" + INSTRUCAO,
            }}, ensure_ascii=False))
        return 0

    # Stop
    pend = verificar(documentos([]))
    sessao = entrada.get("session_id", "")
    if sessao and sessao_editou_docs(entrada.get("transcript_path")):
        apendice = APENDICE.read_text(encoding="utf-8") if APENDICE.exists() else ""
        if f"sessao: {sessao}" not in apendice:
            pend.append(
                "Esta sessão do Claude Code alterou documentos em docs/, mas o Apêndice II não "
                f"tem a marca <!-- sessao: {sessao} -->. Registre a referência de IA no documento "
                "alterado e os prompts literais desta sessão em uma nova seção do Apêndice II, "
                "com essa marca."
            )
    if not pend:
        return 0
    msg = "Referências pendentes:\n- " + "\n- ".join(pend) + "\n" + INSTRUCAO
    if entrada.get("stop_hook_active"):
        print(json.dumps({"systemMessage": msg}, ensure_ascii=False))
        return 0
    print(json.dumps({"decision": "block", "reason": msg}, ensure_ascii=False))
    return 0


def main() -> int:
    args = sys.argv[1:]
    if args[:1] == ["--hook"]:
        return modo_hook(args[1] if len(args) > 1 else "stop")
    pend = verificar(documentos(args))
    for p in pend:
        print(p)
    if not pend:
        print("Referências em dia.")
    return 1 if pend else 0


if __name__ == "__main__":
    sys.exit(main())
