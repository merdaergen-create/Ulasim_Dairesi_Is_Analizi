from __future__ import annotations

import generate_yalin_responsible_process_maps as generator

# Genel düğümlerde de somut bir yalın pozisyon kullanılır.
generator.DEFAULTS.update({
    "trafik_planlama": "Ulaşım Planlama Şube Müdürü",
    "ukome": "UKOME Şube Müdürü",
    "toplu_ulasim": "Toplu Taşıma Şube Müdürü",
    "akilli_ulasim": "AUS ve TKM Şube Müdürü",
    "otogar": "Otogar İşletme Şube Müdürü",
    "trafik_egitim": "Trafik Eğitim ve Farkındalık Sorumlusu",
    "idari_isler": "İdari ve Mali İşler Şube Müdürü",
})

# Daha özel eşleşmeler, mevcut kuralların önüne alınır.
generator.RULES["trafik_planlama"] = [
    (r"AUS: sensör|kamera ve veri platformu", "Ulaşım Veri Platformu ve Analitik Sorumlusu"),
    (r"Toplu Taşıma: hat|yolcu, filo ve hizmet verileri", "Toplu Taşıma Veri Analisti"),
    (r"İmar/Fen: arazi kullanımı|yatırım projeleri", "Yol ve Kavşak Tasarım Sorumlusu"),
    (r"paydaş ve kurum görüşleri", "Ulaşım Planlama Şube Müdürü"),
    (r"uygulama portföyü|onaylı plan ve izleme raporu|periyodik izleme", "Ulaşım Ana Planı ve Modelleme Sorumlusu"),
] + generator.RULES["trafik_planlama"]

generator.RULES["toplu_ulasim"] = [
    (r"AUS: araç, yolcu ve zaman verisi", "Ulaşım Veri Platformu ve Analitik Sorumlusu"),
    (r"Ulaşım Planlama: yol kapasitesi|geometri kontrolü", "Yol ve Kavşak Tasarım Sorumlusu"),
    (r"UKOME teknik teklif|UKOME karar", "Gündem ve Dosya Kabul Sorumlusu / UKOME Karar Yazım Uzmanı"),
    (r"hat, ruhsat, biletleme ve yolcu bilgi sistemlerinin güncellenmesi", "Hat ve Güzergâh Planlama Sorumlusu / Ruhsat ve Vize Birim Sorumlusu / Akıllı Filo Operasyon Sorumlusu"),
] + generator.RULES["toplu_ulasim"]

generator.RULES["akilli_ulasim"] = [
    (r"Ulaşım Planlama: veri, saha ve fizibilite", "Trafik Etüt ve Veri Analizi Uzmanı"),
    (r"Planlama: 30/90/180 günlük etki", "Trafik Etüt ve Veri Analizi Uzmanı"),
    (r"Toplu Taşıma: gösterilecek hizmet bilgisi", "Akıllı Filo Operasyon Sorumlusu"),
    (r"Ulaşım Planlama: fiziksel yer", "Yol ve Kavşak Tasarım Sorumlusu"),
    (r"yetkilendirilmiş birim/Hukuk", "Hukuk ve Mevzuat Koordinatörü"),
] + generator.RULES["akilli_ulasim"]

generator.RULES["idari_isler"] = [
    (r"araç ve sürücü uygunluğu|görev emri|kilometre|yakıt|araç teslim", "Personel ve İzin İşleri Sorumlusu"),
] + generator.RULES["idari_isler"]

# Eski kural setinde kalan genel ifadeler somut varsayılan unvanlarla değiştirilir.
for folder, rules in generator.RULES.items():
    concrete_rules = []
    for pattern, position in rules:
        if "ilgili yalın pozisyonu" in position:
            position = generator.DEFAULTS[folder]
        concrete_rules.append((pattern, position))
    generator.RULES[folder] = concrete_rules

if __name__ == "__main__":
    generator.main()
