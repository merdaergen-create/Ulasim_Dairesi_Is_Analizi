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
    A([Trafik güvenliği veya yönetim ihtiyacı]) --> B[Ulaşım Planlama: veri, saha ve fizibilite analizi]
    B --> C{EDS/AUS uygun çözüm mü?}
    C -- Hayır --> D[Geometrik, işaretleme, eğitim veya denetim alternatifi]
    C -- Evet --> E[Saha listesi, iş gereksinimi ve beklenen etki]
    E --> F[Kolluk, UKOME ve hukuk görüşleri]
    F --> G{Yetki ve mevzuat uygun mu?}
    G -- Hayır --> H[Proje kapsamı/yer/yöntem revizyonu]
    H --> E
    G -- Evet --> I[AUS: sistem mimarisi, veri modeli ve entegrasyon]
    I --> J[Bilgi güvenliği, KVKK, ağ ve süreklilik tasarımı]
    J --> K[Teknik şartname, kabul kriteri ve yaklaşık maliyet]
    K --> L[İhale ve tedarik süreci]
    L --> M[Saha altyapısı, kurulum ve merkez entegrasyonu]
    M --> N[Elektriksel, fonksiyonel, veri ve siber güvenlik testleri]
    N --> O{Kabul kriterleri sağlandı mı?}
    O -- Hayır --> P[Düzeltme ve tekrar test]
    P --> N
    O -- Evet --> Q[Ortak kabul: Planlama + AUS + yetkili kurum]
    Q --> R[Envanter, konfigürasyon, bakım ve işletme devri]
    R --> S[Planlama: 30/90/180 günlük etki analizi]
    S --> T([Etki ve performans raporu])
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
    A([Yeni veri kaynağı veya analiz ihtiyacı]) --> B[İş sahibi şube: amaç ve karar ihtiyacı]
    B --> C[AUS: veri kaynağı, alanlar ve entegrasyon analizi]
    C --> D[Veri sahibi, erişim rolü ve saklama süresi]
    D --> E[KVKK, bilgi güvenliği ve paylaşım kontrolü]
    E --> F{Veri alınabilir mi?}
    F -- Hayır --> G[Anonimleştirme, kapsam azaltma veya hukuki düzenleme]
    G --> E
    F -- Evet --> H[ETL/API ve veri sözlüğü]
    H --> I[Doğruluk, tamlık, güncellik ve tekillik kontrolleri]
    I --> J{Kalite eşiği sağlandı mı?}
    J -- Hayır --> K[Kaynak sistem düzeltmesi ve veri kalite görevi]
    K --> I
    J -- Evet --> L[Veri kataloğu ve erişim yetkisi]
    L --> M[Gösterge paneli, model veya rapor]
    M --> N[İş sahibi şube tarafından anlam ve sonuç doğrulaması]
    N --> O{Karar için uygun mu?}
    O -- Hayır --> M
    O -- Evet --> P[Yayımlama ve periyodik kalite izleme]
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
    A([Onaylı durak veya dijital iyileştirme ihtiyacı]) --> B[Toplu Taşıma: gösterilecek hizmet bilgisi]
    B --> C[Ulaşım Planlama: fiziksel yer ve erişilebilirlik]
    C --> D[AUS: ekran, ses, enerji, ağ ve veri tasarımı]
    D --> E{Altyapı uygun mu?}
    E -- Hayır --> F[Alternatif enerji/haberleşme veya durak revizyonu]
    F --> D
    E -- Evet --> G[Tedarik ve kurulum]
    G --> H[Hat, zaman ve gerçek zamanlı veri entegrasyonu]
    H --> I[Erişilebilirlik, içerik ve teknik test]
    I --> J{Kabul uygun mu?}
    J -- Hayır --> K[Düzeltme]
    K --> I
    J -- Evet --> L[Durak varlık kaydı ve hizmete alma]
    L --> M[Alarm/ihbar ve uzaktan izleme]
    M --> N{Arıza türü}
    N -- Fiziksel --> O[Ulaşım Planlama/Fen bakım]
    N -- Dijital --> P[AUS/yüklenici bakım]
    N -- Veri --> Q[Toplu Taşıma/AUS veri düzeltme]
    O --> R[Servis testi ve kapanış]
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
    A([Görüntü talebi]) --> B[Başvuru kaydı, talep sahibi ve hukuki dayanak]
    B --> C[Yetkilendirilmiş birim/Hukuk: talep yetki kontrolü]
    C --> D{Talep hukuken uygun mu?}
    D -- Hayır --> E[Gerekçeli ret ve kayıt]
    D -- Evet --> F[AUS: kamera, konum ve saklama süresi kontrolü]
    F --> G{Görüntü mevcut mu?}
    G -- Hayır --> H[Mevcut değil/saklama süresi dolmuş cevabı]
    G -- Evet --> I[Yetkili personel tarafından arama ve dışa aktarma]
    I --> J[Bütünlük doğrulaması, maskeleme ve dosya hash]
    J --> K[Güvenli ortamda teslim ve teslim tutanağı]
    K --> L[Tüm erişim, kopyalama ve teslim işlemlerinin loglanması]
    L --> M[Saklama/imha takvimi]
```

**Kritik kontroller:** Rol bazlı erişim, çift onay, tüm işlemlerde log, güvenli teslim kanalı, talep kapsamı dışında görüntü verilmemesi, saklama-imha politikası.

---

## AU-05 — AUS arıza ve değişiklik yönetimi

```mermaid
flowchart LR
    A[Alarm, kullanıcı ihbarı veya değişiklik talebi] --> B[Kayıt ve etki/öncelik]
    B --> C{Arıza mı, değişiklik mi?}
    C -- Arıza --> D[İlk teşhis ve hizmet sürekliliği]
    D --> E[Uygulama, ağ, saha cihazı veya veri kaynağı]
    E --> F[Müdahale, test ve servis dönüşü]
    F --> G[Kök neden ve tekrar önleme]
    C -- Değişiklik --> H[İş sahibi, kapsam, risk ve geri dönüş planı]
    H --> I[Test ortamı ve kullanıcı kabulü]
    I --> J{Onaylandı mı?}
    J -- Hayır --> H
    J -- Evet --> K[Kontrollü canlıya alma]
    K --> L[İzleme ve değişiklik kapanışı]
```
