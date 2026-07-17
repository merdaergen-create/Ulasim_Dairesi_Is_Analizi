# Mevcut Durum Raporu

**Sürüm:** Rev-A  
**Tarih:** 17 Temmuz 2026

## 1. Raporun kapsamı

Bu rapor, GitHub deposunda bulunan Ulaşım Dairesi kaynaklarının yapısını ve bu kaynaklardan görülen organizasyon, görev, süreç, mükerrerlik, veri yönetimi ve mevzuat durumunu değerlendirir.

## 2. Kaynak havuzunun durumu

Repo; Akıllı Ulaşım Sistemleri, Otogar, Toplu Ulaşım, Trafik Eğitim, Trafik Planlama, UKOME ve İdari İşler alanlarında çok sayıda Word, PDF ve Excel belgesi içermektedir. Kaynak türleri şunlardır:

- Teşkilat yönetmeliği ve şube yönergeleri
- Başkanlık prosedürü
- Organizasyon şeması
- Görev tanımları
- Başvuru ve kontrol formları
- İş akışları
- Personel faaliyet açıklamaları
- İhale, sözleşme, hakediş ve mali süreç notları
- Kanun ve teknik standart PDF’leri

Kaynak kapsamı güçlüdür; ancak depo başlangıçta yalnız ham belge havuzu niteliğindedir. Doküman envanteri, sürüm takibi, metodoloji, gizlilik sınıflandırması ve analiz çıktıları bulunmamaktaydı.

## 3. Doküman yönetimi bulguları

### 3.1 Binary dosya yoğunluğu

Belgelerin büyük bölümü Word, PDF ve Excel formatındadır. Bu durum GitHub üzerinde metin araması, sürüm farkı ve değişiklik incelemesini zorlaştırır. Kaynakların doğrulanmış Markdown metin karşılıkları oluşturulmalıdır.

### 3.2 Dosya adları ve kopyalar

Kişi adıyla, `(1)` ekiyle, `2` ifadesiyle veya belirsiz adlarla tutulan dosyalar vardır. Aynı veya benzer içeriğin birden fazla klasörde bulunması güncel sürümün belirlenmesini zorlaştırmaktadır.

### 3.3 Mevzuat güncelliği

Mevzuat PDF’leri yalnız numarayla adlandırılmıştır. Her dosya için resmî kaynak bağlantısı, konsolide metin tarihi, son kontrol tarihi ve ilgili süreçler eklenmelidir.

### 3.4 Gizlilik ve kişisel veri

Personel isimli çalışma raporları, kamera görüntüsü teslimi, EDS, trafik kontrol merkezi ve ağ/sistem belgeleri erişim sınıflandırması gerektirir. Repo özel olsa bile rol bazlı erişim ve paylaşım politikası tanımlanmalıdır.

## 4. Organizasyon ve görev durumu

38 resmî rol kataloglanmıştır. Genel yapı ulaşım hizmetlerinin ana fonksiyonlarını kapsamaktadır; ancak bazı süreçlerde teknik görev, idari takip, kurul sekretaryası ve sistem sahipliği birbirine karışmıştır.

### 4.1 Ulaşım Planlama

Ulaşım Ana Planı, trafik planlama, yol/kavşak tasarımı, işaretleme, sinyalizasyon ve trafik yönetimi gibi geniş bir görev alanına sahiptir. Bazı belgelerde EDS, veri ve taşınır görevlerinin de eklenmesi birimin sınırlarını gereğinden fazla genişletmektedir.

### 4.2 Akıllı Ulaşım Sistemleri

AUS, EDS, veri, entegrasyon, akıllı durak/otopark ve sürdürülebilir ulaşım teknolojilerini kapsar. Trafik politikasının ve saha kararının değil; teknoloji mimarisi, veri platformu ve entegrasyonun sahibi olarak netleştirilmelidir.

### 4.3 Toplu Taşıma

Hat, güzergâh, zaman, tarife, ruhsat, vize ve kontrol görevleri bulunmaktadır. Genel ulaşım planlamasıyla sınır, yol kapasitesi ve geometrik uygunluk üzerinden belirlenmelidir.

### 4.4 Ulaşım Koordinasyon / UKOME

UKOME gündem, alt komisyon, karar, imza, dağıtım ve uygulama takibinin sahibidir. Teknik proje veya hizmet sürecinin sahibi olmamalıdır. Teknik teklif ilgili şube tarafından hazırlanmalı; Koordinasyon dosya kalite kapısı ve kurul sekretaryası olmalıdır.

### 4.5 Otogar

Giriş-çıkış, tahakkuk-tahsilat, peron ve günlük işletme görevleri açıktır. Teknik bakım, temizlik, güvenlik ve ortak tesis hizmetleri ise 2026 değişiklikleri sonrasında Otogar ile Destek Hizmetleri arasında yeniden tanımlanmalıdır.

### 4.6 Trafik Eğitim

Görev alanı diğer şubelere göre daha nettir. Eğitim programları yalnız faaliyet sayısıyla değil, risk grubu, ön/son değerlendirme ve davranış etkisi göstergeleriyle ölçülmelidir.

### 4.7 İdari İşler

Evrak, bütçe, faaliyet raporu, ihale/sözleşme idari dosyası, ödeme ve taşınır süreçlerini yürütür. Teknik şubelerde bulunan paralel idari görevlerin merkezileştirilmesi gereklidir.

## 5. Süreç durumu

Rev-A aşamasında 44 ana süreç belirlenmiştir. En yüksek öncelikli süreçler şunlardır:

- Ulaşım Ana Planı
- Yol/kavşak ve geometrik düzenleme
- Geçiş yolu ve geçici yol kapatma
- UKOME gündem, karar ve kapanış
- Sinyalizasyon kurulumu ve bakımı
- Trafik Kontrol Merkezi operasyonu
- EDS/AUS tasarım ve entegrasyonu
- Toplu taşıma hat, güzergâh, zaman ve tarife
- Ruhsat, vize, izin ve denetim
- Durak yaşam döngüsü
- Otogar gelir ve peron yönetimi
- İhale, sözleşme, hakediş ve kabul
- Bütçe, faaliyet, evrak ve taşınır
- Kamera görüntüsü talep ve teslimi

Süreçlerin büyük kısmında girdi ve çıktı belgeleri mevcuttur; ancak başlangıç, karar, onay, süre, kapanış ve KPI alanları ortak bir standarda bağlı değildir.

## 6. Mükerrerlik ve görev sınırı bulguları

### EDS/TKM

Planlama ile AUS arasında ihtiyaç, kurulum, entegrasyon, bakım ve operasyon rolleri net ayrılmamıştır.

### Veri ve analiz

Planlama, AUS ve Toplu Taşıma kendi verilerini üretmekte; ortak veri sözlüğü, tekil kimlik, kalite kuralı ve sahiplik matrisi bulunmamaktadır.

### Toplu taşıma planlaması

Hat ve hizmet planlaması ile yol/kapasite planlaması aynı “planlama” ifadesi altında karışabilmektedir.

### Durak

İhtiyaç, yer seçimi, montaj, bakım ve dijital ekipman farklı birimlere dağılmıştır; tek yaşam döngüsü yoktur.

### İhale ve sözleşme

Teknik şubeler ile İdari İşler aynı sürecin takibini paralel yapabilmektedir. Teknik ve idari kayıt ayrılmalıdır.

### Taşınır

Planlama ve İdari İşlerde paralel ambar/kayıt sorumluluğu riski bulunmaktadır.

### Evrak ve arşiv

Tek EBYS kayıt noktası yerine şube bazlı paralel kayıtlar oluşabilir.

## 7. Mevzuat uyumu açısından mevcut durum

### Güçlü yönler

- İlgili temel kanunların çoğu kaynak havuzunda bulunmaktadır.
- Şubelerin görevleri yönetmelik ve yönergelerle tanımlanmıştır.
- Başvuru ve kontrol süreçlerinde kurumsal formlar kullanılmaktadır.

### Geliştirilmesi gereken alanlar

- Mevzuat dosyalarının güncellik ve konsolidasyon kontrolü
- Yönetmelik değişikliklerinin alt yönerge ve görevlere yansıtılması
- Denetim ve yaptırımda yetki sınırı
- Kamu ihale, sözleşme, ödeme ve taşınırda görev ayrılığı
- Kamera ve konum verilerinde KVKK, log ve saklama-imha
- Erişilebilirlik kriterlerinin proje ve kabul kontrol listelerine eklenmesi
- Saha işlerinde İSG kapısı ve kanıt kaydı

## 8. Diğer büyükşehirlerle karşılaştırma

İstanbul’da UKOME sekretaryası karar süreçlerine odaklanmaktadır. Ankara’da planlama, trafik kontrol, sinyalizasyon, ruhsat ve idari işler daha belirgin işlevlere ayrılmıştır. Kocaeli’de AUS ve sürdürülebilir ulaşım ayrı bir teknik sahiplik alanı olarak ele alınmakta; planlama çalışmalarında veri, erişilebilirlik, model ve etki analizi kullanılmaktadır.

Denizli’nin mevcut yapısı bu modellerle uyumlu hale getirilebilir. Bunun için ilk aşamada yeni teşkilat kurmak yerine süreç sahipliği, hizmet kataloğu, RACI, SLA ve veri sahipliği açıklaştırılmalıdır.

## 9. Mevcut riskler

| Risk | Etki | Öncelik |
|---|---|---|
| Bir sürecin birden fazla hesap verebilir sahibi olması | Gecikme, sorumluluk boşluğu | Kritik |
| Güncel olmayan yönerge ve görev tanımları | Yetki ve uyum riski | Kritik |
| Teknik ve idari kayıtların paralel tutulması | Mükerrer iş, veri tutarsızlığı | Yüksek |
| Kişisel/operasyonel verinin sınıflandırılmaması | KVKK ve güvenlik riski | Kritik |
| Varlıkların farklı listelerde tutulması | Bakım ve yatırım hatası | Yüksek |
| UKOME kararının kapanışının izlenmemesi | Kararın uygulanmaması | Yüksek |
| Manuel veri ve rapor toplama | Zaman kaybı, hata | Yüksek |

## 10. Sonuç

Kaynak seti kapsamlı ve analiz için yeterlidir. Temel sorun kaynak eksikliği değil; belgelerin tek bir süreç mimarisi, sahiplik modeli, mevzuat matrisi ve veri standardı altında birleştirilmemiş olmasıdır. Öncelik, mevcut görevlerin RACI ile netleştirilmesi ve 44 ana sürecin standart süreç kimlik kartlarıyla yönetilmesidir.
