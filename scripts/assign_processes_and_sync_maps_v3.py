from __future__ import annotations

import re
import shutil
from pathlib import Path

ORG_FILE = Path("14_yalin_organizasyon_semasi/02_sube_birim_pozisyon_semalari.md")
POSITION_DIR = Path("09_yalin_pozisyonlari")
SOURCE_DIR = Path("11_yalin_surec_haritalari_sorumlulari_belirtilmis")
TARGET_DIR = Path("15_yalin_surec_haritalari")

PROCESS_RE = re.compile(r"^(##\s+([A-ZÇĞİÖŞÜ]{2,4}-\d+)\s+[—-]\s+)(.+?)\s*$")
NODE_RE = re.compile(r"(?P<prefix>\b[A-Za-z][A-Za-z0-9_]*\s*)(?P<open>\(\[|\[|\{)(?P<label>.*?)(?P<close>\]\)|\]|\})")
TABLE_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|")

# 10/09 revizyonlarında değişen eski unvanların güncel karşılıkları.
ALIASES = {
    "Ulaşım Veri Platformu ve Analitik Sorumlusu": "Ulaşım Veri Platformu ve Veri Yönetişimi Sorumlusu",
    "Haberleşme, Ağ ve Siber Güvenlik Mühendisi": "Siber Güvenlik, Ağ ve Erişim Sorumlusu",
    "Ulaşım Teknolojileri Proje Yöneticisi": "AUS Proje ve Değişiklik Yöneticisi",
    "TKM Operasyon Birim Sorumlusu": "TKM Operasyon Sorumlusu",
    "Sinyal Optimizasyon ve Operasyon Raporlama Mühendisi": "Sinyal Optimizasyon ve Operasyon Analisti",
    "Tarife, Maliyet ve Kapasite Planlama Uzmanı": "Tarife, Maliyet ve Filo Planlama Uzmanı",
    "Durak Hizmetleri Planlama Uzmanı": "Durak Hizmetleri ve Erişilebilirlik Planlama Uzmanı",
    "İşletmeci İlişkileri ve Sözleşme Teknik Kontrol Sorumlusu": "İşletmeci İlişkileri ve Hizmet Kalitesi Sorumlusu",
    "Hizmet Kalitesi ve Şikâyet Yönetimi Sorumlusu": "İşletmeci İlişkileri ve Hizmet Kalitesi Sorumlusu",
    "Toplu Taşıma Veri Analisti": "Toplu Taşıma Veri ve Performans Analisti",
    "Ruhsat ve Vize Birim Sorumlusu": "Ruhsat ve Vize İşlemleri Sorumlusu",
    "Başvuru, Belge ve Dijital Süreç Uzmanı": "Dijital Başvuru ve Belge Yönetimi Uzmanı",
    "Servis Araçları İşlemleri Sorumlusu": "Servis, Taksi ve Ticari Plaka İşlemleri Sorumlusu",
    "Taksi ve Ticari Plaka İşlemleri Sorumlusu": "Servis, Taksi ve Ticari Plaka İşlemleri Sorumlusu",
    "Arşiv, Mevzuat ve Kalite Kontrol Uzmanı": "Mevzuat ve Kalite Kontrol Uzmanı",
    "Alt Komisyon ve Kurumlar Arası Koordinasyon Sorumlusu": "Alt Komisyon ve Kurum Koordinasyon Sorumlusu",
    "Karar Dağıtım, Tebligat ve Arşiv Sorumlusu": "Karar Dağıtım, Tebligat ve Arşiv Personeli",
    "Terminal Operasyon ve Peron Sorumlusu": "Terminal Operasyon ve Vardiya Sorumlusu",
    "Gişe ve Tahakkuk Sorumlusu": "Gişe, Tahakkuk ve Tarife Sorumlusu",
    "Kasa, Gelir Mutabakat ve Raporlama Sorumlusu": "Kasa ve Gelir Mutabakat Sorumlusu",
    "Güvenlik ve Ortak Hizmetler Koordinatörü": "Terminal Güvenlik ve İSG Koordinatörü",
    "Bütçe, Performans ve Faaliyet Raporlama Sorumlusu": "Bütçe ve Performans Sorumlusu",
    "Sözleşme, Teminat ve Hakediş Dosyası Sorumlusu": "Sözleşme ve Teminat Sorumlusu / Hakediş ve Ödeme Dosyası Sorumlusu",
    "İç Kontrol, Risk ve Süreç Yönetimi Uzmanı": "İç Kontrol ve Risk Sorumlusu",
}

BRANCH_BY_FOLDER = {
    "trafik_planlama": "Ulaşım Planlama Şube Müdürlüğü",
    "trafik_egitim": "Ulaşım Planlama Şube Müdürlüğü",
    "akilli_ulasim": "Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü",
    "toplu_ulasim": "Toplu Taşıma Planlama ve İşletme Şube Müdürlüğü",
    "ukome": "UKOME Şube Müdürlüğü",
    "otogar": "Otogar İşletme Şube Müdürlüğü",
    "idari_isler": "İdari ve Mali İşler Şube Müdürlüğü",
}


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().rstrip("."))


def parse_09_positions() -> tuple[dict[str, str], dict[str, str]]:
    position_to_unit: dict[str, str] = {}
    unit_to_branch: dict[str, str] = {"Şube Müdürlüğü Yönetimi": "İlgili Şube Müdürlüğü"}
    for path in sorted(POSITION_DIR.glob("0[1-8]_*.md")):
        text = path.read_text(encoding="utf-8")
        title = text.splitlines()[0].removeprefix("# ").split(" — ")[0]
        branch = title
        for line in text.splitlines():
            m = TABLE_RE.match(line)
            if not m:
                continue
            position, unit = normalize(m.group(1)), normalize(m.group(2))
            if position in {"Pozisyon", "---"} or unit in {"Bağlı birim", "---"}:
                continue
            position_to_unit[position] = unit
            unit_to_branch[unit] = branch
    # Ortak roller
    common = POSITION_DIR / "09_ortak_pozisyonlar_ve_kadro_ilkeleri.md"
    if common.exists():
        for line in common.read_text(encoding="utf-8").splitlines():
            m = TABLE_RE.match(line)
            if not m:
                continue
            position, unit = normalize(m.group(1)), "Daire Geneli Ortak Uzmanlık Desteği"
            if position in {"Ortak pozisyon", "---"}:
                continue
            position_to_unit[position] = unit
            unit_to_branch[unit] = "Ulaşım Dairesi Başkanlığı"
    return position_to_unit, unit_to_branch


def classify_process(code: str, title: str, folder: str) -> tuple[str, str]:
    t = title.casefold()
    # Ruhsat süreçleri, toplu ulaşım klasöründe olsa da ayrı şubeye atanır.
    if any(k in t for k in ["ruhsat", "vize", "ticari plaka", "servis aracı", "yük nakli", "özel taşıma", "çalışma ruhsatı"]):
        branch = "Ulaşım Ruhsat ve Ticari Araç İşlemleri Şube Müdürlüğü"
        if "yük" in t or "özel taşıma" in t or "servis" in t or "plaka" in t:
            return branch, "Ticari Araç ve Özel İzinler Birimi"
        if "tahakkuk" in t or "tarife" in t or "arşiv" in t:
            return branch, "Belge, Tahakkuk ve Kalite Birimi"
        return branch, "Ruhsat, Vize ve Başvuru Birimi"

    if code.startswith("TP-"):
        branch = "Ulaşım Planlama Şube Müdürlüğü"
        if any(k in t for k in ["ana plan", "model", "etüt", "sayım"]):
            return branch, "Ulaşım Ana Planı, Modelleme ve Veri Birimi"
        if any(k in t for k in ["sinyal", "işaretleme"]):
            return "Trafik Hizmetleri ve Sinyalizasyon Şube Müdürlüğü", (
                "Sinyalizasyon Proje ve İşletme Birimi" if "sinyal" in t else "İşaretleme, Durak ve Saha Uygulama Birimi"
            )
        if any(k in t for k in ["trafik yönetim merkezi", "tkm", "olay yönetimi"]):
            return "Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü", "Trafik Yönetim Merkezi Operasyon Birimi"
        if any(k in t for k in ["otopark erişim", "proje kontrol", "as-built"]):
            return branch, "CBS ve Teknik Proje Kontrol Birimi"
        return branch, "Yol, Kavşak ve Trafik Güvenliği Birimi"

    if code.startswith("TE-"):
        return "Ulaşım Planlama Şube Müdürlüğü", "Trafik Güvenliği ve Eğitim Birimi"

    if code.startswith("AU-"):
        branch = "Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü"
        if any(k in t for k in ["veri platform", "kamera", "görüntü", "veri yönetimi", "siber"]):
            return branch, "Veri, Güvenlik ve Platform Birimi"
        if any(k in t for k in ["trafik yönetim", "olay", "vardiya"]):
            return branch, "Trafik Yönetim Merkezi Operasyon Birimi"
        return branch, "AUS Sistemleri ve Entegrasyon Birimi"

    if code.startswith("TU-"):
        branch = "Toplu Taşıma Planlama ve İşletme Şube Müdürlüğü"
        if any(k in t for k in ["veri", "performans", "filo", "denetim", "şikâyet"]):
            return branch, "Toplu Taşıma Veri ve Akıllı Filo Birimi"
        if any(k in t for k in ["işletmeci", "hizmet kalitesi", "sözleşme"]):
            return branch, "İşletmeci ve Hizmet Kalitesi Birimi"
        return branch, "Hat, Sefer ve Kapasite Planlama Birimi"

    if code.startswith("UK-"):
        branch = "UKOME Şube Müdürlüğü"
        if any(k in t for k in ["alt komisyon", "kurum görüş"]):
            return branch, "Alt Komisyon ve Kurum Koordinasyon Birimi"
        if any(k in t for k in ["karar", "dağıtım", "tebligat", "uygulama", "kapanış", "arşiv"]):
            return branch, "Karar, Dağıtım ve Uygulama Takip Birimi"
        return branch, "Gündem ve Dosya Kabul Birimi"

    if code.startswith("OT-"):
        branch = "Otogar İşletme Şube Müdürlüğü"
        if any(k in t for k in ["tahakkuk", "tahsilat", "kasa", "gelir", "gişe", "belge"]):
            return branch, "Gişe, Tahakkuk ve Gelir Birimi"
        if any(k in t for k in ["teknik", "arıza", "bakım", "güvenlik", "temizlik"]):
            return branch, "Teknik İşletme ve Güvenlik Koordinasyon Birimi"
        return branch, "Terminal Operasyon ve Peron Birimi"

    if code.startswith("ID-"):
        branch = "İdari ve Mali İşler Şube Müdürlüğü"
        if any(k in t for k in ["bütçe", "performans", "faaliyet raporu"]):
            return branch, "Bütçe, Performans ve Raporlama Birimi"
        if any(k in t for k in ["ihale", "satın alma", "sözleşme", "hakediş", "ödeme", "teminat"]):
            return branch, "İhale, Sözleşme ve Ödeme Dosyası Birimi"
        return branch, "EBYS, Taşınır, Personel ve İç Kontrol Birimi"

    return BRANCH_BY_FOLDER.get(folder, "Ulaşım Dairesi Başkanlığı"), "Şube Müdürlüğü Yönetimi"


def assign_source_processes() -> None:
    for path in sorted(SOURCE_DIR.rglob("*.md")):
        if path == SOURCE_DIR / "README.md":
            continue
        folder = path.parent.name
        lines = path.read_text(encoding="utf-8").splitlines()
        out: list[str] = []
        i = 0
        while i < len(lines):
            line = lines[i]
            m = PROCESS_RE.match(line)
            if not m:
                out.append(line)
                i += 1
                continue
            code, title = m.group(2), m.group(3)
            branch, unit = classify_process(code, title, folder)
            out.append(line)
            i += 1
            while i < len(lines) and (
                lines[i].startswith("**Atanan şube:**")
                or lines[i].startswith("**Atanan ana birim:**")
                or lines[i].startswith("**Organizasyon kaynağı:**")
            ):
                i += 1
            out.extend([
                "",
                f"**Atanan şube:** {branch}  ",
                f"**Atanan ana birim:** {unit}  ",
                "**Organizasyon kaynağı:** `14_yalin_organizasyon_semasi/02_sube_birim_pozisyon_semalari.md`",
            ])
        path.write_text("\n".join(out) + "\n", encoding="utf-8")


def update_label(label: str, position_to_unit: dict[str, str], unit_to_branch: dict[str, str], folder: str) -> str:
    if "Sorumlu:" not in label:
        return label
    base = re.sub(r"<br/>Birim:.*?(?=<br/>Şube:|$)", "", label)
    base = re.sub(r"<br/>Şube:.*$", "", base)
    prefix, responsible = base.rsplit("Sorumlu:", 1)
    old_positions = [normalize(p) for p in responsible.split("/")]
    current_positions: list[str] = []
    for pos in old_positions:
        replacement = ALIASES.get(pos, pos)
        for item in [normalize(x) for x in replacement.split("/")]:
            if item and item not in current_positions:
                current_positions.append(item)
    units: list[str] = []
    branches: list[str] = []
    for pos in current_positions:
        unit = position_to_unit.get(pos, "Şube Müdürlüğü Yönetimi")
        if unit not in units:
            units.append(unit)
        branch = unit_to_branch.get(unit)
        if not branch or branch == "İlgili Şube Müdürlüğü":
            branch = BRANCH_BY_FOLDER.get(folder, "Ulaşım Dairesi Başkanlığı")
        if branch not in branches:
            branches.append(branch)
    return (
        prefix + "Sorumlu: " + " / ".join(current_positions)
        + "<br/>Birim: " + " / ".join(units)
        + "<br/>Şube: " + " / ".join(branches)
    )


def sync_target_maps() -> None:
    position_to_unit, unit_to_branch = parse_09_positions()
    if TARGET_DIR.exists():
        shutil.rmtree(TARGET_DIR)
    shutil.copytree(SOURCE_DIR, TARGET_DIR)
    for path in sorted(TARGET_DIR.rglob("*.md")):
        folder = path.parent.name
        text = path.read_text(encoding="utf-8")
        updated = NODE_RE.sub(
            lambda m: m.group("prefix") + m.group("open")
            + update_label(m.group("label"), position_to_unit, unit_to_branch, folder)
            + m.group("close"),
            text,
        )
        path.write_text(updated, encoding="utf-8")

    readme = TARGET_DIR / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        note = (
            "\n## Güncel organizasyon ve sorumluluk kaynağı\n\n"
            "Süreçlerin şube ve ana birim atamaları `14_yalin_organizasyon_semasi/02_sube_birim_pozisyon_semalari.md`; "
            "diyagramlardaki güncel pozisyon adları ve bağlı birimler `09_yalin_pozisyonlari` esas alınarak üretilmiştir. "
            "Her düğümde `Sorumlu:`, `Birim:` ve `Şube:` bilgileri birlikte gösterilir.\n"
        )
        if "## Güncel organizasyon ve sorumluluk kaynağı" not in text:
            text = text.rstrip() + "\n" + note
        readme.write_text(text, encoding="utf-8")


def main() -> None:
    if not ORG_FILE.exists() or not SOURCE_DIR.exists() or not POSITION_DIR.exists():
        raise SystemExit("Gerekli kaynak klasör veya dosyalardan biri bulunamadı.")
    assign_source_processes()
    sync_target_maps()


if __name__ == "__main__":
    main()
