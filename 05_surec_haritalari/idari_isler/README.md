# İdari İşler Süreç Haritaları

Bu bölüm evrak, ihale, sözleşme, hakediş, ödeme, bütçe, performans, faaliyet raporu ve taşınır süreçlerini gösterir. Teknik gereksinim ve teknik kabul ilgili teknik şubenin; idari dosya, süre, teminat, ödeme evrakı ve merkezi kayıt İdari İşlerin sorumluluğundadır.

---

## ID-01 — İhale ve satın alma dosyası

**Süreç sahibi:** İdari İşler Şefliği  
**Teknik içerik sahibi:** İhtiyaç sahibi şube  
**Hesap verebilir:** Harcama yetkilisi  
**Girdiler:** Onaylı ihtiyaç, bütçe/ödenek, teknik şartname, miktar, yaklaşık maliyet, iş programı ve uygun ihale yöntemi.  
**Çıktılar:** Onay belgesi, ihale/temin dosyası, EKAP kayıtları, değerlendirme ve sözleşme.

```mermaid
flowchart TD
    A([Onaylı ihtiyaç]) --> B[Teknik şube: kapsam, şartname ve miktar]
    B --> C[Teknik şube: yaklaşık maliyet girdileri]
    C --> D[İdari İşler: bütçe, ödenek ve satın alma yöntemi kontrolü]
    D --> E{Dosya tam ve mevzuata uygun mu?}
    E -- Hayır --> F[Eksik/düzeltme listesi]
    F --> B
    E -- Evet --> G{İhale/temin türü}
    G -- Açık/Diğer ihale --> H[İhale onayı, ilan/davet ve EKAP süreci]
    G -- Doğrudan temin --> I[Onay, piyasa fiyat araştırması ve EKAP kaydı]
    H --> J[Tekliflerin alınması ve açılması]
    I --> K[Teslim/sipariş kararı]
    J --> L[İhale komisyonu değerlendirmesi]
    L --> M{Geçerli ve uygun teklif var mı?}
    M -- Hayır --> N[İptal veya yeniden ihale kararı]
    N --> B
    M -- Evet --> O[Karar, bildirim ve sözleşmeye davet]
    O --> P[Sözleşme ve teminat kontrolleri]
    P --> Q[İş programı ve teknik kontrol ekibine devir]
    K --> Q
```

**Görev ayrılığı:** Şartnameyi hazırlayan, teklifi değerlendiren, işi kontrol eden, kabul eden ve ödemeyi gerçekleştiren roller mevzuata uygun biçimde ayrılmalıdır.

**Önerilen KPI:** Dosya hazırlama süresi, eksik dosya oranı, ihale iptal oranı, rekabet/teklif sayısı, planlanan–gerçekleşen satın alma süresi.

---

## ID-02 — Sözleşme, hakediş, muayene-kabul ve ödeme

**Süreç sahibi:** İdari İşler — idari ve mali dosya  
**Teknik kontrol sahibi:** İlgili teknik şube  
**Girdiler:** Sözleşme, iş programı, teslim/saha kayıtları, metraj, faturalar, teminat ve kontrol raporları.  
**Çıktılar:** Hakediş, muayene-kabul, kesinti/ceza, ödeme emri evrakı, geçici/kesin kabul ve sözleşme kapanışı.

```mermaid
flowchart TD
    A([Sözleşme imzalandı]) --> B[İdari İşler: sözleşme takvimi, teminat ve yükümlülük kaydı]
    B --> C[Teknik şube: işe başlama ve kontrol planı]
    C --> D[Yüklenici uygulama/teslim]
    D --> E[Teknik kontrol: miktar, kalite, süre ve kanıt]
    E --> F{İş uygun mu?}
    F -- Hayır --> G[Eksik/kusurlu iş tutanağı ve düzeltme]
    G --> D
    F -- Evet --> H[Hakediş/metraj veya teslim raporu]
    H --> I[İdari İşler: sözleşme, süre, fiyat farkı, kesinti ve teminat kontrolü]
    I --> J{Belgeler tam mı?}
    J -- Hayır --> K[Eksik evrak bildirimi]
    K --> H
    J -- Evet --> L[Bağımsız muayene-kabul komisyonu]
    L --> M{Kabul uygun mu?}
    M -- Hayır --> G
    M -- Evet --> N[Fatura ve ödeme emri belgesi]
    N --> O[Mali kontrol ve ödeme]
    O --> P{Son hakediş/kabul mü?}
    P -- Hayır --> D
    P -- Evet --> Q[Geçici/kesin kabul ve teminat iade takvimi]
    Q --> R[Sözleşme performans ve kapanış dosyası]
```

**Kontroller:** Sözleşme kilometre taşları, teminat bitiş uyarısı, gecikme/ceza kontrolü, hakediş–metraj eşleşmesi, kabul komisyonu bağımsızlığı.

---

## ID-03 — Bütçe, performans programı ve faaliyet raporu

**Süreç sahibi:** İdari İşler Şefliği  
**Veri sahibi:** Her şube  
**Girdiler:** Stratejik plan, hedefler, faaliyetler, bütçe ihtiyaçları, gerçekleşmeler, KPI ve mali veriler.  
**Çıktılar:** Gider/gelir bütçe teklifi, performans programı, faaliyet raporu ve aylık yönetici göstergeleri.

```mermaid
flowchart TD
    A([Bütçe/rapor dönemi başlar]) --> B[İdari İşler: takvim, şablon ve veri sözlüğü]
    B --> C[Şubeler: hedef, faaliyet, bütçe ve KPI girişi]
    C --> D[Otomatik tamlık ve tutarlılık kontrolü]
    D --> E{Veriler tam ve tutarlı mı?}
    E -- Hayır --> F[Düzeltme talebi]
    F --> C
    E -- Evet --> G[İdari İşler: konsolidasyon ve önceki dönem karşılaştırması]
    G --> H[Daire Başkanı: öncelik ve kaynak değerlendirmesi]
    H --> I{Revizyon gerekli mi?}
    I -- Evet --> C
    I -- Hayır --> J[Mali Hizmetler/Strateji birimine gönderim]
    J --> K[Görüş ve bütçe sınırı]
    K --> L{Uygun mu?}
    L -- Hayır --> G
    L -- Evet --> M[Onaylı bütçe ve performans hedefleri]
    M --> N[Aylık gerçekleşme ve sapma takibi]
    N --> O[Yıl sonu faaliyet raporu]
```

**Önerilen KPI:** Zamanında veri giriş oranı, bütçe sapması, hedef gerçekleşme oranı, manuel düzeltme sayısı, rapor üretim süresi.

---

## ID-04 — Evrak, EBYS, izin ve arşiv

**Süreç sahibi:** İdari İşler Şefliği  
**Girdiler:** Gelen/giden evrak, olur, görev/izin/rapor, dosya planı ve kurum yazışmaları.  
**Çıktılar:** Doğru birime yönlendirilmiş evrak, işlem izi, cevap, izin kaydı ve arşiv.

```mermaid
flowchart TD
    A([Gelen evrak veya iç yazışma]) --> B[EBYS kayıt, güvenlik ve kişisel veri sınıflandırması]
    B --> C[Konu, süre ve yetkili birim belirleme]
    C --> D[İlgili şubeye elektronik havale]
    D --> E[Şube işlem sahibi ve sorumlu personel]
    E --> F{Görüş/onay başka birimden gerekli mi?}
    F -- Evet --> G[EBYS üzerinden görüş talebi]
    G --> H[Görüşlerin konsolidasyonu]
    F -- Hayır --> I[Cevap/olur/işlem taslağı]
    H --> I
    I --> J[Yetkili kontrol ve e-imza]
    J --> K[Giden evrak veya iç karar]
    K --> L[Saklama planı, erişim seviyesi ve arşiv]
    L --> M{Yasal/idari süre içinde tamamlandı mı?}
    M -- Hayır --> N[Gecikme bildirimi ve escalation]
    M -- Evet --> O([Dosya kapanışı])
```

**Temel kontrol:** Şubeler paralel evrak kayıt defteri oluşturmamalı; EBYS tek resmî kayıt noktası olmalıdır.

---

## ID-05 — Taşınır, ambar, zimmet ve sayım

**Süreç sahibi:** İdari İşler / Taşınır Kayıt Yetkilisi  
**Girdiler:** Muayene-kabul edilmiş mal, TİF, talep, zimmet, devir ve sayım listesi.  
**Çıktılar:** Giriş-çıkış kaydı, zimmet, ambar bakiyesi, sayım tutanağı, hurda/kayıp işlemi ve konsolide cetvel.

```mermaid
flowchart TD
    A([Mal teslimi veya mevcut taşınır işlemi]) --> B[Muayene-kabul ve belge kontrolü]
    B --> C{Teslim uygun mu?}
    C -- Hayır --> D[Ret/iade veya eksik teslim tutanağı]
    C -- Evet --> E[Taşınır işlem fişi ve varlık kaydı]
    E --> F[Etiket/seri no ve ambar konumu]
    F --> G{Kullanıcıya teslim mi?}
    G -- Evet --> H[Talep/onay ve zimmet]
    G -- Hayır --> I[Ambar stok kaydı]
    H --> J[Kullanıcı/teknik şube koruma sorumluluğu]
    I --> K[Periyodik stok ve çevre koşulu kontrolü]
    J --> L[Devir, iade, kayıp, arıza veya hurda bildirimi]
    K --> M[Yıl sonu/ara sayım]
    L --> M
    M --> N[Fiziki kayıt ile sistem karşılaştırması]
    N --> O{Fark var mı?}
    O -- Evet --> P[Sayım farkı inceleme ve mevzuat işlemi]
    O -- Hayır --> Q[Konsolide cetvel ve kapanış]
    P --> Q
```

**Görev paylaşımı:** Kayıt, ambar ve zimmet İdari İşlerde; teknik şube taşınırın kullanıcı ve koruma sorumlusudur.

---

## ID-06 — Yönetmelik, yönerge ve görev tanımı değişikliği

```mermaid
flowchart TD
    A[Mevzuat/organizasyon/süreç değişikliği] --> B[İdari İşler: etkilenen dokümanların envanteri]
    B --> C[İlgili şube: içerik ve görev etkisi]
    C --> D[Hukuk Müşavirliği: yetki ve mevzuat kontrolü]
    D --> E{Uygun mu?}
    E -- Hayır --> F[Revizyon ve çelişki giderme]
    F --> C
    E -- Evet --> G[Gerekli başkanlık/meclis/kurul onayı]
    G --> H[Yeni revizyon, yürürlük ve mülga referansları]
    H --> I[Personel tebliği ve eğitim]
    I --> J[Eski kopyaların arşivlenmesi ve kullanım dışı bırakılması]
```
