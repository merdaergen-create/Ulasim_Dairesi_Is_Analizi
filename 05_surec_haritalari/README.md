# 05 — Süreç Haritaları

Bu dizin, Ulaşım Dairesi iş süreçlerinin departman bazında hazırlanmış Mermaid akışlarını içerir. Haritalar **hedef işletim modelini** gösterir; mevcut uygulama ile farklı olan noktalar süreç yürürlüğe alınmadan önce ilgili yönetmelik, yönerge, görev tanımı ve Hukuk Müşavirliği görüşüyle doğrulanmalıdır.

## Dizin

| Departman | Kapsanan ana süreçler |
|---|---|
| [`trafik_planlama/`](trafik_planlama/) | Ulaşım Ana Planı, yol/kavşak, geçiş yolu, yol kapatma, sinyalizasyon, işaretleme, Trafik Yönetim Merkezi ve otopark erişim uygunluğu |
| [`ukome/`](ukome/) | Teknik teklif kabulü, alt komisyon, gündem, karar, dağıtım ve uygulama kapanışı |
| [`toplu_ulasim/`](toplu_ulasim/) | Hat–güzergâh–zaman–tarife, ruhsat/vize/izin, kontrol, durak yaşam döngüsü, ticari plaka, servis ve özel taşıma izinleri |
| [`akilli_ulasim/`](akilli_ulasim/) | EDS/AUS, veri platformu, akıllı durak, entegrasyon ve kamera verisi yönetimi |
| [`otogar/`](otogar/) | Araç giriş-çıkış, tahakkuk/tahsilat, peron ve teknik tesis hizmetleri |
| [`trafik_egitim/`](trafik_egitim/) | Eğitim programı ve trafik eğitim parkı işletimi |
| [`idari_isler/`](idari_isler/) | Evrak, ihale, sözleşme, hakediş, ödeme, bütçe, raporlama, taşınır ve taşıt görevlendirme |

## Kaynak incelemesiyle eklenen süreçler

- `TP-07` — Otopark erişim uygunluk belgesi
- `TU-06` — Ticari plaka tahsis, devir ve iptal
- `TU-07` — Servis aracı izin belgesi
- `TU-08` — Yük nakli ve özel taşıma izni
- `TU-09` — Ticari araç uygunluk, çalışma ruhsatı ve vize yenileme
- `ID-07` — Taşıt görev emri ve hizmet aracı görevlendirme

Karşılaştırma gerekçeleri için [`kaynak_karsilastirma_ve_ek_surecler.md`](kaynak_karsilastirma_ve_ek_surecler.md) dosyasına bakınız.

## Harita standardı

Her süreç haritasında aşağıdaki unsurlar bulunur:

1. **Süreç sahibi:** Nihai hesap verebilir birim.
2. **Girdiler:** Süreci başlatmak ve karar vermek için zorunlu bilgi/belgeler.
3. **Faaliyetler:** İşi yapan birimler ve departman aktarımları.
4. **Karar noktaları:** Uygunluk, eksiklik, onay veya ret kararları.
5. **Çıktılar:** Karar, proje, belge, uygulama, kayıt veya rapor.
6. **Kapanış kanıtı:** İşin tamamlandığını gösteren kayıt.
7. **Kontroller:** Mevzuat, görev ayrılığı, kişisel veri, mali kontrol ve teknik kabul.
8. **KPI:** Süre, kalite, tekrar işlem, gecikme ve hizmet performansı göstergeleri.

## Sorumluluk ilkeleri

- Her süreçte yalnız bir **A — hesap verebilir sahip** bulunur.
- UKOME teknik projenin sahibi değil, kurul ve karar sürecinin sahibidir.
- Teknik şube ihtiyacı, teknik şartnameyi ve teknik kabulü yürütür.
- İdari İşler ihale/sözleşme dosyası, süre, teminat ve ödeme evrakını yönetir.
- Akıllı Ulaşım Sistemleri teknoloji, veri ve entegrasyon sahibidir; trafik politikası ve trafik mühendisliği Ulaşım Planlamanın sorumluluğundadır.
- Süreç dijitalleştirilmeden önce mükerrer adımlar kaldırılır ve yetki sınırları yazılı hale getirilir.

## Durum

Bu haritalar **Rev-A hedef süreç taslağıdır**. Yürürlüğe alma için süreç sahibi, İdari İşler, Hukuk Müşavirliği ve gerekiyorsa UKOME/Meclis onayı gerekir.
