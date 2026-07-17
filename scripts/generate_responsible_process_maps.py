from __future__ import annotations

import re
import shutil
from pathlib import Path

SOURCE = Path("05_surec_haritalari")
TARGET = Path("08_surec_haritalari_sorumlulari_belirtilmis")

# Sıralama önemlidir: daha özel kurallar önce değerlendirilir.
RULES: dict[str, list[tuple[str, str]]] = {
    "trafik_planlama": [
        (r"UKOME gündem|UKOME kararı|Yetkili kurul/UKOME/Meclis", "UKOME Karar Yazım Uzmanı / UKOME Şube Müdürü"),
        (r"kapsam ve çalışma programı|plan, yatırım programı|teknik onay", "Ulaşım Planlama Şube Müdürü"),
        (r"veri ihtiyaç planı|mevcut durum modeli|kalibrasyon|alternatif senaryo|etki analizi", "Ulaşım Ana Planı ve Modelleme Birim Sorumlusu"),
        (r"AUS:|sensör|kamera|veri platformu", "Ulaşım Veri Platformu Sorumlusu"),
        (r"Toplu Taşıma:|hat, yolcu, filo", "Toplu Taşıma Veri Analisti"),
        (r"İmar/Fen|arazi kullanımı|mülkiyet|altyapı görüş", "Yol ve Kavşak Tasarım Birim Sorumlusu"),
        (r"veri kalite|ek sayım|anket|saha etüdü|ön inceleme|sayım", "Trafik Etüt ve Veri Analizi Uzmanı"),
        (r"Yol Tasarım|geometrik|halihazır|yol gövdesi", "Yol ve Kavşak Tasarım Birim Sorumlusu"),
        (r"trafik güvenliği|hız|yaya|erişilebilirlik", "Trafik Güvenliği Uzmanı"),
        (r"sinyal|faz planı|süre hesabı|programlama|Sinyalizasyon Servisi", "Sinyalizasyon Proje ve İşletme Sorumlusu"),
        (r"arıza|periyodik bakım|SLA", "Sinyalizasyon Bakım Sorumlusu"),
        (r"yatay çizgi|levha uygulaması|işaretleme", "Yatay/Düşey İşaretleme Sorumlusu"),
        (r"İSG|saha güvenlik", "İSG Saha Koordinatörü"),
        (r"kalite kontrol|kabul kriter|ortak saha kontrol|as-built|CBS", "Teknik Proje Kontrol Mühendisi / CBS ve Ulaşım Envanteri Uzmanı"),
        (r"Trafik Yönetim|olay doğrulama|Canlı veri|vardiya|dinamik mesaj|izleme", "Trafik Operasyon Birim Sorumlusu / Vardiya Amiri"),
        (r"Emniyet|sağlık|itfaiye|acil", "Olay Yönetimi Koordinatörü"),
    ],
    "ukome": [
        (r"kayıt ve dosya tamlık|Zorunlu belgeler|Eksik belge", "Gündem ve Dosya Kabul Sorumlusu"),
        (r"önceki karar|Yetki, mevzuat", "Arşiv ve Karar Araştırma Personeli"),
        (r"Alt komisyon|Saha/teknik inceleme ve kurum görüş", "Alt Komisyon Koordinatörü"),
        (r"Gündem maddesi|Gündem ve dosyaların", "Gündem ve Dosya Kabul Sorumlusu"),
        (r"toplantısı|oylama|Karar sonucu", "UKOME Şube Müdürü"),
        (r"kararının yazılması|Karar metni|uygulama şartları", "UKOME Karar Yazım Uzmanı"),
        (r"imzaları|karar numarası|e-imza|arşiv", "Dijital UKOME Sistem Sorumlusu"),
        (r"dağıtım|bildirimi|tebliğ", "Karar Dağıtım ve Tebligat Personeli"),
        (r"uygulama takibi|görev ve süre|hedef tarih|kanıt|kapanış|gecikme|escalation", "Karar Uygulama Takip Uzmanı"),
        (r"kurum|teknik şubenin belirlenmesi", "Kurumlar Arası Koordinasyon Uzmanı"),
        (r"teknik inceleme|teklif dosyası", "İlgili Teknik Şube Pozisyonu"),
    ],
    "toplu_ulasim": [
        (r"talep ve mevcut hizmet|Alternatif hat|güzergâh|sefer|zaman", "Hat ve Güzergâh Planlama Sorumlusu"),
        (r"araç, yolcu ve zaman verisi|doluluk|KPI|performans", "Toplu Taşıma Veri Analisti"),
        (r"yol kapasitesi|geometri|trafik güvenliği", "Yol ve Kavşak Tasarım Birim Sorumlusu / Trafik Güvenliği Uzmanı"),
        (r"Maliyet|tarife|sosyal etki", "Tarife ve Maliyet Analizi Uzmanı"),
        (r"filo|kapasite", "Filo ve Kapasite Planlama Uzmanı"),
        (r"işletmeci görüş|İşletmeci uygulaması|düzeltici faaliyet", "İşletmeci İlişkileri Sorumlusu"),
        (r"UKOME", "Gündem ve Dosya Kabul Sorumlusu / UKOME Karar Yazım Uzmanı"),
        (r"başvuru|belge|evrak|ruhsat|vize|plaka|hak uygunluğu", "Başvuru ve Belge Kontrol Personeli / Ruhsat ve Vize Birim Sorumlusu"),
        (r"Araç, şoför|muayene|uygunluk", "Mevzuat ve Kalite Kontrol Uzmanı"),
        (r"Ücret|tahsilat", "Tahakkuk ve Tarife Kontrol Personeli"),
        (r"Belge üretimi|e-imza|süre takvimi|otomatik bildirim", "Dijital Başvuru Süreç Uzmanı / Arşiv ve Belge Yönetimi Personeli"),
        (r"kontrol planı|şikâyet|ihlal|hizmet kusuru|kök neden", "Hizmet Kalitesi ve KPI Sorumlusu"),
        (r"durak|yürüme|erişilebilirlik", "Durak Hizmetleri Planlama Uzmanı"),
        (r"akıllı ekran|yolcu bilgi|canlı filo", "Akıllı Filo Operasyon Sorumlusu"),
        (r"sözleşme/ruhsat", "Sözleşme Teknik Kontrol Uzmanı"),
    ],
    "akilli_ulasim": [
        (r"veri, saha ve fizibilite|Saha listesi|etki analizi", "Trafik Etüt ve Veri Analizi Uzmanı / Trafik Güvenliği Uzmanı"),
        (r"sistem mimarisi|veri modeli|entegrasyon|ekran, ses, enerji, ağ", "AUS Sistem Mimarı"),
        (r"veri kaynağı|ETL/API|veri sözlüğü|veri kataloğu|kalite", "Ulaşım Veri Platformu Sorumlusu"),
        (r"KVKK|bilgi güvenliği|erişim|saklama|log|siber", "Siber Güvenlik ve Erişim Sorumlusu / Veri Koruma Süreç Sorumlusu"),
        (r"teknik şartname|yaklaşık maliyet|tedarik|kurulum|kabul", "Ulaşım Teknolojileri Proje Yöneticisi"),
        (r"EDS", "EDS Sistem Sorumlusu"),
        (r"hat, zaman|yolcu bilgi|akıllı durak", "Akıllı Durak ve Yolcu Bilgilendirme Sorumlusu"),
        (r"kamera|sensör|dışa aktarma|maskeleme|hash", "Sistem Entegrasyon Mühendisi / Veri Koruma Süreç Sorumlusu"),
        (r"ağ|haberleşme|fiber|radyo", "Haberleşme ve Ağ Mühendisi"),
        (r"gösterge paneli|model veya rapor|analiz", "Veri Analisti / Veri Bilimci"),
        (r"Alarm|arıza|ilk teşhis|Müdahale|servis dönüşü|değişiklik", "Sistem Entegrasyon Mühendisi"),
    ],
    "otogar": [
        (r"Plaka tanıma|gişe kaydı|tahakkuk|Tahsilat|Makbuz", "Gişe ve Tahakkuk Sorumlusu"),
        (r"Firma, sefer ve yetki|belge doğrulama", "Firma ve Yetki Belgesi Kontrol Personeli"),
        (r"kasa|mutabakat|mali sistem|Fark tutanağı", "Kasa ve Gelir Mutabakat Sorumlusu"),
        (r"peron|sefer ve peron kapasite", "Peron Planlama ve Tahsis Sorumlusu"),
        (r"saha|İndirme-bindirme|olay kaydı", "Terminal Operasyon Birim Sorumlusu"),
        (r"Vardiya|devir", "Vardiya Amiri"),
        (r"Arıza|bakım|teknik çağrı|Elektrik/Mekanik|iş emri", "Terminal Teknik İşletme Sorumlusu"),
        (r"güvenlik riski|kolluk", "Terminal Güvenlik Koordinatörü"),
        (r"faaliyet göstergeleri|aylık araç ve gelir|yönetici paneli", "Faaliyet ve Gelir Raporlama Uzmanı"),
        (r"Şube Müdürü onayı", "Otogar İşletme Şube Müdürü"),
    ],
    "trafik_egitim": [
        (r"Hedef grup|öğrenme ihtiyacı|Eğitim amacı|içerik|müfredat|program", "Eğitim Programları Sorumlusu"),
        (r"Kaza/ihlal verisi|öncelikli davranış", "Ölçme ve Değerlendirme Uzmanı"),
        (r"Okul/kurum|katılımcı|veli", "Okul ve Kurum Koordinatörü"),
        (r"Ön test|Son test|kazanım|Memnuniyet|etki raporu", "Ölçme ve Değerlendirme Uzmanı"),
        (r"Teorik ve uygulamalı eğitim|Ek eğitim", "Trafik Eğitim Uzmanı"),
        (r"park|seans|ekipman|bakım|güvenlik kontrol", "Eğitim Parkı İşletme Sorumlusu / Eğitim Parkı Teknik Personeli"),
        (r"kaza, ramak kala|İlk müdahale|kök neden", "Eğitim Parkı İşletme Sorumlusu"),
        (r"Taslak materyal|görsel|dil|Yayımlama", "Eğitim Materyali ve İletişim Uzmanı"),
        (r"Yetkili onay", "Trafik Eğitim Şube Müdürü"),
    ],
    "idari_isler": [
        (r"Teknik şube: kapsam|şartname|yaklaşık maliyet|Teknik kontrol", "İlgili Teknik Şube Pozisyonu"),
        (r"bütçe, ödenek|satın alma yöntemi|İhale onayı|EKAP|piyasa fiyat", "İhale ve Satın Alma Koordinatörü"),
        (r"İhale komisyonu|değerlendirme", "Yetkili İhale Komisyonu"),
        (r"Sözleşme|teminat|fiyat farkı|kesinti|ceza", "Sözleşme ve Teminat Sorumlusu"),
        (r"Hakediş|metraj|Fatura|ödeme emri|eksik evrak", "Hakediş ve Ödeme Dosyası Sorumlusu"),
        (r"muayene-kabul|Kabul uygun", "Yetkili Muayene ve Kabul Komisyonu"),
        (r"takvim, şablon|konsolidasyon|bütçe|performans hedef", "Bütçe ve Performans Sorumlusu"),
        (r"faaliyet raporu|gerçekleşme|KPI", "Faaliyet Raporlama Uzmanı"),
        (r"EBYS|evrak|havale|e-imza|arşiv|dosya kapanışı", "EBYS ve Arşiv Sorumlusu"),
        (r"izin|personel", "Personel ve İzin İşleri Sorumlusu"),
        (r"Taşınır|ambar|zimmet|sayım|TİF|varlık kaydı", "Taşınır Kayıt ve Ambar Sorumlusu"),
        (r"Mevzuat/organizasyon|etkilenen doküman|revizyon|mülga|tebliğ", "Doküman Kontrol ve Mevzuat Takip Uzmanı"),
        (r"risk|uygunsuzluk|düzeltme", "İç Kontrol ve Risk Sorumlusu"),
        (r"Daire Başkanı", "İdari ve Mali İşler Şube Müdürü / Ulaşım Dairesi Başkanı"),
    ],
}

NODE_RE = re.compile(r"(?P<prefix>\b[A-Za-z][A-Za-z0-9_]*\s*)(?P<open>\(\[|\[|\{)(?P<label>.*?)(?P<close>\]\)|\]|\})")


def position_for(folder: str, label: str) -> str:
    for pattern, position in RULES.get(folder, []):
        if re.search(pattern, label, flags=re.IGNORECASE):
            return position
    defaults = {
        "trafik_planlama": "Ulaşım Planlama Şube Müdürlüğü ilgili süreç pozisyonu",
        "ukome": "UKOME Şube Müdürlüğü ilgili süreç pozisyonu",
        "toplu_ulasim": "Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu",
        "akilli_ulasim": "Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu",
        "otogar": "Otogar İşletme ilgili süreç pozisyonu",
        "trafik_egitim": "Trafik Eğitim ilgili süreç pozisyonu",
        "idari_isler": "İdari ve Mali İşler ilgili süreç pozisyonu",
    }
    return defaults[folder]


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
            # Sadece düğüm tanımına dokunulur; oklar, karar dalları ve düğüm kimliği korunur.
            position = position_for(folder, label)
            return f'{match.group("prefix")}{match.group("open")}{label}<br/>Sorumlu: {position}{match.group("close")}'

        # Aynı satırda yalnız ilk düğüm tanımı değiştirilir. Okun hedefindeki düğüm de ayrı tanımsa ikinci geçişte işlenir.
        previous = None
        updated = line
        while previous != updated:
            previous = updated
            updated = NODE_RE.sub(repl, updated, count=1)
            # Eklenen etiketi tekrar eşleştirmeyi önle.
            if "Sorumlu:" in updated:
                break
        output.append(updated)
    return "\n".join(output) + ("\n" if text.endswith("\n") else "")


def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"Kaynak klasör bulunamadı: {SOURCE}")
    if TARGET.exists():
        shutil.rmtree(TARGET)
    TARGET.mkdir(parents=True)

    index: list[str] = [
        "# Sorumlu Pozisyonları Belirtilmiş Süreç Haritaları",
        "",
        "Bu klasör `05_surec_haritalari` içeriğinin birebir korunmuş kopyasıdır. Yalnız Mermaid düğümlerinin mevcut metinlerinin sonuna ilgili hedef pozisyon eklenmiştir.",
        "",
        "- Süreç adımı, karar noktası, sıra ve ok yönü değiştirilmez.",
        "- Yeni süreç adımı veya yeni karar düğümü eklenmez.",
        "- Pozisyon atamaları `07_hedef_gorev_tanimlari` esas alınarak yapılır.",
        "",
        "## Haritalar",
        "",
    ]

    for source_readme in sorted(SOURCE.glob("*/README.md")):
        folder = source_readme.parent.name
        if folder not in RULES:
            continue
        target_dir = TARGET / folder
        target_dir.mkdir(parents=True, exist_ok=True)
        original = source_readme.read_text(encoding="utf-8")
        annotated = annotate_mermaid(original, folder)
        (target_dir / "README.md").write_text(annotated, encoding="utf-8")
        title = original.splitlines()[0].removeprefix("# ")
        index.append(f"- [{title}]({folder}/README.md)")

    (TARGET / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
