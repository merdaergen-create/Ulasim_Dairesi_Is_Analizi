# Trafik Eğitim Süreç Haritaları

Bu bölüm Trafik Eğitim Şube Müdürlüğünün eğitim programı, katılımcı organizasyonu, ölçme-değerlendirme ve trafik eğitim parkı işletme süreçlerini gösterir.

---

## TE-01 — Trafik eğitimi ve farkındalık programı

**Süreç sahibi:** Trafik Eğitim Şube Müdürlüğü  
**Girdiler:** Hedef grup talebi, kaza/risk verisi, okul/kurum takvimi, eğitim ihtiyacı, müfredat ve kapasite.  
**Çıktılar:** Yıllık eğitim programı, materyal, katılım kaydı, ön/son test, memnuniyet ve faaliyet raporu.

```mermaid
flowchart TD
    A([Yıllık plan veya eğitim talebi]) --> B[Hedef grup, yaş, risk ve öğrenme ihtiyacı]
    B --> C[Kaza/ihlal verisi ve öncelikli davranışların analizi]
    C --> D[Eğitim amacı, içerik ve ölçme yöntemi]
    D --> E[Okul/kurum, eğitmen, salon/park ve tarih planı]
    E --> F{Kaynak ve kapasite uygun mu?}
    F -- Hayır --> G[Tarih, grup veya yöntem revizyonu]
    G --> E
    F -- Evet --> H[Katılımcı ve veli/kurum bilgilendirmesi]
    H --> I[Ön test veya başlangıç ölçümü]
    I --> J[Teorik ve uygulamalı eğitim]
    J --> K[Son test ve uygulama gözlemi]
    K --> L{Asgari kazanım sağlandı mı?}
    L -- Hayır --> M[Ek eğitim/tekrar uygulama]
    M --> K
    L -- Evet --> N[Katılım kaydı ve belge]
    N --> O[Memnuniyet ve eğitmen değerlendirmesi]
    O --> P[Aylık/yıllık faaliyet ve etki raporu]
```

**Önerilen KPI:** Katılımcı sayısı, planlanan eğitimin gerçekleşme oranı, ön/son test gelişimi, tekrar eğitim ihtiyacı, memnuniyet ve hedef gruba erişim oranı.

---

## TE-02 — Trafik eğitim parkı seans ve güvenlik işletimi

**İşletme sahibi:** Trafik Eğitim Şube Müdürlüğü  
**Fiziksel proje/bakım paydaşları:** Ulaşım Planlama, Fen İşleri, Destek Hizmetleri ve İSG  
**Girdiler:** Onaylı eğitim programı, seans listesi, park kapasitesi, ekipman ve güvenlik kontrolü.  
**Çıktılar:** Güvenli eğitim seansı, katılımcı/ekipman kaydı, olay/ramak kala kaydı ve bakım iş emri.

```mermaid
flowchart TD
    A([Planlı park seansı]) --> B[Katılımcı, eğitmen ve kapasite kontrolü]
    B --> C[Günlük park, araç, işaret, enerji ve güvenlik kontrol listesi]
    C --> D{Park güvenli ve kullanılabilir mi?}
    D -- Hayır --> E[Alanı kapatma ve bakım/arıza iş emri]
    E --> F[Teknik müdahale ve güvenlik testi]
    F --> C
    D -- Evet --> G[Katılımcı kabulü ve güvenlik bilgilendirmesi]
    G --> H[Grup ve istasyon dağılımı]
    H --> I[Uygulamalı eğitim seansı]
    I --> J{Kaza, ramak kala veya ekipman sorunu var mı?}
    J -- Evet --> K[İlk müdahale, kayıt ve gerekirse seansı durdurma]
    K --> L[Kök neden ve düzeltici faaliyet]
    L --> C
    J -- Hayır --> M[Seans sonu değerlendirme]
    M --> N[Ekipman teslimi ve park kapanış kontrolü]
    N --> O[Seans, katılımcı ve faaliyet kaydı]
```

**Temel kontroller:** Katılımcı yaşına uygun ekipman, kapasite sınırı, günlük saha kontrolü, acil durum prosedürü, kaza/ramak kala kaydı, çocuk ve kişisel veri güvenliği.

---

## TE-03 — Eğitim materyali hazırlama ve yayımlama

```mermaid
flowchart LR
    A[Eğitim ihtiyacı] --> B[İçerik hedefi ve hedef grup]
    B --> C[Mevzuat/teknik doğrulama]
    C --> D[Taslak materyal]
    D --> E[Eğitim uzmanı ve ilgili teknik şube incelemesi]
    E --> F{Doğru ve anlaşılır mı?}
    F -- Hayır --> D
    F -- Evet --> G[Erişilebilirlik, görsel ve dil kontrolü]
    G --> H[Yetkili onay ve sürüm numarası]
    H --> I[Yayımlama/dağıtım]
    I --> J[Geri bildirim ve periyodik güncelleme]
```
