# Daire Geneli Ortak Uzmanlıklar — Sorumlu Pozisyonlu Kontrol Haritaları

## Yeni veya değişen süreç/doküman kontrolü

```mermaid
flowchart LR
 A["Süreç/doküman değişiklik talebi<br/>Sorumlu: İlgili süreç sahibi"] --> B["Süreç ve RACI tasarımı<br/>Sorumlu: Kalite ve Süreç Yönetimi Uzmanı"]
 B --> C["Mevzuat etki analizi<br/>Sorumlu: Hukuk ve Mevzuat Koordinatörü"]
 C --> D["Risk ve iç kontrol analizi<br/>Sorumlu: İç Kontrol ve Risk Sorumlusu"]
 D --> E{"Veri veya sistem etkisi var mı?<br/>Sorumlu: Kalite ve Süreç Yönetimi Uzmanı"}
 E -- Veri --> F["Veri sahipliği, kalite ve saklama kontrolü<br/>Sorumlu: Veri Yönetişimi Sorumlusu"]
 E -- Kişisel veri/güvenlik --> G["KVKK ve bilgi güvenliği kontrolü<br/>Sorumlu: KVKK ve Bilgi Güvenliği Koordinatörü"]
 E -- CBS --> H["CBS veri modeli ve katman kontrolü<br/>Sorumlu: CBS Yöneticisi"]
 E -- Proje --> I["Kapsam, takvim, maliyet ve bağımlılık kontrolü<br/>Sorumlu: Proje Yönetim Ofisi Uzmanı"]
 F --> J["Nihai süreç/doküman paketi<br/>Sorumlu: Kalite ve Süreç Yönetimi Uzmanı"]
 G --> J
 H --> J
 I --> J
 J --> K["Yetkili makam onayı ve yayımlama<br/>Sorumlu: İlgili şube müdürü / Daire Başkanı"]
```

## Proje ve yatırım portföyü yönetişimi

```mermaid
flowchart LR
 A["Şubelerden proje teklifleri<br/>Sorumlu: İlgili şube müdürleri"] --> B["Portföy kaydı ve bağımlılık analizi<br/>Sorumlu: Proje Yönetim Ofisi Uzmanı"]
 B --> C["CBS ve konumsal çakışma kontrolü<br/>Sorumlu: CBS Yöneticisi"]
 C --> D["Veri, entegrasyon ve sistem etkisi<br/>Sorumlu: Veri Yönetişimi Sorumlusu"]
 D --> E["Mevzuat ve yetki kontrolü<br/>Sorumlu: Hukuk ve Mevzuat Koordinatörü"]
 E --> F["KVKK ve bilgi güvenliği kontrolü<br/>Sorumlu: KVKK ve Bilgi Güvenliği Koordinatörü"]
 F --> G["Risk ve kontrol planı<br/>Sorumlu: İç Kontrol ve Risk Sorumlusu"]
 G --> H["Süreç/KPI tasarımı<br/>Sorumlu: Kalite ve Süreç Yönetimi Uzmanı"]
 H --> I["Portföy önceliklendirme kararı<br/>Onay: Ulaşım Dairesi Başkanı"]
```

## İlke

Ortak uzmanlık pozisyonları teknik sürecin sahibi değildir. Bu roller; mevzuat, veri, CBS, proje, kalite, iç kontrol, KVKK ve bilgi güvenliği açısından bağımsız kontrol ve standart desteği sağlar.