from __future__ import annotations

import re
import shutil
from pathlib import Path

SOURCE = Path("05_surec_haritalari")
TARGET = Path("11_yalin_surec_haritalari_sorumlulari_belirtilmis")

RULES: dict[str, list[tuple[str, str]]] = {
    "trafik_planlama": [
        (r"UKOME|kurul|Meclis", "UKOME Şube Müdürlüğü ilgili yalın pozisyonu"),
        (r"kapsam ve çalışma programı|teknik onay|yatırım programı", "Ulaşım Planlama Şube Müdürü"),
        (r"model|kalibrasyon|senaryo|talep tahmini", "Ulaşım Ana Planı ve Modelleme Sorumlusu"),
        (r"sayım|anket|etüt|veri kalite|yoğunluk|kaza verisi", "Trafik Etüt ve Veri Analizi Uzmanı"),
        (r"geometrik|Yol Tasarım|halihazır|mülkiyet|otopark erişim|manevra", "Yol ve Kavşak Tasarım Sorumlusu"),
        (r"trafik güvenliği|yaya|bisiklet|erişilebilirlik|görüş mesafesi|hız", "Trafik Güvenliği ve Sürdürülebilir Ulaşım Uzmanı"),
        (r"CBS|envanter|as-built|varlık kaydı", "CBS ve Ulaşım Envanteri Uzmanı"),
        (r"kalite|kabul kriter|standart|uygulanabilirlik", "Teknik Proje Kontrol Mühendisi"),
        (r"sinyal|faz planı|programlama", "Sinyalizasyon Proje ve İşletme Sorumlusu"),
        (r"arıza|bakım|elektrik|elektronik", "Sinyalizasyon Bakım ve Elektronik Sorumlusu"),
        (r"işaretleme|yatay çizgi|levha|saha uygulama", "İşaretleme ve Trafik Saha Uygulama Sorumlusu"),
        (r"İSG|saha güvenlik", "Saha Kalite, Kabul ve İSG Teknikeri"),
        (r"Canlı veri|olay doğrulama|Trafik Yönetim|vardiya", "TKM Operasyon Birim Sorumlusu / Vardiya Amiri"),
        (r"Emniyet|sağlık|itfaiye|duyuru|alternatif güzergâh", "Olay Yönetimi ve Trafik Bilgilendirme Sorumlusu"),
    ],
    "ukome": [
        (r"kayıt|dosya tamlık|Eksik belge|gündem maddesi", "Gündem ve Dosya Kabul Sorumlusu"),
        (r"önceki karar|arşiv araştırma|mevzuat taraması", "Arşiv ve Karar Araştırma Personeli"),
        (r"Alt komisyon|kurum görüş", "Alt Komisyon Koordinatörü"),
        (r"toplantı|oylama|Karar sonucu", "UKOME Şube Müdürü"),
        (r"karar metni|tutanak|gerekçeli ret", "UKOME Karar Yazım Uzmanı"),
        (r"e-imza|karar numarası|dijital arşiv", "Dijital UKOME Sistem Sorumlusu"),
        (r"dağıtım|tebliğ|başvuru sahibine", "Karar Dağıtım ve Tebligat Personeli"),
        (r"uygulama|kanıt|hedef tarih|kapanış|gecikme", "Karar Uygulama Takip Uzmanı"),
        (r"kurum|yetkili birim", "Kurumlar Arası Koordinasyon Uzmanı"),
    ],
    "toplu_ulasim": [
        (r"hat|güzergâh|sefer|zaman|hizmet analizi", "Hat ve Güzergâh Planlama Sorumlusu"),
        (r"maliyet|tarife|sosyal etki", "Tarife ve Maliyet Analizi Uzmanı"),
        (r"filo|kapasite|araç tipi", "Filo ve Kapasite Planlama Uzmanı"),
        (r"doluluk|KPI|performans|veri analizi", "Toplu Taşıma Veri Analisti"),
        (r"işletmeci|düzeltici faaliyet", "İşletmeci İlişkileri Sorumlusu"),
        (r"şikâyet|hizmet kusuru|kalite", "Hizmet Kalitesi ve KPI Sorumlusu"),
        (r"durak|yürüme bağlantısı", "Durak Hizmetleri Planlama Uzmanı"),
        (r"canlı filo|biletleme|yolcu bilgi", "Akıllı Filo Operasyon Sorumlusu"),
        (r"başvuru|belge|evrak|plaka|tahsis|devir|iptal", "Başvuru ve Belge Kontrol Personeli"),
        (r"ruhsat|vize|yenileme|çalışma ruhsatı", "Ruhsat ve Vize Birim Sorumlusu"),
        (r"servis|okul servisi|personel servisi", "Servis Araçları İşlemleri Sorumlusu"),
        (r"taksi|ticari plaka", "Taksi ve Ticari Plaka İşlemleri Sorumlusu"),
        (r"yük nakli|özel taşıma|mevsimlik", "Yük ve Özel Taşıma İzinleri Sorumlusu"),
        (r"ücret|tahakkuk|tahsilat", "Tahakkuk ve Tarife Kontrol Personeli"),
        (r"e-başvuru|e-imza|otomatik bildirim", "Dijital Başvuru Süreç Uzmanı"),
        (r"arşiv|dosya kaydı", "Arşiv ve Belge Yönetimi Personeli"),
        (r"mevzuat|uygunluk|muayene", "Mevzuat ve Kalite Kontrol Uzmanı"),
    ],
    "akilli_ulasim": [
        (r"sistem mimarisi|entegrasyon|kamera|sensör|teknik şartname", "AUS Sistem Mimarı ve Entegrasyon Sorumlusu"),
        (r"veri kaynağı|ETL|API|veri sözlüğü|katalog|panel|analiz", "Ulaşım Veri Platformu ve Analitik Sorumlusu"),
        (r"ağ|haberleşme|fiber|radyo|siber|erişim|log|yedekleme|KVKK", "Haberleşme, Ağ ve Siber Güvenlik Mühendisi"),
        (r"EDS|saha sistemi|cihaz izleme", "EDS ve Saha Sistemleri Sorumlusu"),
        (r"akıllı durak|yolcu bilgi|ekran|ses", "Akıllı Durak ve Yolcu Bilgilendirme Sorumlusu"),
        (r"tedarik|kurulum|test|kabul|proje kapsamı", "Ulaşım Teknolojileri Proje Yöneticisi"),
        (r"Alarm|arıza|değişiklik|ilk teşhis|servis dönüşü", "AUS Sistem Mimarı ve Entegrasyon Sorumlusu"),
    ],
    "otogar": [
        (r"plaka tanıma|gişe|tahakkuk|tahsilat|makbuz", "Gişe ve Tahakkuk Sorumlusu"),
        (r"firma|sefer|yetki belgesi", "Firma ve Yetki Belgesi Kontrol Personeli"),
        (r"kasa|mutabakat|banka|POS|fark tutanağı", "Kasa ve Gelir Mutabakat Sorumlusu"),
        (r"peron|kapasite planı", "Peron Planlama ve Tahsis Sorumlusu"),
        (r"saha|indirme-bindirme|işletme", "Terminal Operasyon Birim Sorumlusu"),
        (r"vardiya|devir", "Vardiya Amiri"),
        (r"arıza|bakım|teknik çağrı|elektrik|mekanik", "Terminal Teknik İşletme Sorumlusu"),
        (r"güvenlik|kolluk", "Terminal Güvenlik Koordinatörü"),
        (r"faaliyet|gelir raporu|gösterge", "Faaliyet ve Gelir Raporlama Uzmanı"),
        (r"Şube Müdürü onayı", "Otogar İşletme Şube Müdürü"),
    ],
    "trafik_egitim": [
        (r"hedef grup|öğrenme ihtiyacı|program|müfredat|okul/kurum", "Trafik Eğitim ve Farkındalık Sorumlusu"),
        (r"teorik|uygulamalı eğitim|ön test|son test|kazanım|materyal", "Trafik Eğitim Uzmanı"),
        (r"park|seans|ekipman|bakım|güvenlik|ramak kala", "Eğitim Parkı İşletme ve Teknik Sorumlusu"),
        (r"onay|faaliyet raporu", "Ulaşım Planlama Şube Müdürü"),
    ],
    "idari_isler": [
        (r"şartname|yaklaşık maliyet|teknik kontrol", "İlgili Teknik Şubenin Yalın Pozisyonu"),
        (r"bütçe|ödenek|satın alma yöntemi|EKAP|piyasa fiyat", "İhale ve Satın Alma Koordinatörü"),
        (r"ihale komisyonu|tekliflerin değerlendirilmesi", "Yetkili İhale Komisyonu"),
        (r"sözleşme|teminat|fiyat farkı|ceza", "Sözleşme ve Teminat Sorumlusu"),
        (r"hakediş|metraj|fatura|ödeme emri|eksik evrak", "Hakediş ve Ödeme Dosyası Sorumlusu"),
        (r"muayene-kabul|kabul uygun", "Yetkili Muayene ve Kabul Komisyonu"),
        (r"takvim|şablon|performans programı|bütçe teklifi", "Bütçe ve Performans Sorumlusu"),
        (r"faaliyet raporu|gerçekleşme|KPI", "Faaliyet Raporlama Uzmanı"),
        (r"EBYS|evrak|havale|e-imza|arşiv", "EBYS ve Arşiv Sorumlusu"),
        (r"izin|personel|taşıt görev emri|araç görevlendirme", "Personel ve İzin İşleri Sorumlusu"),
        (r"taşınır|ambar|zimmet|sayım|TİF", "Taşınır Kayıt ve Ambar Sorumlusu"),
        (r"mevzuat|doküman|revizyon|mülga|tebliğ", "Doküman Kontrol ve Mevzuat Takip Uzmanı"),
        (r"risk|uygunsuzluk|düzeltme", "İç Kontrol ve Risk Sorumlusu"),
        (r"Daire Başkanı", "İdari ve Mali İşler Şube Müdürü / Ulaşım Dairesi Başkanı"),
    ],
}

NODE_RE = re.compile(r"(?P<prefix>\b[A-Za-z][A-Za-z0-9_]*\s*)(?P<open>\(\[|\[|\{)(?P<label>.*?)(?P<close>\]\)|\]|\})")

DEFAULTS = {
    "trafik_planlama": "Ulaşım Planlama ilgili yalın pozisyonu",
    "ukome": "UKOME ilgili yalın pozisyonu",
    "toplu_ulasim": "Toplu Taşıma veya Ruhsat ilgili yalın pozisyonu",
    "akilli_ulasim": "AUS ve TKM ilgili yalın pozisyonu",
    "otogar": "Otogar İşletme ilgili yalın pozisyonu",
    "trafik_egitim": "Ulaşım Planlama Trafik Eğitim ilgili yalın pozisyonu",
    "idari_isler": "İdari ve Mali İşler ilgili yalın pozisyonu",
}


def position_for(folder: str, label: str) -> str:
    for pattern, position in RULES.get(folder, []):
        if re.search(pattern, label, flags=re.IGNORECASE):
            return position
    return DEFAULTS[folder]


def annotate_mermaid(text: str, folder: str) -> str:
    in_mermaid = False
    output: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped == "```mermaid":
            in_mermaid = True
            output.append(line)
            continue
        if in_mermaid and stripped == "```":
            in_mermaid = False
            output.append(line)
            continue
        if not in_mermaid or "Sorumlu:" in line:
            output.append(line)
            continue

        def repl(match: re.Match[str]) -> str:
            label = match.group("label")
            position = position_for(folder, label)
            return f'{match.group("prefix")}{match.group("open")}{label}<br/>Sorumlu: {position}{match.group("close")}'

        updated = NODE_RE.sub(repl, line)
        output.append(updated)
    return "\n".join(output) + ("\n" if text.endswith("\n") else "")


def main() -> None:
    if TARGET.exists():
        shutil.rmtree(TARGET)
    TARGET.mkdir(parents=True)

    index = [
        "# 11 — Yalın Sorumlu Pozisyonları Belirtilmiş Süreç Haritaları",
        "",
        "Bu klasör `05_surec_haritalari` içeriğinin yapısal olarak aynen korunmuş kopyasıdır. Yalnız Mermaid düğümlerinin sonuna `10_yalin_pozisyon_gorev_tanimlari` esas alınarak `Sorumlu:` bilgisi eklenmiştir.",
        "",
        "- Süreç adımları, sırası, karar noktaları ve ok yönleri değiştirilmez.",
        "- Yeni adım veya karar düğümü eklenmez.",
        "- `05_surec_haritalari` altındaki ek süreç dosyaları da kapsanır.",
        "",
        "## Haritalar",
        "",
    ]

    for source_file in sorted(SOURCE.rglob("*.md")):
        rel = source_file.relative_to(SOURCE)
        if len(rel.parts) < 2:
            continue
        folder = rel.parts[0]
        if folder not in RULES:
            continue
        target_file = TARGET / rel
        target_file.parent.mkdir(parents=True, exist_ok=True)
        original = source_file.read_text(encoding="utf-8")
        target_file.write_text(annotate_mermaid(original, folder), encoding="utf-8")
        if source_file.name == "README.md":
            title = original.splitlines()[0].removeprefix("# ")
            index.append(f"- [{title}]({folder}/README.md)")

    (TARGET / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
