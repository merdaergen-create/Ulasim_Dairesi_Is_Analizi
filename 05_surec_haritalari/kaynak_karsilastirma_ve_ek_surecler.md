# Kaynak Belgeler ile Süreç Haritaları Karşılaştırması

**İnceleme kapsamı:** `01_kaynaklar` sınıflandırma yapısı, repodaki ham kaynak belge grupları ve `05_surec_haritalari` altındaki mevcut süreçler.  
**Amaç:** Kaynaklarda tanımlanan işlerden mevcut süreç haritalarında bağımsız biçimde gösterilmeyenleri belirlemek ve süreçleştirmek.

## İnceleme notu

`01_kaynaklar` dizini kaynakların hedef sınıflandırma yapısını göstermektedir. Ham kaynak belgeler repo içinde orijinal birim klasörlerinde korunmaktadır. Karşılaştırmada yönetmelik, yönerge, görev tanımı, form ve uygulama belgelerinin dosya adları ile mevcut süreçlerin kapsamı birlikte değerlendirilmiştir.

## Mevcut süreçlerle kapsanan kaynak işleri

Aşağıdaki iş grupları mevcut haritalarda yeterli düzeyde yer aldığı için yeni süreç oluşturulmamıştır:

- Ulaşım Ana Planı, yol ve kavşak projesi
- Geçiş yolu, yol kapatma ve yol daraltma
- Sinyalizasyon, yatay ve düşey işaretleme
- Trafik Yönetim Merkezi günlük operasyonu
- UKOME gündem, karar, dağıtım ve uygulama takibi
- Hat, güzergâh, sefer, zaman ve tarife planlama
- Toplu taşıma izleme, kontrol ve şikâyet yönetimi
- Durak yaşam döngüsü
- EDS/AUS kurulum, veri platformu, akıllı durak ve kamera görüntüsü teslimi
- Otogar giriş-çıkış, tahakkuk, tahsilat, peron, teknik tesis ve raporlama
- Trafik eğitimi ve eğitim parkı
- İhale, sözleşme, hakediş, ödeme, bütçe, EBYS, arşiv, taşınır ve doküman değişikliği

## Bağımsız süreç olarak eksik bulunan işler

| Yeni süreç | Eksikliğin nedeni | Eklendiği dosya |
|---|---|---|
| TP-07 Otopark erişim uygunluk belgesi | Yol ve kavşak projelerinden farklı olarak bireysel başvuru, mimari proje, erişim noktası, yaya güvenliği ve belge üretimi içeren ayrı izin süreci olması | `trafik_planlama/ek_surecler.md` |
| TU-06 Ticari plaka tahsis, devir ve iptal | Genel ruhsat sürecinden farklı hak sahipliği, kurul kararı, eski hakkın kapatılması ve plaka kaydı kontrolleri içermesi | `toplu_ulasim/ek_surecler.md` |
| TU-07 Servis aracı izin belgesi | Okul, personel, özel plaka ve müşteri servislerinde araç, sürücü, rehber, sözleşme ve güzergâh kontrollerinin farklılaşması | `toplu_ulasim/ek_surecler.md` |
| TU-08 Yük nakli ve özel taşıma izni | Taşıma türü, kapasite, güvenlik, güzergâh, süre ve kurum görüşü temelli özel izin akışı gerektirmesi | `toplu_ulasim/ek_surecler.md` |
| TU-09 Ticari araç uygunluk, çalışma ruhsatı ve vize | Araç muayenesi, uygunluk kontrol formu, tekrar kontrol ve süre yenileme adımlarının ayrı operasyon yükü oluşturması | `toplu_ulasim/ek_surecler.md` |
| ID-07 Taşıt görev emri ve hizmet aracı görevlendirme | Kurum içi araç-sürücü tahsisi, görev emri, kilometre-yakıt ve görev kapanışı kayıtlarının mevcut idari süreçlerde bulunmaması | `idari_isler/ek_surecler.md` |

## Ayrı süreç oluşturulmayan kaynak belgeler

Bazı kaynaklar yeni bir uçtan uca süreç değil, mevcut süreçlerin girdisi veya kontrol belgesidir:

- Otogar ücret tarifesi: `OT-01` için tarife girdisi
- Otogar araç ve gelir raporu formu: `OT-04` çıktısı
- Ticari araç uygunluk formu: `TU-09` kontrol kaydı
- Kamera görüntüsü teslim formu: `AU-04` teslim ve kapanış kaydı
- Yol daraltma günlük çalışma dilekçesi: `TP-03` başvuru girdisi
- Mevzuat PDF'leri: ilgili süreçlerin hukuki kontrol dayanağı
- Görev tanımları: süreç sahipliği ve RACI girdisi

## Uygulama ve doğrulama notu

Yeni süreçler hedef süreç taslağıdır. Süreç sahibi, belge adı, onay makamı, ücret/tarife, süre, kurul gereksinimi ve yaptırım adımları yürürlüğe alınmadan önce güncel Denizli Büyükşehir Belediyesi teşkilat düzenlemeleri, yetki devri, UKOME kararları ve Hukuk Müşavirliği görüşüyle doğrulanmalıdır.
