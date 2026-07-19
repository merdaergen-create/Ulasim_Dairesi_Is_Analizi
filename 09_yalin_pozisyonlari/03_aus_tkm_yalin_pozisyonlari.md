# Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü — Yalın Pozisyon Yapısı

## Organizasyon amacı
AUS, EDS, ulaşım veri platformu, akıllı durak ve otopark sistemleri ile Trafik Yönetim Merkezinin teknik ve operasyonel faaliyetlerini tek şube altında, ancak teknoloji ve operasyon görevlerini ayrı birimler halinde yürütmek.

## Önerilen iç yapı

```text
AUS ve TKM Şube Müdürü
├── AUS Sistemleri ve Entegrasyon Birimi
├── Veri, Güvenlik ve Platform Birimi
└── Trafik Yönetim Merkezi Operasyon Birimi
```

## Yalın pozisyonlar

| Pozisyon | Ana süreçler | Birleştirilen görev alanları |
|---|---|---|
| AUS ve TKM Şube Müdürü | Teknoloji portföyü ve trafik merkezi yönetimi | Bütçe, kaynak, sistem sürekliliği ve operasyon koordinasyonu |
| AUS Sistem Mimarı ve Entegrasyon Sorumlusu | EDS, sensör, kamera, akıllı durak, filo entegrasyonu | Mimari, teknik şartname, entegrasyon ve kabul |
| Ulaşım Veri Platformu ve Analitik Sorumlusu | Veri kataloğu, API, kalite, panel ve analiz | Veri yönetişimi, veri analizi ve karar destek |
| Haberleşme, Ağ ve Siber Güvenlik Mühendisi | Fiber, radyo, saha ağı, erişim, log ve yedekleme | Ağ sürekliliği, güvenlik, yetki ve olay yönetimi |
| EDS ve Saha Sistemleri Sorumlusu | EDS teknik platformu ve saha sistemleri | Kolluk entegrasyonu, cihaz izleme, arıza ve performans |
| Akıllı Durak ve Yolcu Bilgilendirme Sorumlusu | Dijital durak, gerçek zamanlı bilgi ve içerik | Ekran, ses, enerji, haberleşme ve veri entegrasyonu |
| Ulaşım Teknolojileri Proje Yöneticisi | Teknoloji tedarik, uygulama ve kabul | Kapsam, takvim, risk, yüklenici ve test yönetimi |
| TKM Operasyon Birim Sorumlusu | 7/24 trafik izleme ve olay yönetimi | Vardiya, olay, yoğunluk ve kurum koordinasyonu |
| Vardiya Amiri | Vardiya yönetimi ve olay önceliklendirme | Görev dağılımı, devir, kayıt ve kritik bildirim |
| Trafik Kontrol Operatörü | Kamera, sensör, sinyal ve olay ekranları | Olay doğrulama, kayıt, ilk müdahale ve bilgilendirme |
| Olay Yönetimi ve Trafik Bilgilendirme Sorumlusu | Kaza, kapanma, afet ve kamu bilgilendirmesi | Kurum koordinasyonu, alternatif güzergâh ve duyuru |
| Sinyal Optimizasyon ve Operasyon Raporlama Mühendisi | Canlı trafik analizi ve performans raporu | Sinyal optimizasyonu, olay analizi ve vardiya KPI'ları |

## Süreç sahipliği

- AUS ve EDS teknik mimarisi
- Ulaşım veri platformu ve karar destek
- Kamera, sensör ve akıllı otopark sistemleri
- Akıllı durak ve yolcu bilgilendirme
- Sistem entegrasyonu, ağ ve siber güvenlik
- AUS arıza ve değişiklik yönetimi
- Trafik Yönetim Merkezi günlük operasyonu
- Olay, yoğunluk ve acil durum koordinasyonu
- Trafik bilgilendirme ve operasyon raporlaması

## Zorunlu görev ayrılığı

- TKM operasyonu trafik müdahalesini yürütür; AUS birimleri platform, ağ ve entegrasyonu işletir.
- Kalıcı trafik projesi ve politika kararı Ulaşım Planlamaya aittir.
- Saha cihazının fiziksel bakımı Trafik Hizmetleriyle koordineli yürütülür.
- Kamera/plaka/konum verisi erişimleri rol bazlı, kayıtlı ve mevzuata uygun olmalıdır.

## Ölçekleme eşiği

Kesintisiz vardiya, ayrı bütçe, yüksek olay hacmi ve sürekli kurum koordinasyonu oluştuğunda TKM Operasyon Birimi bağımsız Trafik Yönetim Merkezi Şube Müdürlüğüne dönüştürülmelidir.
