# Ulaşım Dairesi Yalın Organizasyon ve Süreç Tasarım Gerekçesi Raporu

## 1. Raporun amacı

Bu rapor, `05_surec_haritalari` ve `06_raporlar` içinde tespit edilen organizasyonel, yönetsel ve operasyonel eksiklerin hangi gerekçelerle aşağıdaki çalışmalara dönüştürüldüğünü açıklar:

- `09_yalin_pozisyonlari`
- `10_yalin_pozisyon_gorev_tanimlari`
- `12_formlar`
- `14_yalin_organizasyon_semasi`
- `15_yalin_surec_haritalari`

Çalışmanın ana yaklaşımı, yalnız bir organizasyon şeması oluşturmak değil; süreç, pozisyon, görev tanımı, birim, sorumluluk ve form yapısını birbiriyle tutarlı tek bir işletim modeline dönüştürmektir.

## 2. İncelenen temel kaynaklar

### 2.1. `05_surec_haritalari`

Bu klasörde Ulaşım Dairesinin trafik planlama, UKOME, toplu ulaşım, AUS, otogar, trafik eğitim ve idari işler süreçleri departman bazında haritalanmıştır. Süreçlerde girdiler, faaliyetler, karar noktaları, çıktılar, kapanış kanıtları, kontroller ve KPI alanları gösterilmiştir.

Kaynak incelemesi sonucunda ayrıca şu süreçler eklenmiştir:

- TP-07 — Otopark erişim uygunluk belgesi
- TU-06 — Ticari plaka tahsis, devir ve iptal
- TU-07 — Servis aracı izin belgesi
- TU-08 — Yük nakli ve özel taşıma izni
- TU-09 — Ticari araç uygunluk, çalışma ruhsatı ve vize yenileme
- ID-07 — Taşıt görev emri ve hizmet aracı görevlendirme

### 2.2. `06_raporlar`

Özellikle `optimum_organizasyon_ve_pozisyon_onerisi.md` raporunda şu temel tasarım ilkeleri ortaya konmuştur:

- Planlama ile saha işletmesinin ayrılması
- UKOME'nin teknik proje üretmeyip sekretarya ve karar sürecine odaklanması
- AUS'un teknoloji, veri ve entegrasyon sahibi olması
- Ruhsat ve ticari araç işlemlerinin toplu taşıma hizmet planlamasından ayrılması
- İhale, sözleşme, ödeme, taşınır ve evrak süreçlerinin merkezileştirilmesi
- TKM operasyonu ile teknik platform işletmesinin ayrılması
- Yeni şubelerin yalnız iş hacmi, vardiya ve uzmanlık gereği oluştuğunda kurulması

Aynı raporda tam hedef model 10 şube olarak tanımlanmış; Denizli ölçeği için ilk aşamada 8 şubeli yalın geçiş modeli önerilmiştir.

## 3. `05_surec_haritalari` içinde görülen eksikler

### 3.1. Süreçlerin organizasyon karşılığının tam tanımlı olmaması

Süreç haritaları hangi faaliyetin hangi departmanda yürütüldüğünü gösterse de, her sürecin hangi organizasyon birimi ve hangi yalın pozisyon tarafından yürütüleceği başlangıçta tam olarak tanımlı değildi.

Bu durum şu riskleri doğuruyordu:

- Aynı işin birden fazla şube tarafından sahiplenilmesi
- Sürecin yalnız “şube” seviyesinde tanımlanması
- Gerçek uygulayıcı pozisyonun bilinmemesi
- Vekâlet ve yedekleme yapısının kurulamaması
- İş yükünün kadro ihtiyacına dönüştürülememesi

### 3.2. Süreç ile görev tanımı arasında doğrudan bağlantı bulunmaması

Süreç adımları ayrı, görev tanımları ayrı dokümanlarda bulunuyordu. Bir pozisyonun hangi süreç kodunda ve hangi adımda görev yaptığı bütüncül biçimde görülemiyordu.

### 3.3. Süreçlerde sorumlu pozisyonun görünür olmaması

Haritalarda süreç sahibi ilkesi bulunmasına rağmen, her düğümün yanında ilgili sorumlu pozisyon ve bağlı birim bilgisi bulunmuyordu. Bu nedenle operasyonel sorumluluk dağılımı uygulamaya dönük yeterince açık değildi.

### 3.4. Başvuru, kontrol, kabul ve kapanış belgelerinin standart olmaması

Süreçlerde başvuru, eksik belge kontrolü, teknik inceleme, saha kontrolü, karar, teslim, kabul ve kapanış adımları vardı; ancak her süreç adımı için standart form gereksinimi toplu olarak tanımlanmamıştı.

### 3.5. Kaynak belgelerde bulunan bazı işlerin süreç haritalarında bağımsız görünmemesi

Mevcut kaynaklarda yer alan otopark erişim uygunluğu, ticari plaka, servis aracı, yük nakli, özel taşıma, ruhsat-vize ve taşıt görevlendirme işleri ilk süreç setinde yeterince ayrıştırılmamıştı. Bu işler daha sonra ayrı süreçler halinde eklenmiştir.

### 3.6. Birim seviyesinin eksik kalması

Süreç haritaları şube ve departman düzeyindeydi. Şube müdürlüğü altında hangi uzmanlık birimlerinin bulunacağı ve pozisyonların bu birimlere nasıl dağıtılacağı tanımlı değildi.

## 4. `06_raporlar` içinde görülen eksikler

### 4.1. Önerilen organizasyonun uygulama detayının sınırlı olması

Optimum organizasyon raporu şube ve pozisyon önerilerini ortaya koyuyordu; ancak her pozisyonun:

- hangi birimde yer alacağı,
- hangi süreç adımlarını yürüteceği,
- hangi girdileri kullanacağı,
- hangi çıktıları üreteceği,
- hangi yetki sınırına sahip olacağı,
- hangi KPI ile değerlendirileceği

ayrıntılı olarak tek tek tanımlanmamıştı.

### 4.2. 10 şubeli hedef model ile 8 şubeli geçiş modelinin operasyonel açılımının eksik olması

Raporda 10 şubeli hedef model ile 8 şubeli yalın geçiş modeli birlikte bulunuyordu. Ancak 8 şubeli modelde birleşecek rollerin, birimlerin ve pozisyonların tam yapısı ayrıca geliştirilmeliydi.

### 4.3. Pozisyon önerilerinin yalınlaştırılması ihtiyacı

Hedef modelde bazı uzmanlıklar ayrı pozisyonlar olarak önerilmişti. Denizli ölçeğinde ilk aşamada bu pozisyonların bir kısmının görev ayrılığı korunarak birleştirilmesi gerekiyordu.

Örnekler:

- Trafik güvenliği ile sürdürülebilir ulaşım
- Sinyal bakım ile saha elektroniği
- Veri platformu ile analitik
- Bütçe, performans ve faaliyet raporlama
- Sözleşme, teminat ve hakediş dosyası
- EBYS, arşiv ve personel işleri

### 4.4. Organizasyon önerisinin süreç haritalarına bağlanmamış olması

Rapor pozisyonları öneriyor, süreç haritaları faaliyetleri gösteriyordu; ancak önerilen organizasyonun süreç adımlarında nasıl çalışacağı doğrudan gösterilmiyordu.

### 4.5. Form ve kayıt düzeninin organizasyon tasarımına entegre edilmemesi

Rapor organizasyon ve görev ayrılığına odaklanıyordu. Başvuru, kontrol, kabul, teslim, karar ve kapanış formlarının hangi süreç adımında kullanılacağı ayrı bir çalışma gerektiriyordu.

## 5. Eksikler doğrultusunda oluşturulan çalışmalar

## 5.1. `09_yalin_pozisyonlari`

### Giderilen eksik

8 şubeli yalın geçiş modelinin yalnız şube adı düzeyinde kalması ve pozisyon yapısının uygulama ölçeğinde net olmaması.

### Yapılan tasarım

Her şube için:

- organizasyon amacı,
- önerilen iç yapı,
- yalın pozisyonlar,
- ana süreçler,
- birleştirilen görev alanları,
- süreç sahipliği,
- görev sınırları,
- ölçekleme eşikleri

tanımlanmıştır.

### Başlıca kararlar

- Trafik Eğitim, Ulaşım Planlama altında birim olarak konumlandırılmıştır.
- TKM, AUS altında ayrı operasyon birimi olarak başlatılmıştır.
- Ruhsat ve ticari araç işlemleri Toplu Taşımadan ayrılmıştır.
- UKOME yalnız sekretarya, karar ve uygulama takibi odağında yapılandırılmıştır.
- İdari ve mali destek süreçleri merkezileştirilmiştir.

## 5.2. `10_yalin_pozisyon_gorev_tanimlari`

### Giderilen eksik

Pozisyon önerilerinin süreç adımları, yetki sınırları, çıktıları ve KPI'larıyla ilişkilendirilmemiş olması.

### Yapılan tasarım

Her pozisyon için:

- amaç,
- bağlılık,
- birim,
- ilgili süreç kodları,
- sorumlu süreç adımları,
- temel görevler,
- girdiler,
- çıktılar,
- yetki sınırları,
- koordinasyon ilişkileri,
- KPI,
- vekâlet ve görev ayrılığı

tanımlanmıştır.

### Yönetimsel katkı

Bu yapı, görev tanımlarını soyut unvan metni olmaktan çıkarıp süreç bazlı performans ve sorumluluk dokümanına dönüştürmüştür.

## 5.3. `14_yalin_organizasyon_semasi`

### Giderilen eksik

Şube müdürlüklerinin altında bulunacak birimlerin ve pozisyonların hiyerarşik ilişkisinin görünür olmaması.

### Yapılan tasarım

Ulaşım Dairesi Başkanı altında 8 şube müdürlüğü gösterilmiş; her şubenin altında önerilen birimler ve bu birimlerin altında yalın pozisyonlar yerleştirilmiştir.

### Yönetimsel katkı

- Şube–birim–pozisyon ilişkisi netleşmiştir.
- Personel görevlendirmesi için organizasyon altlığı oluşmuştur.
- Süreç sahipliği ile teşkilat yapısı birbirine bağlanmıştır.
- Hangi pozisyonun hangi birimde yer aldığı açık hale gelmiştir.

## 5.4. `15_yalin_surec_haritalari`

### Giderilen eksik

Süreç haritalarındaki adımların yalnız faaliyet olarak görünmesi; sorumlu pozisyon ve bağlı birim bilgisinin süreç üzerinde birlikte yer almaması.

### Yapılan tasarım

`11_yalin_surec_haritalari_sorumlulari_belirtilmis` içeriği yapısal olarak aynen korunmuş ve her Mermaid düğümünde:

- sorumlu pozisyon,
- bağlı organizasyon birimi

birlikte gösterilmiştir.

### Korunan unsurlar

- Süreç adımları
- Düğüm kimlikleri
- Karar noktaları
- Evet/Hayır dalları
- Ok yönleri
- Sıralama
- Kontroller
- KPI ve açıklama metinleri

### Yönetimsel katkı

Süreç haritası aynı zamanda operasyonel görev dağılımı ve organizasyon görünümü kazanmıştır.

## 5.5. `12_formlar`

### Giderilen eksik

Başvuru, kontrol, izin, karar, teslim, kabul, rapor ve kapanış kayıtlarının süreçlerle bütünleşik standart bir form setine sahip olmaması.

### Yapılan tasarım

Formlar şu gruplarda hazırlanmıştır:

- Trafik Planlama
- UKOME
- Toplu Ulaşım ve Ruhsat
- Akıllı Ulaşım ve TKM
- Otogar
- Trafik Eğitim
- İdari ve Mali İşler
- Ortak kontrol, teslim ve kapanış

Her formda:

- form kodu,
- bağlı süreç kodu,
- kullanıldığı süreç adımı,
- başvuru veya işlem alanları,
- ekler,
- kontrol listesi,
- karar/sonuç,
- imza,
- kayıt ve kapanış bölümü

bulunmaktadır.

### Yönetimsel katkı

- Fiziki form ile dijital kayıt arasında bağlantı kurulmuştur.
- Süreç kapanış kanıtı standartlaştırılmıştır.
- Eksik belge ve tekrar işlem riski azaltılmıştır.
- Denetim izi güçlendirilmiştir.

## 6. Temel eksik–çözüm eşleştirmesi

| Tespit edilen eksik | Kaynak | Üretilen çözüm |
|---|---|---|
| 8 şubeli modelin pozisyon yapısının ayrıntısız olması | 06 | 09_yalin_pozisyonlari |
| Pozisyonların süreç adımlarıyla bağlı olmaması | 05 + 06 | 10_yalin_pozisyon_gorev_tanimlari |
| Şube altı birimlerin tanımlı olmaması | 06 | 14_yalin_organizasyon_semasi |
| Süreç adımlarında sorumlu pozisyonun görünmemesi | 05 | 11 ve ardından 15_yalin_surec_haritalari |
| Süreç adımlarında bağlı birimin görünmemesi | 05 + 14 | 15_yalin_surec_haritalari |
| Başvuru ve çıktı formlarının standart olmaması | 05 + kaynak belgeler | 12_formlar |
| Ruhsat ile hizmet planlamasının karışması | 05 + 06 | Ruhsat şubesi ve ayrı süreç/pozisyon seti |
| UKOME'nin teknik işlere kayma riski | 05 + 06 | UKOME sekretarya ve karar takip modeli |
| AUS, TKM ve Planlama sınırlarının belirsizliği | 05 + 06 | Ayrı birimler, görev tanımları ve süreç sorumlulukları |
| Teknik süreç ile idari/mali dosya yönetiminin karışması | 05 + 06 | İdari ve Mali İşler merkezileştirmesi |
| Saha kabul, teslim ve kapanış kanıtlarının dağınık olması | 05 | 12_formlar ortak kontrol/teslim/kapanış seti |

## 7. Elde edilen bütünleşik işletim modeli

Oluşturulan çalışmalar birlikte değerlendirildiğinde şu zincir kurulmuştur:

```text
Süreç ihtiyacı
   ↓
Süreç haritası
   ↓
Süreç sahibi şube
   ↓
Şube altındaki birim
   ↓
Sorumlu yalın pozisyon
   ↓
Pozisyon görev tanımı
   ↓
Kullanılan başvuru/kontrol/karar/kapanış formu
   ↓
KPI, kayıt ve denetim kanıtı
```

Bu yapı sayesinde organizasyon şeması, görev tanımı, süreç haritası ve form seti birbirinden bağımsız dokümanlar olmaktan çıkarılmıştır.

## 8. Çalışmanın sınırları

Bu çalışmalar hedef işletim modeli taslağıdır. Aşağıdaki konular ayrıca doğrulanmalıdır:

- Norm kadro ve unvan uygunluğu
- Teşkilat yönetmeliği
- Yetki devri
- UKOME, Encümen ve Meclis yetkileri
- Mali mevzuat ve görev ayrılığı
- KVKK ve bilgi güvenliği
- İhale, muayene-kabul ve ödeme rolleri
- Personel iş yükü ve vardiya ihtiyacı
- Bilgi sistemleri ve EBYS entegrasyonu

## 9. Sonuç

`05_surec_haritalari` işin nasıl yürütüleceğini, `06_raporlar` ise nasıl bir organizasyon ayrışması gerektiğini ortaya koymuştur. Ancak uygulamaya geçiş için şube–birim–pozisyon–görev–süreç adımı–form ilişkilerinin tamamlanması gerekiyordu.

Bu nedenle:

- `09_yalin_pozisyonlari` organizasyonun yalın insan kaynağı modelini,
- `10_yalin_pozisyon_gorev_tanimlari` pozisyonların süreç bazlı görevlerini,
- `14_yalin_organizasyon_semasi` şube, birim ve pozisyon hiyerarşisini,
- `15_yalin_surec_haritalari` her adımın sorumlu pozisyon ve birimini,
- `12_formlar` süreçlerin belge, kontrol ve kapanış altyapısını

oluşturmuştur.

Sonuçta yalnız bir organizasyon önerisi değil; görevlerin, süreçlerin, sorumlulukların ve kayıtların birbiriyle uyumlu olduğu uygulanabilir bir yalın işletim modeli ortaya çıkarılmıştır.
