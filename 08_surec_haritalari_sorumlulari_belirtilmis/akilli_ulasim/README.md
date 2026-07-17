# Akıllı Ulaşım Sistemleri Süreç Haritaları

Bu bölüm EDS/AUS sistemleri, ulaşım veri platformu, akıllı durak ve kamera/veri yönetimi süreçlerini gösterir. Akıllı Ulaşım Sistemleri teknoloji, veri, entegrasyon ve sistem sürekliliğinin sahibidir; trafik ihtiyacı, yer seçimi ve trafik mühendisliği Ulaşım Planlama tarafından yürütülür.

---

## AU-01 — EDS/AUS ihtiyacı, tasarımı, kurulumu ve kabulü

**İş ihtiyacı sahibi:** Ulaşım Planlama  
**Teknoloji ve sistem sahibi:** Akıllı Ulaşım Sistemleri Şube Müdürlüğü  
**Karar paydaşları:** UKOME, kolluk, Hukuk Müşavirliği, Bilgi İşlem ve ilgili kurumlar  
**Girdiler:** Kaza/ihlal ve trafik verisi, saha etüdü, mevzuat kriterleri, kurum görüşleri, mevcut mimari, bütçe.  
**Çıktılar:** Onaylı saha/iş gereksinimi, teknik mimari, kurulmuş ve kabul edilmiş sistem, veri akışı ve etki raporu.

```mermaid
flowchart TD
    A([Trafik güvenliği veya yönetim ihtiyacı<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]) --> B[Ulaşım Planlama: veri, saha ve fizibilite analizi]
    B --> C{EDS/AUS uygun çözüm mü?<br/>Sorumlu: EDS Sistem Sorumlusu}
    C -- Hayır --> D[Geometrik, işaretleme, eğitim veya denetim alternatifi<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    C -- Evet --> E[Saha listesi, iş gereksinimi ve beklenen etki<br/>Sorumlu: Trafik Etüt ve Veri Analizi Uzmanı / Trafik Güvenliği Uzmanı]
    E --> F[Kolluk, UKOME ve hukuk görüşleri<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    F --> G{Yetki ve mevzuat uygun mu?<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu}
    G -- Hayır --> H[Proje kapsamı/yer/yöntem revizyonu<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    H --> E
    G -- Evet --> I[AUS: sistem mimarisi, veri modeli ve entegrasyon<br/>Sorumlu: AUS Sistem Mimarı]
    I --> J[Bilgi güvenliği, KVKK, ağ ve süreklilik tasarımı<br/>Sorumlu: Siber Güvenlik ve Erişim Sorumlusu / Veri Koruma Süreç Sorumlusu]
    J --> K[Teknik şartname, kabul kriteri ve yaklaşık maliyet<br/>Sorumlu: Ulaşım Teknolojileri Proje Yöneticisi]
    K --> L[İhale ve tedarik süreci<br/>Sorumlu: Ulaşım Teknolojileri Proje Yöneticisi]
    L --> M[Saha altyapısı, kurulum ve merkez entegrasyonu<br/>Sorumlu: AUS Sistem Mimarı]
    M --> N[Elektriksel, fonksiyonel, veri ve siber güvenlik testleri<br/>Sorumlu: Siber Güvenlik ve Erişim Sorumlusu / Veri Koruma Süreç Sorumlusu]
    N --> O{Kabul kriterleri sağlandı mı?<br/>Sorumlu: Ulaşım Teknolojileri Proje Yöneticisi}
    O -- Hayır --> P[Düzeltme ve tekrar test<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    P --> N
    O -- Evet --> Q[Ortak kabul: Planlama + AUS + yetkili kurum<br/>Sorumlu: Ulaşım Teknolojileri Proje Yöneticisi]
    Q --> R[Envanter, konfigürasyon, bakım ve işletme devri<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    R --> S[Planlama: 30/90/180 günlük etki analizi<br/>Sorumlu: Trafik Etüt ve Veri Analizi Uzmanı / Trafik Güvenliği Uzmanı]
    S --> T([Etki ve performans raporu<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu])
```

**Temel kontroller:** Yetki ve veri işleme dayanağı, loglama, zaman senkronizasyonu, siber güvenlik testi, veri saklama süresi, yedekleme, kabul sırasında uçtan uca veri doğrulaması.

**Önerilen KPI:** Sistem kullanılabilirliği, veri kaybı oranı, arıza çözüm süresi, hedeflenen kaza/ihlal değişimi, yanlış tespit/yanlış alarm oranı.

---

## AU-02 — Ulaşım veri platformu ve karar destek

**Süreç sahibi:** Akıllı Ulaşım Sistemleri Şube Müdürlüğü  
**Veri sahipleri:** İlgili şubeler  
**Girdiler:** Kamera, sensör, sinyal, araç, hat, ruhsat, otogar, şikâyet, kaza ve saha varlık verileri.  
**Çıktılar:** Veri kataloğu, kalite skoru, ortak gösterge paneli, API, analiz raporu ve yetkili veri paylaşımı.

```mermaid
flowchart TD
    A([Yeni veri kaynağı veya analiz ihtiyacı<br/>Sorumlu: Ulaşım Veri Platformu Sorumlusu]) --> B[İş sahibi şube: amaç ve karar ihtiyacı]
    B --> C[AUS: veri kaynağı, alanlar ve entegrasyon analizi<br/>Sorumlu: AUS Sistem Mimarı]
    C --> D[Veri sahibi, erişim rolü ve saklama süresi<br/>Sorumlu: Siber Güvenlik ve Erişim Sorumlusu / Veri Koruma Süreç Sorumlusu]
    D --> E[KVKK, bilgi güvenliği ve paylaşım kontrolü<br/>Sorumlu: Siber Güvenlik ve Erişim Sorumlusu / Veri Koruma Süreç Sorumlusu]
    E --> F{Veri alınabilir mi?<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu}
    F -- Hayır --> G[Anonimleştirme, kapsam azaltma veya hukuki düzenleme<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    G --> E
    F -- Evet --> H[ETL/API ve veri sözlüğü<br/>Sorumlu: Ulaşım Veri Platformu Sorumlusu]
    H --> I[Doğruluk, tamlık, güncellik ve tekillik kontrolleri<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    I --> J{Kalite eşiği sağlandı mı?<br/>Sorumlu: Ulaşım Veri Platformu Sorumlusu}
    J -- Hayır --> K[Kaynak sistem düzeltmesi ve veri kalite görevi<br/>Sorumlu: Ulaşım Veri Platformu Sorumlusu]
    K --> I
    J -- Evet --> L[Veri kataloğu ve erişim yetkisi<br/>Sorumlu: Ulaşım Veri Platformu Sorumlusu]
    L --> M[Gösterge paneli, model veya rapor<br/>Sorumlu: Veri Analisti / Veri Bilimci]
    M --> N[İş sahibi şube tarafından anlam ve sonuç doğrulaması<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    N --> O{Karar için uygun mu?<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu}
    O -- Hayır --> M
    O -- Evet --> P[Yayımlama ve periyodik kalite izleme<br/>Sorumlu: Ulaşım Veri Platformu Sorumlusu]
```

**Yönetişim ilkesi:** AUS verinin teknik platform sahibidir; verinin anlamı, iş kuralı ve doğruluğundan kaynak şube sorumludur.

**Önerilen KPI:** Veri kaynağı kullanılabilirliği, güncellik gecikmesi, kalite skoru, yetkisiz erişim olayı, manuel rapor üretim süresi.

---

## AU-03 — Akıllı durak ve yolcu bilgilendirme sistemi

**Hizmet sahibi:** Toplu Taşıma  
**Fiziksel durak sahibi:** Ulaşım Planlama  
**Dijital sistem sahibi:** Akıllı Ulaşım Sistemleri  
**Girdiler:** Onaylı durak, hat/zaman verisi, enerji/haberleşme, erişilebilirlik, yolcu bilgi gereksinimleri.  
**Çıktılar:** Gerçek zamanlı yolcu bilgisi, çalışan ekran/sesli sistem, bakım kaydı ve hizmet KPI.

```mermaid
flowchart TD
    A([Onaylı durak veya dijital iyileştirme ihtiyacı<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]) --> B[Toplu Taşıma: gösterilecek hizmet bilgisi]
    B --> C[Ulaşım Planlama: fiziksel yer ve erişilebilirlik<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    C --> D[AUS: ekran, ses, enerji, ağ ve veri tasarımı<br/>Sorumlu: AUS Sistem Mimarı]
    D --> E{Altyapı uygun mu?<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu}
    E -- Hayır --> F[Alternatif enerji/haberleşme veya durak revizyonu<br/>Sorumlu: Haberleşme ve Ağ Mühendisi]
    F --> D
    E -- Evet --> G[Tedarik ve kurulum<br/>Sorumlu: Ulaşım Teknolojileri Proje Yöneticisi]
    G --> H[Hat, zaman ve gerçek zamanlı veri entegrasyonu<br/>Sorumlu: AUS Sistem Mimarı]
    H --> I[Erişilebilirlik, içerik ve teknik test<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    I --> J{Kabul uygun mu?<br/>Sorumlu: Ulaşım Teknolojileri Proje Yöneticisi}
    J -- Hayır --> K[Düzeltme<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    K --> I
    J -- Evet --> L[Durak varlık kaydı ve hizmete alma<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    L --> M[Alarm/ihbar ve uzaktan izleme<br/>Sorumlu: Sistem Entegrasyon Mühendisi]
    M --> N{Arıza türü<br/>Sorumlu: Sistem Entegrasyon Mühendisi}
    N -- Fiziksel --> O[Ulaşım Planlama/Fen bakım<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    N -- Dijital --> P[AUS/yüklenici bakım<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    N -- Veri --> Q[Toplu Taşıma/AUS veri düzeltme<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    O --> R[Servis testi ve kapanış<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    P --> R
    Q --> R
```

---

## AU-04 — Kamera görüntüsü talebi, erişim ve teslim

**Teknik veri saklama sahibi:** Akıllı Ulaşım Sistemleri  
**Hukuki karar sahibi:** Yetkilendirilmiş birim/Hukuk Müşavirliği  
**Girdiler:** Yetkili kurum veya kişi talebi, olay, tarih-saat, konum ve hukuki dayanak.  
**Çıktılar:** Yetki kontrolü, arama kaydı, güvenli teslim veya gerekçeli ret, erişim ve silme logu.

```mermaid
flowchart TD
    A([Görüntü talebi<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]) --> B[Başvuru kaydı, talep sahibi ve hukuki dayanak]
    B --> C[Yetkilendirilmiş birim/Hukuk: talep yetki kontrolü<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    C --> D{Talep hukuken uygun mu?<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu}
    D -- Hayır --> E[Gerekçeli ret ve kayıt<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    D -- Evet --> F[AUS: kamera, konum ve saklama süresi kontrolü<br/>Sorumlu: Siber Güvenlik ve Erişim Sorumlusu / Veri Koruma Süreç Sorumlusu]
    F --> G{Görüntü mevcut mu?<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu}
    G -- Hayır --> H[Mevcut değil/saklama süresi dolmuş cevabı<br/>Sorumlu: Siber Güvenlik ve Erişim Sorumlusu / Veri Koruma Süreç Sorumlusu]
    G -- Evet --> I[Yetkili personel tarafından arama ve dışa aktarma<br/>Sorumlu: Sistem Entegrasyon Mühendisi / Veri Koruma Süreç Sorumlusu]
    I --> J[Bütünlük doğrulaması, maskeleme ve dosya hash<br/>Sorumlu: Sistem Entegrasyon Mühendisi / Veri Koruma Süreç Sorumlusu]
    J --> K[Güvenli ortamda teslim ve teslim tutanağı<br/>Sorumlu: Haberleşme ve Ağ Mühendisi]
    K --> L[Tüm erişim, kopyalama ve teslim işlemlerinin loglanması<br/>Sorumlu: Siber Güvenlik ve Erişim Sorumlusu / Veri Koruma Süreç Sorumlusu]
    L --> M[Saklama/imha takvimi<br/>Sorumlu: Siber Güvenlik ve Erişim Sorumlusu / Veri Koruma Süreç Sorumlusu]
```

**Kritik kontroller:** Rol bazlı erişim, çift onay, tüm işlemlerde log, güvenli teslim kanalı, talep kapsamı dışında görüntü verilmemesi, saklama-imha politikası.

---

## AU-05 — AUS arıza ve değişiklik yönetimi

```mermaid
flowchart LR
    A[Alarm, kullanıcı ihbarı veya değişiklik talebi<br/>Sorumlu: Sistem Entegrasyon Mühendisi] --> B[Kayıt ve etki/öncelik]
    B --> C{Arıza mı, değişiklik mi?<br/>Sorumlu: Sistem Entegrasyon Mühendisi}
    C -- Arıza --> D[İlk teşhis ve hizmet sürekliliği<br/>Sorumlu: Sistem Entegrasyon Mühendisi]
    D --> E[Uygulama, ağ, saha cihazı veya veri kaynağı<br/>Sorumlu: Ulaşım Veri Platformu Sorumlusu]
    E --> F[Müdahale, test ve servis dönüşü<br/>Sorumlu: Sistem Entegrasyon Mühendisi]
    F --> G[Kök neden ve tekrar önleme<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    C -- Değişiklik --> H[İş sahibi, kapsam, risk ve geri dönüş planı<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    H --> I[Test ortamı ve kullanıcı kabulü<br/>Sorumlu: Ulaşım Teknolojileri Proje Yöneticisi]
    I --> J{Onaylandı mı?<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu}
    J -- Hayır --> H
    J -- Evet --> K[Kontrollü canlıya alma<br/>Sorumlu: Akıllı ve Sürdürülebilir Ulaşım Sistemleri ilgili süreç pozisyonu]
    K --> L[İzleme ve değişiklik kapanışı<br/>Sorumlu: Sistem Entegrasyon Mühendisi]
```
