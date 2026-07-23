# Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü — Yalın Pozisyon Yapısı

## Organizasyon amacı
AUS, EDS, ulaşım veri platformu, akıllı durak ve otopark sistemleri ile Trafik Yönetim Merkezinin teknik ve operasyonel faaliyetlerini tek şube altında, ancak teknoloji ve operasyon görevlerini ayrı birimler halinde yürütmek.

## Önerilen iç yapı

```text
AUS ve TKM Şube Müdürü
├── AUS Sistemleri ve Entegrasyon Birimi
│   ├── AUS Sistem Mimarı ve Entegrasyon Sorumlusu
│   ├── EDS ve Saha Sistemleri Sorumlusu
│   └── Akıllı Durak ve Yolcu Bilgilendirme Sorumlusu
├── Daire Geneli Ortak Uzmanlık Desteği
│   ├── Ulaşım Veri Platformu ve Veri Yönetişimi Sorumlusu
│   ├── Siber Güvenlik, Ağ ve Erişim Sorumlusu
│   ├── AUS Proje ve Değişiklik Yöneticisi
│   ├── TKM Operasyon Sorumlusu
│   └── Sinyal Optimizasyon ve Operasyon Analisti
├── Trafik Yönetim Merkezi Operasyon Birimi / Terminal Operasyon ve Peron Birimi
│   └── Vardiya Amiri
└── Trafik Yönetim Merkezi Operasyon Birimi
    ├── Trafik Kontrol Operatörü
    └── Olay Yönetimi ve Trafik Bilgilendirme Sorumlusu
```

## Yalın pozisyonlar

| Pozisyon | Bağlı birim | Ana görev odağı |
|---|---|---|
| AUS ve TKM Şube Müdürü | Şube Müdürlüğü Yönetimi | Teknoloji platformları ile trafik operasyonunu aynı şube altında fakat görev ayrılığı korunarak yönetmek |
| AUS Sistem Mimarı ve Entegrasyon Sorumlusu | AUS Sistemleri ve Entegrasyon Birimi | AUS Sistem Mimarı ve Entegrasyon Sorumlusu görev alanındaki işlerin düzenli, izlenebilir ve mevzuata uygun yürütülmesini sağlamak |
| Ulaşım Veri Platformu ve Veri Yönetişimi Sorumlusu | Daire Geneli Ortak Uzmanlık Desteği | Ulaşım Veri Platformu ve Veri Yönetişimi Sorumlusu görev alanındaki işlerin düzenli, izlenebilir ve mevzuata uygun yürütülmesini sağlamak |
| Siber Güvenlik, Ağ ve Erişim Sorumlusu | Daire Geneli Ortak Uzmanlık Desteği | Siber Güvenlik, Ağ ve Erişim Sorumlusu görev alanındaki işlerin düzenli, izlenebilir ve mevzuata uygun yürütülmesini sağlamak |
| EDS ve Saha Sistemleri Sorumlusu | AUS Sistemleri ve Entegrasyon Birimi | EDS ve Saha Sistemleri Sorumlusu görev alanındaki işlerin düzenli, izlenebilir ve mevzuata uygun yürütülmesini sağlamak |
| Akıllı Durak ve Yolcu Bilgilendirme Sorumlusu | AUS Sistemleri ve Entegrasyon Birimi | Akıllı Durak ve Yolcu Bilgilendirme Sorumlusu görev alanındaki işlerin düzenli, izlenebilir ve mevzuata uygun yürütülmesini sağlamak |
| AUS Proje ve Değişiklik Yöneticisi | Daire Geneli Ortak Uzmanlık Desteği | AUS Proje ve Değişiklik Yöneticisi görev alanındaki işlerin düzenli, izlenebilir ve mevzuata uygun yürütülmesini sağlamak |
| TKM Operasyon Sorumlusu | Daire Geneli Ortak Uzmanlık Desteği | TP-06 kapsamındaki 7/24 operasyonu yönetmek |
| Vardiya Amiri | Trafik Yönetim Merkezi Operasyon Birimi / Terminal Operasyon ve Peron Birimi | Vardiya Amiri görev alanındaki işlerin düzenli, izlenebilir ve mevzuata uygun yürütülmesini sağlamak |
| Trafik Kontrol Operatörü | Trafik Yönetim Merkezi Operasyon Birimi | Trafik Kontrol Operatörü görev alanındaki işlerin düzenli, izlenebilir ve mevzuata uygun yürütülmesini sağlamak |
| Olay Yönetimi ve Trafik Bilgilendirme Sorumlusu | Trafik Yönetim Merkezi Operasyon Birimi | Olay Yönetimi ve Trafik Bilgilendirme Sorumlusu görev alanındaki işlerin düzenli, izlenebilir ve mevzuata uygun yürütülmesini sağlamak |
| Sinyal Optimizasyon ve Operasyon Analisti | Daire Geneli Ortak Uzmanlık Desteği | Sinyal Optimizasyon ve Operasyon Analisti görev alanındaki işlerin düzenli, izlenebilir ve mevzuata uygun yürütülmesini sağlamak |

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
