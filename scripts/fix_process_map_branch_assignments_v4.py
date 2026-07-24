from __future__ import annotations

import re
from pathlib import Path

POSITION_DIR = Path("09_yalin_pozisyonlari")
TARGET_DIR = Path("15_yalin_surec_haritalari")

NODE_RE = re.compile(r"(?P<prefix>\b[A-Za-z][A-Za-z0-9_]*\s*)(?P<open>\(\[|\[|\{)(?P<label>.*?)(?P<close>\]\)|\]|\})")
TABLE_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|")

FOLDER_BRANCH = {
    "trafik_planlama": "Ulaşım Planlama Şube Müdürlüğü",
    "trafik_egitim": "Ulaşım Planlama Şube Müdürlüğü",
    "akilli_ulasim": "Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü",
    "toplu_ulasim": "Toplu Taşıma Planlama ve İşletme Şube Müdürlüğü",
    "ukome": "UKOME Şube Müdürlüğü",
    "otogar": "Otogar İşletme Şube Müdürlüğü",
    "idari_isler": "İdari ve Mali İşler Şube Müdürlüğü",
}


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().rstrip("."))


def branch_from_title(title: str) -> str:
    if title.startswith("AUS ve TKM") or title.startswith("Akıllı Ulaşım Sistemleri"):
        return "Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü"
    if title.startswith("Toplu Taşıma"):
        return "Toplu Taşıma Planlama ve İşletme Şube Müdürlüğü"
    return title


def parse_position_branches() -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted(POSITION_DIR.glob("0[1-8]_*.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        title = lines[0].removeprefix("# ").split(" — ")[0]
        branch = branch_from_title(title)
        for line in lines:
            match = TABLE_RE.match(line)
            if not match:
                continue
            position = clean(match.group(1))
            unit = clean(match.group(2))
            if position in {"Pozisyon", "---"} or unit in {"Bağlı birim", "---"}:
                continue
            result[position] = branch

    common = POSITION_DIR / "09_ortak_pozisyonlar_ve_kadro_ilkeleri.md"
    if common.exists():
        for line in common.read_text(encoding="utf-8").splitlines():
            match = TABLE_RE.match(line)
            if not match:
                continue
            position = clean(match.group(1))
            if position not in {"Ortak pozisyon", "---"}:
                result[position] = "Ulaşım Dairesi Başkanlığı"
    return result


def fix_label(label: str, position_branch: dict[str, str], folder: str) -> str:
    if "Sorumlu:" not in label or "<br/>Şube:" not in label:
        return label
    before_branch = label.split("<br/>Şube:", 1)[0]
    responsible_part = before_branch.split("Sorumlu:", 1)[1].split("<br/>Birim:", 1)[0]
    positions = [clean(x) for x in responsible_part.split("/")]
    branches: list[str] = []
    for position in positions:
        branch = position_branch.get(position, FOLDER_BRANCH.get(folder, "Ulaşım Dairesi Başkanlığı"))
        if branch not in branches:
            branches.append(branch)
    return before_branch + "<br/>Şube: " + " / ".join(branches)


def main() -> None:
    position_branch = parse_position_branches()
    for path in sorted(TARGET_DIR.rglob("*.md")):
        folder = path.parent.name
        text = path.read_text(encoding="utf-8")
        updated = NODE_RE.sub(
            lambda m: m.group("prefix") + m.group("open")
            + fix_label(m.group("label"), position_branch, folder)
            + m.group("close"),
            text,
        )
        path.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
