# Toplu Ulaşım — Kaynak İncelemesi Sonucu Ek Süreçler

Bu dosya, kaynak formlar ve görev belgelerinde ayrı belge ve karar mantığı bulunan ancak mevcut `TU-01–TU-05` haritalarında bağımsız süreç olarak gösterilmeyen işleri içerir.

---

## TU-06 — Ticari plaka tahsis, devir ve iptal süreci

**Süreç sahibi:** Ulaşım Ruhsat ve Ticari Araç İşlemleri Birimi  
**Karar paydaşları:** UKOME, Mali Hizmetler, Hukuk Müşavirliği ve ilgili kamu kurumları  
**Kaynak dayanağı:** Ticari Plaka Tahsis Belgesi Başvuru Formu, Ticari Plaka Devir Belgesi Başvuru Formu ve Yetki Belgesi İptali Başvuru Formu.  
**Girdiler:** Başvuru, kimlik/şirket belgeleri, plaka ve hak bilgisi, UKOME kararı, borç ve ücret bilgileri, devir veya iptal gerekçesi.  
**Çıktılar:** Tahsis/devir/iptal kararı, güncel plaka ve hak kaydı, tahakkuk, belge, gerekçeli ret ve arşiv kaydı.

```mermaid
flowchart TD
    A([Tahsis, devir veya iptal başvurusu]) --> B[Başvuru türü ve kimlik/şirket kontrolü]
    B --> C[Plaka, hak, önceki karar ve aktif kayıt araştırması]
    C --> D{Başvuru türüne ait belgeler tam mı?}
    D -- Hayır --> E[Eksik belge bildirimi]
    E --> B
    D -- Evet --> F[Mevzuat, hak sahipliği, borç ve kısıt kontrolü]
    F --> G{UKOME veya başka kurul kararı gerekli mi?}
    G -- Evet --> H[Teknik/idari teklif dosyasının hazırlanması]
    H --> I[UKOME/kurul karar süreci]
    I --> J{Karar olumlu mu?}
    J -- Hayır --> K[Gerekçeli ret ve kayıt kapanışı]
    J -- Evet --> L[Ücret, vergi, harç ve tahakkuk işlemleri]
    G -- Hayır --> L
    L --> M[Tahsilat doğrulaması]
    M --> N[Tahsis/devir/iptal belgesinin hazırlanması]
    N --> O[Yetkili kontrol, e-imza ve belge numarası]
    O --> P[Plaka, hak, ruhsat ve denetim sistemlerinin güncellenmesi]
    P --> Q[Eski belge/hak kaydının iptali veya arşivlenmesi]
    Q --> R[Başvuru sahibine bildirim ve dosya kapanışı]
```

**Temel kontroller:** Çift tahsis ve mükerrer hak engeli, haciz/şerh/kısıt kontrolü, kurul kararı-belge eşleşmesi, ücret tarifesi sürümü, eski belgenin kullanım dışı bırakılması.

**Önerilen KPI:** Ortalama sonuçlandırma süresi, eksik başvuru oranı, mükerrer kayıt sayısı, karar-belge uyumsuzluğu, iptal sonrası açık kayıt oranı.

---

## TU-07 — Servis aracı izin belgesi süreci

**Süreç sahibi:** Ulaşım Ruhsat ve Ticari Araç İşlemleri Birimi  
**Hizmet türleri:** S plaka okul servisi, S plaka personel servisi, özel plaka okul/personel servisi ve müşteri servisi.  
**Kaynak dayanağı:** S Plaka Okul Servis Aracı, S Plaka Personel Servis Aracı, Özel Plaka Okul Servis Aracı, Özel Kuruluş Personel Servis Aracı ve Müşteri Servis Aracı izin başvuru formları.  
**Girdiler:** Araç, sürücü, rehber personel, işletmeci/kurum, güzergâh ve hizmet sözleşmesi belgeleri; muayene, sigorta ve ücret bilgileri.  
**Çıktılar:** Servis izin belgesi, güzergâh/hizmet kaydı, gerekçeli ret, yenileme takvimi ve denetim kaydı.

```mermaid
flowchart TD
    A([Servis izin başvurusu]) --> B[Servis türünün ve hizmet ilişkisinin belirlenmesi]
    B --> C[Araç, sürücü, rehber ve işletmeci belgelerinin kontrolü]
    C --> D{Başvuru tam mı?}
    D -- Hayır --> E[Eksik belge bildirimi ve süre verilmesi]
    E --> C
    D -- Evet --> F[Plaka/hak, yaş, kapasite, sigorta ve muayene kontrolü]
    F --> G[Güzergâh, okul/kurum ve hizmet sözleşmesi doğrulaması]
    G --> H{Araç uygunluk kontrolü gerekli mi?}
    H -- Evet --> I[Standart araç uygunluk kontrolü]
    I --> J{Uygun mu?}
    J -- Hayır --> K[Uygunsuzluk listesi ve düzeltme süresi]
    K --> I
    J -- Evet --> L[Ücret ve tahakkuk işlemleri]
    H -- Hayır --> L
    L --> M[Tahsilat doğrulaması]
    M --> N{Tüm şartlar sağlandı mı?}
    N -- Hayır --> O[Gerekçeli ret veya bekleme]
    N -- Evet --> P[İzin belgesi, e-imza ve kayıt]
    P --> Q[Denetim, güzergâh ve süre takip sistemine aktarım]
    Q --> R[Yenileme öncesi bildirim]
```

**Temel kontroller:** Başvuru türüne özel kontrol listesi, araç ve sürücü belge geçerliliği, kapasite ve yaş şartı, okul servislerinde rehber personel kontrolü, güzergâh ve kurum sözleşmesi tutarlılığı.

**Önerilen KPI:** Belge sonuçlandırma süresi, ilk kontrolde uygun araç oranı, eksik başvuru oranı, süresi geçen izin oranı, tekrar uygunsuzluk oranı.

---

## TU-08 — Yük nakli ve özel taşıma izin süreci

**Süreç sahibi:** Ulaşım Ruhsat ve Ticari Araç İşlemleri Birimi  
**Kapsam:** Yük nakli, mevsimlik tarım işçisi taşımacılığı ve özel/geçici taşıma izinleri.  
**Kaynak dayanağı:** Yük Nakli İzin Belgesi Başvuru Formu ve Mevsimlik Tarım İşçisi Taşımacılığı İzin Belgesi Başvuru Formu.  
**Girdiler:** Başvuru, araç ve sürücü belgeleri, taşıma konusu, güzergâh, süre, kapasite, sigorta, güvenlik ve kurum görüşleri.  
**Çıktılar:** Süreli izin belgesi, güzergâh ve koşullar, gerekçeli ret, denetim ve kapanış kaydı.

```mermaid
flowchart TD
    A([Yük veya özel taşıma izin başvurusu]) --> B[Taşıma türü, süre ve güzergâh sınıflandırması]
    B --> C[Araç, sürücü, sigorta ve yetki belgelerinin kontrolü]
    C --> D{Belgeler tam mı?}
    D -- Hayır --> E[Eksik belge bildirimi]
    E --> C
    D -- Evet --> F[Yük/yolcu türü, kapasite ve güvenlik şartlarının kontrolü]
    F --> G[Güzergâh, yol kapasitesi, saat ve trafik etkisi analizi]
    G --> H{Kurum/kolluk/UKOME görüşü gerekli mi?}
    H -- Evet --> I[İlgili kurum görüşlerinin alınması]
    I --> J{Görüşler olumlu mu?}
    J -- Hayır --> K[Alternatif güzergâh, süre veya şart revizyonu]
    K --> G
    J -- Evet --> L[İzin şartları ve denetim koşulları]
    H -- Hayır --> L
    L --> M[Ücret ve tahakkuk işlemleri]
    M --> N[Tahsilat doğrulaması]
    N --> O[İzin belgesinin hazırlanması ve e-imza]
    O --> P[Denetim ve süre takip sistemine aktarım]
    P --> Q[İzin süresi sonunda kapanış veya yenileme]
```

**Temel kontroller:** Taşıma türüne uygun araç, kapasite ve güvenlik şartı; süreli izin; güzergâh ve saat kısıtı; kolluk ve kurum görüşü; denetim sistemine aktarım.

**Önerilen KPI:** Sonuçlandırma süresi, revize güzergâh oranı, izin şartı ihlali, süresi geçen açık izin, denetim kaydı tamlığı.

---

## TU-09 — Ticari araç uygunluk, çalışma ruhsatı ve vize yenileme süreci

**Süreç sahibi:** Ulaşım Ruhsat ve Ticari Araç İşlemleri Birimi  
**Kaynak dayanağı:** Ticari Plakalı Araç Uygunluk Kontrol Formu ve Ticari Araçların M/T Plaka Çalışma Ruhsatı Başvuru Formu.  
**Girdiler:** Ruhsat/vize başvurusu, araç ve sürücü belgeleri, plaka/hak kaydı, muayene ve sigorta, ücret ve borç bilgileri.  
**Çıktılar:** Uygunluk kontrol sonucu, çalışma ruhsatı/vize, uygunsuzluk bildirimi, yenileme ve denetim kaydı.

```mermaid
flowchart TD
    A([Çalışma ruhsatı veya vize başvurusu]) --> B[Plaka, hak ve mevcut ruhsat kaydının doğrulanması]
    B --> C[Araç, sürücü, sigorta, muayene ve belge kontrolü]
    C --> D{Belgeler tam ve geçerli mi?}
    D -- Hayır --> E[Eksik/geçersiz belge bildirimi]
    E --> C
    D -- Evet --> F[Standart araç uygunluk muayenesi]
    F --> G{Araç uygun mu?}
    G -- Hayır --> H[Uygunsuzluk listesi ve düzeltme süresi]
    H --> F
    G -- Evet --> I[Ceza, borç, önceki ihlal ve kısıt kontrolü]
    I --> J[Ücret ve tahakkuk işlemleri]
    J --> K[Tahsilat doğrulaması]
    K --> L{Tüm koşullar sağlandı mı?}
    L -- Hayır --> M[Gerekçeli ret veya bekleme]
    L -- Evet --> N[Ruhsat/vize belgesinin hazırlanması]
    N --> O[Yetkili kontrol, e-imza ve süre kaydı]
    O --> P[Denetim sistemine aktarım]
    P --> Q[Yenileme öncesi otomatik bildirim]
```

**Temel kontroller:** Mükerrer ruhsat engeli, araç uygunluk kontrolünün standart forma bağlanması, belge ve ücret tarifesi sürümü, yetkisiz belge düzenleme engeli, vize süresi takibi.

**Önerilen KPI:** Ortalama ruhsat/vize süresi, ilk muayenede uygunluk oranı, tekrar muayene sayısı, süresi geçen ruhsat oranı, belge hata oranı.
