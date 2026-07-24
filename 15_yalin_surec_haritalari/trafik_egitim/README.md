# Trafik Eğitim Süreç Haritaları

Bu bölüm Trafik Eğitim Şube Müdürlüğünün eğitim programı, katılımcı organizasyonu, ölçme-değerlendirme ve trafik eğitim parkı işletme süreçlerini gösterir.

---

## TE-01 — Trafik eğitimi ve farkındalık programı

**Atanan şube:** Ulaşım Planlama Şube Müdürlüğü  
**Atanan ana birim:** Trafik Güvenliği ve Eğitim Birimi  
**Organizasyon kaynağı:** `14_yalin_organizasyon_semasi/02_sube_birim_pozisyon_semalari.md`

**Süreç sahibi:** Trafik Eğitim Şube Müdürlüğü  
**Girdiler:** Hedef grup talebi, kaza/risk verisi, okul/kurum takvimi, eğitim ihtiyacı, müfredat ve kapasite.  
**Çıktılar:** Yıllık eğitim programı, materyal, katılım kaydı, ön/son test, memnuniyet ve faaliyet raporu.

```mermaid
flowchart TD
    A([Yıllık plan veya eğitim talebi<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]) --> B[Hedef grup, yaş, risk ve öğrenme ihtiyacı<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    B --> C[Kaza/ihlal verisi ve öncelikli davranışların analizi<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    C --> D[Eğitim amacı, içerik ve ölçme yöntemi<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    D --> E[Okul/kurum, eğitmen, salon/park ve tarih planı<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    E --> F{Kaynak ve kapasite uygun mu?<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü}
    F -- Hayır --> G[Tarih, grup veya yöntem revizyonu<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    G --> E
    F -- Evet --> H[Katılımcı ve veli/kurum bilgilendirmesi<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    H --> I[Ön test veya başlangıç ölçümü<br/>Sorumlu: Trafik Eğitim Uzmanı<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    I --> J[Teorik ve uygulamalı eğitim<br/>Sorumlu: Trafik Eğitim Uzmanı<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    J --> K[Son test ve uygulama gözlemi<br/>Sorumlu: Trafik Eğitim Uzmanı<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    K --> L{Asgari kazanım sağlandı mı?<br/>Sorumlu: Trafik Eğitim Uzmanı<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü}
    L -- Hayır --> M[Ek eğitim/tekrar uygulama<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    M --> K
    L -- Evet --> N[Katılım kaydı ve belge<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    N --> O[Memnuniyet ve eğitmen değerlendirmesi<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    O --> P[Aylık/yıllık faaliyet ve etki raporu<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
```

**Önerilen KPI:** Katılımcı sayısı, planlanan eğitimin gerçekleşme oranı, ön/son test gelişimi, tekrar eğitim ihtiyacı, memnuniyet ve hedef gruba erişim oranı.

---

## TE-02 — Trafik eğitim parkı seans ve güvenlik işletimi

**Atanan şube:** Ulaşım Planlama Şube Müdürlüğü  
**Atanan ana birim:** Trafik Güvenliği ve Eğitim Birimi  
**Organizasyon kaynağı:** `14_yalin_organizasyon_semasi/02_sube_birim_pozisyon_semalari.md`

**İşletme sahibi:** Trafik Eğitim Şube Müdürlüğü  
**Fiziksel proje/bakım paydaşları:** Ulaşım Planlama, Fen İşleri, Destek Hizmetleri ve İSG  
**Girdiler:** Onaylı eğitim programı, seans listesi, park kapasitesi, ekipman ve güvenlik kontrolü.  
**Çıktılar:** Güvenli eğitim seansı, katılımcı/ekipman kaydı, olay/ramak kala kaydı ve bakım iş emri.

```mermaid
flowchart TD
    A([Planlı park seansı<br/>Sorumlu: Eğitim Parkı İşletme ve Teknik Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]) --> B[Katılımcı, eğitmen ve kapasite kontrolü<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    B --> C[Günlük park, araç, işaret, enerji ve güvenlik kontrol listesi<br/>Sorumlu: Eğitim Parkı İşletme ve Teknik Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    C --> D{Park güvenli ve kullanılabilir mi?<br/>Sorumlu: Eğitim Parkı İşletme ve Teknik Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü}
    D -- Hayır --> E[Alanı kapatma ve bakım/arıza iş emri<br/>Sorumlu: Eğitim Parkı İşletme ve Teknik Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    E --> F[Teknik müdahale ve güvenlik testi<br/>Sorumlu: Eğitim Parkı İşletme ve Teknik Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    F --> C
    D -- Evet --> G[Katılımcı kabulü ve güvenlik bilgilendirmesi<br/>Sorumlu: Eğitim Parkı İşletme ve Teknik Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    G --> H[Grup ve istasyon dağılımı<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    H --> I[Uygulamalı eğitim seansı<br/>Sorumlu: Trafik Eğitim Uzmanı<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    I --> J{Kaza, ramak kala veya ekipman sorunu var mı?<br/>Sorumlu: Eğitim Parkı İşletme ve Teknik Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü}
    J -- Evet --> K[İlk müdahale, kayıt ve gerekirse seansı durdurma<br/>Sorumlu: Eğitim Parkı İşletme ve Teknik Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    K --> L[Kök neden ve düzeltici faaliyet<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    L --> C
    J -- Hayır --> M[Seans sonu değerlendirme<br/>Sorumlu: Eğitim Parkı İşletme ve Teknik Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    M --> N[Ekipman teslimi ve park kapanış kontrolü<br/>Sorumlu: Eğitim Parkı İşletme ve Teknik Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    N --> O[Seans, katılımcı ve faaliyet kaydı<br/>Sorumlu: Eğitim Parkı İşletme ve Teknik Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
```

**Temel kontroller:** Katılımcı yaşına uygun ekipman, kapasite sınırı, günlük saha kontrolü, acil durum prosedürü, kaza/ramak kala kaydı, çocuk ve kişisel veri güvenliği.

---

## TE-03 — Eğitim materyali hazırlama ve yayımlama

**Atanan şube:** Ulaşım Planlama Şube Müdürlüğü  
**Atanan ana birim:** Trafik Güvenliği ve Eğitim Birimi  
**Organizasyon kaynağı:** `14_yalin_organizasyon_semasi/02_sube_birim_pozisyon_semalari.md`

```mermaid
flowchart LR
    A[Eğitim ihtiyacı<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü] --> B[İçerik hedefi ve hedef grup<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    B --> C[Mevzuat/teknik doğrulama<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    C --> D[Taslak materyal<br/>Sorumlu: Trafik Eğitim Uzmanı<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    D --> E[Eğitim uzmanı ve ilgili teknik şube incelemesi<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    E --> F{Doğru ve anlaşılır mı?<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü}
    F -- Hayır --> D
    F -- Evet --> G[Erişilebilirlik, görsel ve dil kontrolü<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    G --> H[Yetkili onay ve sürüm numarası<br/>Sorumlu: Ulaşım Planlama Şube Müdürü<br/>Birim: Şube Müdürlüğü Yönetimi<br/>Şube: İdari ve Mali İşler Şube Müdürlüğü]
    H --> I[Yayımlama/dağıtım<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
    I --> J[Geri bildirim ve periyodik güncelleme<br/>Sorumlu: Trafik Eğitim ve Farkındalık Sorumlusu<br/>Birim: Trafik Güvenliği ve Eğitim Birimi<br/>Şube: Ulaşım Planlama Şube Müdürlüğü]
```
