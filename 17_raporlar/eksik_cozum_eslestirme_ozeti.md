# Eksik–Çözüm Eşleştirme Özeti

## Yönetici özeti

`05_surec_haritalari` süreçlerin akışını, `06_raporlar` ise hedef organizasyon ayrışmasını göstermiştir. Buna karşılık uygulama için gerekli olan pozisyon, görev tanımı, birim, adım bazlı sorumluluk ve form altyapısı başlangıçta eksikti.

Bu nedenle aşağıdaki tamamlayıcı çalışmalar hazırlanmıştır.

| Kaynaklarda görülen eksik | Oluşturulan çalışma | Sağlanan sonuç |
|---|---|---|
| 8 şubeli geçiş modelinde ayrıntılı pozisyon setinin bulunmaması | `09_yalin_pozisyonlari` | Şube bazında yalın pozisyonlar, görev kümeleri ve ölçekleme eşikleri |
| Pozisyonların süreç adımlarıyla ilişkilendirilmemesi | `10_yalin_pozisyon_gorev_tanimlari` | Pozisyon bazında süreç, görev, çıktı, yetki ve KPI tanımı |
| Şube müdürlükleri altında birimlerin görünmemesi | `14_yalin_organizasyon_semasi` | Şube–birim–pozisyon hiyerarşisi |
| Süreç adımlarında uygulayıcı pozisyon ve birim bilgisinin olmaması | `15_yalin_surec_haritalari` | Her adımda sorumlu pozisyon ve bağlı birim |
| Başvuru, kontrol, karar, kabul ve kapanış formlarının dağınık olması | `12_formlar` | Süreç kodu ve kullanım adımı belirtilmiş standart form seti |
| Ruhsat ile hizmet planlamasının aynı yapı içinde karışması | `09`, `10`, `14`, `15` | Ayrı Ulaşım Ruhsat ve Ticari Araç İşlemleri yapısı |
| UKOME'nin teknik proje sahibi gibi algılanabilmesi | `09`, `10`, `14`, `15` | Sekretarya, karar yazımı, dağıtım ve uygulama takip modeli |
| Planlama, saha uygulaması, AUS ve TKM sınırlarının bulanık olması | `09`, `10`, `14`, `15` | Teknik politika, saha işletmesi, teknoloji ve operasyon ayrımı |
| Teknik işler ile ihale/sözleşme/ödeme dosyasının karışması | `09`, `10`, `14` | İdari ve Mali İşlerde merkezi dosya yönetimi ve görev ayrılığı |
| Süreç kapanış kanıtlarının standart olmaması | `12_formlar` | Teknik kabul, teslim, uygunsuzluk ve kapanış şablonları |

## Oluşturulan bütünleşik yapı

```text
05 — Süreç haritaları
        ↓
09 — Yalın pozisyonlar
        ↓
10 — Pozisyon görev tanımları ve birimleri
        ↓
14 — Organizasyon şeması
        ↓
15 — Pozisyonu ve birimi belirtilmiş süreç haritaları
        ↓
12 — Süreç adımına bağlı formlar ve kapanış kayıtları
```

## Temel tasarım kararları

1. Ulaşım Planlama politika, modelleme, yol-kavşak ve trafik güvenliği sahibidir.
2. Trafik Hizmetleri ve Sinyalizasyon saha altyapısı, bakım ve uygulama sahibidir.
3. AUS ve TKM aynı şube içinde teknoloji ve operasyon olarak ayrı birimlerdir.
4. Toplu Taşıma hizmet planlamasını, Ruhsat Şubesi izin ve belge süreçlerini yürütür.
5. UKOME teknik proje hazırlamaz; kurul, karar ve uygulama takibini yönetir.
6. Otogar günlük terminal, peron, tahakkuk ve teknik işletme süreçlerini yönetir.
7. İdari ve Mali İşler ihale, sözleşme, ödeme evrakı, bütçe, taşınır ve EBYS süreçlerini merkezileştirir.
8. Trafik Eğitim ilk aşamada Ulaşım Planlama altında birim olarak çalışır.

## Sonuç

Tamamlayıcı çalışmaların temel gerekçesi, süreç akışlarını uygulanabilir organizasyon ve kayıt düzenine dönüştürmektir. Böylece her iş için “hangi süreç, hangi şube, hangi birim, hangi pozisyon, hangi form ve hangi kapanış kanıtı” sorularına ortak ve izlenebilir cevap verilmiştir.
