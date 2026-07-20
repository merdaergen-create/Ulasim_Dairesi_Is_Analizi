# UKOME Süreç Haritaları

Bu bölüm Ulaşım Koordinasyon Şube Müdürlüğünün UKOME sekretaryası, kurul yönetimi ve karar takip sorumluluklarını gösterir. Teknik teklifin sahibi ilgili teknik şubedir; Ulaşım Koordinasyon teknik projeyi üretmez veya uygulamaz.

---

## UK-01 — UKOME gündem, alt komisyon ve karar süreci

**Süreç sahibi:** Ulaşım Koordinasyon Şube Müdürlüğü  
**Teknik dosya sahibi:** Teklifi hazırlayan şube  
**Girdiler:** İmzalı teknik rapor, proje/harita, mevzuat dayanağı, kurum görüşleri, önceki UKOME kararları, başvuru ve ekleri.  
**Çıktılar:** Gündem, alt komisyon raporu, toplantı tutanağı, imzalı UKOME kararı, dağıtım ve dijital karar kaydı.

```mermaid
flowchart TD
    A([Teknik şubeden teklif dosyası<br/>Sorumlu: UKOME Şube Müdürü]) --> B[UKOME sekretaryası: kayıt ve dosya tamlık kontrolü<br/>Sorumlu: Gündem ve Dosya Kabul Sorumlusu]
    B --> C{Zorunlu belgeler tam mı?<br/>Sorumlu: UKOME Şube Müdürü}
    C -- Hayır --> D[Eksik belge ve düzeltme listesi<br/>Sorumlu: Gündem ve Dosya Kabul Sorumlusu]
    D --> E[Teknik şube dosyayı tamamlar<br/>Sorumlu: UKOME Şube Müdürü]
    E --> B
    C -- Evet --> F[Yetki, mevzuat ve önceki karar taraması<br/>Sorumlu: Arşiv ve Karar Araştırma Personeli]
    F --> G{Alt komisyon gerekli mi?<br/>Sorumlu: Alt Komisyon Koordinatörü}
    G -- Evet --> H[Alt komisyon üyeleri ve toplantı tarihi<br/>Sorumlu: Alt Komisyon Koordinatörü]
    H --> I[Saha/teknik inceleme ve kurum görüşleri<br/>Sorumlu: Alt Komisyon Koordinatörü]
    I --> J[Alt komisyon raporu<br/>Sorumlu: Alt Komisyon Koordinatörü]
    G -- Hayır --> K[Gündem maddesi hazırlanması<br/>Sorumlu: Gündem ve Dosya Kabul Sorumlusu]
    J --> K
    K --> L[Gündem ve dosyaların üyelere süresinde gönderilmesi<br/>Sorumlu: UKOME Şube Müdürü]
    L --> M[UKOME toplantısı, görüşme ve oylama<br/>Sorumlu: UKOME Şube Müdürü]
    M --> N{Karar sonucu<br/>Sorumlu: UKOME Şube Müdürü}
    N -- İade --> O[Gerekçe ile teknik şubeye iade<br/>Sorumlu: UKOME Şube Müdürü]
    O --> E
    N -- Ret --> P[Gerekçeli ret kararının yazılması<br/>Sorumlu: UKOME Karar Yazım Uzmanı]
    N -- Kabul --> Q[Karar metni ve uygulama şartları<br/>Sorumlu: UKOME Karar Yazım Uzmanı]
    P --> R[Üye imzaları ve kesinleşme kontrolü<br/>Sorumlu: UKOME Şube Müdürü]
    Q --> R
    R --> S[Karar numarası, e-imza ve arşiv<br/>Sorumlu: Dijital UKOME Sistem Sorumlusu]
    S --> T[İlgili kurum, birim ve başvuru sahibine dağıtım<br/>Sorumlu: Karar Dağıtım ve Tebligat Personeli]
    T --> U([Karar uygulama takibine aktarılır<br/>Sorumlu: Karar Uygulama Takip Uzmanı])
```

**Zorunlu kalite kapısı**

- Teknik raporda ihtiyaç, mevcut durum, alternatifler, öneri, etki, mevzuat ve uygulama sorumlusu bulunmalıdır.
- Önceki kararlarla çelişki kontrolü yapılmalıdır.
- Gündem, karar metni ve eklerde cadde, koordinat, plaka, güzergâh ve süre bilgileri tutarlı olmalıdır.
- Karar sahibine, uygulayıcıya ve kapanış tarihine yer verilmelidir.

**Önerilen KPI:** Eksik dosya oranı, gündeme alınma süresi, alt komisyon çevrim süresi, karar yazım süresi, imza tamamlama süresi.

---

## UK-02 — UKOME kararının uygulama ve kapanış takibi

**Takip sahibi:** Ulaşım Koordinasyon Şube Müdürlüğü  
**Uygulama sahibi:** Kararda belirtilen teknik şube veya kurum  
**Girdiler:** İmzalı karar, uygulama şartları, sorumlu birimler, süre ve varsa bütçe/ihale ihtiyacı.  
**Çıktılar:** İş emri, uygulama kanıtı, saha kontrolü, gecikme/escalation raporu ve kapanış kaydı.

```mermaid
flowchart TD
    A([İmzalı UKOME kararı<br/>Sorumlu: UKOME Şube Müdürü]) --> B[Karar maddelerinin görev ve süre bazında ayrıştırılması<br/>Sorumlu: UKOME Şube Müdürü]
    B --> C[Her madde için uygulama sahibi ve hedef tarih<br/>Sorumlu: Karar Uygulama Takip Uzmanı]
    C --> D[EBYS/karar takip sistemi üzerinden bildirim<br/>Sorumlu: UKOME Şube Müdürü]
    D --> E[Uygulama sahibi: iş planı ve kaynak kontrolü<br/>Sorumlu: Karar Uygulama Takip Uzmanı]
    E --> F{Ek proje, bütçe veya ihale gerekli mi?<br/>Sorumlu: UKOME Şube Müdürü}
    F -- Evet --> G[İlgili teknik/idari hazırlık süreci<br/>Sorumlu: UKOME Şube Müdürü]
    G --> H[Uygulama<br/>Sorumlu: Karar Uygulama Takip Uzmanı]
    F -- Hayır --> H
    H --> I[Fotoğraf, proje, tutanak, belge veya sistem kaydı yükleme<br/>Sorumlu: UKOME Karar Yazım Uzmanı]
    I --> J[UKOME sekretaryası: kanıt ve süre kontrolü<br/>Sorumlu: Karar Uygulama Takip Uzmanı]
    J --> K{Karar tam uygulanmış mı?<br/>Sorumlu: UKOME Şube Müdürü}
    K -- Hayır --> L[Düzeltme veya eksik uygulama bildirimi<br/>Sorumlu: Karar Uygulama Takip Uzmanı]
    L --> M{Hedef süre aşıldı mı?<br/>Sorumlu: UKOME Şube Müdürü}
    M -- Hayır --> H
    M -- Evet --> N[Daire Başkanı/Genel Sekreterlik escalation raporu<br/>Sorumlu: UKOME Şube Müdürü]
    N --> H
    K -- Evet --> O[Gerekirse ortak saha doğrulaması<br/>Sorumlu: UKOME Şube Müdürü]
    O --> P{Saha uygun mu?<br/>Sorumlu: UKOME Şube Müdürü}
    P -- Hayır --> L
    P -- Evet --> Q[Karar maddesinin kapanışı<br/>Sorumlu: Karar Uygulama Takip Uzmanı]
    Q --> R[Karar performans ve gecikme raporu<br/>Sorumlu: Karar Uygulama Takip Uzmanı]
```

**Temel kontrol:** Ulaşım Koordinasyon uygulamayı kendi yapmamalı; takip, kanıt doğrulama ve gecikme yönetimini yürütmelidir.

**Önerilen KPI:** Zamanında uygulanan karar oranı, açık karar maddesi sayısı, ortalama kapanış süresi, kanıt eksikliği oranı.

---

## UK-03 — Kurum veya vatandaş başvurusunun UKOME sürecine alınması

**Girdiler:** Başvuru dilekçesi/e-başvuru, ek belgeler, talep konusu ve konum bilgisi.  
**Çıktılar:** Teknik şubeye yönlendirme, kurul kararı gerekmiyorsa idari cevap, UKOME kararı gerekiyorsa tamamlanmış teklif dosyası.

```mermaid
flowchart LR
    A[Başvuru<br/>Sorumlu: UKOME Şube Müdürü] --> B[Ulaşım Koordinasyon: konu ve yetki sınıflandırması<br/>Sorumlu: UKOME Şube Müdürü]
    B --> C{UKOME yetkisinde mi?<br/>Sorumlu: UKOME Şube Müdürü}
    C -- Hayır --> D[Yetkili birime/kuruma yönlendirme<br/>Sorumlu: Kurumlar Arası Koordinasyon Uzmanı]
    C -- Evet --> E[İlgili teknik şubenin belirlenmesi<br/>Sorumlu: UKOME Şube Müdürü]
    E --> F[Teknik inceleme ve saha/veri çalışması<br/>Sorumlu: UKOME Şube Müdürü]
    F --> G{Kurul kararı gerekli mi?<br/>Sorumlu: UKOME Şube Müdürü}
    G -- Hayır --> H[Teknik/idari cevap ve başvuru kapanışı<br/>Sorumlu: Karar Uygulama Takip Uzmanı]
    G -- Evet --> I[Standart UKOME teklif dosyası<br/>Sorumlu: UKOME Şube Müdürü]
    I --> J[UK-01 gündem ve karar süreci<br/>Sorumlu: UKOME Şube Müdürü]
    J --> K[Başvuru sahibine karar bildirimi<br/>Sorumlu: Karar Dağıtım ve Tebligat Personeli]
```

**Kontrol:** Başvurunun doğrudan gündeme alınması yerine önce yetkili teknik şube tarafından teknik rapor hazırlanmalıdır.
