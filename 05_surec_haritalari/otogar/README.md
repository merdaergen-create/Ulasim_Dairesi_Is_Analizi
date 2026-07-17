# Otogar Süreç Haritaları

Bu bölüm otogar araç giriş-çıkış, tahakkuk/tahsilat, peron ve teknik tesis işletme süreçlerini gösterir. 16 Haziran 2026 tarihli yönetmelik değişikliğinin eski Otogar yönergesi ve görev tanımlarına etkisi ayrıca doğrulanmalıdır.

---

## OT-01 — Araç giriş-çıkış, tahakkuk ve tahsilat

**Süreç sahibi:** Gişe ve Tahsilat İşlemleri Birimi  
**Hesap verebilir:** Otogar Şube Müdürü  
**Girdiler:** Plaka, firma/sefer, araç sınıfı, giriş-çıkış zamanı, yetki belgesi, güncel ücret tarifesi ve muafiyet bilgisi.  
**Çıktılar:** Geçiş kaydı, tahakkuk, makbuz, kasa mutabakatı, gelir ve araç sayısı raporu.

```mermaid
flowchart TD
    A([Araç otogar girişine gelir]) --> B[Plaka tanıma veya gişe kaydı]
    B --> C[Firma, sefer ve yetki belgesi doğrulama]
    C --> D{Girişe uygun mu?}
    D -- Hayır --> E[Ret/istisna kaydı ve işletme sorumlusuna bildirim]
    D -- Evet --> F[Araç sınıfı ve tarife sürümünün belirlenmesi]
    F --> G[Otomatik tahakkuk]
    G --> H{Muafiyet veya özel karar var mı?}
    H -- Evet --> I[Yetki ve dayanak doğrulaması]
    H -- Hayır --> J[Tahsilat]
    I --> J
    J --> K[Makbuz ve mali sistem kaydı]
    K --> L[Peron/işletme sürecine aktarım]
    L --> M[Araç çıkış kaydı]
    M --> N{Giriş, tahakkuk, tahsilat ve çıkış eşleşiyor mu?}
    N -- Hayır --> O[İstisna incelemesi ve yetkili düzeltme]
    O --> P[Çift onay ve log]
    P --> Q[Gün sonu mutabakat]
    N -- Evet --> Q
    Q --> R[Kasa, banka/POS ve mali sistem karşılaştırması]
    R --> S{Fark var mı?}
    S -- Evet --> T[Fark tutanağı ve inceleme]
    S -- Hayır --> U[Gün sonu kapama]
    T --> U
    U --> V[Aylık araç ve gelir raporu]
```

**Temel kontroller:** Tarife sürüm numarası, manuel plaka/tutar değişikliğinde çift onay, muafiyet dayanağı, günlük kasa mutabakatı, mali sistem entegrasyonu.

**Önerilen KPI:** Otomatik plaka tanıma oranı, manuel düzeltme oranı, kasa farkı, tahsilat başarı oranı, işlem süresi.

---

## OT-02 — Peron tahsisi ve günlük saha işletimi

**Süreç sahibi:** Otogar İşletme Birimi  
**Girdiler:** Firma ve yetki bilgileri, sefer planı, peron kapasitesi, geliş/gidiş zamanı, özel durum ve işletme kuralları.  
**Çıktılar:** Peron tahsisi, günlük peron planı, gecikme/çakışma kaydı, olay ve vardiya raporu.

```mermaid
flowchart TD
    A([Onaylı sefer veya araç giriş kaydı]) --> B[Günlük sefer ve peron kapasite planı]
    B --> C[Uygun peronun kurallara göre atanması]
    C --> D{Peron çakışması var mı?}
    D -- Evet --> E[Öncelik, süre ve alternatif peron analizi]
    E --> C
    D -- Hayır --> F[Firma/şoföre dijital peron bildirimi]
    F --> G[Araç perona yönlendirilir]
    G --> H[İndirme-bindirme, bekleme ve hareket kontrolü]
    H --> I{Gecikme, ihlal veya olay var mı?}
    I -- Evet --> J[Olay kaydı ve ilgili birim/kolluk koordinasyonu]
    J --> K[Gerekirse peron yeniden planlama]
    K --> H
    I -- Hayır --> L[Seferin tamamlanması ve peronun boşaltılması]
    L --> M[Sistem ve saha kaydının kapatılması]
    M --> N[Vardiya devir ve günlük işletme raporu]
```

**Kontroller:** Kapasiteye dayalı otomatik çakışma kontrolü, yetkisiz peron değişikliği engeli, olay kayıtlarının plaka/sefer/peronla ilişkilendirilmesi.

---

## OT-03 — Teknik bakım, arıza ve tesis hizmeti

**Süreç sahibi:** Otogar teknik işletme sahibi olarak belirlenecek birim  
**Ortak hizmet paydaşları:** Destek Hizmetleri, Bilgi İşlem, İtfaiye/İSG ve yükleniciler  
**Girdiler:** Arıza ihbarı/alarm, bakım planı, tesis envanteri, sözleşme/SLA, yedek parça ve iş güvenliği koşulları.  
**Çıktılar:** İş emri, giderilmiş arıza, bakım/kabul kaydı, hizmet KPI ve maliyet raporu.

```mermaid
flowchart TD
    A([Arıza, alarm veya periyodik bakım]) --> B[Teknik çağrı kaydı ve varlık ID]
    B --> C[Öncelik ve hizmet kesintisi etkisi]
    C --> D{Acil güvenlik riski var mı?}
    D -- Evet --> E[Alanı güvene alma ve acil kurum koordinasyonu]
    D -- Hayır --> F[İş emri ve sorumlu ekip]
    E --> F
    F --> G{Arıza türü}
    G -- Elektrik/Mekanik --> H[Otogar teknik ekip veya yüklenici]
    G -- Bilişim/Otomasyon --> I[Bilgi İşlem/AUS veya yüklenici]
    G -- Ortak hizmet --> J[Destek Hizmetleri/yüklenici]
    H --> K[İSG ve enerji izolasyonu kontrolü]
    I --> K
    J --> K
    K --> L[Müdahale ve parça/işçilik kaydı]
    L --> M[Fonksiyon ve güvenlik testi]
    M --> N{Hizmet geri geldi mi?}
    N -- Hayır --> O[Üst seviye teknik destek ve escalation]
    O --> L
    N -- Evet --> P[Kullanıcı/işletme kabulü]
    P --> Q[İş emri kapanışı ve envanter güncelleme]
    Q --> R[Aylık arıza, SLA ve kök neden analizi]
```

**Kritik yönetişim notu:** Temizlik, güvenlik, bakım ve ortak tesis hizmetlerinin Otogar ile Destek Hizmetleri arasındaki sahipliği güncel yönetmelik değişikliğine göre yazılı olarak yeniden belirlenmelidir.

---

## OT-04 — Otogar gelir ve faaliyet raporlaması

```mermaid
flowchart LR
    A[Gişe ve plaka kayıtları] --> E[Veri kalite kontrolü]
    B[Peron ve sefer kayıtları] --> E
    C[Arıza ve işletme olayları] --> E
    D[Mali sistem tahsilatları] --> E
    E --> F{Kayıtlar tutarlı mı?}
    F -- Hayır --> G[Kaynak sistem ve istisna düzeltmesi]
    G --> E
    F -- Evet --> H[Günlük ve aylık faaliyet göstergeleri]
    H --> I[Otogar Şube Müdürü onayı]
    I --> J[İdari İşler faaliyet raporu ve yönetici paneli]
```
