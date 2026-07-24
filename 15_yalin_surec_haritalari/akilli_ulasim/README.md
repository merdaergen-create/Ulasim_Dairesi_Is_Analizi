# Akıllı Ulaşım Sistemleri Süreç Haritaları

Bu bölüm EDS/AUS sistemleri, ulaşım veri platformu, akıllı durak ve kamera/veri yönetimi süreçlerini gösterir. Akıllı Ulaşım Sistemleri teknoloji, veri, entegrasyon ve sistem sürekliliğinin sahibidir; trafik ihtiyacı, yer seçimi ve trafik mühendisliği Ulaşım Planlama tarafından yürütülür.

---

## AU-01 — EDS/AUS ihtiyacı, tasarımı, kurulumu ve kabulü

**Atanan şube:** Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü  
**Atanan ana birim:** AUS Sistemleri ve Entegrasyon Birimi  
**Organizasyon kaynağı:** `14_yalin_organizasyon_semasi/02_sube_birim_pozisyon_semalari.md`

**İş ihtiyacı sahibi:** Ulaşım Planlama  
**Teknoloji ve sistem sahibi:** Akıllı Ulaşım Sistemleri Şube Müdürlüğü  
**Karar paydaşları:** UKOME, kolluk, Hukuk Müşavirliği, Bilgi İşlem ve ilgili kurumlar  
**Girdiler:** Kaza/ihlal ve trafik verisi, saha etüdü, mevzuat kriterleri, kurum görüşleri, mevcut mimari, bütçe.  
**Çıktılar:** Onaylı saha/iş gereksinimi, teknik mimari, kurulmuş ve kabul edilmiş sistem, veri akışı ve etki raporu.

```mermaid
flowchart TD
    A([Trafik güvenliği veya yönetim ihtiyacı<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]) --> B[Ulaşım Planlama: veri, saha ve fizibilite analizi<br/>Sorumlu: Trafik Etüt ve Veri Analizi Uzmanı<br/>Birim: Ulaşım Ana Planı, Modelleme ve Veri Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    B --> C{EDS/AUS uygun çözüm mü?<br/>Sorumlu: EDS ve Saha Sistemleri Sorumlusu<br/>Birim: AUS Sistemleri ve Entegrasyon Birimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü}
    C -- Hayır --> D[Geometrik, işaretleme, eğitim veya denetim alternatifi<br/>Sorumlu: Ulaşım Veri Platformu ve Veri Yönetişimi Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    C -- Evet --> E[Saha listesi, iş gereksinimi ve beklenen etki<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    E --> F[Kolluk, UKOME ve hukuk görüşleri<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    F --> G{Yetki ve mevzuat uygun mu?<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü}
    G -- Hayır --> H[Proje kapsamı/yer/yöntem revizyonu<br/>Sorumlu: AUS Proje ve Değişiklik Yöneticisi<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    H --> E
    G -- Evet --> I[AUS: sistem mimarisi, veri modeli ve entegrasyon<br/>Sorumlu: AUS Sistem Mimarı ve Entegrasyon Sorumlusu<br/>Birim: AUS Sistemleri ve Entegrasyon Birimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    I --> J[Bilgi güvenliği, KVKK, ağ ve süreklilik tasarımı<br/>Sorumlu: Siber Güvenlik, Ağ ve Erişim Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    J --> K[Teknik şartname, kabul kriteri ve yaklaşık maliyet<br/>Sorumlu: AUS Sistem Mimarı ve Entegrasyon Sorumlusu<br/>Birim: AUS Sistemleri ve Entegrasyon Birimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    K --> L[İhale ve tedarik süreci<br/>Sorumlu: AUS Proje ve Değişiklik Yöneticisi<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    L --> M[Saha altyapısı, kurulum ve merkez entegrasyonu<br/>Sorumlu: AUS Sistem Mimarı ve Entegrasyon Sorumlusu<br/>Birim: AUS Sistemleri ve Entegrasyon Birimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    M --> N[Elektriksel, fonksiyonel, veri ve siber güvenlik testleri<br/>Sorumlu: Siber Güvenlik, Ağ ve Erişim Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    N --> O{Kabul kriterleri sağlandı mı?<br/>Sorumlu: Siber Güvenlik, Ağ ve Erişim Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü}
    O -- Hayır --> P[Düzeltme ve tekrar test<br/>Sorumlu: AUS Proje ve Değişiklik Yöneticisi<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    P --> N
    O -- Evet --> Q[Ortak kabul: Planlama + AUS + yetkili kurum<br/>Sorumlu: AUS Proje ve Değişiklik Yöneticisi<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    Q --> R[Envanter, konfigürasyon, bakım ve işletme devri<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    R --> S[Planlama: 30/90/180 günlük etki analizi<br/>Sorumlu: Trafik Etüt ve Veri Analizi Uzmanı<br/>Birim: Ulaşım Ana Planı, Modelleme ve Veri Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    S --> T([Etki ve performans raporu<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü])
```

**Temel kontroller:** Yetki ve veri işleme dayanağı, loglama, zaman senkronizasyonu, siber güvenlik testi, veri saklama süresi, yedekleme, kabul sırasında uçtan uca veri doğrulaması.

**Önerilen KPI:** Sistem kullanılabilirliği, veri kaybı oranı, arıza çözüm süresi, hedeflenen kaza/ihlal değişimi, yanlış tespit/yanlış alarm oranı.

---

## AU-02 — Ulaşım veri platformu ve karar destek

**Atanan şube:** Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü  
**Atanan ana birim:** Veri, Güvenlik ve Platform Birimi  
**Organizasyon kaynağı:** `14_yalin_organizasyon_semasi/02_sube_birim_pozisyon_semalari.md`

**Süreç sahibi:** Akıllı Ulaşım Sistemleri Şube Müdürlüğü  
**Veri sahipleri:** İlgili şubeler  
**Girdiler:** Kamera, sensör, sinyal, araç, hat, ruhsat, otogar, şikâyet, kaza ve saha varlık verileri.  
**Çıktılar:** Veri kataloğu, kalite skoru, ortak gösterge paneli, API, analiz raporu ve yetkili veri paylaşımı.

```mermaid
flowchart TD
    A([Yeni veri kaynağı veya analiz ihtiyacı<br/>Sorumlu: Ulaşım Veri Platformu ve Veri Yönetişimi Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]) --> B[İş sahibi şube: amaç ve karar ihtiyacı<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    B --> C[AUS: veri kaynağı, alanlar ve entegrasyon analizi<br/>Sorumlu: AUS Sistem Mimarı ve Entegrasyon Sorumlusu<br/>Birim: AUS Sistemleri ve Entegrasyon Birimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    C --> D[Veri sahibi, erişim rolü ve saklama süresi<br/>Sorumlu: Siber Güvenlik, Ağ ve Erişim Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    D --> E[KVKK, bilgi güvenliği ve paylaşım kontrolü<br/>Sorumlu: Siber Güvenlik, Ağ ve Erişim Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    E --> F{Veri alınabilir mi?<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü}
    F -- Hayır --> G[Anonimleştirme, kapsam azaltma veya hukuki düzenleme<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    G --> E
    F -- Evet --> H[ETL/API ve veri sözlüğü<br/>Sorumlu: Ulaşım Veri Platformu ve Veri Yönetişimi Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    H --> I[Doğruluk, tamlık, güncellik ve tekillik kontrolleri<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    I --> J{Kalite eşiği sağlandı mı?<br/>Sorumlu: Siber Güvenlik, Ağ ve Erişim Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü}
    J -- Hayır --> K[Kaynak sistem düzeltmesi ve veri kalite görevi<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    K --> I
    J -- Evet --> L[Veri kataloğu ve erişim yetkisi<br/>Sorumlu: Siber Güvenlik, Ağ ve Erişim Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    L --> M[Gösterge paneli, model veya rapor<br/>Sorumlu: Ulaşım Veri Platformu ve Veri Yönetişimi Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    M --> N[İş sahibi şube tarafından anlam ve sonuç doğrulaması<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    N --> O{Karar için uygun mu?<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü}
    O -- Hayır --> M
    O -- Evet --> P[Yayımlama ve periyodik kalite izleme<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
```

**Yönetişim ilkesi:** AUS verinin teknik platform sahibidir; verinin anlamı, iş kuralı ve doğruluğundan kaynak şube sorumludur.

**Önerilen KPI:** Veri kaynağı kullanılabilirliği, güncellik gecikmesi, kalite skoru, yetkisiz erişim olayı, manuel rapor üretim süresi.

---

## AU-03 — Akıllı durak ve yolcu bilgilendirme sistemi

**Atanan şube:** Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü  
**Atanan ana birim:** AUS Sistemleri ve Entegrasyon Birimi  
**Organizasyon kaynağı:** `14_yalin_organizasyon_semasi/02_sube_birim_pozisyon_semalari.md`

**Hizmet sahibi:** Toplu Taşıma  
**Fiziksel durak sahibi:** Ulaşım Planlama  
**Dijital sistem sahibi:** Akıllı Ulaşım Sistemleri  
**Girdiler:** Onaylı durak, hat/zaman verisi, enerji/haberleşme, erişilebilirlik, yolcu bilgi gereksinimleri.  
**Çıktılar:** Gerçek zamanlı yolcu bilgisi, çalışan ekran/sesli sistem, bakım kaydı ve hizmet KPI.

```mermaid
flowchart TD
    A([Onaylı durak veya dijital iyileştirme ihtiyacı<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]) --> B[Toplu Taşıma: gösterilecek hizmet bilgisi<br/>Sorumlu: Akıllı Filo Operasyon Sorumlusu<br/>Birim: Toplu Taşıma Veri ve Akıllı Filo Birimi<br/>Şube: Toplu Taşıma Planlama ve İşletme Şube Müdürlüğü]
    B --> C[Ulaşım Planlama: fiziksel yer ve erişilebilirlik<br/>Sorumlu: Yol ve Kavşak Tasarım Sorumlusu<br/>Birim: Yol, Kavşak ve Trafik Güvenliği Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    C --> D[AUS: ekran, ses, enerji, ağ ve veri tasarımı<br/>Sorumlu: Siber Güvenlik, Ağ ve Erişim Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    D --> E{Altyapı uygun mu?<br/>Sorumlu: Ulaşım Veri Platformu ve Veri Yönetişimi Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü}
    E -- Hayır --> F[Alternatif enerji/haberleşme veya durak revizyonu<br/>Sorumlu: Siber Güvenlik, Ağ ve Erişim Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    F --> D
    E -- Evet --> G[Tedarik ve kurulum<br/>Sorumlu: AUS Proje ve Değişiklik Yöneticisi<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    G --> H[Hat, zaman ve gerçek zamanlı veri entegrasyonu<br/>Sorumlu: AUS Sistem Mimarı ve Entegrasyon Sorumlusu<br/>Birim: AUS Sistemleri ve Entegrasyon Birimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    H --> I[Erişilebilirlik, içerik ve teknik test<br/>Sorumlu: AUS Proje ve Değişiklik Yöneticisi<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    I --> J{Kabul uygun mu?<br/>Sorumlu: AUS Proje ve Değişiklik Yöneticisi<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü}
    J -- Hayır --> K[Düzeltme<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    K --> I
    J -- Evet --> L[Durak varlık kaydı ve hizmete alma<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    L --> M[Alarm/ihbar ve uzaktan izleme<br/>Sorumlu: AUS Sistem Mimarı ve Entegrasyon Sorumlusu<br/>Birim: AUS Sistemleri ve Entegrasyon Birimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    M --> N{Arıza türü<br/>Sorumlu: AUS Sistem Mimarı ve Entegrasyon Sorumlusu<br/>Birim: AUS Sistemleri ve Entegrasyon Birimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü}
    N -- Fiziksel --> O[Ulaşım Planlama/Fen bakım<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    N -- Dijital --> P[AUS/yüklenici bakım<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    N -- Veri --> Q[Toplu Taşıma/AUS veri düzeltme<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    O --> R[Servis testi ve kapanış<br/>Sorumlu: AUS Proje ve Değişiklik Yöneticisi<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    P --> R
    Q --> R
```

---

## AU-04 — Kamera görüntüsü talebi, erişim ve teslim

**Atanan şube:** Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü  
**Atanan ana birim:** Veri, Güvenlik ve Platform Birimi  
**Organizasyon kaynağı:** `14_yalin_organizasyon_semasi/02_sube_birim_pozisyon_semalari.md`

**Teknik veri saklama sahibi:** Akıllı Ulaşım Sistemleri  
**Hukuki karar sahibi:** Yetkilendirilmiş birim/Hukuk Müşavirliği  
**Girdiler:** Yetkili kurum veya kişi talebi, olay, tarih-saat, konum ve hukuki dayanak.  
**Çıktılar:** Yetki kontrolü, arama kaydı, güvenli teslim veya gerekçeli ret, erişim ve silme logu.

```mermaid
flowchart TD
    A([Görüntü talebi<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]) --> B[Başvuru kaydı, talep sahibi ve hukuki dayanak<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    B --> C[Yetkilendirilmiş birim/Hukuk: talep yetki kontrolü<br/>Sorumlu: Hukuk ve Mevzuat Koordinatörü<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Ulaşım Dairesi Başkanlığı]
    C --> D{Talep hukuken uygun mu?<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü}
    D -- Hayır --> E[Gerekçeli ret ve kayıt<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    D -- Evet --> F[AUS: kamera, konum ve saklama süresi kontrolü<br/>Sorumlu: AUS Sistem Mimarı ve Entegrasyon Sorumlusu<br/>Birim: AUS Sistemleri ve Entegrasyon Birimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    F --> G{Görüntü mevcut mu?<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü}
    G -- Hayır --> H[Mevcut değil/saklama süresi dolmuş cevabı<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    G -- Evet --> I[Yetkili personel tarafından arama ve dışa aktarma<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    I --> J[Bütünlük doğrulaması, maskeleme ve dosya hash<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    J --> K[Güvenli ortamda teslim ve teslim tutanağı<br/>Sorumlu: Siber Güvenlik, Ağ ve Erişim Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    K --> L[Tüm erişim, kopyalama ve teslim işlemlerinin loglanması<br/>Sorumlu: Siber Güvenlik, Ağ ve Erişim Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    L --> M[Saklama/imha takvimi<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
```

**Kritik kontroller:** Rol bazlı erişim, çift onay, tüm işlemlerde log, güvenli teslim kanalı, talep kapsamı dışında görüntü verilmemesi, saklama-imha politikası.

---

## AU-05 — AUS arıza ve değişiklik yönetimi

**Atanan şube:** Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü  
**Atanan ana birim:** AUS Sistemleri ve Entegrasyon Birimi  
**Organizasyon kaynağı:** `14_yalin_organizasyon_semasi/02_sube_birim_pozisyon_semalari.md`

```mermaid
flowchart LR
    A[Alarm, kullanıcı ihbarı veya değişiklik talebi<br/>Sorumlu: AUS Sistem Mimarı ve Entegrasyon Sorumlusu<br/>Birim: AUS Sistemleri ve Entegrasyon Birimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü] --> B[Kayıt ve etki/öncelik<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    B --> C{Arıza mı, değişiklik mi?<br/>Sorumlu: AUS Sistem Mimarı ve Entegrasyon Sorumlusu<br/>Birim: AUS Sistemleri ve Entegrasyon Birimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü}
    C -- Arıza --> D[İlk teşhis ve hizmet sürekliliği<br/>Sorumlu: AUS Sistem Mimarı ve Entegrasyon Sorumlusu<br/>Birim: AUS Sistemleri ve Entegrasyon Birimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    D --> E[Uygulama, ağ, saha cihazı veya veri kaynağı<br/>Sorumlu: Ulaşım Veri Platformu ve Veri Yönetişimi Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    E --> F[Müdahale, test ve servis dönüşü<br/>Sorumlu: AUS Proje ve Değişiklik Yöneticisi<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    F --> G[Kök neden ve tekrar önleme<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    C -- Değişiklik --> H[İş sahibi, kapsam, risk ve geri dönüş planı<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    H --> I[Test ortamı ve kullanıcı kabulü<br/>Sorumlu: AUS Proje ve Değişiklik Yöneticisi<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    I --> J{Onaylandı mı?<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü}
    J -- Hayır --> H
    J -- Evet --> K[Kontrollü canlıya alma<br/>Sorumlu: AUS ve TKM Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
    K --> L[İzleme ve değişiklik kapanışı<br/>Sorumlu: AUS Sistem Mimarı ve Entegrasyon Sorumlusu<br/>Birim: AUS Sistemleri ve Entegrasyon Birimi<br/>Şube: Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü]
```
