# Şube, Birim ve Pozisyon Şemaları

## 1. Ulaşım Planlama Şube Müdürlüğü

```mermaid
flowchart TD
    M[Ulaşım Planlama Şube Müdürü]
    M --> B1[Ulaşım Ana Planı, Modelleme ve Veri Birimi]
    M --> B2[Yol, Kavşak ve Trafik Güvenliği Birimi]
    M --> B3[CBS ve Teknik Proje Kontrol Birimi]
    M --> B4[Trafik Güvenliği ve Eğitim Birimi]

    B1 --> P1[Ulaşım Ana Planı ve Modelleme Sorumlusu]
    B1 --> P2[Trafik Etüt ve Veri Analizi Uzmanı]

    B2 --> P3[Yol ve Kavşak Tasarım Sorumlusu]
    B2 --> P4[Trafik Güvenliği ve Sürdürülebilir Ulaşım Uzmanı]

    B3 --> P5[CBS ve Ulaşım Envanteri Uzmanı]
    B3 --> P6[Teknik Proje Kontrol Mühendisi]

    B4 --> P7[Trafik Eğitim ve Farkındalık Sorumlusu]
    B4 --> P8[Trafik Eğitim Uzmanı]
    B4 --> P9[Eğitim Parkı İşletme ve Teknik Sorumlusu]
```

## 2. Trafik Hizmetleri ve Sinyalizasyon Şube Müdürlüğü

```mermaid
flowchart TD
    M[Trafik Hizmetleri ve Sinyalizasyon Şube Müdürü]
    M --> B1[Sinyalizasyon Proje ve İşletme Birimi]
    M --> B2[Sinyalizasyon Bakım ve Saha Elektroniği Birimi]
    M --> B3[İşaretleme, Durak ve Saha Uygulama Birimi]

    B1 --> P1[Sinyalizasyon Proje ve İşletme Sorumlusu]

    B2 --> P2[Sinyalizasyon Bakım ve Elektronik Sorumlusu]
    B2 --> P3[Saha Uygulama Teknik Personeli]

    B3 --> P4[İşaretleme ve Trafik Saha Uygulama Sorumlusu]
    B3 --> P5[Durak Fiziksel Varlık Sorumlusu]
    B3 --> P6[Saha Kalite, Kabul ve İSG Teknikeri]
    B3 --> P7[Saha Uygulama Teknik Personeli]
```

## 3. Akıllı Ulaşım Sistemleri ve Trafik Yönetim Merkezi Şube Müdürlüğü

```mermaid
flowchart TD
    M[AUS ve TKM Şube Müdürü]
    M --> B1[AUS Sistemleri ve Entegrasyon Birimi]
    M --> B2[Veri, Güvenlik ve Platform Birimi]
    M --> B3[Trafik Yönetim Merkezi Operasyon Birimi]

    B1 --> P1[AUS Sistem Mimarı ve Entegrasyon Sorumlusu]
    B1 --> P2[EDS ve Saha Sistemleri Sorumlusu]
    B1 --> P3[Akıllı Durak ve Yolcu Bilgilendirme Sorumlusu]
    B1 --> P4[Ulaşım Teknolojileri Proje Yöneticisi]

    B2 --> P5[Ulaşım Veri Platformu ve Analitik Sorumlusu]
    B2 --> P6[Haberleşme, Ağ ve Siber Güvenlik Mühendisi]

    B3 --> P7[TKM Operasyon Birim Sorumlusu]
    B3 --> P8[Vardiya Amiri]
    B3 --> P9[Trafik Kontrol Operatörü]
    B3 --> P10[Olay Yönetimi ve Trafik Bilgilendirme Sorumlusu]
    B3 --> P11[Sinyal Optimizasyon ve Operasyon Raporlama Mühendisi]
```

## 4. Toplu Taşıma Planlama ve İşletme Şube Müdürlüğü

```mermaid
flowchart TD
    M[Toplu Taşıma Şube Müdürü]
    M --> B1[Hat, Sefer ve Kapasite Planlama Birimi]
    M --> B2[İşletmeci ve Hizmet Kalitesi Birimi]
    M --> B3[Toplu Taşıma Veri ve Akıllı Filo Birimi]

    B1 --> P1[Hat, Güzergâh ve Sefer Planlama Sorumlusu]
    B1 --> P2[Tarife, Maliyet ve Kapasite Planlama Uzmanı]
    B1 --> P3[Durak Hizmetleri Planlama Uzmanı]

    B2 --> P4[İşletmeci İlişkileri ve Sözleşme Teknik Kontrol Sorumlusu]
    B2 --> P5[Hizmet Kalitesi ve Şikâyet Yönetimi Sorumlusu]

    B3 --> P6[Toplu Taşıma Veri ve Performans Analisti]
    B3 --> P7[Akıllı Filo Operasyon Sorumlusu]
```

## 5. Ulaşım Ruhsat ve Ticari Araç İşlemleri Şube Müdürlüğü

```mermaid
flowchart TD
    M[Ulaşım Ruhsat ve Ticari Araç İşlemleri Şube Müdürü]
    M --> B1[Ruhsat, Vize ve Başvuru Birimi]
    M --> B2[Ticari Araç ve Özel İzinler Birimi]
    M --> B3[Belge, Tahakkuk ve Kalite Birimi]

    B1 --> P1[Ruhsat ve Vize Birim Sorumlusu]
    B1 --> P2[Başvuru, Belge ve Dijital Süreç Uzmanı]

    B2 --> P3[Servis Araçları İşlemleri Sorumlusu]
    B2 --> P4[Taksi ve Ticari Plaka İşlemleri Sorumlusu]
    B2 --> P5[Yük ve Özel Taşıma İzinleri Sorumlusu]

    B3 --> P6[Tahakkuk ve Tarife Kontrol Personeli]
    B3 --> P7[Arşiv, Mevzuat ve Kalite Kontrol Uzmanı]
```

## 6. UKOME Şube Müdürlüğü

```mermaid
flowchart TD
    M[UKOME Şube Müdürü]
    M --> B1[Gündem ve Dosya Kabul Birimi]
    M --> B2[Alt Komisyon ve Kurum Koordinasyon Birimi]
    M --> B3[Karar, Dağıtım ve Uygulama Takip Birimi]

    B1 --> P1[Gündem ve Dosya Kabul Sorumlusu]
    B1 --> P2[Dijital UKOME Sistem Sorumlusu]

    B2 --> P3[Alt Komisyon ve Kurumlar Arası Koordinasyon Sorumlusu]

    B3 --> P4[UKOME Karar Yazım Uzmanı]
    B3 --> P5[Karar Dağıtım, Tebligat ve Arşiv Sorumlusu]
    B3 --> P6[Karar Uygulama Takip Uzmanı]
```

## 7. Otogar İşletme Şube Müdürlüğü

```mermaid
flowchart TD
    M[Otogar İşletme Şube Müdürü]
    M --> B1[Terminal Operasyon ve Peron Birimi]
    M --> B2[Gişe, Tahakkuk ve Gelir Birimi]
    M --> B3[Teknik İşletme ve Güvenlik Koordinasyon Birimi]

    B1 --> P1[Terminal Operasyon ve Peron Sorumlusu]
    B1 --> P2[Vardiya Amiri]
    B1 --> P3[Gişe ve Saha Operasyon Personeli]

    B2 --> P4[Gişe ve Tahakkuk Sorumlusu]
    B2 --> P5[Kasa, Gelir Mutabakat ve Raporlama Sorumlusu]
    B2 --> P6[Firma ve Yetki Belgesi Kontrol Personeli]

    B3 --> P7[Terminal Teknik İşletme Sorumlusu]
    B3 --> P8[Güvenlik ve Ortak Hizmetler Koordinatörü]
```

## 8. İdari ve Mali İşler Şube Müdürlüğü

```mermaid
flowchart TD
    M[İdari ve Mali İşler Şube Müdürü]
    M --> B1[Bütçe, Performans ve Raporlama Birimi]
    M --> B2[İhale, Sözleşme ve Ödeme Dosyası Birimi]
    M --> B3[EBYS, Taşınır, Personel ve İç Kontrol Birimi]

    B1 --> P1[Bütçe, Performans ve Faaliyet Raporlama Sorumlusu]

    B2 --> P2[İhale ve Satın Alma Koordinatörü]
    B2 --> P3[Sözleşme, Teminat ve Hakediş Dosyası Sorumlusu]

    B3 --> P4[Taşınır Kayıt ve Ambar Sorumlusu]
    B3 --> P5[EBYS, Arşiv ve Personel İşleri Sorumlusu]
    B3 --> P6[Doküman Kontrol ve Mevzuat Takip Uzmanı]
    B3 --> P7[İç Kontrol, Risk ve Süreç Yönetimi Uzmanı]
    B3 --> P8[İdari Destek Personeli]
```

## Daire geneli ortak uzmanlık desteği

Aşağıdaki uzmanlıkların her şubede ayrı ayrı kurulması yerine ortak hizmet modeliyle çalışması önerilir:

- Hukuk ve Mevzuat Koordinatörü
- CBS Yöneticisi
- Veri Yönetişimi Sorumlusu
- Proje Yönetim Ofisi Uzmanı
- Kalite ve Süreç Yönetimi Uzmanı
- KVKK ve Bilgi Güvenliği Koordinatörü
- İş Sağlığı ve Güvenliği Koordinatörü
