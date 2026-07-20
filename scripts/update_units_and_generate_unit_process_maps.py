from __future__ import annotations

import re
import shutil
from pathlib import Path

JOB_DIR = Path("10_yalin_pozisyon_gorev_tanimlari")
SOURCE_MAPS = Path("11_yalin_surec_haritalari_sorumlulari_belirtilmis")
TARGET_MAPS = Path("15_yalin_surec_haritalari")

POSITION_TO_UNIT: dict[str, str] = {
    # Ulaşım Planlama
    "Ulaşım Planlama Şube Müdürü": "Şube Müdürlüğü Yönetimi",
    "Ulaşım Ana Planı ve Modelleme Sorumlusu": "Ulaşım Ana Planı, Modelleme ve Veri Birimi",
    "Trafik Etüt ve Veri Analizi Uzmanı": "Ulaşım Ana Planı, Modelleme ve Veri Birimi",
    "Yol ve Kavşak Tasarım Sorumlusu": "Yol, Kavşak ve Trafik Güvenliği Birimi",
    "Trafik Güvenliği ve Sürdürülebilir Ulaşım Uzmanı": "Yol, Kavşak ve Trafik Güvenliği Birimi",
    "CBS ve Ulaşım Envanteri Uzmanı": "CBS ve Teknik Proje Kontrol Birimi",
    "Teknik Proje Kontrol Mühendisi": "CBS ve Teknik Proje Kontrol Birimi",
    "Trafik Eğitim ve Farkındalık Sorumlusu": "Trafik Güvenliği ve Eğitim Birimi",
    "Trafik Eğitim Uzmanı": "Trafik Güvenliği ve Eğitim Birimi",
    "Eğitim Parkı İşletme ve Teknik Sorumlusu": "Trafik Güvenliği ve Eğitim Birimi",

    # Trafik Hizmetleri ve Sinyalizasyon
    "Trafik Hizmetleri ve Sinyalizasyon Şube Müdürü": "Şube Müdürlüğü Yönetimi",
    "Sinyalizasyon Proje ve İşletme Sorumlusu": "Sinyalizasyon Proje ve İşletme Birimi",
    "Sinyalizasyon Bakım ve Elektronik Sorumlusu": "Sinyalizasyon Bakım ve Saha Elektroniği Birimi",
    "İşaretleme ve Trafik Saha Uygulama Sorumlusu": "İşaretleme, Durak ve Saha Uygulama Birimi",
    "Durak Fiziksel Varlık Sorumlusu": "İşaretleme, Durak ve Saha Uygulama Birimi",
    "Saha Kalite, Kabul ve İSG Teknikeri": "İşaretleme, Durak ve Saha Uygulama Birimi",
    "Saha Uygulama Teknik Personeli": "Sinyalizasyon Bakım ve Saha Elektroniği Birimi / İşaretleme, Durak ve Saha Uygulama Birimi",

    # AUS ve TKM
    "AUS ve TKM Şube Müdürü": "Şube Müdürlüğü Yönetimi",
    "AUS Sistem Mimarı ve Entegrasyon Sorumlusu": "AUS Sistemleri ve Entegrasyon Birimi",
    "EDS ve Saha Sistemleri Sorumlusu": "AUS Sistemleri ve Entegrasyon Birimi",
    "Akıllı Durak ve Yolcu Bilgilendirme Sorumlusu": "AUS Sistemleri ve Entegrasyon Birimi",
    "Ulaşım Teknolojileri Proje Yöneticisi": "AUS Sistemleri ve Entegrasyon Birimi",
    "Ulaşım Veri Platformu ve Analitik Sorumlusu": "Veri, Güvenlik ve Platform Birimi",
    "Haberleşme, Ağ ve Siber Güvenlik Mühendisi": "Veri, Güvenlik ve Platform Birimi",
    "TKM Operasyon Birim Sorumlusu": "Trafik Yönetim Merkezi Operasyon Birimi",
    "Vardiya Amiri": "Trafik Yönetim Merkezi Operasyon Birimi / Terminal Operasyon ve Peron Birimi",
    "Trafik Kontrol Operatörü": "Trafik Yönetim Merkezi Operasyon Birimi",
    "Olay Yönetimi ve Trafik Bilgilendirme Sorumlusu": "Trafik Yönetim Merkezi Operasyon Birimi",
    "Sinyal Optimizasyon ve Operasyon Raporlama Mühendisi": "Trafik Yönetim Merkezi Operasyon Birimi",

    # Toplu Taşıma
    "Toplu Taşıma Şube Müdürü": "Şube Müdürlüğü Yönetimi",
    "Hat, Güzergâh ve Sefer Planlama Sorumlusu": "Hat, Sefer ve Kapasite Planlama Birimi",
    "Tarife, Maliyet ve Kapasite Planlama Uzmanı": "Hat, Sefer ve Kapasite Planlama Birimi",
    "Durak Hizmetleri Planlama Uzmanı": "Hat, Sefer ve Kapasite Planlama Birimi",
    "İşletmeci İlişkileri ve Sözleşme Teknik Kontrol Sorumlusu": "İşletmeci ve Hizmet Kalitesi Birimi",
    "Hizmet Kalitesi ve Şikâyet Yönetimi Sorumlusu": "İşletmeci ve Hizmet Kalitesi Birimi",
    "Toplu Taşıma Veri ve Performans Analisti": "Toplu Taşıma Veri ve Akıllı Filo Birimi",
    "Toplu Taşıma Veri Analisti": "Toplu Taşıma Veri ve Akıllı Filo Birimi",
    "Akıllı Filo Operasyon Sorumlusu": "Toplu Taşıma Veri ve Akıllı Filo Birimi",

    # Ruhsat
    "Ulaşım Ruhsat ve Ticari Araç İşlemleri Şube Müdürü": "Şube Müdürlüğü Yönetimi",
    "Ruhsat ve Vize Birim Sorumlusu": "Ruhsat, Vize ve Başvuru Birimi",
    "Başvuru, Belge ve Dijital Süreç Uzmanı": "Ruhsat, Vize ve Başvuru Birimi",
    "Servis Araçları İşlemleri Sorumlusu": "Ticari Araç ve Özel İzinler Birimi",
    "Taksi ve Ticari Plaka İşlemleri Sorumlusu": "Ticari Araç ve Özel İzinler Birimi",
    "Yük ve Özel Taşıma İzinleri Sorumlusu": "Ticari Araç ve Özel İzinler Birimi",
    "Tahakkuk ve Tarife Kontrol Personeli": "Belge, Tahakkuk ve Kalite Birimi",
    "Arşiv, Mevzuat ve Kalite Kontrol Uzmanı": "Belge, Tahakkuk ve Kalite Birimi",

    # UKOME
    "UKOME Şube Müdürü": "Şube Müdürlüğü Yönetimi",
    "Gündem ve Dosya Kabul Sorumlusu": "Gündem ve Dosya Kabul Birimi",
    "Dijital UKOME Sistem Sorumlusu": "Gündem ve Dosya Kabul Birimi",
    "Alt Komisyon ve Kurumlar Arası Koordinasyon Sorumlusu": "Alt Komisyon ve Kurum Koordinasyon Birimi",
    "UKOME Karar Yazım Uzmanı": "Karar, Dağıtım ve Uygulama Takip Birimi",
    "Karar Dağıtım, Tebligat ve Arşiv Sorumlusu": "Karar, Dağıtım ve Uygulama Takip Birimi",
    "Karar Uygulama Takip Uzmanı": "Karar, Dağıtım ve Uygulama Takip Birimi",

    # Otogar
    "Otogar İşletme Şube Müdürü": "Şube Müdürlüğü Yönetimi",
    "Terminal Operasyon ve Peron Sorumlusu": "Terminal Operasyon ve Peron Birimi",
    "Gişe ve Saha Operasyon Personeli": "Terminal Operasyon ve Peron Birimi",
    "Gişe ve Tahakkuk Sorumlusu": "Gişe, Tahakkuk ve Gelir Birimi",
    "Kasa, Gelir Mutabakat ve Raporlama Sorumlusu": "Gişe, Tahakkuk ve Gelir Birimi",
    "Firma ve Yetki Belgesi Kontrol Personeli": "Gişe, Tahakkuk ve Gelir Birimi",
    "Terminal Teknik İşletme Sorumlusu": "Teknik İşletme ve Güvenlik Koordinasyon Birimi",
    "Güvenlik ve Ortak Hizmetler Koordinatörü": "Teknik İşletme ve Güvenlik Koordinasyon Birimi",

    # İdari ve Mali İşler
    "İdari ve Mali İşler Şube Müdürü": "Şube Müdürlüğü Yönetimi",
    "Bütçe, Performans ve Faaliyet Raporlama Sorumlusu": "Bütçe, Performans ve Raporlama Birimi",
    "İhale ve Satın Alma Koordinatörü": "İhale, Sözleşme ve Ödeme Dosyası Birimi",
    "Sözleşme, Teminat ve Hakediş Dosyası Sorumlusu": "İhale, Sözleşme ve Ödeme Dosyası Birimi",
    "Taşınır Kayıt ve Ambar Sorumlusu": "EBYS, Taşınır, Personel ve İç Kontrol Birimi",
    "EBYS, Arşiv ve Personel İşleri Sorumlusu": "EBYS, Taşınır, Personel ve İç Kontrol Birimi",
    "Doküman Kontrol ve Mevzuat Takip Uzmanı": "EBYS, Taşınır, Personel ve İç Kontrol Birimi",
    "İç Kontrol, Risk ve Süreç Yönetimi Uzmanı": "EBYS, Taşınır, Personel ve İç Kontrol Birimi",
    "İdari Destek Personeli": "EBYS, Taşınır, Personel ve İç Kontrol Birimi",

    # Ortak uzmanlıklar
    "Hukuk ve Mevzuat Koordinatörü": "Daire Geneli Ortak Uzmanlık Desteği",
    "CBS Yöneticisi": "Daire Geneli Ortak Uzmanlık Desteği",
    "Veri Yönetişimi Sorumlusu": "Daire Geneli Ortak Uzmanlık Desteği",
    "Proje Yönetim Ofisi Uzmanı": "Daire Geneli Ortak Uzmanlık Desteği",
    "Kalite ve Süreç Yönetimi Uzmanı": "Daire Geneli Ortak Uzmanlık Desteği",
    "KVKK ve Bilgi Güvenliği Koordinatörü": "Daire Geneli Ortak Uzmanlık Desteği",
    "İş Sağlığı ve Güvenliği Koordinatörü": "Daire Geneli Ortak Uzmanlık Desteği",
}

FOLDER_DEFAULT_UNIT = {
    "trafik_planlama": "Ulaşım Planlama Şube Müdürlüğü Yönetimi",
    "trafik_egitim": "Trafik Güvenliği ve Eğitim Birimi",
    "ukome": "UKOME Şube Müdürlüğü Yönetimi",
    "toplu_ulasim": "Toplu Taşıma Planlama ve İşletme Şube Müdürlüğü Yönetimi",
    "akilli_ulasim": "AUS ve TKM Şube Müdürlüğü Yönetimi",
    "otogar": "Otogar İşletme Şube Müdürlüğü Yönetimi",
    "idari_isler": "İdari ve Mali İşler Şube Müdürlüğü Yönetimi",
}

HEADING_RE = re.compile(r"^(##\s+\d+\.\s+)(.+?)\s*$")
NODE_RE = re.compile(r"(?P<prefix>\b[A-Za-z][A-Za-z0-9_]*\s*)(?P<open>\(\[|\[|\{)(?P<label>.*?)(?P<close>\]\)|\]|\})")


def units_for_responsible(responsible: str, folder: str) -> str:
    units: list[str] = []
    # Birden fazla sorumlu slash ile gösterilir.
    for position in [p.strip() for p in responsible.split("/")]:
        unit = POSITION_TO_UNIT.get(position)
        if unit:
            for item in [x.strip() for x in unit.split("/")]:
                if item and item not in units:
                    units.append(item)
    return " / ".join(units) if units else FOLDER_DEFAULT_UNIT.get(folder, "İlgili Şube Müdürlüğü Yönetimi")


def add_units_to_job_description(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        match = HEADING_RE.match(line)
        if match:
            position = match.group(2).strip()
            # Önceden eklenmiş Birim satırı varsa tekrar ekleme.
            next_line = lines[i + 1] if i + 1 < len(lines) else ""
            if not next_line.startswith("**Birim:**"):
                unit = POSITION_TO_UNIT.get(position, "Daire Geneli Ortak Uzmanlık Desteği")
                out.append(f"**Birim:** {unit}.")
        i += 1
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def update_job_descriptions() -> None:
    if not JOB_DIR.exists():
        raise SystemExit(f"Görev tanımı klasörü bulunamadı: {JOB_DIR}")
    for path in sorted(JOB_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        original = path.read_text(encoding="utf-8")
        updated = add_units_to_job_description(original)
        path.write_text(updated, encoding="utf-8")


def add_unit_to_mermaid_label(label: str, folder: str) -> str:
    if "Sorumlu:" not in label or "Birim:" in label:
        return label
    responsible = label.split("Sorumlu:", 1)[1].strip()
    unit = units_for_responsible(responsible, folder)
    return f"{label}<br/>Birim: {unit}"


def annotate_mermaid(text: str, folder: str) -> str:
    in_mermaid = False
    out: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped == "```mermaid":
            in_mermaid = True
            out.append(line)
            continue
        if in_mermaid and stripped == "```":
            in_mermaid = False
            out.append(line)
            continue
        if not in_mermaid or "Sorumlu:" not in line:
            out.append(line)
            continue

        def repl(match: re.Match[str]) -> str:
            label = add_unit_to_mermaid_label(match.group("label"), folder)
            return f'{match.group("prefix")}{match.group("open")}{label}{match.group("close")}'

        out.append(NODE_RE.sub(repl, line))
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def generate_unit_process_maps() -> None:
    if not SOURCE_MAPS.exists():
        raise SystemExit(f"Kaynak süreç haritaları bulunamadı: {SOURCE_MAPS}")
    if TARGET_MAPS.exists():
        shutil.rmtree(TARGET_MAPS)
    TARGET_MAPS.mkdir(parents=True)

    index = [
        "# 15 — Birim ve Sorumlu Pozisyonları Belirtilmiş Yalın Süreç Haritaları",
        "",
        "Bu klasör `11_yalin_surec_haritalari_sorumlulari_belirtilmis` içeriğinin yapısal olarak aynen korunmuş kopyasıdır. Mermaid diyagramlarındaki mevcut `Sorumlu:` bilgisinin yanına `14_yalin_organizasyon_semasi` esas alınarak `Birim:` bilgisi eklenmiştir.",
        "",
        "- Süreç adımları, karar noktaları, sıra ve ok yönleri değiştirilmez.",
        "- Yeni süreç adımı veya karar düğümü eklenmez.",
        "- Sorumlu pozisyon bilgisi korunur; yalnız bağlı birim bilgisi eklenir.",
        "",
        "## Haritalar",
        "",
    ]

    for source in sorted(SOURCE_MAPS.rglob("*.md")):
        rel = source.relative_to(SOURCE_MAPS)
        if rel == Path("README.md"):
            continue
        target = TARGET_MAPS / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        folder = rel.parts[0] if len(rel.parts) > 1 else ""
        original = source.read_text(encoding="utf-8")
        target.write_text(annotate_mermaid(original, folder), encoding="utf-8")

    for subdir in sorted(p for p in TARGET_MAPS.iterdir() if p.is_dir()):
        readme = subdir / "README.md"
        if readme.exists():
            title = readme.read_text(encoding="utf-8").splitlines()[0].removeprefix("# ")
            index.append(f"- [{title}]({subdir.name}/README.md)")

    (TARGET_MAPS / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")


def main() -> None:
    # Kullanıcının istediği sıra: önce görev tanımları, sonra süreç haritaları.
    update_job_descriptions()
    generate_unit_process_maps()


if __name__ == "__main__":
    main()
