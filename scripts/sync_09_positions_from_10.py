from __future__ import annotations

import re
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POS_DIR = ROOT / "09_yalin_pozisyonlari"
DESC_DIR = ROOT / "10_yalin_pozisyon_gorev_tanimlari"

FILE_MAP = OrderedDict([
    ("01_ulasim_planlama_yalin_pozisyonlari.md", "01_ulasim_planlama_yalin_gorev_tanimlari.md"),
    ("02_trafik_hizmetleri_sinyalizasyon_yalin_pozisyonlari.md", "02_trafik_hizmetleri_sinyalizasyon_yalin_gorev_tanimlari.md"),
    ("03_aus_tkm_yalin_pozisyonlari.md", "03_aus_tkm_yalin_gorev_tanimlari.md"),
    ("04_toplu_tasima_yalin_pozisyonlari.md", "04_toplu_tasima_yalin_gorev_tanimlari.md"),
    ("05_ulasim_ruhsat_yalin_pozisyonlari.md", "05_ulasim_ruhsat_yalin_gorev_tanimlari.md"),
    ("06_ukome_yalin_pozisyonlari.md", "06_ukome_yalin_gorev_tanimlari.md"),
    ("07_otogar_yalin_pozisyonlari.md", "07_otogar_yalin_gorev_tanimlari.md"),
    ("08_idari_mali_isler_yalin_pozisyonlari.md", "08_idari_mali_isler_yalin_gorev_tanimlari.md"),
])

HEADING_RE = re.compile(r"^##\s+\d+\.\s+(.+?)\s*$", re.MULTILINE)


def clean_value(value: str) -> str:
    return value.strip().rstrip(".").strip()


def parse_positions(text: str) -> list[dict[str, str]]:
    matches = list(HEADING_RE.finditer(text))
    positions: list[dict[str, str]] = []
    for index, match in enumerate(matches):
        title = clean_value(match.group(1))
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[start:end]
        unit_match = re.search(r"\*\*Birim:\*\*\s*(.+)", block)
        purpose_match = re.search(r"\*\*Pozisyonun amacı:\*\*\s*(.+)", block)
        if not unit_match:
            raise ValueError(f"Birim bilgisi bulunamadı: {title}")
        positions.append({
            "title": title,
            "unit": clean_value(unit_match.group(1)),
            "purpose": clean_value(purpose_match.group(1)) if purpose_match else "Görev tanımında belirtilen süreç ve hizmet sorumluluklarını yürütmek",
        })
    if not positions:
        raise ValueError("Görev tanımı dosyasında pozisyon başlığı bulunamadı")
    return positions


def make_tree(positions: list[dict[str, str]]) -> str:
    managers = [p for p in positions if p["unit"] == "Şube Müdürlüğü Yönetimi"]
    manager = managers[0] if managers else positions[0]
    grouped: OrderedDict[str, list[str]] = OrderedDict()
    for position in positions:
        if position is manager or position["title"] == manager["title"]:
            continue
        grouped.setdefault(position["unit"], []).append(position["title"])

    lines = [manager["title"]]
    unit_items = list(grouped.items())
    for unit_index, (unit, titles) in enumerate(unit_items):
        last_unit = unit_index == len(unit_items) - 1
        lines.append(("└── " if last_unit else "├── ") + unit)
        for title_index, title in enumerate(titles):
            last_title = title_index == len(titles) - 1
            prefix = "    " if last_unit else "│   "
            lines.append(prefix + ("└── " if last_title else "├── ") + title)
    return "\n".join(lines)


def make_position_table(positions: list[dict[str, str]]) -> str:
    lines = [
        "| Pozisyon | Bağlı birim | Ana görev odağı |",
        "|---|---|---|",
    ]
    for position in positions:
        purpose = position["purpose"].replace("|", "/")
        lines.append(f"| {position['title']} | {position['unit']} | {purpose} |")
    return "\n".join(lines)


def replace_sections(current: str, positions: list[dict[str, str]]) -> str:
    replacement = (
        "## Önerilen iç yapı\n\n"
        "```text\n"
        f"{make_tree(positions)}\n"
        "```\n\n"
        "## Yalın pozisyonlar\n\n"
        f"{make_position_table(positions)}\n\n"
    )
    pattern = re.compile(
        r"## Önerilen iç yapı\s+```text.*?```\s+## Yalın pozisyonlar\s+.*?(?=## Süreç sahipliği)",
        re.DOTALL,
    )
    updated, count = pattern.subn(replacement, current, count=1)
    if count != 1:
        raise ValueError("09 dosyasındaki iç yapı/pozisyon bölümleri bulunamadı")
    return updated


def sync_branch_files() -> None:
    for pos_name, desc_name in FILE_MAP.items():
        pos_path = POS_DIR / pos_name
        desc_path = DESC_DIR / desc_name
        positions = parse_positions(desc_path.read_text(encoding="utf-8"))
        current = pos_path.read_text(encoding="utf-8")
        updated = replace_sections(current, positions)
        pos_path.write_text(updated, encoding="utf-8")


def sync_common_positions() -> None:
    desc_path = DESC_DIR / "09_ortak_pozisyonlar_yalin_gorev_tanimlari.md"
    pos_path = POS_DIR / "09_ortak_pozisyonlar_ve_kadro_ilkeleri.md"
    positions = parse_positions(desc_path.read_text(encoding="utf-8"))
    current = pos_path.read_text(encoding="utf-8")
    lines = [
        "## Ortak pozisyonlar\n",
        "| Ortak pozisyon | Birim | Ana görev odağı |",
        "|---|---|---|",
    ]
    for position in positions:
        purpose = position["purpose"].replace("|", "/")
        lines.append(f"| {position['title']} | {position['unit']} | {purpose} |")
    replacement = "\n".join(lines) + "\n\n"
    pattern = re.compile(r"## Ortak pozisyonlar\s+.*?(?=## Yalın kadro ilkeleri)", re.DOTALL)
    updated, count = pattern.subn(replacement, current, count=1)
    if count != 1:
        raise ValueError("Ortak pozisyonlar bölümü bulunamadı")
    pos_path.write_text(updated, encoding="utf-8")


def update_readme() -> None:
    path = POS_DIR / "README.md"
    text = path.read_text(encoding="utf-8")
    marker = "## Pozisyon ve birim eşleştirme standardı"
    section = (
        "\n## Pozisyon ve birim eşleştirme standardı\n\n"
        "Bu klasördeki pozisyon adları ve birim yerleşimleri `10_yalin_pozisyon_gorev_tanimlari` içindeki güncel `Birim:` ve pozisyon başlıklarıyla birebir eşleştirilmiştir. Görev tanımlarındaki unvan veya birim değişikliği, bu klasördeki iç yapı ve pozisyon tablolarına birlikte yansıtılır.\n"
    )
    if marker not in text:
        text = text.rstrip() + "\n" + section
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    sync_branch_files()
    sync_common_positions()
    update_readme()
