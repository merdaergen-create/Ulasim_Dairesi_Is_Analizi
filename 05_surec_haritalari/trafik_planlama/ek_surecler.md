# Trafik Planlama — Kaynak İncelemesi Sonucu Ek Süreçler

Bu dosya, kaynak belgelerde yer aldığı halde mevcut `TP-01–TP-06` haritalarında bağımsız bir süreç olarak gösterilmeyen işleri içerir.

---

## TP-07 — Otopark erişim uygunluk belgesi

**Süreç sahibi:** Ulaşım Planlama Şube Müdürlüğü  
**Karar/kurum paydaşları:** İmar ve Şehircilik, Fen İşleri, UKOME ve ilgili ilçe belediyesi  
**Kaynak dayanağı:** Otopark erişim uygunluk belgesi ve Ulaşım Planlama görev/yönerge belgeleri.  
**Girdiler:** Başvuru dilekçesi, vaziyet planı, mimari proje, tapu/imar bilgisi, araç giriş-çıkış noktaları, yol ve kaldırım geometrisi, mevcut trafik düzeni.  
**Çıktılar:** Teknik uygunluk raporu, uygunluk belgesi, proje revizyon talebi veya gerekçeli ret; CBS ve başvuru kapanış kaydı.

```mermaid
flowchart TD
    A([Otopark erişim uygunluğu başvurusu]) --> B[Başvuru ve proje eklerinin kayıt altına alınması]
    B --> C{Zorunlu belgeler tam mı?}
    C -- Hayır --> D[Eksik belge ve proje bildirim listesi]
    D --> B
    C -- Evet --> E[İmar durumu, yetki alanı ve yol sorumluluğu kontrolü]
    E --> F[Saha incelemesi ve mevcut trafik düzeninin tespiti]
    F --> G[Araç giriş-çıkış görüş mesafesi ve manevra analizi]
    G --> H[Yaya, bisiklet, engelli erişimi ve kaldırım sürekliliği kontrolü]
    H --> I[Yakın kavşak, durak, sinyal, geçit ve yol güvenliği etkisi]
    I --> J{Erişim teknik olarak uygun mu?}
    J -- Hayır --> K[Alternatif giriş-çıkış veya proje revizyon talebi]
    K --> L{Revize proje sunuldu mu?}
    L -- Hayır --> M[Gerekçeli ret ve dosya kapanışı]
    L -- Evet --> F
    J -- Evet --> N{UKOME veya başka kurul kararı gerekli mi?}
    N -- Evet --> O[Standart teknik teklif dosyasının hazırlanması]
    O --> P[UKOME/ilgili kurul karar süreci]
    P --> Q{Karar olumlu mu?}
    Q -- Hayır --> M
    Q -- Evet --> R[Uygunluk şartları ve uygulama koşulları]
    N -- Hayır --> R
    R --> S[Yetkili teknik onay ve uygunluk belgesinin düzenlenmesi]
    S --> T[Başvuru sahibine bildirim ve ilgili kurumlara dağıtım]
    T --> U[Gerekirse uygulama sonrası saha doğrulaması]
    U --> V[CBS, belge ve kapanış kaydı]
```

**Temel kontroller**

- Yol güvenliği, görüş mesafesi ve manevra alanı ölçülebilir kriterlerle değerlendirilmelidir.
- Otopark erişimi yaya yolu, bisiklet güzergâhı, durak, sinyal, yaya geçidi veya kavşak işlevini bozacak şekilde onaylanmamalıdır.
- İmar ve yapı ruhsatı uygunluğu ilgili yetkili birimce; trafik erişim uygunluğu Ulaşım Planlama tarafından değerlendirilmelidir.
- Uygunluk belgesinde giriş-çıkış konumu, proje sürümü ve varsa uygulama şartları açıkça yazılmalıdır.

**Önerilen KPI:** Ortalama sonuçlandırma süresi, ilk başvuruda belge tamlık oranı, revizyon sayısı, uygulama sonrası uygunsuzluk oranı, saha doğrulama süresi.
