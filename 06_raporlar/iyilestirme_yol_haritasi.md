# İyileştirme Yol Haritası

**Sürüm:** Rev-A  
**Başlangıç:** Temmuz 2026  
**Hedef dönem:** 12 ay

## 1. Hedef

Ulaşım Dairesindeki görev ve süreçleri tek sahiplik, mevzuat uyumu, ölçülebilir performans, ortak veri ve dijital iş akışı ilkeleriyle yeniden düzenlemek.

## 2. Uygulama ilkeleri

1. Bir süreçte yalnız bir **A — hesap verebilir sahip** bulunur.
2. Teknik karar ile idari dosya takibi ayrılır.
3. UKOME teknik iş sahibi değil karar ve sekretarya sahibidir.
4. Veri sahibi ile bilgi sistemi sahibi açıkça ayrılır.
5. Kaynak belgeler silinmeden önce envanter, sürüm ve gizlilik kontrolü yapılır.
6. Mevzuat ve görev değişiklikleri Hukuk Müşavirliği tarafından doğrulanır.
7. Dijitalleştirme, hatalı veya mükerrer süreci otomatikleştirmek yerine önce süreci sadeleştirir.

## 3. Faz 0 — Yönetişim ve acil kontroller

**Süre:** 0–30 gün

| İş paketi | Ana sahip | Çıktı | Başarı ölçütü |
|---|---|---|---|
| Proje yürütme kurulu kurulması | Daire Başkanlığı | Karar ve toplantı düzeni | Sahipler ve karar yetkileri yazılı |
| 2026/419 etki analizi | İdari İşler + Hukuk | Etkilenen yönetmelik/yönerge/görev listesi | Tüm alt belgeler için aksiyon atanmış |
| Geçici RACI yayımlanması | Daire Başkanlığı | EDS/TKM, ihale, taşınır, durak, planlama RACI’si | Kritik çakışmalar için tek A belirlenmiş |
| Bilgi sınıflandırması | İdari İşler + Bilgi İşlem | Kamuya açık/kurum içi/kişisel/hassas sınıfları | Repodaki kaynakların tamamı etiketlenmiş |
| Mevzuat doğrulama yöntemi | Hukuk + İdari İşler | Resmî bağlantı ve kontrol tarihi standardı | Her mevzuat kaydında güncellik alanı |

## 4. Faz 1 — Envanter ve süreç standardı

**Süre:** 30–90 gün

### 4.1 Doküman envanteri

- Bütün belgeler kod, ad, birim, tür, revizyon, tarih, kaynak yolu ve gizlilik sınıfıyla kaydedilir.
- Kopya ve eski sürümler işaretlenir; hiçbir dosya onaysız silinmez.
- Word ve PDF kaynakların doğrulanmış Markdown metinleri hazırlanır.

### 4.2 Görev envanteri

- 38 rolün görevleri madde bazında çıkarılır.
- Her görev bir veya daha fazla süreç ID’sine bağlanır.
- Yetki, onay, kayıt ve KPI alanları görev tanımlarına eklenir.

### 4.3 Süreç kimlik kartları

44 süreç için şu alanlar doldurulur:

- Amaç ve kapsam
- Tetikleyici
- Girdiler
- Adımlar ve karar noktaları
- RACI
- Çıktılar ve kayıtlar
- Mevzuat
- SLA
- KPI
- Risk ve kontrol
- Kişisel veri ve saklama süresi

**Faz kabul kriteri:** 44 sürecin en az yüzde 80’i süreç sahibi ve ilgili paydaşlarca doğrulanmış olmalıdır.

## 5. Faz 2 — Kritik süreçlerin yeniden tasarımı

**Süre:** 60–150 gün

### 5.1 UKOME

Hedef akış:

`Teknik teklif → belge tamlık kontrolü → alt komisyon → gündem → karar → e-imza → dağıtım → uygulama kanıtı → kapanış`

KPI:

- Eksik dosya oranı
- Gündeme alınma süresi
- Karar imza süresi
- Süresinde kapanan karar oranı

### 5.2 EDS ve Trafik Kontrol Merkezi

- Planlama trafik ihtiyacı ve saha kararının sahibi
- AUS sistem, veri ve entegrasyon sahibi
- Trafik Yönetim günlük operasyon sahibi
- Bilgi İşlem siber güvenlik ve kurumsal altyapı paydaşı

KPI:

- Sistem kullanılabilirliği
- Arıza giderme süresi
- Veri kalite skoru
- Kaza/ihlal etkisi

### 5.3 Toplu taşıma

- Hat, güzergâh, zaman ve tarife: Toplu Taşıma
- Yol kapasitesi ve geometrik uygunluk: Ulaşım Planlama
- Karar: UKOME
- Canlı filo ve yolcu bilgisi platformu: AUS

KPI:

- Sefer düzenliliği
- Doluluk ve kapasite dengesi
- Başvuru/şikâyet kapanış süresi
- Hat değişikliği sonrası etki

### 5.4 Durak yaşam döngüsü

`İhtiyaç → trafik ve erişilebilirlik kontrolü → UKOME → fiziksel montaj → dijital ekipman → ortak kabul → tek varlık kaydı → bakım`

KPI:

- Erişilebilir durak oranı
- Arıza SLA’sı
- Envanter doğruluk oranı
- Gerçek zamanlı bilgi kullanılabilirliği

### 5.5 İhale, sözleşme ve hakediş

- Teknik şube: ihtiyaç, şartname, yaklaşık maliyet, kontrol ve teknik kabul
- İdari İşler: dosya, takvim, yazışma, teminat ve ödeme evrakı
- Destek Hizmetleri: proje dışı mal/hizmet alımı ihalesi
- Mali Hizmetler: mali kontrol ve ödeme

KPI:

- Zamanında ihale hazırlığı
- Teminat ve sözleşme süresi kaçırma sayısı
- Hakediş işlem süresi
- Eksik ödeme dosyası oranı

## 6. Faz 3 — Dijital altyapı

**Süre:** 90–240 gün

### 6.1 Ortak e-başvuru

İlk paket:

- Ruhsat ve vize
- Geçiş yolu
- Yol kapatma/daraltma
- Kamera görüntüsü talebi
- Otogar/peron işlemleri

Ortak akış:

`Başvuru → otomatik tamlık kontrolü → teknik inceleme → görüş/onay → ödeme → e-imza → bildirim → arşiv`

### 6.2 Tek ulaşım veri kataloğu

- Veri seti adı ve sahibi
- Kaynak sistem
- Güncelleme sıklığı
- Kalite kuralı
- Erişim seviyesi
- Saklama süresi
- API ve rapor kullanımları

### 6.3 Tek varlık kataloğu

CBS üzerinde tekil kimlikle:

- Durak
- Levha
- Sinyal kontrol cihazı
- Kamera
- EDS noktası
- Akıllı ulaşım saha cihazı
- Yol sorumluluk alanı

### 6.4 Sözleşme ve bakım takvimi

Teminat, iş programı, hakediş, bakım, arıza, geçici/kesin kabul ve garanti süreleri tek sistemden izlenmelidir.

## 7. Faz 4 — Performans ve sürekli iyileştirme

**Süre:** 180–365 gün

### Yönetici gösterge paneli

- Süreç çevrim süreleri
- Bekleyen ve geciken işler
- UKOME karar kapanış oranı
- Ruhsat ve izin sonuçlanma süresi
- Sinyal/AUS arıza SLA’sı
- Otogar gelir mutabakat farkı
- İhale ve hakediş süreleri
- Vatandaş memnuniyeti
- Veri ve varlık kalite skoru

### Süreç madenciliği

EBYS, UKOME, ruhsat, bakım, mali sistem ve e-başvuru olay kayıtlarından gerçek süreç akışı çıkarılmalı; tekrar işlem, bekleme ve darboğazlar periyodik incelenmelidir.

### Yıllık gözden geçirme

- Mevzuat değişiklikleri
- Görev ve organizasyon değişiklikleri
- KPI hedefleri
- Risk ve kontrol etkinliği
- Dijital sistem performansı
- Kullanıcı ve vatandaş geri bildirimi

## 8. Yönetişim modeli

| Kurul/rol | Sorumluluk |
|---|---|
| Daire Başkanı | Sponsor, öncelik ve nihai karar |
| Süreç Yürütme Kurulu | Çakışma çözümü, faz kabulü, kaynak planı |
| Süreç sahibi | Süreç tasarımı, KPI ve sonuç |
| İdari İşler | Doküman kontrolü, proje takibi ve raporlama |
| Hukuk Müşavirliği | Mevzuat ve yetki doğrulaması |
| Bilgi İşlem | Mimari, entegrasyon, güvenlik ve işletim standardı |
| İç Kontrol/Denetim | Kontrol tasarımı ve etkinlik değerlendirmesi |

## 9. Temel riskler ve önlemler

| Risk | Önlem |
|---|---|
| Birimlerin görev kaybı algısı | Tasarımı kişi değil süreç ve çıktı üzerinden yürütmek |
| Belgelerin güncel olmaması | Resmî bağlantı ve periyodik doğrulama |
| Dijital sistemlerin birbirinden kopuk kurulması | Ortak veri ve entegrasyon mimarisi |
| Süreç sahibinin belirsiz kalması | Her süreçte tek A zorunluluğu |
| Kişisel verinin geniş paylaşılması | Rol bazlı erişim, log, maskeleme, saklama-imha |
| Sadece doküman üretilip uygulama yapılmaması | Faz kabul kriteri, KPI ve yönetici paneli |

## 10. Bir yıllık hedef sonuçlar

- 44 sürecin tamamında onaylı sahiplik ve RACI
- Kritik süreçlerin en az yüzde 80’inde dijital takip
- Paralel evrak, taşınır ve sözleşme kayıtlarının kaldırılması
- UKOME kararlarının uygulama ve kapanışının ölçülmesi
- Tek ulaşım veri ve varlık kataloğunun devreye alınması
- Mevzuat, gizlilik ve görev değişikliklerinin sürümlü yönetilmesi
- Süreç süreleri ve hizmet performansının yönetici panelinden izlenmesi
