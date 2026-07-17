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
    A([Teknik şubeden teklif dosyası]) --> B[UKOME sekretaryası: kayıt ve dosya tamlık kontrolü]
    B --> C{Zorunlu belgeler tam mı?}
    C -- Hayır --> D[Eksik belge ve düzeltme listesi]
    D --> E[Teknik şube dosyayı tamamlar]
    E --> B
    C -- Evet --> F[Yetki, mevzuat ve önceki karar taraması]
    F --> G{Alt komisyon gerekli mi?}
    G -- Evet --> H[Alt komisyon üyeleri ve toplantı tarihi]
    H --> I[Saha/teknik inceleme ve kurum görüşleri]
    I --> J[Alt komisyon raporu]
    G -- Hayır --> K[Gündem maddesi hazırlanması]
    J --> K
    K --> L[Gündem ve dosyaların üyelere süresinde gönderilmesi]
    L --> M[UKOME toplantısı, görüşme ve oylama]
    M --> N{Karar sonucu}
    N -- İade --> O[Gerekçe ile teknik şubeye iade]
    O --> E
    N -- Ret --> P[Gerekçeli ret kararının yazılması]
    N -- Kabul --> Q[Karar metni ve uygulama şartları]
    P --> R[Üye imzaları ve kesinleşme kontrolü]
    Q --> R
    R --> S[Karar numarası, e-imza ve arşiv]
    S --> T[İlgili kurum, birim ve başvuru sahibine dağıtım]
    T --> U([Karar uygulama takibine aktarılır])
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
    A([İmzalı UKOME kararı]) --> B[Karar maddelerinin görev ve süre bazında ayrıştırılması]
    B --> C[Her madde için uygulama sahibi ve hedef tarih]
    C --> D[EBYS/karar takip sistemi üzerinden bildirim]
    D --> E[Uygulama sahibi: iş planı ve kaynak kontrolü]
    E --> F{Ek proje, bütçe veya ihale gerekli mi?}
    F -- Evet --> G[İlgili teknik/idari hazırlık süreci]
    G --> H[Uygulama]
    F -- Hayır --> H
    H --> I[Fotoğraf, proje, tutanak, belge veya sistem kaydı yükleme]
    I --> J[UKOME sekretaryası: kanıt ve süre kontrolü]
    J --> K{Karar tam uygulanmış mı?}
    K -- Hayır --> L[Düzeltme veya eksik uygulama bildirimi]
    L --> M{Hedef süre aşıldı mı?}
    M -- Hayır --> H
    M -- Evet --> N[Daire Başkanı/Genel Sekreterlik escalation raporu]
    N --> H
    K -- Evet --> O[Gerekirse ortak saha doğrulaması]
    O --> P{Saha uygun mu?}
    P -- Hayır --> L
    P -- Evet --> Q[Karar maddesinin kapanışı]
    Q --> R[Karar performans ve gecikme raporu]
```

**Temel kontrol:** Ulaşım Koordinasyon uygulamayı kendi yapmamalı; takip, kanıt doğrulama ve gecikme yönetimini yürütmelidir.

**Önerilen KPI:** Zamanında uygulanan karar oranı, açık karar maddesi sayısı, ortalama kapanış süresi, kanıt eksikliği oranı.

---

## UK-03 — Kurum veya vatandaş başvurusunun UKOME sürecine alınması

**Girdiler:** Başvuru dilekçesi/e-başvuru, ek belgeler, talep konusu ve konum bilgisi.  
**Çıktılar:** Teknik şubeye yönlendirme, kurul kararı gerekmiyorsa idari cevap, UKOME kararı gerekiyorsa tamamlanmış teklif dosyası.

```mermaid
flowchart LR
    A[Başvuru] --> B[Ulaşım Koordinasyon: konu ve yetki sınıflandırması]
    B --> C{UKOME yetkisinde mi?}
    C -- Hayır --> D[Yetkili birime/kuruma yönlendirme]
    C -- Evet --> E[İlgili teknik şubenin belirlenmesi]
    E --> F[Teknik inceleme ve saha/veri çalışması]
    F --> G{Kurul kararı gerekli mi?}
    G -- Hayır --> H[Teknik/idari cevap ve başvuru kapanışı]
    G -- Evet --> I[Standart UKOME teklif dosyası]
    I --> J[UK-01 gündem ve karar süreci]
    J --> K[Başvuru sahibine karar bildirimi]
```

**Kontrol:** Başvurunun doğrudan gündeme alınması yerine önce yetkili teknik şube tarafından teknik rapor hazırlanmalıdır.
