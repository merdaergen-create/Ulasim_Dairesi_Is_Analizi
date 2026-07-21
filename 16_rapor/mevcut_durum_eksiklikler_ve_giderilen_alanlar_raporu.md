# Ulaşım Dairesi Başkanlığı Mevcut Durum, Eksiklikler ve Giderilen Alanlar Raporu

## 1. Raporun amacı

Bu rapor, Ulaşım Dairesi Başkanlığı için hazırlanan mevcut durum analizi ile daha sonra geliştirilen yalın organizasyon, görev tanımı, süreç sorumluluğu ve form çalışmalarını tek bir gelişim çizgisi içinde açıklamak amacıyla hazırlanmıştır.

Raporun temel yaklaşımı şöyledir:

> **Mevcut durumun tespiti → eksiklik ve risklerin belirlenmesi → organizasyon, görev, süreç ve form katmanlarının birlikte tasarlanması.**

Bu kapsamda aşağıdaki dokümanlar birlikte değerlendirilmiştir:

- `06_raporlar/mevcut_durum_raporu.md`
- `06_raporlar/yonetici_ozeti.md`
- `10_yalin_pozisyon_gorev_tanimlari/README.md`
- `11_yalin_surec_haritalari_sorumlulari_belirtilmis/README.md`
- `12_formlar/README.md`
- `14_yalin_organizasyon_semasi/README.md`
- `15_yalin_surec_haritalari/README.md`

---

## 2. Mevcut durum neydi?

### 2.1. Güçlü fakat dağınık bir kaynak havuzu bulunuyordu

Ulaşım Dairesi Başkanlığına ait kaynak havuzunda yönetmelik, yönerge, prosedür, organizasyon şeması, görev tanımı, başvuru ve kontrol formu, iş akışı, personel faaliyet açıklaması, ihale-sözleşme-hakediş notları ve mevzuat dosyaları bulunuyordu.

Bu nedenle temel sorun kaynak eksikliği değildi. Asıl sorun, güçlü kaynak havuzunun tek bir süreç mimarisi, sahiplik modeli ve doküman yönetim standardı altında birleştirilmemiş olmasıydı.

Kaynakların önemli bölümü Word, PDF ve Excel biçimindeydi. Bu durum:

- metin içinde arama yapmayı,
- sürüm farklarını izlemeyi,
- aynı işin farklı belgelerde nasıl tanımlandığını karşılaştırmayı,
- görev ve süreç çakışmalarını görünür hale getirmeyi

zorlaştırıyordu.

Ayrıca kişi adıyla, belirsiz adlarla veya `(1)` benzeri eklerle tutulan dosyalar güncel sürümün belirlenmesini güçleştiriyordu.

### 2.2. Organizasyon ana ulaşım fonksiyonlarını kapsıyordu ancak görev sınırları net değildi

İlk analizde 38 resmî rol kataloglanmıştı. Yapı, ulaşım hizmetlerinin temel alanlarını kapsıyordu; ancak teknik görev, idari takip, kurul sekretaryası, veri sahipliği, sistem işletimi ve saha uygulaması bazı noktalarda birbirine karışmıştı.

Öne çıkan mevcut durum örnekleri:

- **Ulaşım Planlama**, ana planlama yanında sinyalizasyon, işaretleme, TKM, EDS, veri ve kimi idari görevleri de kapsayacak kadar genişlemişti.
- **AUS**, teknoloji, veri ve entegrasyon işlerini yürütürken trafik politikası ve saha kararlarıyla sınırı yeterince belirgin değildi.
- **Toplu Taşıma**, hat-güzergâh-zaman-tarife ile ruhsat-vize-izin işlerini aynı yapı içinde yürütüyordu.
- **UKOME**, kurul ve karar sekretaryasının yanında teknik iş sahibi gibi algılanabilecek bir konumdaydı.
- **İdari İşler** ile teknik şubeler arasında ihale, sözleşme, hakediş, ödeme, taşınır ve evrak görevlerinde paralel takip riski bulunuyordu.
- **TKM**, teknoloji platformu, saha cihazı ve günlük 7/24 operasyon arasında açık görev ayrımına sahip değildi.

### 2.3. Süreçler belirlenmişti fakat kurumsal standart tam değildi

İlk envanter sonucunda 44 ana süreç belirlenmişti. Süreçlerin çoğu için girdi veya çıktı belgeleri bulunmasına rağmen aşağıdaki unsurlar ortak standarda bağlanmamıştı:

- süreç başlangıcı,
- tek hesap verebilir sahip,
- faaliyet bazlı sorumlu kişi,
- karar ve onay noktası,
- işlem süresi veya SLA,
- kapanış kanıtı,
- KPI,
- görev ayrılığı,
- kişisel veri ve bilgi güvenliği kontrolü.

Bu nedenle bir işin akışının bilinmesi, o işin hangi pozisyon ve hangi organizasyon birimi tarafından yürütüleceğinin açık olduğu anlamına gelmiyordu.

### 2.4. Formlar vardı ancak süreçle bütünleşik bir form sistemi bulunmuyordu

Başvuru ve kontrol işlemlerinde kurumsal formlar kullanılıyordu. Buna rağmen formlar arasında ortak bir tasarım standardı bulunmuyordu.

Özellikle şu alanlarda eksiklik vardı:

- formun hangi süreç koduna bağlı olduğunun gösterilmemesi,
- hangi süreç adımında kullanıldığının belirtilmemesi,
- başvuru, kontrol, karar, kabul, teslim ve kapanış belgelerinin ortak yapıda olmaması,
- tekrar eden bilgilerin farklı formlarda yeniden istenmesi,
- fiziksel form ile EBYS veya iş takip kaydının ilişkilendirilmemesi,
- kişisel veri, plaka, kamera ve konum bilgilerinin erişim ve saklama kurallarının form tasarımına yansıtılmaması.

### 2.5. Kritik mükerrerlik ve sorumluluk boşlukları bulunuyordu

Mevcut durum ve yönetici özeti aşağıdaki kritik alanları öne çıkarmıştı:

- EDS ve TKM görevlerinin Planlama, AUS ve Trafik Yönetim arasında karışması,
- Planlama, AUS ve Toplu Taşımanın ayrı veri setleri üretmesi; ortak veri sözlüğü ve sahiplik modelinin bulunmaması,
- toplu taşıma hizmet planlamasıyla genel ulaşım ve yol kapasitesi planlamasının karışması,
- durak ihtiyacı, yer seçimi, montaj, bakım ve dijital ekipmanın farklı birimlere dağılması,
- teknik şubelerle İdari İşlerin ihale ve sözleşme takibini paralel yürütmesi,
- taşınır ve ambar kayıtlarının birden fazla yerde tutulma riski,
- şubeler bazında paralel evrak ve arşiv kayıtları,
- UKOME kararlarının uygulama ve kapanışının sistematik izlenmemesi.

---

## 3. Mevcut durumun temel eksiklikleri

### 3.1. Tek hesap verebilir süreç sahibi eksikliği

Bir sürecin birden fazla birim tarafından sahiplenilmesi veya hiçbir birimin nihai hesap verebilirliğinin açık olmaması, gecikme ve sorumluluk boşluğu yaratıyordu.

Yönetici özetinde önerilen ana ilke şuydu:

> Her sürecin yalnız bir hesap verebilir sahibi olmalı; diğer birimler RACI yöntemiyle sürece katılmalıdır.

Ancak bu ilkenin pozisyon ve süreç adımı seviyesinde uygulanmış bir karşılığı henüz yoktu.

### 3.2. Pozisyon görevlerinin süreç adımlarıyla ilişkilendirilmemesi

Mevcut görev tanımları unvan bazlı görev listeleri sunuyordu. Fakat şu sorular her zaman açık cevaplanamıyordu:

- Bu pozisyon hangi sürecin hangi adımını yürütür?
- Hangi çıktıyı üretir?
- Yetki sınırı nedir?
- Hangi birimlerle koordinasyon kurar?
- Performansı hangi göstergeyle ölçülür?
- Vekâlet veya görev devri nasıl yapılır?

### 3.3. Organizasyon şemasında birim ve pozisyon bağlantısının eksikliği

Şube müdürlükleri bilinse de şube altındaki önerilen birimler ve bu birimlerde konumlanacak pozisyonlar bütünleşik bir organizasyon şemasında gösterilmiyordu.

Bu durum özellikle şu alanlarda sorun yaratıyordu:

- pozisyonun bağlı olduğu birimin belirsizliği,
- benzer uzmanlıkların hangi birimde toplanacağının net olmaması,
- birim kurma veya birleştirme kararlarının süreçlere dayanmaması,
- kadro planlamasının iş yükü yerine tarihsel unvanlara göre yapılması riski.

### 3.4. Süreç diyagramlarında sorumlu pozisyon ve birim görünürlüğünün olmaması

Süreç haritalarında faaliyetler, karar noktaları ve oklar bulunmasına rağmen ilk aşamada adımların yanında doğrudan sorumlu pozisyon yer almıyordu.

Daha sonra pozisyon eklense bile organizasyon birimi bilgisi görünür değildi. Bu nedenle bir adımı kimin yaptığı bilinse de o kişinin hangi birim adına hareket ettiği süreç diyagramından doğrudan anlaşılamıyordu.

### 3.5. Formların süreç kontrol aracı olarak tasarlanmamış olması

Formların yalnız başvuru veya kayıt belgesi olarak görülmesi; karar, kontrol, teknik kabul, teslim ve süreç kapanış kanıtı rollerinin yeterince standartlaşmamasına yol açıyordu.

Bu eksiklik özellikle:

- teknik kabul,
- saha kontrolü,
- UKOME karar uygulama takibi,
- ruhsat ve izin dosyaları,
- kamera görüntüsü teslimi,
- otogar kasa ve tahakkuk mutabakatı,
- ihale ve hakediş kontrolü

gibi denetim izi gerektiren süreçlerde önemliydi.

### 3.6. Görev ayrılığı ve mevzuat kontrolünün operasyonel dokümanlara yansımaması

Mevcut raporlarda kamu ihale, sözleşme, ödeme, taşınır, kamera/plaka/konum verisi, erişilebilirlik ve İSG konularında görev ayrılığı ihtiyacı belirtilmişti.

Ancak bu gerekliliklerin:

- görev tanımına,
- süreç adımına,
- organizasyon birimine,
- forma ve imza alanına

birlikte yansıtılması gerekiyordu.

---

## 4. Eksiklikleri nasıl giderdik?

Çözüm tek bir dokümanla değil, birbirini tamamlayan beş katmanla geliştirildi.

```text
Mevcut durum ve yönetici özeti
        ↓
Yalın pozisyon ve görev tanımı
        ↓
Sorumlusu belirtilmiş süreç haritası
        ↓
Yalın organizasyon şeması
        ↓
Pozisyonu ve birimi belirtilmiş süreç haritası
        ↓
Süreç adımına bağlı standart form seti
```

### 4.1. Yalın pozisyon görev tanımlarıyla görevler somutlaştırıldı

`10_yalin_pozisyon_gorev_tanimlari` çalışması, 8 şubeli yalın organizasyondaki pozisyonların görevlerini `05_surec_haritalari` içindeki gerçek süreç adımları üzerinden tanımladı.

Her pozisyon için ortak bir standart oluşturuldu:

- amaç,
- organizasyonel bağlılık,
- bağlı olduğu birim,
- sorumlu süreçler,
- süreç adımları,
- görevler,
- girdiler,
- çıktılar,
- yetki sınırları,
- koordinasyon ilişkileri,
- performans göstergeleri,
- vekâlet ilkeleri.

Böylece genel görev ifadeleri, ölçülebilir ve süreçle ilişkili sorumluluklara dönüştürüldü.

Bu çalışma şu eksikleri giderdi:

- unvanın ne yaptığına ilişkin belirsizlik,
- teknik ve idari görevlerin aynı pozisyonda toplanması,
- yetki sınırı eksikliği,
- performans ve çıktı tanımının bulunmaması,
- görev devri ve vekâlet belirsizliği.

### 4.2. Süreç adımlarına sorumlu pozisyon eklendi

`11_yalin_surec_haritalari_sorumlulari_belirtilmis` çalışmasında `05_surec_haritalari` yapısal olarak aynen korundu.

Süreç adımları, karar noktaları, sıra ve ok yönleri değiştirilmeden yalnızca her Mermaid düğümüne:

```text
Sorumlu: İlgili yalın pozisyon
```

bilgisi eklendi.

Bu yöntemle:

- süreç haritası görev tanımıyla bağlandı,
- her adımın işi yapan pozisyonu görünür oldu,
- süreç sahibinin yanında operasyonel sorumlular ayrıştırıldı,
- bir adımın sahipsiz veya mükerrer kalıp kalmadığı kontrol edilebilir hale geldi.

### 4.3. Yalın organizasyon şemasıyla şube–birim–pozisyon ilişkisi kuruldu

`14_yalin_organizasyon_semasi` çalışması; süreç haritaları, yalın pozisyonlar, görev tanımları, sorumluluk atanmış süreçler ve formlar birlikte değerlendirilerek oluşturuldu.

Şema üç seviyeyi görünür hale getirdi:

1. Ulaşım Dairesi Başkanı,
2. 8 şube müdürlüğü,
3. şubelerin altındaki birimler ve bu birimlerdeki yalın pozisyonlar.

Böylece yalnız “hangi unvan var?” sorusuna değil, “bu unvan hangi birimde ve hangi süreç kümesini yönetiyor?” sorusuna da cevap verildi.

Bu çalışma şu eksikleri giderdi:

- şube altı birimlerin görünür olmaması,
- pozisyonların organizasyon içinde konumlandırılamaması,
- görev sınırlarının yalnız metin içinde kalması,
- birimlerin tarihsel alışkanlıkla değil süreç sahipliğiyle kurulması ihtiyacı.

### 4.4. Süreç adımlarına birim bilgisi eklendi

`15_yalin_surec_haritalari`, `11_yalin_surec_haritalari_sorumlulari_belirtilmis` içeriğini yapısal olarak koruyarak mevcut `Sorumlu:` bilgisinin yanına:

```text
Birim: İlgili organizasyon birimi
```

bilgisini ekledi.

Bu sayede her süreç adımında üç bilgi birlikte görülür hale geldi:

- yapılan iş,
- sorumlu pozisyon,
- pozisyonun bağlı olduğu birim.

Bu çalışma özellikle birden fazla şubenin katıldığı süreçlerde kurumsal sınırı netleştirdi. Örneğin Planlama, AUS, Toplu Taşıma, UKOME ve İdari-Mali İşlerin aynı akışta yer aldığı durumlarda görev aktarım noktaları görünür hale geldi.

### 4.5. Standart form setiyle süreç kanıtı ve kapanış düzeni oluşturuldu

`12_formlar` çalışması, süreç haritalarındaki ihtiyaçlar ile mevcut başvuru, kontrol, izin, teslim ve raporlama belgelerini karşılaştırarak oluşturuldu.

Her form doğrudan doldurulabilir şablon biçiminde tasarlandı ve şu alanları içerdi:

- bağlı süreç kodu,
- kullanıldığı süreç adımı,
- başvuru veya işlem alanları,
- kontrol listesi,
- sonuç veya karar,
- ekler,
- sorumlu birim,
- imza,
- kapanış kaydı.

Form seti sekiz ana grupta düzenlendi:

- Trafik Planlama,
- UKOME,
- Toplu Ulaşım ve Ruhsat,
- AUS ve TKM,
- Otogar,
- Trafik Eğitim,
- İdari ve Mali İşler,
- Ortak Kontrol, Teslim ve Kapanış.

Mevcut `D37.FR` formlarının doğrudan iptal edilmesi önerilmedi. Yeni şablonlarla karşılaştırılarak revize edilmesi, mükerrer formların birleştirilmesi ve kurumsal kodlama sistemine bağlanması önerildi.

Fiziki form kullanılmaya devam edilse bile kayıt numarasının EBYS veya ilgili iş takip sisteminden üretilmesi ilkesi getirildi.

---

## 5. Eksik–çözüm eşleştirme tablosu

| Mevcut eksiklik | Oluşturulan çözüm | Sağlanan sonuç |
|---|---|---|
| Bir sürecin birden fazla hesabı verilebilir sahibi olması | Yalın görev tanımları ve sorumlulu süreç haritaları | Sorumlu pozisyon ve yetki sınırı görünür hale geldi |
| Görev tanımlarının genel ve süreçten kopuk olması | `10_yalin_pozisyon_gorev_tanimlari` | Görevler süreç adımı, çıktı, KPI ve yetki sınırıyla tanımlandı |
| Şube altında birimlerin ve pozisyonların gösterilmemesi | `14_yalin_organizasyon_semasi` | Şube–birim–pozisyon hiyerarşisi oluşturuldu |
| Süreç adımlarında işi yapan kişinin belli olmaması | `11_yalin_surec_haritalari_sorumlulari_belirtilmis` | Her adıma sorumlu pozisyon eklendi |
| Sorumlu pozisyonun hangi birim adına çalıştığının görünmemesi | `15_yalin_surec_haritalari` | Her adıma bağlı birim bilgisi eklendi |
| Formların süreçle bağlantısının gösterilmemesi | `12_formlar` | Her forma süreç kodu ve kullanıldığı süreç adımı eklendi |
| Başvuru, kontrol, kabul ve kapanış kayıtlarının farklı yapıda olması | Ortak form standardı | Denetim izi ve kapanış kanıtı güçlendirildi |
| Teknik ve idari rollerin karışması | Görev tanımları, organizasyon şeması ve birimli süreçler | Teknik iş sahipliği ile dosya, sözleşme ve ödeme takibi ayrıştırıldı |
| UKOME’nin teknik iş sahibi gibi algılanması | UKOME görev tanımı ve süreç sorumluluğu | UKOME sekretarya, karar, dağıtım ve kapanış takibiyle sınırlandı |
| Ruhsat ve toplu taşıma planlamasının aynı yapı içinde karışması | Ayrı Ruhsat ve Ticari Araç şube/birim yapısı | Hizmet planı ile izin-belge süreçleri ayrıştırıldı |
| AUS, TKM ve Planlama sınırlarının belirsizliği | Ayrı pozisyon, birim ve süreç sorumlulukları | Politika, teknoloji, saha ve operasyon görevleri ayrıldı |
| Fiziki form ile dijital kayıt arasında bağ olmaması | Form tasarım ilkeleri | EBYS/iş takip numarası ve kayıt bütünlüğü önerildi |
| Kişisel veri ve operasyonel veri kontrollerinin dağınık olması | Görev tanımı, süreç kontrolü ve form alanları | Erişim, saklama, paylaşım ve log kontrolleri görünür hale getirildi |

---

## 6. Önce–sonra karşılaştırması

### Önce

- Kaynaklar kapsamlı fakat dağınıktı.
- Süreçler vardı ancak ortak süreç standardı tam değildi.
- Görev tanımları süreç adımlarına bağlanmamıştı.
- Sorumlu pozisyonlar süreç haritasında görünmüyordu.
- Pozisyonların bağlı olduğu birimler açık değildi.
- Organizasyon şeması süreç sahipliğini tam yansıtmıyordu.
- Formlar süreç kodu ve adımıyla ilişkilendirilmemişti.
- Teknik, idari, kurul ve sistem sahipliği rolleri karışabiliyordu.

### Sonra

- Yalın pozisyon görev tanımları süreç adımlarına göre oluşturuldu.
- Her pozisyonun amacı, görevi, çıktısı, yetki sınırı ve KPI’ı tanımlandı.
- Süreç diyagramlarına sorumlu pozisyon eklendi.
- Şube altında birimler ve bu birimlerdeki pozisyonlar gösterildi.
- Süreç diyagramlarına birim bilgisi eklendi.
- Başvuru, kontrol, kabul, teslim ve kapanış formları standartlaştırıldı.
- Formlar ilgili süreç kodu ve süreç adımıyla ilişkilendirildi.
- UKOME, Planlama, AUS/TKM, Ruhsat, Toplu Taşıma ve İdari-Mali İşler arasındaki sınırlar daha açık hale getirildi.

---

## 7. Kurumsal kazanımlar

Hazırlanan çalışmaların birlikte uygulanması halinde aşağıdaki kazanımlar beklenmektedir:

- tek hesap verebilir süreç sahipliği,
- görev ve yetki sınırlarının netleşmesi,
- mükerrer işlerin azalması,
- iş aktarım noktalarının görünür hale gelmesi,
- karar ve işlem sürelerinin ölçülebilmesi,
- süreç bazlı kadro ve iş yükü planlaması,
- denetim izi ve kapanış kanıtının güçlenmesi,
- fiziksel ve dijital kayıt bütünlüğü,
- UKOME kararlarının daha etkin izlenmesi,
- ihale, sözleşme, kabul ve ödeme görev ayrılığının güçlenmesi,
- kamera, plaka, konum ve personel verilerinde erişim kontrolünün iyileşmesi,
- üst yönetime KPI ve süreç performans raporu üretilebilmesi.

---

## 8. Tamamlanmayan veya yürürlüğe alma öncesinde doğrulanması gereken alanlar

Hazırlanan dokümanlar hedef işletim modeli niteliğindedir. Aşağıdaki çalışmalar tamamlanmadan doğrudan bağlayıcı uygulamaya geçilmemelidir:

1. Teşkilat yönetmeliği ve norm kadro uygunluk incelemesi
2. Pozisyon unvanları ve atama şartlarının İnsan Kaynaklarıyla doğrulanması
3. Yetki devri ve imza yetkileri düzenlemesi
4. 4734, 4735 ve 5018 kapsamındaki görev ayrılığının Hukuk ve Mali Hizmetlerle kontrolü
5. Mevcut `D37.FR` formlarının yeni form setiyle karşılaştırılması
6. Form kodu, revizyon numarası, yürürlük tarihi ve saklama süresinin belirlenmesi
7. Kamera, plaka, konum ve iletişim verileri için KVKK ve bilgi güvenliği değerlendirmesi
8. Süreç sahibi, SLA ve KPI değerlerinin gerçek iş yükü verileriyle doğrulanması
9. UKOME, ruhsat, saha iş emri ve teknik kabul süreçlerinde pilot uygulama
10. Süreç haritası, görev tanımı, organizasyon şeması ve form revizyonlarının birlikte yönetileceği doküman kontrol düzeni

---

## 9. Sonuç

Başlangıçta Ulaşım Dairesi Başkanlığının temel sorunu iş veya belge eksikliği değildi. Temel sorun; mevcut belgelerin, görevlerin ve iş akışlarının ortak bir organizasyon, süreç sahipliği, pozisyon sorumluluğu ve form standardı altında bütünleştirilmemiş olmasıydı.

Hazırlanan çalışmalar bu eksikliği katmanlı biçimde giderdi:

- `10_yalin_pozisyon_gorev_tanimlari` ile pozisyonların ne yapacağı,
- `11_yalin_surec_haritalari_sorumlulari_belirtilmis` ile süreç adımını kimin yürüteceği,
- `14_yalin_organizasyon_semasi` ile pozisyonun hangi birimde yer alacağı,
- `15_yalin_surec_haritalari` ile süreçte hangi pozisyon ve birimin sorumlu olduğu,
- `12_formlar` ile işlemin hangi belge ve kapanış kanıtıyla kayıt altına alınacağı

birbirine bağlandı.

Böylece dağınık belge ve görev yapısından, süreç–pozisyon–birim–form bütünlüğüne dayanan izlenebilir bir hedef işletim modeli oluşturuldu.
