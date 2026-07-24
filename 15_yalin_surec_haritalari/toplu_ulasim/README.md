# Toplu Ulaşım Süreç Haritaları

Bu bölüm Toplu Taşıma Şube Müdürlüğünün hizmet planlama, ruhsat/vize/izin, izleme-kontrol ve durak süreçlerini gösterir. Yol kapasitesi ve trafik geometrisi Ulaşım Planlama; UKOME kurul ve karar süreci Ulaşım Koordinasyon; dijital platform ve veri entegrasyonu Akıllı Ulaşım Sistemleri sorumluluğundadır.

---

## TU-01 — Hat, güzergâh, zaman, sefer ve tarife planlama

**Atanan şube:** Toplu Taşıma Planlama ve İşletme Şube Müdürlüğü  
**Atanan ana birim:** Hat, Sefer ve Kapasite Planlama Birimi  
**Organizasyon kaynağı:** `14_yalin_organizasyon_semasi/02_sube_birim_pozisyon_semalari.md`

**Süreç sahibi:** Toplu Taşıma Planlama Birimi  
**Girdiler:** Yolcu talebi, doluluk, filo ve maliyet verileri, mevcut hatlar, şikâyetler, imar/yol ağı, duraklar ve trafik koşulları.  
**Çıktılar:** Teknik rapor, hat–güzergâh–zaman–tarife önerisi, UKOME kararı, işletmeci talimatı ve izleme raporu.

```mermaid
flowchart TD
    A([Yeni talep veya performans sorunu<br/>Sorumlu: Toplu Taşıma Veri ve Performans Analisti<br/>Birim: Toplu Taşıma Veri ve Akıllı Filo Birimi<br/>Şube: Toplu Taşıma Planlama ve İşletme Şube Müdürlüğü]) --> B[Toplu Taşıma: talep ve mevcut hizmet analizi<br/>Sorumlu: Hat ve Güzergâh Planlama Sorumlusu<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    B --> C[AUS: araç, yolcu ve zaman verisi<br/>Sorumlu: Ulaşım Veri Platformu ve Veri Yönetişimi Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Ulaşım Dairesi Başkanlığı]
    C --> D[Alternatif hat/güzergâh/zaman senaryoları<br/>Sorumlu: Hat ve Güzergâh Planlama Sorumlusu<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    D --> E[Ulaşım Planlama: yol kapasitesi ve geometri kontrolü<br/>Sorumlu: Yol ve Kavşak Tasarım Sorumlusu<br/>Birim: Yol, Kavşak ve Trafik Güvenliği Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    E --> F[Maliyet, filo, tarife ve sosyal etki analizi<br/>Sorumlu: Tarife ve Maliyet Analizi Uzmanı<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    F --> G{Hizmet ve mali kriterler uygun mu?<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü}
    G -- Hayır --> D
    G -- Evet --> H[Paydaş/işletmeci görüşü<br/>Sorumlu: İşletmeci İlişkileri Sorumlusu<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    H --> I[UKOME teknik teklif dosyası<br/>Sorumlu: Gündem ve Dosya Kabul Sorumlusu / UKOME Karar Yazım Uzmanı<br/>Birim: Gündem ve Dosya Kabul Birimi / Karar, Dağıtım ve Uygulama Takip Birimi<br/>Şube: UKOME Şube Müdürlüğü]
    I --> J[UKOME karar süreci<br/>Sorumlu: Gündem ve Dosya Kabul Sorumlusu / UKOME Karar Yazım Uzmanı<br/>Birim: Gündem ve Dosya Kabul Birimi / Karar, Dağıtım ve Uygulama Takip Birimi<br/>Şube: UKOME Şube Müdürlüğü]
    J --> K{Karar sonucu<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü}
    K -- İade/Ret --> L[Gerekçe ve senaryo revizyonu<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    L --> D
    K -- Kabul --> M[Hat, ruhsat, biletleme ve yolcu bilgi sistemlerinin güncellenmesi<br/>Sorumlu: Hat ve Güzergâh Planlama Sorumlusu / Ruhsat ve Vize İşlemleri Sorumlusu / Akıllı Filo Operasyon Sorumlusu<br/>Birim: Şube Müdürlüğü Yönetimi / Daire Geneli Ortak Uzmanlık Desteği / Toplu Taşıma Veri ve Akıllı Filo Birimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü / Ulaşım Dairesi Başkanlığı / Toplu Taşıma Planlama ve İşletme Şube Müdürlüğü]
    M --> N[İşletmeci uygulaması<br/>Sorumlu: İşletmeci İlişkileri Sorumlusu<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    N --> O[30/60/90 günlük performans izleme<br/>Sorumlu: Toplu Taşıma Veri ve Performans Analisti<br/>Birim: Toplu Taşıma Veri ve Akıllı Filo Birimi<br/>Şube: Toplu Taşıma Planlama ve İşletme Şube Müdürlüğü]
    O --> P{Hedefler sağlandı mı?<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü}
    P -- Hayır --> D
    P -- Evet --> Q([Süreç kapanışı ve periyodik izleme<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü])
```

**Önerilen KPI:** Sefer düzenliliği, doluluk, yolcu başına maliyet, aktarma süresi, şikâyet oranı, zamanında sefer yüzdesi.

---

## TU-02 — Ruhsat, vize, izin ve yetki belgesi

**Atanan şube:** Ulaşım Ruhsat ve Ticari Araç İşlemleri Şube Müdürlüğü  
**Atanan ana birim:** Ruhsat, Vize ve Başvuru Birimi  
**Organizasyon kaynağı:** `14_yalin_organizasyon_semasi/02_sube_birim_pozisyon_semalari.md`

**Süreç sahibi:** Ruhsat ve Vize İşlemleri Birimi  
**Girdiler:** E-başvuru, araç/şoför/şirket belgeleri, UKOME kararı, muayene/uygunluk, ücret ve borç bilgileri.  
**Çıktılar:** Ruhsat/vize/izin/yetki belgesi, gerekçeli ret, süre ve yenileme kaydı.

```mermaid
flowchart TD
    A([Başvuru<br/>Sorumlu: Başvuru ve Belge Kontrol Personeli<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Ulaşım Dairesi Başkanlığı]) --> B[E-başvuru, kimlik ve başvuru türü kontrolü<br/>Sorumlu: Başvuru ve Belge Kontrol Personeli<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Ulaşım Dairesi Başkanlığı]
    B --> C[Otomatik belge, süre ve eksik evrak kontrolü<br/>Sorumlu: Başvuru ve Belge Kontrol Personeli<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Ulaşım Dairesi Başkanlığı]
    C --> D{Başvuru tam mı?<br/>Sorumlu: Başvuru ve Belge Kontrol Personeli<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Ulaşım Dairesi Başkanlığı}
    D -- Hayır --> E[Eksik belge bildirimi ve süre verilmesi<br/>Sorumlu: Başvuru ve Belge Kontrol Personeli<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Ulaşım Dairesi Başkanlığı]
    E --> C
    D -- Evet --> F[UKOME kararı ve plaka/hak uygunluğu<br/>Sorumlu: Gündem ve Dosya Kabul Sorumlusu / UKOME Karar Yazım Uzmanı<br/>Birim: Gündem ve Dosya Kabul Birimi / Karar, Dağıtım ve Uygulama Takip Birimi<br/>Şube: UKOME Şube Müdürlüğü]
    F --> G[Araç, şoför ve işletmeci mevzuat kontrolü<br/>Sorumlu: İşletmeci İlişkileri Sorumlusu<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    G --> H{Saha/araç uygunluk kontrolü gerekli mi?<br/>Sorumlu: Mevzuat ve Kalite Kontrol Uzmanı<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Ulaşım Dairesi Başkanlığı}
    H -- Evet --> I[Standart kontrol formu ve muayene<br/>Sorumlu: Mevzuat ve Kalite Kontrol Uzmanı<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Ulaşım Dairesi Başkanlığı]
    H -- Hayır --> J[Ücret/tahsilat hesaplama<br/>Sorumlu: Tahakkuk ve Tarife Kontrol Personeli<br/>Birim: Belge, Tahakkuk ve Kalite Birimi<br/>Şube: Ulaşım Ruhsat ve Ticari Araç İşlemleri Şube Müdürlüğü]
    I --> K{Uygun mu?<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü}
    K -- Hayır --> L[Gerekçeli uygunsuzluk ve düzeltme süresi<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    L --> I
    K -- Evet --> J
    J --> M[Tahsilat doğrulaması<br/>Sorumlu: Tahakkuk ve Tarife Kontrol Personeli<br/>Birim: Belge, Tahakkuk ve Kalite Birimi<br/>Şube: Ulaşım Ruhsat ve Ticari Araç İşlemleri Şube Müdürlüğü]
    M --> N{Tüm koşullar tamam mı?<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü}
    N -- Hayır --> O[Gerekçeli ret veya bekleme<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    N -- Evet --> P[Belge üretimi, e-imza ve kayıt<br/>Sorumlu: Başvuru ve Belge Kontrol Personeli<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Ulaşım Dairesi Başkanlığı]
    P --> Q[Denetim sistemine ve süre takvimine aktarım<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    Q --> R[Yenileme öncesi otomatik bildirim<br/>Sorumlu: Ruhsat ve Vize İşlemleri Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Ulaşım Dairesi Başkanlığı]
```

**Kontroller:** Başvuru türüne göre mevzuat kontrol listesi, belge geçerlilik tarihi, çift kayıt önleme, ücret tarifesi sürümü, yetkisiz belge düzenleme engeli.

**Önerilen KPI:** Ortalama belge sonuçlandırma süresi, eksik başvuru oranı, tekrar işlem oranı, süresi geçen belge oranı.

---

## TU-03 — İzleme, kontrol, şikâyet ve karar uygulama

**Atanan şube:** Toplu Taşıma Planlama ve İşletme Şube Müdürlüğü  
**Atanan ana birim:** Toplu Taşıma Veri ve Akıllı Filo Birimi  
**Organizasyon kaynağı:** `14_yalin_organizasyon_semasi/02_sube_birim_pozisyon_semalari.md`

**Süreç sahibi:** Toplu Taşıma İzleme ve Kontrol Birimi  
**Girdiler:** Denetim planı, UKOME kararları, araç/hat verileri, vatandaş şikâyeti, kolluk veya kurum bildirimi.  
**Çıktılar:** Kontrol/tespit raporu, düzeltici işlem, yetkili makama bildirim, trend ve hizmet kalite raporu.

```mermaid
flowchart TD
    A([Planlı kontrol veya şikâyet<br/>Sorumlu: Hizmet Kalitesi ve KPI Sorumlusu<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]) --> B[Kayıt, konu ve yetki sınıflandırması<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    B --> C{Masa başında doğrulanabilir mi?<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü}
    C -- Evet --> D[AUS, ruhsat ve sefer kayıtlarının incelenmesi<br/>Sorumlu: Hat ve Güzergâh Planlama Sorumlusu<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    C -- Hayır --> E[Saha kontrol planı<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    E --> F{Kolluk katılımı gerekli mi?<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü}
    F -- Evet --> G[Kolluk koordinasyonu/refakat<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    F -- Hayır --> H[Belediye görev sınırı içinde saha kontrolü<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    G --> I[Standart kontrol formu ve kanıt<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    H --> I
    D --> J{İhlal veya hizmet kusuru var mı?<br/>Sorumlu: Hizmet Kalitesi ve KPI Sorumlusu<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü}
    I --> J
    J -- Hayır --> K[Sonuç bildirimi ve kayıt kapanışı<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    J -- Evet --> L[İhlalin türü ve yetkili makamın belirlenmesi<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    L --> M{Belediyenin düzeltme/işlem yetkisi var mı?<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü}
    M -- Evet --> N[Düzeltici işlem, süre ve takip<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    M -- Hayır --> O[Yetkili kolluk/kuruma kanıtlı bildirim<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    N --> P{Düzeltme tamamlandı mı?<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü}
    P -- Hayır --> Q[Escalation ve sözleşme/ruhsat hükümleri<br/>Sorumlu: Ruhsat ve Vize İşlemleri Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Ulaşım Dairesi Başkanlığı]
    Q --> N
    P -- Evet --> R[Dosya kapanışı<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    O --> R
    R --> S[Aylık ihlal, şikâyet ve kök neden analizi<br/>Sorumlu: Hizmet Kalitesi ve KPI Sorumlusu<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
```

**Temel kontrol:** Denetim süreci belediye personeline mevzuatta bulunmayan kolluk yetkisi tanımlamamalıdır; yaptırım ve tutanak yetkisi işlem türüne göre açıkça doğrulanmalıdır.

---

## TU-04 — Durak yeri ve durak yaşam döngüsü

**Atanan şube:** Toplu Taşıma Planlama ve İşletme Şube Müdürlüğü  
**Atanan ana birim:** Hat, Sefer ve Kapasite Planlama Birimi  
**Organizasyon kaynağı:** `14_yalin_organizasyon_semasi/02_sube_birim_pozisyon_semalari.md`

**Hizmet ihtiyacı sahibi:** Toplu Taşıma  
**Trafik ve fiziksel varlık sahibi:** Ulaşım Planlama  
**Dijital ekipman sahibi:** Akıllı Ulaşım Sistemleri  
**Girdiler:** Hat planı, yolcu talebi, yürüme mesafesi, erişilebilirlik, yol geometrisi, güvenlik ve mevcut durak envanteri.  
**Çıktılar:** Durak yeri kararı, erişilebilir fiziksel durak, akıllı yolcu bilgi sistemi, tekil varlık kaydı ve bakım SLA’sı.

```mermaid
flowchart TD
    A([Yeni durak veya yer değişikliği ihtiyacı<br/>Sorumlu: Durak Hizmetleri ve Erişilebilirlik Planlama Uzmanı<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Ulaşım Dairesi Başkanlığı]) --> B[Toplu Taşıma: hizmet ve yolcu talebi analizi<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    B --> C[Ulaşım Planlama: yol, görüş, yaya ve trafik güvenliği kontrolü<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    C --> D[Erişilebilirlik ve yürüme bağlantısı kontrolü<br/>Sorumlu: Durak Hizmetleri ve Erişilebilirlik Planlama Uzmanı<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Ulaşım Dairesi Başkanlığı]
    D --> E{Yer uygun mu?<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü}
    E -- Hayır --> F[Alternatif yer analizi<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    F --> C
    E -- Evet --> G[UKOME teknik teklif ve karar<br/>Sorumlu: Gündem ve Dosya Kabul Sorumlusu / UKOME Karar Yazım Uzmanı<br/>Birim: Gündem ve Dosya Kabul Birimi / Karar, Dağıtım ve Uygulama Takip Birimi<br/>Şube: UKOME Şube Müdürlüğü]
    G --> H{Karar olumlu mu?<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü}
    H -- Hayır --> F
    H -- Evet --> I[Durak tipi, ölçü ve iş programı<br/>Sorumlu: Durak Hizmetleri ve Erişilebilirlik Planlama Uzmanı<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Ulaşım Dairesi Başkanlığı]
    I --> J[Ulaşım Planlama/Fen: fiziksel montaj<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    J --> K[AUS: akıllı ekran, enerji ve haberleşme<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    K --> L[Ortak teknik ve erişilebilirlik kabulü<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    L --> M{Kabul uygun mu?<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü}
    M -- Hayır --> N[Düzeltme iş emri<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    N --> L
    M -- Evet --> O[Tekil durak ID, CBS ve yolcu bilgi sistemine kayıt<br/>Sorumlu: Durak Hizmetleri ve Erişilebilirlik Planlama Uzmanı<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Ulaşım Dairesi Başkanlığı]
    O --> P[Arıza ve bakım çağrılarının ekipman türüne göre yönlendirilmesi<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
```

**Önerilen KPI:** Yolcu kapsama alanı, erişilebilir durak oranı, durak arıza çözüm süresi, gerçek zamanlı bilgi kullanılabilirliği.

---

## TU-05 — Hat veya işletmeci performans gözden geçirmesi

**Atanan şube:** Toplu Taşıma Planlama ve İşletme Şube Müdürlüğü  
**Atanan ana birim:** Toplu Taşıma Veri ve Akıllı Filo Birimi  
**Organizasyon kaynağı:** `14_yalin_organizasyon_semasi/02_sube_birim_pozisyon_semalari.md`

```mermaid
flowchart LR
    A[Aylık hat/işletmeci verisi<br/>Sorumlu: Hat ve Güzergâh Planlama Sorumlusu<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü] --> B[Sefer, doluluk, düzenlilik ve şikâyet KPI<br/>Sorumlu: Hat ve Güzergâh Planlama Sorumlusu<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    B --> C{Eşik dışı performans var mı?<br/>Sorumlu: Toplu Taşıma Veri ve Performans Analisti<br/>Birim: Toplu Taşıma Veri ve Akıllı Filo Birimi<br/>Şube: Toplu Taşıma Planlama ve İşletme Şube Müdürlüğü}
    C -- Hayır --> D[Periyodik rapor ve izleme<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    C -- Evet --> E[Kök neden: plan, filo, sürücü, trafik veya sistem<br/>Sorumlu: Filo ve Kapasite Planlama Uzmanı<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    E --> F[Düzeltici faaliyet sahibi ve hedef tarih<br/>Sorumlu: İşletmeci İlişkileri Sorumlusu<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    F --> G[Uygulama ve 30 günlük yeniden ölçüm<br/>Sorumlu: Toplu Taşıma Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    G --> H{Performans düzeldi mi?<br/>Sorumlu: Toplu Taşıma Veri ve Performans Analisti<br/>Birim: Toplu Taşıma Veri ve Akıllı Filo Birimi<br/>Şube: Toplu Taşıma Planlama ve İşletme Şube Müdürlüğü}
    H -- Hayır --> I[Sözleşme/ruhsat/UKOME aksiyonu<br/>Sorumlu: Ruhsat ve Vize İşlemleri Sorumlusu<br/>Birim: Daire Geneli Ortak Uzmanlık Desteği<br/>Şube: Ulaşım Dairesi Başkanlığı]
    H -- Evet --> D
```
