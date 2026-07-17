# Veri Güvenliği ve Erişim Sınıflandırması

## Sınıflar

| Sınıf | Tanım | Örnek | Erişim |
|---|---|---|---|
| Kamuya Açık | Resmî olarak yayımlanmış ve paylaşımı serbest belge | Kanun, yayımlanmış yönetmelik | Herkes |
| Kurum İçi | Kurumsal çalışma için gerekli, kamuya açık olmayan belge | İç iş akışı, görev dağılımı | Yetkili personel |
| Kişisel Veri | Kimliği belirli veya belirlenebilir kişiye ilişkin veri | Personel raporu, imza, telefon, plaka | Rol bazlı sınırlı erişim |
| Operasyonel Hassas | Güvenlik veya hizmet sürekliliğini etkileyebilecek bilgi | TKM/EDS ağ yapısı, kamera erişimi | Özel yetki ve kayıtlı erişim |

## Kontroller

- Personel adıyla tutulan dosyalar kişisel veri kontrolünden geçirilmelidir.
- Kamera görüntüsü, araç konumu ve plaka verileri için hukuki dayanak, erişim rolü, saklama süresi ve işlem kaydı tanımlanmalıdır.
- EDS, ağ ve sistem mimarisi dokümanları kamuya açık raporlara ayrıntılı biçimde aktarılmamalıdır.
- Analiz dosyalarında mümkün olduğunca görev unvanı kullanılmalı; kişi adı kullanılmamalıdır.
- Hassas belgelerin indirilmesi, paylaşılması ve değişikliği kayıt altına alınmalıdır.
- Süresi dolan kişisel veriler onaylı saklama-imha politikasına göre silinmeli veya anonimleştirilmelidir.

## Repo uygulaması

Her kaynak, `dokuman_envanteri.csv` içinde gizlilik sınıfı ve kişisel veri durumu ile işaretlenmelidir. Kamuya açılacak bir sürüm hazırlanacaksa hassas ve kişisel içerikler ayrı bir özel depoda tutulmalıdır.
