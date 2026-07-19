# İdari İşler — Kaynak İncelemesi Sonucu Ek Süreçler

Bu dosya, kaynak belgelerde yer aldığı halde mevcut `ID-01–ID-06` haritalarında bağımsız süreç olarak gösterilmeyen işi içerir.

---

## ID-07 — Taşıt görev emri ve hizmet aracı görevlendirme süreci

**Süreç sahibi:** İdari ve Mali İşler / İdari Destek Birimi  
**Araç ve sürücü operasyonu:** İlgili araç havuzu veya görevlendirilen şube  
**Kaynak dayanağı:** Taşıt Görev Emri Formu ve Şoför Görev Tanımı.  
**Girdiler:** Görev talebi, görev amacı, güzergâh, tarih-saat, personel/yük bilgisi, araç ve sürücü uygunluğu, yakıt ve bakım durumu.  
**Çıktılar:** Onaylı taşıt görev emri, araç/sürücü tahsisi, kilometre-yakıt ve görev gerçekleşme kaydı, uygunsuzluk veya iptal kaydı.

```mermaid
flowchart TD
    A([Hizmet aracı talebi]) --> B[Görev amacı, tarih, güzergâh ve yolcu/yük bilgisinin kaydı]
    B --> C{Talep kurumsal görev kapsamında mı?}
    C -- Hayır --> D[Gerekçeli ret ve kayıt kapanışı]
    C -- Evet --> E[Uygun araç sınıfı ve sürücü ihtiyacının belirlenmesi]
    E --> F[Araç bakım, muayene, sigorta ve yakıt uygunluğu]
    F --> G[Sürücü ehliyet, görev, çalışma ve dinlenme uygunluğu]
    G --> H{Araç ve sürücü uygun mu?}
    H -- Hayır --> I[Alternatif araç/sürücü veya tarih planlaması]
    I --> E
    H -- Evet --> J[Taşıt görev emrinin hazırlanması]
    J --> K[Yetkili amir onayı]
    K --> L{Onaylandı mı?}
    L -- Hayır --> D
    L -- Evet --> M[Araç ve sürücüye görev bildirimi]
    M --> N[Başlangıç kilometresi, yakıt ve araç teslim kontrolü]
    N --> O[Görevin gerçekleştirilmesi]
    O --> P{Kaza, arıza, gecikme veya güzergâh değişikliği oldu mu?}
    P -- Evet --> Q[Olay kaydı ve gerekli kurum/amir bildirimi]
    Q --> R[Görevin tamamlanması veya güvenli şekilde sonlandırılması]
    P -- Hayır --> R
    R --> S[Bitiş kilometresi, yakıt, süre ve görev sonucu kaydı]
    S --> T[Araç teslim ve hasar/eksik kontrolü]
    T --> U[Görev emri kapanışı ve dönemsel kullanım raporu]
```

**Temel kontroller**

- Araç yalnız onaylı kurumsal görev için kullanılmalıdır.
- Görev emri olmadan araç çıkışı yapılamamalı; acil görevlendirmeler sonradan kayıt altına alınmalıdır.
- Sürücü ehliyet sınıfı, çalışma-dinlenme süresi ve görev uygunluğu kontrol edilmelidir.
- Başlangıç/bitiş kilometresi, yakıt ve olay kayıtları araç bazında izlenmelidir.
- Kaza veya hasar halinde sigorta, kolluk, İSG ve idari bildirim süreçleri tetiklenmelidir.

**Önerilen KPI:** Talep karşılama oranı, araç tahsis süresi, boş kilometre oranı, kilometre-yakıt sapması, plansız arıza ve olay bildirim süresi.
