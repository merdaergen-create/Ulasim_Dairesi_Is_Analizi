# Toplu Ulaşım Süreç Haritaları

Bu bölüm Toplu Taşıma Şube Müdürlüğünün hizmet planlama, ruhsat/vize/izin, izleme-kontrol ve durak süreçlerini gösterir. Yol kapasitesi ve trafik geometrisi Ulaşım Planlama; UKOME kurul ve karar süreci Ulaşım Koordinasyon; dijital platform ve veri entegrasyonu Akıllı Ulaşım Sistemleri sorumluluğundadır.

---

## TU-01 — Hat, güzergâh, zaman, sefer ve tarife planlama

**Süreç sahibi:** Toplu Taşıma Planlama Birimi  
**Girdiler:** Yolcu talebi, doluluk, filo ve maliyet verileri, mevcut hatlar, şikâyetler, imar/yol ağı, duraklar ve trafik koşulları.  
**Çıktılar:** Teknik rapor, hat–güzergâh–zaman–tarife önerisi, UKOME kararı, işletmeci talimatı ve izleme raporu.

```mermaid
flowchart TD
    A([Yeni talep veya performans sorunu]) --> B[Toplu Taşıma: talep ve mevcut hizmet analizi]
    B --> C[AUS: araç, yolcu ve zaman verisi]
    C --> D[Alternatif hat/güzergâh/zaman senaryoları]
    D --> E[Ulaşım Planlama: yol kapasitesi ve geometri kontrolü]
    E --> F[Maliyet, filo, tarife ve sosyal etki analizi]
    F --> G{Hizmet ve mali kriterler uygun mu?}
    G -- Hayır --> D
    G -- Evet --> H[Paydaş/işletmeci görüşü]
    H --> I[UKOME teknik teklif dosyası]
    I --> J[UKOME karar süreci]
    J --> K{Karar sonucu}
    K -- İade/Ret --> L[Gerekçe ve senaryo revizyonu]
    L --> D
    K -- Kabul --> M[Hat, ruhsat, biletleme ve yolcu bilgi sistemlerinin güncellenmesi]
    M --> N[İşletmeci uygulaması]
    N --> O[30/60/90 günlük performans izleme]
    O --> P{Hedefler sağlandı mı?}
    P -- Hayır --> D
    P -- Evet --> Q([Süreç kapanışı ve periyodik izleme])
```

**Önerilen KPI:** Sefer düzenliliği, doluluk, yolcu başına maliyet, aktarma süresi, şikâyet oranı, zamanında sefer yüzdesi.

---

## TU-02 — Ruhsat, vize, izin ve yetki belgesi

**Süreç sahibi:** Ruhsat ve Vize İşlemleri Birimi  
**Girdiler:** E-başvuru, araç/şoför/şirket belgeleri, UKOME kararı, muayene/uygunluk, ücret ve borç bilgileri.  
**Çıktılar:** Ruhsat/vize/izin/yetki belgesi, gerekçeli ret, süre ve yenileme kaydı.

```mermaid
flowchart TD
    A([Başvuru]) --> B[E-başvuru, kimlik ve başvuru türü kontrolü]
    B --> C[Otomatik belge, süre ve eksik evrak kontrolü]
    C --> D{Başvuru tam mı?}
    D -- Hayır --> E[Eksik belge bildirimi ve süre verilmesi]
    E --> C
    D -- Evet --> F[UKOME kararı ve plaka/hak uygunluğu]
    F --> G[Araç, şoför ve işletmeci mevzuat kontrolü]
    G --> H{Saha/araç uygunluk kontrolü gerekli mi?}
    H -- Evet --> I[Standart kontrol formu ve muayene]
    H -- Hayır --> J[Ücret/tahsilat hesaplama]
    I --> K{Uygun mu?}
    K -- Hayır --> L[Gerekçeli uygunsuzluk ve düzeltme süresi]
    L --> I
    K -- Evet --> J
    J --> M[Tahsilat doğrulaması]
    M --> N{Tüm koşullar tamam mı?}
    N -- Hayır --> O[Gerekçeli ret veya bekleme]
    N -- Evet --> P[Belge üretimi, e-imza ve kayıt]
    P --> Q[Denetim sistemine ve süre takvimine aktarım]
    Q --> R[Yenileme öncesi otomatik bildirim]
```

**Kontroller:** Başvuru türüne göre mevzuat kontrol listesi, belge geçerlilik tarihi, çift kayıt önleme, ücret tarifesi sürümü, yetkisiz belge düzenleme engeli.

**Önerilen KPI:** Ortalama belge sonuçlandırma süresi, eksik başvuru oranı, tekrar işlem oranı, süresi geçen belge oranı.

---

## TU-03 — İzleme, kontrol, şikâyet ve karar uygulama

**Süreç sahibi:** Toplu Taşıma İzleme ve Kontrol Birimi  
**Girdiler:** Denetim planı, UKOME kararları, araç/hat verileri, vatandaş şikâyeti, kolluk veya kurum bildirimi.  
**Çıktılar:** Kontrol/tespit raporu, düzeltici işlem, yetkili makama bildirim, trend ve hizmet kalite raporu.

```mermaid
flowchart TD
    A([Planlı kontrol veya şikâyet]) --> B[Kayıt, konu ve yetki sınıflandırması]
    B --> C{Masa başında doğrulanabilir mi?}
    C -- Evet --> D[AUS, ruhsat ve sefer kayıtlarının incelenmesi]
    C -- Hayır --> E[Saha kontrol planı]
    E --> F{Kolluk katılımı gerekli mi?}
    F -- Evet --> G[Kolluk koordinasyonu/refakat]
    F -- Hayır --> H[Belediye görev sınırı içinde saha kontrolü]
    G --> I[Standart kontrol formu ve kanıt]
    H --> I
    D --> J{İhlal veya hizmet kusuru var mı?}
    I --> J
    J -- Hayır --> K[Sonuç bildirimi ve kayıt kapanışı]
    J -- Evet --> L[İhlalin türü ve yetkili makamın belirlenmesi]
    L --> M{Belediyenin düzeltme/işlem yetkisi var mı?}
    M -- Evet --> N[Düzeltici işlem, süre ve takip]
    M -- Hayır --> O[Yetkili kolluk/kuruma kanıtlı bildirim]
    N --> P{Düzeltme tamamlandı mı?}
    P -- Hayır --> Q[Escalation ve sözleşme/ruhsat hükümleri]
    Q --> N
    P -- Evet --> R[Dosya kapanışı]
    O --> R
    R --> S[Aylık ihlal, şikâyet ve kök neden analizi]
```

**Temel kontrol:** Denetim süreci belediye personeline mevzuatta bulunmayan kolluk yetkisi tanımlamamalıdır; yaptırım ve tutanak yetkisi işlem türüne göre açıkça doğrulanmalıdır.

---

## TU-04 — Durak yeri ve durak yaşam döngüsü

**Hizmet ihtiyacı sahibi:** Toplu Taşıma  
**Trafik ve fiziksel varlık sahibi:** Ulaşım Planlama  
**Dijital ekipman sahibi:** Akıllı Ulaşım Sistemleri  
**Girdiler:** Hat planı, yolcu talebi, yürüme mesafesi, erişilebilirlik, yol geometrisi, güvenlik ve mevcut durak envanteri.  
**Çıktılar:** Durak yeri kararı, erişilebilir fiziksel durak, akıllı yolcu bilgi sistemi, tekil varlık kaydı ve bakım SLA’sı.

```mermaid
flowchart TD
    A([Yeni durak veya yer değişikliği ihtiyacı]) --> B[Toplu Taşıma: hizmet ve yolcu talebi analizi]
    B --> C[Ulaşım Planlama: yol, görüş, yaya ve trafik güvenliği kontrolü]
    C --> D[Erişilebilirlik ve yürüme bağlantısı kontrolü]
    D --> E{Yer uygun mu?}
    E -- Hayır --> F[Alternatif yer analizi]
    F --> C
    E -- Evet --> G[UKOME teknik teklif ve karar]
    G --> H{Karar olumlu mu?}
    H -- Hayır --> F
    H -- Evet --> I[Durak tipi, ölçü ve iş programı]
    I --> J[Ulaşım Planlama/Fen: fiziksel montaj]
    J --> K[AUS: akıllı ekran, enerji ve haberleşme]
    K --> L[Ortak teknik ve erişilebilirlik kabulü]
    L --> M{Kabul uygun mu?}
    M -- Hayır --> N[Düzeltme iş emri]
    N --> L
    M -- Evet --> O[Tekil durak ID, CBS ve yolcu bilgi sistemine kayıt]
    O --> P[Arıza ve bakım çağrılarının ekipman türüne göre yönlendirilmesi]
```

**Önerilen KPI:** Yolcu kapsama alanı, erişilebilir durak oranı, durak arıza çözüm süresi, gerçek zamanlı bilgi kullanılabilirliği.

---

## TU-05 — Hat veya işletmeci performans gözden geçirmesi

```mermaid
flowchart LR
    A[Aylık hat/işletmeci verisi] --> B[Sefer, doluluk, düzenlilik ve şikâyet KPI]
    B --> C{Eşik dışı performans var mı?}
    C -- Hayır --> D[Periyodik rapor ve izleme]
    C -- Evet --> E[Kök neden: plan, filo, sürücü, trafik veya sistem]
    E --> F[Düzeltici faaliyet sahibi ve hedef tarih]
    F --> G[Uygulama ve 30 günlük yeniden ölçüm]
    G --> H{Performans düzeldi mi?}
    H -- Hayır --> I[Sözleşme/ruhsat/UKOME aksiyonu]
    H -- Evet --> D
```
