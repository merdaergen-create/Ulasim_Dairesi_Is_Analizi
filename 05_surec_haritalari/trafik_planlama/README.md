# Trafik Planlama Süreç Haritaları

Bu bölüm Ulaşım Planlama Şube Müdürlüğünün teknik sahipliğinde yürütülmesi önerilen ulaşım planlama, yol/kavşak, erişim, sinyalizasyon, işaretleme ve Trafik Yönetim Merkezi süreçlerini gösterir.

---

## TP-01 — Ulaşım Ana Planı hazırlama ve revizyonu

**Süreç sahibi:** Ulaşım Planlama Şube Müdürlüğü  
**Hesap verebilir:** Ulaşım Dairesi Başkanı  
**Girdiler:** Stratejik plan, nazım imar planı, nüfus ve arazi kullanımı, yolculuk anketleri, trafik/toplu taşıma sayımları, kaza verisi, AUS verisi, yatırım ve bütçe sınırları.  
**Çıktılar:** Onaylı Ulaşım Ana Planı, ulaşım modeli, alternatif analizi, yatırım programı, uygulama takvimi ve KPI seti.

```mermaid
flowchart TD
    A([Plan/revizyon ihtiyacı]) --> B[Ulaşım Planlama: kapsam ve çalışma programı]
    B --> C[Veri ihtiyaç planı ve veri sorumluları]
    C --> D[AUS: sensör, kamera ve veri platformu çıktıları]
    C --> E[Toplu Taşıma: hat, yolcu, filo ve hizmet verileri]
    C --> F[İmar/Fen: arazi kullanımı ve yatırım projeleri]
    D --> G[Veri kalite ve eksiklik kontrolü]
    E --> G
    F --> G
    G --> H{Veri yeterli mi?}
    H -- Hayır --> I[Ek sayım, anket veya saha etüdü]
    I --> G
    H -- Evet --> J[Mevcut durum modeli ve kalibrasyon]
    J --> K[Alternatif senaryolar ve etki analizi]
    K --> L[Paydaş ve kurum görüşleri]
    L --> M{Teknik ve mali olarak uygulanabilir mi?}
    M -- Hayır --> K
    M -- Evet --> N[Tercih edilen plan, yatırım programı ve KPI]
    N --> O[Yetkili kurul/UKOME/Meclis süreci]
    O --> P{Onaylandı mı?}
    P -- Hayır --> Q[Gerekçe ve revizyon]
    Q --> N
    P -- Evet --> R[Uygulama portföyü ve sorumlu birimler]
    R --> S[Periyodik izleme ve plan revizyonu]
    S --> T([Onaylı plan ve izleme raporu])
```

**Temel kontroller**

- Plan verileri tek veri kataloğunda sürümlenmelidir.
- Senaryolar erişilebilirlik, güvenlik, çevresel etki, toplu taşıma ve mali uygulanabilirlik açısından karşılaştırılmalıdır.
- UKOME teknik planı hazırlamaz; karar gerektiren maddeleri kurul sürecine alır.

**Önerilen KPI:** Veri tamlık oranı, model kalibrasyon başarısı, proje gerçekleşme oranı, planlanan/gerçekleşen yatırım farkı, erişilebilirlik ve yolculuk süresi değişimi.

---

## TP-02 — Yol, kavşak ve geometrik düzenleme projesi

**Süreç sahibi:** Ulaşım Planlama / Yol Tasarım Servisi  
**Girdiler:** Talep veya sorun kaydı, kaza/yoğunluk verisi, halihazır harita, imar planı, trafik sayımı, mülkiyet ve altyapı verileri.  
**Çıktılar:** Onaylı avan/uygulama projesi, UKOME teklif dosyası, yaklaşık maliyet girdileri, uygulama ve kabul kaydı.

```mermaid
flowchart TD
    A([Talep, kaza veya kapasite sorunu]) --> B[Planlama Servisi: ön inceleme]
    B --> C{Ulaşım Dairesi yetki alanında mı?}
    C -- Hayır --> D[Yetkili kuruma yönlendirme ve kayıt kapatma]
    C -- Evet --> E[Saha etüdü, sayım ve halihazır kontrolü]
    E --> F[Yol Tasarım: alternatif geometrik çözümler]
    F --> G[İmar, mülkiyet, altyapı ve erişilebilirlik görüşleri]
    G --> H[Trafik güvenliği ve kapasite analizi]
    H --> I{Teknik çözüm uygun mu?}
    I -- Hayır --> F
    I -- Evet --> J{UKOME kararı gerekli mi?}
    J -- Evet --> K[UKOME teknik teklif dosyası]
    K --> L[UKOME kararı]
    J -- Hayır --> M[Yetkili teknik onay]
    L --> N[Uygulama paketi ve iş programı]
    M --> N
    N --> O[Fen İşleri: yol gövdesi/yapım]
    N --> P[Ulaşım Planlama: sinyal ve işaretleme]
    O --> Q[Ortak saha kontrolü]
    P --> Q
    Q --> R{Proje ve kalite kriterlerine uygun mu?}
    R -- Hayır --> S[Düzeltici iş emri]
    S --> Q
    R -- Evet --> T[CBS envanteri, as-built ve kabul]
    T --> U([Proje kapanışı])
```

**Görev paylaşımı:** Trafik geometrisi ve trafik projesi Ulaşım Planlamada; yol gövdesi yapımı Fen İşlerinde; sinyalizasyon ve işaretleme Ulaşım Planlama Uygulama/Yapım biriminde olmalıdır.

**Önerilen KPI:** Ön inceleme süresi, proje revizyon sayısı, uygulama sonrası kaza/yoğunluk değişimi, as-built kayıt tamlığı.

---

## TP-03 — Geçiş yolu, yol kapatma ve yol daraltma izni

**Süreç sahibi:** Ulaşım Planlama Şube Müdürlüğü  
**Karar/sekretarya:** Ulaşım Koordinasyon / UKOME  
**Girdiler:** E-başvuru, vaziyet veya çalışma projesi, süre, iş programı, trafik yönetim planı, tapu/imar ve kurum izinleri.  
**Çıktılar:** Teknik uygunluk raporu, onaylı geçici trafik planı, izin/UKOME kararı veya gerekçeli ret, saha kapanış kaydı.

```mermaid
flowchart TD
    A([Başvuru]) --> B[E-başvuru ve belge tamlık kontrolü]
    B --> C{Belgeler tam mı?}
    C -- Hayır --> D[Eksik belge bildirimi]
    D --> B
    C -- Evet --> E[Planlama: yetki alanı ve mevzuat kontrolü]
    E --> F[Saha incelemesi ve trafik güvenliği analizi]
    F --> G[İmar, altyapı, AYKOME, kolluk ve ilgili kurum görüşleri]
    G --> H{Teknik olarak uygun mu?}
    H -- Hayır --> I[Gerekçeli ret veya proje revizyon talebi]
    I --> J([Süreç kapatılır veya yeniden başvuru])
    H -- Evet --> K{UKOME kararı gerekli mi?}
    K -- Evet --> L[UKOME gündem ve karar süreci]
    K -- Hayır --> M[Yetkili idari/teknik onay]
    L --> N[İzin ve trafik tedbir şartlarının yayımlanması]
    M --> N
    N --> O[Başlangıç öncesi saha güvenlik kontrolü]
    O --> P[Çalışma süresince denetim]
    P --> Q{Süre/şart ihlali var mı?}
    Q -- Evet --> R[Düzeltme, durdurma veya ilgili makama bildirim]
    R --> P
    Q -- Hayır --> S[Çalışma bitişi ve yolun eski hale getirilmesi]
    S --> T[Saha kabulü, fotoğraf ve kapanış kaydı]
    T --> U([Süreç tamamlandı])
```

**Temel kontroller:** Standart kontrol listesi, yetki alanı doğrulaması, erişilebilir yaya güzergâhı, acil servis erişimi, başlangıç/bitiş fotoğrafı, süre aşımı uyarısı.

---

## TP-04 — Sinyalize kavşak kurulumu, bakım ve optimizasyon

**Süreç sahibi:** Ulaşım Planlama / Sinyalizasyon Servisi  
**Teknoloji ve merkez entegrasyonu:** Akıllı Ulaşım Sistemleri / Bilgi İşlem  
**Girdiler:** Kaza ve yoğunluk verisi, sayım, kavşak geometrisi, enerji/iletişim imkânı, UKOME kararı, arıza alarmı veya bakım planı.  
**Çıktılar:** Onaylı sinyal projesi, kurulu ve test edilmiş kavşak, güncel sinyal planı, bakım/arıza kaydı ve performans raporu.

```mermaid
flowchart TD
    A([Yeni ihtiyaç veya mevcut kavşak problemi]) --> B[Trafik mühendisliği ve sayım]
    B --> C{Sinyalizasyon uygun çözüm mü?}
    C -- Hayır --> D[Alternatif geometrik/işaretleme çözümü]
    C -- Evet --> E[Faz planı, süre hesabı ve ekipman projesi]
    E --> F[AUS/Bilgi İşlem: ağ ve merkez entegrasyon tasarımı]
    F --> G[UKOME/kurum onayları]
    G --> H[Tedarik ve saha kurulum planı]
    H --> I[İSG, enerji ve altyapı hazırlığı]
    I --> J[Montaj, kablolama ve programlama]
    J --> K[Elektriksel, fonksiyonel ve trafik güvenliği testleri]
    K --> L{Kabul kriterleri sağlandı mı?}
    L -- Hayır --> M[Hata giderme]
    M --> K
    L -- Evet --> N[Envanter, as-built ve yedek konfigürasyon]
    N --> O[Trafik Yönetim Merkezi işletimi]
    O --> P[Alarm, ihbar veya periyodik bakım]
    P --> Q[Arıza sınıflandırma ve SLA]
    Q --> R{Saha ekipmanı mı, merkez/ağ mı?}
    R -- Saha --> S[Sinyalizasyon Servisi müdahalesi]
    R -- Merkez/Ağ --> T[AUS/Bilgi İşlem müdahalesi]
    S --> U[Test ve servis kapanışı]
    T --> U
    U --> V[Veriyle süre optimizasyonu]
```

**Önerilen KPI:** Arıza ilk yanıt süresi, ortalama onarım süresi, kavşak kullanılabilirliği, gecikme/kuyruk değişimi, tekrar arıza oranı.

---

## TP-05 — Yatay ve düşey işaretleme yaşam döngüsü

**Süreç sahibi:** Ulaşım Planlama / Uygulama ve Yapım Birimi  
**Girdiler:** Onaylı trafik projesi veya UKOME kararı, yol ve levha envanteri, saha kontrolü, aşınma/hasar bildirimi, yıllık program.  
**Çıktılar:** Uygulanmış çizgi/levha, kalite ölçümü, metraj, fotoğraf ve güncel CBS envanteri.

```mermaid
flowchart TD
    A([Proje, karar veya bakım ihtiyacı]) --> B[Envanter ve saha doğrulaması]
    B --> C{Onaylı proje/karar var mı?}
    C -- Hayır --> D[Planlama ve onay sürecine yönlendirme]
    C -- Evet --> E[Risk, yol sınıfı ve aşınmaya göre öncelik]
    E --> F[Yıllık/aylık iş programı]
    F --> G[Malzeme, ekip, trafik tedbiri ve İSG hazırlığı]
    G --> H[Yatay çizgi veya levha uygulaması]
    H --> I[Konum, ölçü, görünürlük ve malzeme kalite kontrolü]
    I --> J{Uygun mu?}
    J -- Hayır --> K[Düzeltme/yenileme]
    K --> I
    J -- Evet --> L[Fotoğraf, metraj ve CBS güncellemesi]
    L --> M[Periyodik performans ve aşınma izlemesi]
```

**Temel kontrol:** Proje veya karar olmadan saha uygulaması yapılmamalı; levha ve işaretler tekil varlık numarasıyla izlenmelidir.

---

## TP-06 — Trafik Yönetim Merkezi günlük operasyonu

**Operasyon sahibi:** Ulaşım Planlama / Trafik Yönetim Servisi  
**Platform sahibi:** Akıllı Ulaşım Sistemleri  
**Girdiler:** Canlı kamera/sensör/sinyal verisi, olay ihbarı, planlı yol çalışması, hava ve etkinlik bilgisi.  
**Çıktılar:** Olay kaydı, trafik müdahalesi, kurum koordinasyonu, yol kullanıcı bilgilendirmesi ve vardiya raporu.

```mermaid
flowchart LR
    A[Canlı veri ve ihbar] --> B[Trafik Yönetim: olay doğrulama]
    B --> C{Olay türü}
    C -- Kaza/Acil --> D[Emniyet, sağlık, itfaiye koordinasyonu]
    C -- Arıza --> E[Sinyalizasyon veya AUS teknik ekibi]
    C -- Yoğunluk --> F[Sinyal planı ve yönlendirme müdahalesi]
    C -- Planlı çalışma --> G[Onaylı trafik yönetim planının uygulanması]
    D --> H[Dinamik mesaj, duyuru ve alternatif güzergâh]
    E --> H
    F --> H
    G --> H
    H --> I[Olay süresince izleme]
    I --> J{Normal işletime dönüldü mü?}
    J -- Hayır --> I
    J -- Evet --> K[Olay kapanışı ve müdahale kayıtları]
    K --> L[Vardiya raporu ve tekrar eden sorun analizi]
```

**Kontroller:** Yetkili personel matrisi, tüm manuel müdahalelerin loglanması, kamera erişim yetkisi, vardiya devir kontrol listesi, kritik sistem yedekliliği.

**Önerilen KPI:** Olay doğrulama süresi, müdahale başlatma süresi, olay kapanış süresi, sistem kullanılabilirliği, yanlış alarm oranı.
