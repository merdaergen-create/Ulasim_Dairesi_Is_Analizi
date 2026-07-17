# İdari ve Mali İşler — Sorumlu Pozisyonlu Süreç Haritaları

## İhale, sözleşme, hakediş ve ödeme dosyası

```mermaid
flowchart LR
 A["Onaylı ihtiyaç ve teknik belgeler<br/>Sorumlu: İlgili teknik şube"] --> B["İhale yöntemi ve dosya kontrolü<br/>Sorumlu: İhale ve Satın Alma Koordinatörü"]
 B --> C["Bütçe ve ödenek doğrulaması<br/>Sorumlu: Bütçe ve Performans Sorumlusu"]
 C --> D["İhale/EKAP ve sözleşme hazırlığı<br/>Sorumlu: İhale ve Satın Alma Koordinatörü"]
 D --> E["Sözleşme, teminat ve süre takvimi<br/>Sorumlu: Sözleşme ve Teminat Sorumlusu"]
 E --> F["Teknik kontrol, metraj ve kabul kanıtı<br/>Sorumlu: İlgili teknik şube"]
 F --> G["Hakediş ve ödeme evrakı kontrolü<br/>Sorumlu: Hakediş ve Ödeme Dosyası Sorumlusu"]
 G --> H["İç kontrol ve risk kontrolü<br/>Sorumlu: İç Kontrol ve Risk Sorumlusu"]
 H --> I{"Dosya tam mı?<br/>Onay: İdari ve Mali İşler Şube Müdürü"}
 I -- Hayır --> G
 I -- Evet --> J["Mali Hizmetlere ödeme için sevk<br/>Sorumlu: Hakediş ve Ödeme Dosyası Sorumlusu"]
```

## Bütçe, performans ve faaliyet raporu

```mermaid
flowchart LR
 A["Şube hedef ve bütçe talepleri<br/>Sorumlu: Bütçe ve Performans Sorumlusu"] --> B["Veri ve faaliyet konsolidasyonu<br/>Sorumlu: Faaliyet Raporlama Uzmanı"]
 B --> C["Risk ve kontrol değerlendirmesi<br/>Sorumlu: İç Kontrol ve Risk Sorumlusu"]
 C --> D["Bütçe-performans taslağı<br/>Sorumlu: Bütçe ve Performans Sorumlusu"]
 D --> E["Yönetim kontrolü<br/>Sorumlu: İdari ve Mali İşler Şube Müdürü"]
 E --> F["Mali Hizmetler/üst yönetime sunum<br/>Sorumlu: Bütçe ve Performans Sorumlusu"]
 F --> G["Gerçekleşme ve faaliyet raporu<br/>Sorumlu: Faaliyet Raporlama Uzmanı"]
```

## EBYS, personel, taşınır ve doküman kontrolü

```mermaid
flowchart LR
 A["Gelen evrak ve dağıtım<br/>Sorumlu: EBYS ve Arşiv Sorumlusu"] --> B{"İşlem türü<br/>Sorumlu: İdari ve Mali İşler Şube Müdürü"}
 B -- Personel --> C["İzin, görev ve personel yazışması<br/>Sorumlu: Personel ve İzin İşleri Sorumlusu"]
 B -- Taşınır --> D["TİF, ambar, zimmet ve sayım<br/>Sorumlu: Taşınır Kayıt ve Ambar Sorumlusu"]
 B -- Doküman --> E["Yönetmelik, yönerge ve görev tanımı kontrolü<br/>Sorumlu: Doküman Kontrol ve Mevzuat Takip Uzmanı"]
 C --> F["EBYS kayıt ve arşiv kapanışı<br/>Sorumlu: EBYS ve Arşiv Sorumlusu"]
 D --> F
 E --> G["Mevzuat/uygunluk kontrolü<br/>Sorumlu: İç Kontrol ve Risk Sorumlusu"]
 G --> F
```
