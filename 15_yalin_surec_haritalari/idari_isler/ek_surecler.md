# İdari İşler — Kaynak İncelemesi Sonucu Ek Süreçler

Bu dosya, kaynak belgelerde yer aldığı halde mevcut `ID-01–ID-06` haritalarında bağımsız süreç olarak gösterilmeyen işi içerir.

---

## ID-07 — Taşıt görev emri ve hizmet aracı görevlendirme süreci

**Atanan şube:** İdari ve Mali İşler Şube Müdürlüğü  
**Atanan ana birim:** EBYS, Taşınır, Personel ve İç Kontrol Birimi  
**Organizasyon kaynağı:** `14_yalin_organizasyon_semasi/02_sube_birim_pozisyon_semalari.md`

**Süreç sahibi:** İdari ve Mali İşler / İdari Destek Birimi  
**Araç ve sürücü operasyonu:** İlgili araç havuzu veya görevlendirilen şube  
**Kaynak dayanağı:** Taşıt Görev Emri Formu ve Şoför Görev Tanımı.  
**Girdiler:** Görev talebi, görev amacı, güzergâh, tarih-saat, personel/yük bilgisi, araç ve sürücü uygunluğu, yakıt ve bakım durumu.  
**Çıktılar:** Onaylı taşıt görev emri, araç/sürücü tahsisi, kilometre-yakıt ve görev gerçekleşme kaydı, uygunsuzluk veya iptal kaydı.

```mermaid
flowchart TD
    A([Hizmet aracı talebi<br/>Sorumlu: İdari ve Mali İşler Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]) --> B[Görev amacı, tarih, güzergâh ve yolcu/yük bilgisinin kaydı<br/>Sorumlu: İdari ve Mali İşler Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    B --> C{Talep kurumsal görev kapsamında mı?<br/>Sorumlu: İdari ve Mali İşler Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü}
    C -- Hayır --> D[Gerekçeli ret ve kayıt kapanışı<br/>Sorumlu: İdari ve Mali İşler Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    C -- Evet --> E[Uygun araç sınıfı ve sürücü ihtiyacının belirlenmesi<br/>Sorumlu: İdari ve Mali İşler Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    E --> F[Araç bakım, muayene, sigorta ve yakıt uygunluğu<br/>Sorumlu: Personel ve İzin İşleri Sorumlusu<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    F --> G[Sürücü ehliyet, görev, çalışma ve dinlenme uygunluğu<br/>Sorumlu: İdari ve Mali İşler Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    G --> H{Araç ve sürücü uygun mu?<br/>Sorumlu: İdari ve Mali İşler Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü}
    H -- Hayır --> I[Alternatif araç/sürücü veya tarih planlaması<br/>Sorumlu: Taşınır Kayıt ve Ambar Sorumlusu<br/>Birim: EBYS, Taşınır, Personel ve İç Kontrol Birimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    I --> E
    H -- Evet --> J[Taşıt görev emrinin hazırlanması<br/>Sorumlu: Personel ve İzin İşleri Sorumlusu<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    J --> K[Yetkili amir onayı<br/>Sorumlu: İdari ve Mali İşler Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    K --> L{Onaylandı mı?<br/>Sorumlu: İdari ve Mali İşler Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü}
    L -- Hayır --> D
    L -- Evet --> M[Araç ve sürücüye görev bildirimi<br/>Sorumlu: İdari ve Mali İşler Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    M --> N[Başlangıç kilometresi, yakıt ve araç teslim kontrolü<br/>Sorumlu: Personel ve İzin İşleri Sorumlusu<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    N --> O[Görevin gerçekleştirilmesi<br/>Sorumlu: İdari ve Mali İşler Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    O --> P{Kaza, arıza, gecikme veya güzergâh değişikliği oldu mu?<br/>Sorumlu: İdari ve Mali İşler Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü}
    P -- Evet --> Q[Olay kaydı ve gerekli kurum/amir bildirimi<br/>Sorumlu: İdari ve Mali İşler Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    Q --> R[Görevin tamamlanması veya güvenli şekilde sonlandırılması<br/>Sorumlu: İdari ve Mali İşler Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    P -- Hayır --> R
    R --> S[Bitiş kilometresi, yakıt, süre ve görev sonucu kaydı<br/>Sorumlu: Personel ve İzin İşleri Sorumlusu<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    S --> T[Araç teslim ve hasar/eksik kontrolü<br/>Sorumlu: Personel ve İzin İşleri Sorumlusu<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    T --> U[Görev emri kapanışı ve dönemsel kullanım raporu<br/>Sorumlu: Personel ve İzin İşleri Sorumlusu<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
```

**Temel kontroller**

- Araç yalnız onaylı kurumsal görev için kullanılmalıdır.
- Görev emri olmadan araç çıkışı yapılamamalı; acil görevlendirmeler sonradan kayıt altına alınmalıdır.
- Sürücü ehliyet sınıfı, çalışma-dinlenme süresi ve görev uygunluğu kontrol edilmelidir.
- Başlangıç/bitiş kilometresi, yakıt ve olay kayıtları araç bazında izlenmelidir.
- Kaza veya hasar halinde sigorta, kolluk, İSG ve idari bildirim süreçleri tetiklenmelidir.

**Önerilen KPI:** Talep karşılama oranı, araç tahsis süresi, boş kilometre oranı, kilometre-yakıt sapması, plansız arıza ve olay bildirim süresi.
