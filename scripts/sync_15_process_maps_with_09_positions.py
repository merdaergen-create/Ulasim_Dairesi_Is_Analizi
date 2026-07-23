from __future__ import annotations

import re
from pathlib import Path

POSITION_DIR = Path("09_yalin_pozisyonlari")
MAP_DIR = Path("15_yalin_surec_haritalari")

# 15 numaralı haritalarda daha önce kullanılan unvanların 09 numaralı
# güncel yalın pozisyon yapısındaki karşılıkları.
ALIASES: dict[str, str] = {
    # AUS ve TKM
    "Ulaşım Veri Platformu ve Analitik Sorumlusu": "Ulaşım Veri Platformu ve Veri Yönetişimi Sorumlusu",
    "Haberleşme, Ağ ve Siber Güvenlik Mühendisi": "Siber Güvenlik, Ağ ve Erişim Sorumlusu",
    "Ulaşım Teknolojileri Proje Yöneticisi": "AUS Proje ve Değişiklik Yöneticisi",
    "TKM Operasyon Birim Sorumlusu": "TKM Operasyon Sorumlusu",
    "Sinyal Optimizasyon ve Operasyon Raporlama Mühendisi": "Sinyal Optimizasyon ve Operasyon Analisti",

    # Toplu taşıma
    "Tarife, Maliyet ve Kapasite Planlama Uzmanı": "Tarife, Maliyet ve Filo Planlama Uzmanı",
    "Hizmet Kalitesi ve Şikâyet Yönetimi Sorumlusu": "İşletmeci İlişkileri ve Hizmet Kalitesi Sorumlusu",
    "Durak Hizmetleri Planlama Uzmanı": "Durak Hizmetleri ve Erişilebilirlik Planlama Uzmanı",
    "İşletmeci İlişkileri ve Sözleşme Teknik Kontrol Sorumlusu": "İşletmeci İlişkileri ve Hizmet Kalitesi Sorumlusu / Sözleşme Teknik Kontrol Uzmanı",
    "Toplu Taşıma Veri Analisti": "Toplu Taşıma Veri ve Performans Analisti",

    # Ruhsat ve ticari araç
    "Ruhsat ve Vize Birim Sorumlusu": "Ruhsat ve Vize İşlemleri Sorumlusu",
    "Servis Araçları İşlemleri Sorumlusu": "Servis, Taksi ve Ticari Plaka İşlemleri Sorumlusu",
    "Taksi ve Ticari Plaka İşlemleri Sorumlusu": "Servis, Taksi ve Ticari Plaka İşlemleri Sorumlusu",
    "Başvuru, Belge ve Dijital Süreç Uzmanı": "Dijital Başvuru ve Belge Yönetimi Uzmanı",
    "Arşiv, Mevzuat ve Kalite Kontrol Uzmanı": "Mevzuat ve Kalite Kontrol Uzmanı",

    # UKOME
    "Alt Komisyon ve Kurumlar Arası Koordinasyon Sorumlusu": "Alt Komisyon ve Kurum Koordinasyon Sorumlusu",
    "Karar Dağıtım, Tebligat ve Arşiv Sorumlusu": "Karar Dağıtım, Tebligat ve Arşiv Personeli",

    # Otogar
    "Terminal Operasyon ve Peron Sorumlusu": "Terminal Operasyon ve Vardiya Sorumlusu / Peron Planlama ve Tahsis Sorumlusu",
    "Gişe ve Tahakkuk Sorumlusu": "Gişe, Tahakkuk ve Tarife Sorumlusu",
    "Kasa, Gelir Mutabakat ve Raporlama Sorumlusu": "Kasa ve Gelir Mutabakat Sorumlusu / Faaliyet ve Gelir Raporlama Uzmanı",
    "Güvenlik ve Ortak Hizmetler Koordinatörü": "Terminal Güvenlik ve İSG Koordinatörü",

    # İdari ve mali işler
    "Bütçe, Performans ve Faaliyet Raporlama Sorumlusu": "Bütçe ve Performans Sorumlusu / Faaliyet Raporlama Uzmanı",
    "Sözleşme, Teminat ve Hakediş Dosyası Sorumlusu": "Sözleşme ve Teminat Sorumlusu / Hakediş ve Ödeme Dosyası Sorumlusu",
    "İç Kontrol, Risk ve Süreç Yönetimi Uzmanı": "İç Kontrol ve Risk Sorumlusu",
}

ROW_RE = re.compile(r"^\|\s*(?P<position>[^|]+?)\s*\|\s*(?P<unit>[^|]+?)\s*\|")
RESP_RE = re.compile(r"Sorumlu:\s*(?P<value>.*?)(?=<br/>Birim:|<br/>|$)")
UNIT_RE = re.compile(r"Birim:\s*(?P<value>.*?)(?=<br/>|$)")


def load_position_units() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for path in sorted(POSITION_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            match = ROW_RE.match(line)
            if not match:
                continue
            position = match.group("position").strip()
            unit = match.group("unit").strip()
            if position in {"Pozisyon", "Ortak pozisyon"} or set(position) == {"-"}:
                continue
            mapping[position] = unit
    return mapping


def split_positions(value: str, known: dict[str, str]) -> list[str]:
    value = ALIASES.get(value.strip(), value.strip())
    if value in known:
        return [value]
    # Birden fazla güncel rol slash ile gösterilir. Önce tam adları koruyarak ayır.
    parts = [part.strip() for part in value.split(" / ") if part.strip()]
    return parts or [value]


def update_label(label: str, known: dict[str, str]) -> str:
    responsible_match = RESP_RE.search(label)
    if not responsible_match:
        return label

    old_responsible = responsible_match.group("value").strip()
    positions = split_positions(old_responsible, known)
    updated_responsible = " / ".join(positions)

    units: list[str] = []
    for position in positions:
        unit = known.get(position)
        if unit and unit not in units:
            units.append(unit)

    # Kaynakta bulunamayan rol varsa mevcut birim bilgisini koru.
    if not units:
        existing = UNIT_RE.search(label)
        if existing:
            units = [existing.group("value").strip()]

    updated_unit = " / ".join(units) if units else "İlgili Şube Müdürlüğü Yönetimi"

    label = RESP_RE.sub(f"Sorumlu: {updated_responsible}", label, count=1)
    if UNIT_RE.search(label):
        label = UNIT_RE.sub(f"Birim: {updated_unit}", label, count=1)
    else:
        label += f"<br/>Birim: {updated_unit}"
    return label


def update_mermaid_text(text: str, known: dict[str, str]) -> str:
    # Mermaid düğüm etiketlerindeki sorumlu/birim alanlarını günceller;
    # düğüm kimlikleri, şekiller, bağlantılar ve karar dalları korunur.
    node_re = re.compile(
        r"(?P<prefix>\b[A-Za-z][A-Za-z0-9_]*\s*)"
        r"(?P<open>\(\[|\[|\{)"
        r"(?P<label>.*?)"
        r"(?P<close>\]\)|\]|\})"
    )

    def repl(match: re.Match[str]) -> str:
        label = match.group("label")
        if "Sorumlu:" not in label:
            return match.group(0)
        return (
            match.group("prefix")
            + match.group("open")
            + update_label(label, known)
            + match.group("close")
        )

    return node_re.sub(repl, text)


def main() -> None:
    if not POSITION_DIR.exists() or not MAP_DIR.exists():
        raise SystemExit("09 veya 15 numaralı klasör bulunamadı.")

    known = load_position_units()
    if not known:
        raise SystemExit("09_yalin_pozisyonlari içinden pozisyon-birim eşleştirmesi okunamadı.")

    changed = 0
    for path in sorted(MAP_DIR.rglob("*.md")):
        original = path.read_text(encoding="utf-8")
        updated = update_mermaid_text(original, known)
        if path.name == "README.md" and path.parent == MAP_DIR:
            marker = "09_yalin_pozisyonlari"
            if marker not in updated:
                updated += (
                    "\n## Güncel pozisyon ve birim kaynağı\n\n"
                    "Diyagramlardaki `Sorumlu:` ve `Birim:` alanları "
                    "`09_yalin_pozisyonlari` içindeki güncel pozisyon adları ve bağlı birimlerle "
                    "senkronize edilir. Süreç adımları, karar noktaları ve bağlantılar değiştirilmez.\n"
                )
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1

    print(f"Güncellenen dosya sayısı: {changed}")
    print(f"Okunan güncel pozisyon sayısı: {len(known)}")


if __name__ == "__main__":
    main()
