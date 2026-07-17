# Toplu Ulaşım Süreç Haritaları

Bu bölüm Toplu Taşıma Şube Müdürlüğünün hizmet planlama, ruhsat/vize/izin, izleme-kontrol ve durak süreçlerini gösterir. Yol kapasitesi ve trafik geometrisi Ulaşım Planlama; UKOME kurul ve karar süreci Ulaşım Koordinasyon; dijital platform ve veri entegrasyonu Akıllı Ulaşım Sistemleri sorumluluğundadır.

---

## TU-01 — Hat, güzergâh, zaman, sefer ve tarife planlama

**Süreç sahibi:** Toplu Taşıma Planlama Birimi  
**Girdiler:** Yolcu talebi, doluluk, filo ve maliyet verileri, mevcut hatlar, şikâyetler, imar/yol ağı, duraklar ve trafik koşulları.  
**Çıktılar:** Teknik rapor, hat–güzergâh–zaman–tarife önerisi, UKOME kararı, işletmeci talimatı ve izleme raporu.

```mermaid
flowchart TD
    A([Yeni talep veya performans sorunu<br/>Sorumlu: Toplu Taşıma Veri Analisti]) --> B[Toplu Taşıma: talep ve mevcut hizmet analizi]
    B --> C[AUS: araç, yolcu ve zaman verisi<br/>Sorumlu: Hat ve Güzergâh Planlama Sorumlusu]
    C --> D[Alternatif hat/güzergâh/zaman senaryoları<br/>Sorumlu: Hat ve Güzergâh Planlama Sorumlusu]
    D --> E[Ulaşım Planlama: yol kapasitesi ve geometri kontrolü<br/>Sorumlu: Yol ve Kavşak Tasarım Birim Sorumlusu / Trafik Güvenliği Uzmanı]
    E --> F[Maliyet, filo, tarife ve sosyal etki analizi<br/>Sorumlu: Tarife ve Maliyet Analizi Uzmanı]
    F --> G{Hizmet ve mali kriterler uygun mu?<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu}
    G -- Hayır --> D
    G -- Evet --> H[Paydaş/işletmeci görüşü<br/>Sorumlu: İşletmeci İlişkileri Sorumlusu]
    H --> I[UKOME teknik teklif dosyası<br/>Sorumlu: Gündem ve Dosya Kabul Sorumlusu / UKOME Karar Yazım Uzmanı]
    I --> J[UKOME karar süreci<br/>Sorumlu: Gündem ve Dosya Kabul Sorumlusu / UKOME Karar Yazım Uzmanı]
    J --> K{Karar sonucu<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu}
    K -- İade/Ret --> L[Gerekçe ve senaryo revizyonu<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu]
    L --> D
    K -- Kabul --> M[Hat, ruhsat, biletleme ve yolcu bilgi sistemlerinin güncellenmesi<br/>Sorumlu: Başvuru ve Belge Kontrol Personeli / Ruhsat ve Vize Birim Sorumlusu]
    M --> N[İşletmeci uygulaması<br/>Sorumlu: İşletmeci İlişkileri Sorumlusu]
    N --> O[30/60/90 günlük performans izleme<br/>Sorumlu: Toplu Taşıma Veri Analisti]
    O --> P{Hedefler sağlandı mı?<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu}
    P -- Hayır --> D
    P -- Evet --> Q([Süreç kapanışı ve periyodik izleme<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu])
```

**Önerilen KPI:** Sefer düzenliliği, doluluk, yolcu başına maliyet, aktarma süresi, şikâyet oranı, zamanında sefer yüzdesi.

---

## TU-02 — Ruhsat, vize, izin ve yetki belgesi

**Süreç sahibi:** Ruhsat ve Vize İşlemleri Birimi  
**Girdiler:** E-başvuru, araç/şoför/şirket belgeleri, UKOME kararı, muayene/uygunluk, ücret ve borç bilgileri.  
**Çıktılar:** Ruhsat/vize/izin/yetki belgesi, gerekçeli ret, süre ve yenileme kaydı.

```mermaid
flowchart TD
    A([Başvuru<br/>Sorumlu: Başvuru ve Belge Kontrol Personeli / Ruhsat ve Vize Birim Sorumlusu]) --> B[E-başvuru, kimlik ve başvuru türü kontrolü]
    B --> C[Otomatik belge, süre ve eksik evrak kontrolü<br/>Sorumlu: Başvuru ve Belge Kontrol Personeli / Ruhsat ve Vize Birim Sorumlusu]
    C --> D{Başvuru tam mı?<br/>Sorumlu: Başvuru ve Belge Kontrol Personeli / Ruhsat ve Vize Birim Sorumlusu}
    D -- Hayır --> E[Eksik belge bildirimi ve süre verilmesi<br/>Sorumlu: Başvuru ve Belge Kontrol Personeli / Ruhsat ve Vize Birim Sorumlusu]
    E --> C
    D -- Evet --> F[UKOME kararı ve plaka/hak uygunluğu<br/>Sorumlu: Gündem ve Dosya Kabul Sorumlusu / UKOME Karar Yazım Uzmanı]
    F --> G[Araç, şoför ve işletmeci mevzuat kontrolü<br/>Sorumlu: Mevzuat ve Kalite Kontrol Uzmanı]
    G --> H{Saha/araç uygunluk kontrolü gerekli mi?<br/>Sorumlu: Mevzuat ve Kalite Kontrol Uzmanı}
    H -- Evet --> I[Standart kontrol formu ve muayene<br/>Sorumlu: Mevzuat ve Kalite Kontrol Uzmanı]
    H -- Hayır --> J[Ücret/tahsilat hesaplama<br/>Sorumlu: Tahakkuk ve Tarife Kontrol Personeli]
    I --> K{Uygun mu?<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu}
    K -- Hayır --> L[Gerekçeli uygunsuzluk ve düzeltme süresi<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu]
    L --> I
    K -- Evet --> J
    J --> M[Tahsilat doğrulaması<br/>Sorumlu: Tahakkuk ve Tarife Kontrol Personeli]
    M --> N{Tüm koşullar tamam mı?<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu}
    N -- Hayır --> O[Gerekçeli ret veya bekleme<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu]
    N -- Evet --> P[Belge üretimi, e-imza ve kayıt<br/>Sorumlu: Başvuru ve Belge Kontrol Personeli / Ruhsat ve Vize Birim Sorumlusu]
    P --> Q[Denetim sistemine ve süre takvimine aktarım<br/>Sorumlu: Dijital Başvuru Süreç Uzmanı / Arşiv ve Belge Yönetimi Personeli]
    Q --> R[Yenileme öncesi otomatik bildirim<br/>Sorumlu: Dijital Başvuru Süreç Uzmanı / Arşiv ve Belge Yönetimi Personeli]
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
    A([Planlı kontrol veya şikâyet<br/>Sorumlu: Hizmet Kalitesi ve KPI Sorumlusu]) --> B[Kayıt, konu ve yetki sınıflandırması]
    B --> C{Masa başında doğrulanabilir mi?<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu}
    C -- Evet --> D[AUS, ruhsat ve sefer kayıtlarının incelenmesi<br/>Sorumlu: Hat ve Güzergâh Planlama Sorumlusu]
    C -- Hayır --> E[Saha kontrol planı<br/>Sorumlu: Hizmet Kalitesi ve KPI Sorumlusu]
    E --> F{Kolluk katılımı gerekli mi?<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu}
    F -- Evet --> G[Kolluk koordinasyonu/refakat<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu]
    F -- Hayır --> H[Belediye görev sınırı içinde saha kontrolü<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu]
    G --> I[Standart kontrol formu ve kanıt<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu]
    H --> I
    D --> J{İhlal veya hizmet kusuru var mı?<br/>Sorumlu: Hizmet Kalitesi ve KPI Sorumlusu}
    I --> J
    J -- Hayır --> K[Sonuç bildirimi ve kayıt kapanışı<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu]
    J -- Evet --> L[İhlalin türü ve yetkili makamın belirlenmesi<br/>Sorumlu: Hizmet Kalitesi ve KPI Sorumlusu]
    L --> M{Belediyenin düzeltme/işlem yetkisi var mı?<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu}
    M -- Evet --> N[Düzeltici işlem, süre ve takip<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu]
    M -- Hayır --> O[Yetkili kolluk/kuruma kanıtlı bildirim<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu]
    N --> P{Düzeltme tamamlandı mı?<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu}
    P -- Hayır --> Q[Escalation ve sözleşme/ruhsat hükümleri<br/>Sorumlu: Başvuru ve Belge Kontrol Personeli / Ruhsat ve Vize Birim Sorumlusu]
    Q --> N
    P -- Evet --> R[Dosya kapanışı<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu]
    O --> R
    R --> S[Aylık ihlal, şikâyet ve kök neden analizi<br/>Sorumlu: Hizmet Kalitesi ve KPI Sorumlusu]
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
    A([Yeni durak veya yer değişikliği ihtiyacı<br/>Sorumlu: Durak Hizmetleri Planlama Uzmanı]) --> B[Toplu Taşıma: hizmet ve yolcu talebi analizi]
    B --> C[Ulaşım Planlama: yol, görüş, yaya ve trafik güvenliği kontrolü<br/>Sorumlu: Yol ve Kavşak Tasarım Birim Sorumlusu / Trafik Güvenliği Uzmanı]
    C --> D[Erişilebilirlik ve yürüme bağlantısı kontrolü<br/>Sorumlu: Durak Hizmetleri Planlama Uzmanı]
    D --> E{Yer uygun mu?<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu}
    E -- Hayır --> F[Alternatif yer analizi<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu]
    F --> C
    E -- Evet --> G[UKOME teknik teklif ve karar<br/>Sorumlu: Gündem ve Dosya Kabul Sorumlusu / UKOME Karar Yazım Uzmanı]
    G --> H{Karar olumlu mu?<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu}
    H -- Hayır --> F
    H -- Evet --> I[Durak tipi, ölçü ve iş programı<br/>Sorumlu: Durak Hizmetleri Planlama Uzmanı]
    I --> J[Ulaşım Planlama/Fen: fiziksel montaj<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu]
    J --> K[AUS: akıllı ekran, enerji ve haberleşme<br/>Sorumlu: Akıllı Filo Operasyon Sorumlusu]
    K --> L[Ortak teknik ve erişilebilirlik kabulü<br/>Sorumlu: Durak Hizmetleri Planlama Uzmanı]
    L --> M{Kabul uygun mu?<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu}
    M -- Hayır --> N[Düzeltme iş emri<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu]
    N --> L
    M -- Evet --> O[Tekil durak ID, CBS ve yolcu bilgi sistemine kayıt<br/>Sorumlu: Durak Hizmetleri Planlama Uzmanı]
    O --> P[Arıza ve bakım çağrılarının ekipman türüne göre yönlendirilmesi<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu]
```

**Önerilen KPI:** Yolcu kapsama alanı, erişilebilir durak oranı, durak arıza çözüm süresi, gerçek zamanlı bilgi kullanılabilirliği.

---

## TU-05 — Hat veya işletmeci performans gözden geçirmesi

```mermaid
flowchart LR
    A[Aylık hat/işletmeci verisi<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu] --> B[Sefer, doluluk, düzenlilik ve şikâyet KPI]
    B --> C{Eşik dışı performans var mı?<br/>Sorumlu: Toplu Taşıma Veri Analisti}
    C -- Hayır --> D[Periyodik rapor ve izleme<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu]
    C -- Evet --> E[Kök neden: plan, filo, sürücü, trafik veya sistem<br/>Sorumlu: Filo ve Kapasite Planlama Uzmanı]
    E --> F[Düzeltici faaliyet sahibi ve hedef tarih<br/>Sorumlu: İşletmeci İlişkileri Sorumlusu]
    F --> G[Uygulama ve 30 günlük yeniden ölçüm<br/>Sorumlu: Toplu Taşıma Planlama ve İşletme ilgili süreç pozisyonu]
    G --> H{Performans düzeldi mi?<br/>Sorumlu: Toplu Taşıma Veri Analisti}
    H -- Hayır --> I[Sözleşme/ruhsat/UKOME aksiyonu<br/>Sorumlu: Gündem ve Dosya Kabul Sorumlusu / UKOME Karar Yazım Uzmanı]
    H -- Evet --> D
```
