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
    A([Onaylı ihtiyaç<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]) --> B[Teknik şube: kapsam, şartname ve miktar<br/>Sorumlu: İlgili Teknik Şubenin Yalın Pozisyonu]
    B --> C[Teknik şube: yaklaşık maliyet girdileri<br/>Sorumlu: İlgili Teknik Şubenin Yalın Pozisyonu]
    C --> D[İdari İşler: bütçe, ödenek ve satın alma yöntemi kontrolü<br/>Sorumlu: İhale ve Satın Alma Koordinatörü]
    D --> E{Dosya tam ve mevzuata uygun mu?<br/>Sorumlu: Doküman Kontrol ve Mevzuat Takip Uzmanı}
    E -- Hayır --> F[Eksik/düzeltme listesi<br/>Sorumlu: İç Kontrol ve Risk Sorumlusu]
    F --> B
    E -- Evet --> G{İhale/temin türü<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu}
    G -- Açık/Diğer ihale --> H[İhale onayı, ilan/davet ve EKAP süreci<br/>Sorumlu: İhale ve Satın Alma Koordinatörü]
    G -- Doğrudan temin --> I[Onay, piyasa fiyat araştırması ve EKAP kaydı<br/>Sorumlu: İhale ve Satın Alma Koordinatörü]
    H --> J[Tekliflerin alınması ve açılması<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    I --> K[Teslim/sipariş kararı<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    J --> L[İhale komisyonu değerlendirmesi<br/>Sorumlu: Yetkili İhale Komisyonu]
    L --> M{Geçerli ve uygun teklif var mı?<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu}
    M -- Hayır --> N[İptal veya yeniden ihale kararı<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    N --> B
    M -- Evet --> O[Karar, bildirim ve sözleşmeye davet<br/>Sorumlu: Sözleşme ve Teminat Sorumlusu]
    O --> P[Sözleşme ve teminat kontrolleri<br/>Sorumlu: Sözleşme ve Teminat Sorumlusu]
    P --> Q[İş programı ve teknik kontrol ekibine devir<br/>Sorumlu: İlgili Teknik Şubenin Yalın Pozisyonu]
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
    A([Sözleşme imzalandı<br/>Sorumlu: Sözleşme ve Teminat Sorumlusu]) --> B[İdari İşler: sözleşme takvimi, teminat ve yükümlülük kaydı<br/>Sorumlu: Sözleşme ve Teminat Sorumlusu]
    B --> C[Teknik şube: işe başlama ve kontrol planı<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    C --> D[Yüklenici uygulama/teslim<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    D --> E[Teknik kontrol: miktar, kalite, süre ve kanıt<br/>Sorumlu: İlgili Teknik Şubenin Yalın Pozisyonu]
    E --> F{İş uygun mu?<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu}
    F -- Hayır --> G[Eksik/kusurlu iş tutanağı ve düzeltme<br/>Sorumlu: İç Kontrol ve Risk Sorumlusu]
    G --> D
    F -- Evet --> H[Hakediş/metraj veya teslim raporu<br/>Sorumlu: Hakediş ve Ödeme Dosyası Sorumlusu]
    H --> I[İdari İşler: sözleşme, süre, fiyat farkı, kesinti ve teminat kontrolü<br/>Sorumlu: Sözleşme ve Teminat Sorumlusu]
    I --> J{Belgeler tam mı?<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu}
    J -- Hayır --> K[Eksik evrak bildirimi<br/>Sorumlu: Hakediş ve Ödeme Dosyası Sorumlusu]
    K --> H
    J -- Evet --> L[Bağımsız muayene-kabul komisyonu<br/>Sorumlu: Yetkili Muayene ve Kabul Komisyonu]
    L --> M{Kabul uygun mu?<br/>Sorumlu: Yetkili Muayene ve Kabul Komisyonu}
    M -- Hayır --> G
    M -- Evet --> N[Fatura ve ödeme emri belgesi<br/>Sorumlu: Hakediş ve Ödeme Dosyası Sorumlusu]
    N --> O[Mali kontrol ve ödeme<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    O --> P{Son hakediş/kabul mü?<br/>Sorumlu: Hakediş ve Ödeme Dosyası Sorumlusu}
    P -- Hayır --> D
    P -- Evet --> Q[Geçici/kesin kabul ve teminat iade takvimi<br/>Sorumlu: Sözleşme ve Teminat Sorumlusu]
    Q --> R[Sözleşme performans ve kapanış dosyası<br/>Sorumlu: Sözleşme ve Teminat Sorumlusu]
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
    A([Bütçe/rapor dönemi başlar<br/>Sorumlu: İhale ve Satın Alma Koordinatörü]) --> B[İdari İşler: takvim, şablon ve veri sözlüğü<br/>Sorumlu: Bütçe ve Performans Sorumlusu]
    B --> C[Şubeler: hedef, faaliyet, bütçe ve KPI girişi<br/>Sorumlu: İhale ve Satın Alma Koordinatörü]
    C --> D[Otomatik tamlık ve tutarlılık kontrolü<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    D --> E{Veriler tam ve tutarlı mı?<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu}
    E -- Hayır --> F[Düzeltme talebi<br/>Sorumlu: İç Kontrol ve Risk Sorumlusu]
    F --> C
    E -- Evet --> G[İdari İşler: konsolidasyon ve önceki dönem karşılaştırması<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    G --> H[Daire Başkanı: öncelik ve kaynak değerlendirmesi<br/>Sorumlu: İdari ve Mali İşler Şube Müdürü / Ulaşım Dairesi Başkanı]
    H --> I{Revizyon gerekli mi?<br/>Sorumlu: Doküman Kontrol ve Mevzuat Takip Uzmanı}
    I -- Evet --> C
    I -- Hayır --> J[Mali Hizmetler/Strateji birimine gönderim<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    J --> K[Görüş ve bütçe sınırı<br/>Sorumlu: İhale ve Satın Alma Koordinatörü]
    K --> L{Uygun mu?<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu}
    L -- Hayır --> G
    L -- Evet --> M[Onaylı bütçe ve performans hedefleri<br/>Sorumlu: İhale ve Satın Alma Koordinatörü]
    M --> N[Aylık gerçekleşme ve sapma takibi<br/>Sorumlu: Faaliyet Raporlama Uzmanı]
    N --> O[Yıl sonu faaliyet raporu<br/>Sorumlu: Faaliyet Raporlama Uzmanı]
```

**Önerilen KPI:** Zamanında veri giriş oranı, bütçe sapması, hedef gerçekleşme oranı, manuel düzeltme sayısı, rapor üretim süresi.

---

## ID-04 — Evrak, EBYS, izin ve arşiv

**Süreç sahibi:** İdari İşler Şefliği  
**Girdiler:** Gelen/giden evrak, olur, görev/izin/rapor, dosya planı ve kurum yazışmaları.  
**Çıktılar:** Doğru birime yönlendirilmiş evrak, işlem izi, cevap, izin kaydı ve arşiv.

```mermaid
flowchart TD
    A([Gelen evrak veya iç yazışma<br/>Sorumlu: EBYS ve Arşiv Sorumlusu]) --> B[EBYS kayıt, güvenlik ve kişisel veri sınıflandırması<br/>Sorumlu: EBYS ve Arşiv Sorumlusu]
    B --> C[Konu, süre ve yetkili birim belirleme<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    C --> D[İlgili şubeye elektronik havale<br/>Sorumlu: EBYS ve Arşiv Sorumlusu]
    D --> E[Şube işlem sahibi ve sorumlu personel<br/>Sorumlu: Personel ve İzin İşleri Sorumlusu]
    E --> F{Görüş/onay başka birimden gerekli mi?<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu}
    F -- Evet --> G[EBYS üzerinden görüş talebi<br/>Sorumlu: EBYS ve Arşiv Sorumlusu]
    G --> H[Görüşlerin konsolidasyonu<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    F -- Hayır --> I[Cevap/olur/işlem taslağı<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    H --> I
    I --> J[Yetkili kontrol ve e-imza<br/>Sorumlu: EBYS ve Arşiv Sorumlusu]
    J --> K[Giden evrak veya iç karar<br/>Sorumlu: EBYS ve Arşiv Sorumlusu]
    K --> L[Saklama planı, erişim seviyesi ve arşiv<br/>Sorumlu: EBYS ve Arşiv Sorumlusu]
    L --> M{Yasal/idari süre içinde tamamlandı mı?<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu}
    M -- Hayır --> N[Gecikme bildirimi ve escalation<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    M -- Evet --> O([Dosya kapanışı<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu])
```

**Temel kontrol:** Şubeler paralel evrak kayıt defteri oluşturmamalı; EBYS tek resmî kayıt noktası olmalıdır.

---

## ID-05 — Taşınır, ambar, zimmet ve sayım

**Süreç sahibi:** İdari İşler / Taşınır Kayıt Yetkilisi  
**Girdiler:** Muayene-kabul edilmiş mal, TİF, talep, zimmet, devir ve sayım listesi.  
**Çıktılar:** Giriş-çıkış kaydı, zimmet, ambar bakiyesi, sayım tutanağı, hurda/kayıp işlemi ve konsolide cetvel.

```mermaid
flowchart TD
    A([Mal teslimi veya mevcut taşınır işlemi<br/>Sorumlu: Taşınır Kayıt ve Ambar Sorumlusu]) --> B[Muayene-kabul ve belge kontrolü<br/>Sorumlu: Yetkili Muayene ve Kabul Komisyonu]
    B --> C{Teslim uygun mu?<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu}
    C -- Hayır --> D[Ret/iade veya eksik teslim tutanağı<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    C -- Evet --> E[Taşınır işlem fişi ve varlık kaydı<br/>Sorumlu: Taşınır Kayıt ve Ambar Sorumlusu]
    E --> F[Etiket/seri no ve ambar konumu<br/>Sorumlu: Taşınır Kayıt ve Ambar Sorumlusu]
    F --> G{Kullanıcıya teslim mi?<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu}
    G -- Evet --> H[Talep/onay ve zimmet<br/>Sorumlu: Taşınır Kayıt ve Ambar Sorumlusu]
    G -- Hayır --> I[Ambar stok kaydı<br/>Sorumlu: Taşınır Kayıt ve Ambar Sorumlusu]
    H --> J[Kullanıcı/teknik şube koruma sorumluluğu<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    I --> K[Periyodik stok ve çevre koşulu kontrolü<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    J --> L[Devir, iade, kayıp, arıza veya hurda bildirimi<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    K --> M[Yıl sonu/ara sayım<br/>Sorumlu: Taşınır Kayıt ve Ambar Sorumlusu]
    L --> M
    M --> N[Fiziki kayıt ile sistem karşılaştırması<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    N --> O{Fark var mı?<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu}
    O -- Evet --> P[Sayım farkı inceleme ve mevzuat işlemi<br/>Sorumlu: Taşınır Kayıt ve Ambar Sorumlusu]
    O -- Hayır --> Q[Konsolide cetvel ve kapanış<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    P --> Q
```

**Görev paylaşımı:** Kayıt, ambar ve zimmet İdari İşlerde; teknik şube taşınırın kullanıcı ve koruma sorumlusudur.

---

## ID-06 — Yönetmelik, yönerge ve görev tanımı değişikliği

```mermaid
flowchart TD
    A[Mevzuat/organizasyon/süreç değişikliği<br/>Sorumlu: Doküman Kontrol ve Mevzuat Takip Uzmanı] --> B[İdari İşler: etkilenen dokümanların envanteri<br/>Sorumlu: Doküman Kontrol ve Mevzuat Takip Uzmanı]
    B --> C[İlgili şube: içerik ve görev etkisi<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    C --> D[Hukuk Müşavirliği: yetki ve mevzuat kontrolü<br/>Sorumlu: Doküman Kontrol ve Mevzuat Takip Uzmanı]
    D --> E{Uygun mu?<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu}
    E -- Hayır --> F[Revizyon ve çelişki giderme<br/>Sorumlu: Doküman Kontrol ve Mevzuat Takip Uzmanı]
    F --> C
    E -- Evet --> G[Gerekli başkanlık/meclis/kurul onayı<br/>Sorumlu: İdari ve Mali İşler ilgili yalın pozisyonu]
    G --> H[Yeni revizyon, yürürlük ve mülga referansları<br/>Sorumlu: Doküman Kontrol ve Mevzuat Takip Uzmanı]
    H --> I[Personel tebliği ve eğitim<br/>Sorumlu: Personel ve İzin İşleri Sorumlusu]
    I --> J[Eski kopyaların arşivlenmesi ve kullanım dışı bırakılması<br/>Sorumlu: EBYS ve Arşiv Sorumlusu]
```
