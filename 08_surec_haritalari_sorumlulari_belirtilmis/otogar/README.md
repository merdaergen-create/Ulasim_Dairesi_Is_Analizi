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
    A([Araç otogar girişine gelir<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]) --> B[Plaka tanıma veya gişe kaydı]
    B --> C[Firma, sefer ve yetki belgesi doğrulama<br/>Sorumlu: Firma ve Yetki Belgesi Kontrol Personeli]
    C --> D{Girişe uygun mu?<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu}
    D -- Hayır --> E[Ret/istisna kaydı ve işletme sorumlusuna bildirim<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]
    D -- Evet --> F[Araç sınıfı ve tarife sürümünün belirlenmesi<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]
    F --> G[Otomatik tahakkuk<br/>Sorumlu: Gişe ve Tahakkuk Sorumlusu]
    G --> H{Muafiyet veya özel karar var mı?<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu}
    H -- Evet --> I[Yetki ve dayanak doğrulaması<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]
    H -- Hayır --> J[Tahsilat<br/>Sorumlu: Gişe ve Tahakkuk Sorumlusu]
    I --> J
    J --> K[Makbuz ve mali sistem kaydı<br/>Sorumlu: Gişe ve Tahakkuk Sorumlusu]
    K --> L[Peron/işletme sürecine aktarım<br/>Sorumlu: Peron Planlama ve Tahsis Sorumlusu]
    L --> M[Araç çıkış kaydı<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]
    M --> N{Giriş, tahakkuk, tahsilat ve çıkış eşleşiyor mu?<br/>Sorumlu: Gişe ve Tahakkuk Sorumlusu}
    N -- Hayır --> O[İstisna incelemesi ve yetkili düzeltme<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]
    O --> P[Çift onay ve log<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]
    P --> Q[Gün sonu mutabakat<br/>Sorumlu: Kasa ve Gelir Mutabakat Sorumlusu]
    N -- Evet --> Q
    Q --> R[Kasa, banka/POS ve mali sistem karşılaştırması<br/>Sorumlu: Kasa ve Gelir Mutabakat Sorumlusu]
    R --> S{Fark var mı?<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu}
    S -- Evet --> T[Fark tutanağı ve inceleme<br/>Sorumlu: Kasa ve Gelir Mutabakat Sorumlusu]
    S -- Hayır --> U[Gün sonu kapama<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]
    T --> U
    U --> V[Aylık araç ve gelir raporu<br/>Sorumlu: Faaliyet ve Gelir Raporlama Uzmanı]
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
    A([Onaylı sefer veya araç giriş kaydı<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]) --> B[Günlük sefer ve peron kapasite planı]
    B --> C[Uygun peronun kurallara göre atanması<br/>Sorumlu: Peron Planlama ve Tahsis Sorumlusu]
    C --> D{Peron çakışması var mı?<br/>Sorumlu: Peron Planlama ve Tahsis Sorumlusu}
    D -- Evet --> E[Öncelik, süre ve alternatif peron analizi<br/>Sorumlu: Peron Planlama ve Tahsis Sorumlusu]
    E --> C
    D -- Hayır --> F[Firma/şoföre dijital peron bildirimi<br/>Sorumlu: Peron Planlama ve Tahsis Sorumlusu]
    F --> G[Araç perona yönlendirilir<br/>Sorumlu: Peron Planlama ve Tahsis Sorumlusu]
    G --> H[İndirme-bindirme, bekleme ve hareket kontrolü<br/>Sorumlu: Terminal Operasyon Birim Sorumlusu]
    H --> I{Gecikme, ihlal veya olay var mı?<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu}
    I -- Evet --> J[Olay kaydı ve ilgili birim/kolluk koordinasyonu<br/>Sorumlu: Terminal Operasyon Birim Sorumlusu]
    J --> K[Gerekirse peron yeniden planlama<br/>Sorumlu: Peron Planlama ve Tahsis Sorumlusu]
    K --> H
    I -- Hayır --> L[Seferin tamamlanması ve peronun boşaltılması<br/>Sorumlu: Peron Planlama ve Tahsis Sorumlusu]
    L --> M[Sistem ve saha kaydının kapatılması<br/>Sorumlu: Terminal Operasyon Birim Sorumlusu]
    M --> N[Vardiya devir ve günlük işletme raporu<br/>Sorumlu: Vardiya Amiri]
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
    A([Arıza, alarm veya periyodik bakım<br/>Sorumlu: Terminal Teknik İşletme Sorumlusu]) --> B[Teknik çağrı kaydı ve varlık ID]
    B --> C[Öncelik ve hizmet kesintisi etkisi<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]
    C --> D{Acil güvenlik riski var mı?<br/>Sorumlu: Terminal Güvenlik Koordinatörü}
    D -- Evet --> E[Alanı güvene alma ve acil kurum koordinasyonu<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]
    D -- Hayır --> F[İş emri ve sorumlu ekip<br/>Sorumlu: Terminal Teknik İşletme Sorumlusu]
    E --> F
    F --> G{Arıza türü<br/>Sorumlu: Terminal Teknik İşletme Sorumlusu}
    G -- Elektrik/Mekanik --> H[Otogar teknik ekip veya yüklenici<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]
    G -- Bilişim/Otomasyon --> I[Bilgi İşlem/AUS veya yüklenici<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]
    G -- Ortak hizmet --> J[Destek Hizmetleri/yüklenici<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]
    H --> K[İSG ve enerji izolasyonu kontrolü<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]
    I --> K
    J --> K
    K --> L[Müdahale ve parça/işçilik kaydı<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]
    L --> M[Fonksiyon ve güvenlik testi<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]
    M --> N{Hizmet geri geldi mi?<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu}
    N -- Hayır --> O[Üst seviye teknik destek ve escalation<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]
    O --> L
    N -- Evet --> P[Kullanıcı/işletme kabulü<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]
    P --> Q[İş emri kapanışı ve envanter güncelleme<br/>Sorumlu: Terminal Teknik İşletme Sorumlusu]
    Q --> R[Aylık arıza, SLA ve kök neden analizi<br/>Sorumlu: Terminal Teknik İşletme Sorumlusu]
```

**Kritik yönetişim notu:** Temizlik, güvenlik, bakım ve ortak tesis hizmetlerinin Otogar ile Destek Hizmetleri arasındaki sahipliği güncel yönetmelik değişikliğine göre yazılı olarak yeniden belirlenmelidir.

---

## OT-04 — Otogar gelir ve faaliyet raporlaması

```mermaid
flowchart LR
    A[Gişe ve plaka kayıtları<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu] --> E[Veri kalite kontrolü]
    B[Peron ve sefer kayıtları<br/>Sorumlu: Peron Planlama ve Tahsis Sorumlusu] --> E
    C[Arıza ve işletme olayları<br/>Sorumlu: Terminal Teknik İşletme Sorumlusu] --> E
    D[Mali sistem tahsilatları<br/>Sorumlu: Gişe ve Tahakkuk Sorumlusu] --> E
    E --> F{Kayıtlar tutarlı mı?<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu}
    F -- Hayır --> G[Kaynak sistem ve istisna düzeltmesi<br/>Sorumlu: Otogar İşletme ilgili süreç pozisyonu]
    G --> E
    F -- Evet --> H[Günlük ve aylık faaliyet göstergeleri<br/>Sorumlu: Faaliyet ve Gelir Raporlama Uzmanı]
    H --> I[Otogar Şube Müdürü onayı<br/>Sorumlu: Otogar İşletme Şube Müdürü]
    I --> J[İdari İşler faaliyet raporu ve yönetici paneli<br/>Sorumlu: Faaliyet ve Gelir Raporlama Uzmanı]
```
