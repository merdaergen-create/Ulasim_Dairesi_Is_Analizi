from __future__ import annotations

import re
from pathlib import Path

ROOT = Path('10_yalin_pozisyon_gorev_tanimlari')
FILES = sorted(p for p in ROOT.glob('*.md') if p.name != 'README.md')
SECTION_RE = re.compile(r'(?ms)^(##\s+\d+\.\s+.+?)\n(.*?)(?=^##\s+\d+\.\s+|^##\s+Ortak hükümler|\Z)')
FIELD_RE = re.compile(r'^\*\*(.+?):\*\*\s*(.*)$', re.M)

ROLE_RULES = [
    ('Şube Müdürü', [
        'Şubenin yıllık iş programını, hedeflerini, kaynak ihtiyacını ve performans göstergelerini belirler.',
        'Şubeye ait süreçlerin tek hesap verebilir sahibi olarak görev dağılımını ve iş yükü dengesini yönetir.',
        'Teknik, idari, mali ve kurul süreçlerindeki yetki sınırlarını gözetir; görev çakışmalarını giderir.',
        'Kritik karar, risk, gecikme ve uygunsuzlukları Ulaşım Dairesi Başkanına raporlar.',
        'Birimler arası koordinasyonu, vekâlet ve yedekleme düzenini yazılı olarak kurar.',
        'Mevzuat, iç kontrol, kişisel veri, bilgi güvenliği ve iş sağlığı-güvenliği gerekliliklerinin uygulanmasını sağlar.',
        'Süreç KPI sonuçlarını periyodik olarak değerlendirir ve düzeltici/önleyici faaliyet başlatır.',
        'Onaya sunulan proje, rapor, karar veya belge dosyalarının bütünlük ve kalite kontrolünü yaptırır.',
    ]),
    ('Birim Sorumlusu', [
        'Birim iş programını hazırlar, görevleri personele dağıtır ve günlük/haftalık gerçekleşmeyi izler.',
        'Sorumlu olduğu süreç adımlarının süre, kalite, kayıt ve kapanış şartlarını yerine getirir.',
        'Teknik inceleme, kontrol ve raporların standartlara uygun hazırlanmasını sağlar.',
        'Eksik belge, uygunsuzluk, gecikme ve kritik riski kayıt altına alarak şube müdürüne bildirir.',
        'İlgili şubeler, kurumlar, yükleniciler ve başvuru sahipleriyle görev alanı ölçüsünde koordinasyon yürütür.',
        'Birim kayıtlarının EBYS/kurumsal sistemde güncel, izlenebilir ve erişim kontrollü tutulmasını sağlar.',
        'Personel yedekleme, iş devri ve dosya kapanış kontrollerini yürütür.',
    ]),
    ('Sorumlusu', [
        'Görev alanına giren başvuru, talep, olay veya iş emrini kaydeder ve önceliklendirir.',
        'İlgili süreç haritasındaki sorumlu adımları süre ve kalite kriterlerine uygun yürütür.',
        'Girdi belge ve verilerinin tamlık, güncellik ve tutarlılık kontrolünü yapar.',
        'Teknik/operasyonel değerlendirmeyi gerekçeli biçimde hazırlar; gerekli görüşleri toplar.',
        'Sonuç, karar, uygulama veya teslim kaydını kurumsal sisteme işler ve kapanış kanıtını oluşturur.',
        'Uygunsuzluk ve sapmalar için düzeltici faaliyet başlatır, gerçekleşmeyi izler.',
        'Yetki sınırını aşan konuları birim sorumlusu veya şube müdürüne iletir.',
    ]),
    ('Koordinatörü', [
        'İlgili iç ve dış paydaşların görev, süre, görüş ve teslim yükümlülüklerini koordine eder.',
        'Toplantı, saha incelemesi, yazışma ve takip takvimini oluşturur.',
        'Gecikme, görüş ayrılığı ve bağımlılıkları görünür hale getirerek çözüm için yönetime sunar.',
        'Koordinasyon kararları ile teslim kanıtlarını kayıt altına alır.',
        'Yetkili karar mercii yerine geçmeden süreç akışının tamamlanmasını sağlar.',
    ]),
    ('Uzmanı', [
        'Görev alanına ilişkin mevzuat, standart, veri ve teknik kriterleri izler ve uygular.',
        'Analiz, inceleme, kontrol veya değerlendirme çalışmalarını kanıta dayalı yürütür.',
        'Alternatifleri karşılaştırır; bulgu, risk ve önerileri gerekçeli rapora dönüştürür.',
        'Kullanılan veri, yöntem, varsayım ve kaynakların izlenebilirliğini sağlar.',
        'İlgili süreç kayıtlarını ve formlarını eksiksiz oluşturur.',
        'Mesleki uzmanlık gerektiren konularda birim ve şube yönetimine görüş verir.',
    ]),
    ('Mühendisi', [
        'Teknik tasarım, analiz, kontrol, test ve kabul çalışmalarını yürürlükteki standartlara göre yapar.',
        'Teknik hesap, çizim, konfigürasyon, test sonucu ve değişiklik kayıtlarını izlenebilir tutar.',
        'Arıza, risk ve uygunsuzlukların kök nedenini değerlendirir; çözüm ve önleyici faaliyet önerir.',
        'Saha, sistem, proje ve işletme koşullarının birbiriyle uyumunu doğrular.',
        'Yetkili komisyon veya karar merciinin yerine geçmeden teknik görüş ve kanıt üretir.',
    ]),
    ('Amiri', [
        'Vardiya başlangıcında görev dağılımını, açık işleri, kritik riskleri ve sistem durumunu kontrol eder.',
        'Olay ve işlerin önceliklendirilmesini yapar, gerekli eskalasyonu zamanında gerçekleştirir.',
        'Vardiya kayıtlarının tamlığını ve bir sonraki vardiyaya devir kalitesini doğrular.',
        'Personel, saha ve sistem güvenliği kurallarının uygulanmasını sağlar.',
        'Kritik olayları ilgili birim sorumlusu ve şube müdürüne raporlar.',
    ]),
    ('Operatörü', [
        'Yetkili olduğu sistem ve ekranları prosedürlere uygun izler ve kullanır.',
        'Alarm, olay, sapma ve kullanıcı bildirimlerini doğrular ve kayıt altına alır.',
        'Tanımlı ilk müdahale adımlarını uygular; yetkisini aşan durumları vardiya amirine aktarır.',
        'Yapılan işlem, bildirim ve sonuçları zaman damgalı olarak sisteme işler.',
        'Kişisel ve operasyonel verilere yalnız görev gereği ve rol bazlı erişir.',
    ]),
    ('Personeli', [
        'Kendisine verilen başvuru, kayıt, kontrol, saha veya destek görevlerini talimatlara uygun yerine getirir.',
        'Belge, veri ve işlem kayıtlarının tamlık ve doğruluğunu kontrol eder.',
        'İşlem sonucunu ilgili sorumluya iletir ve kapanış kaydını tamamlar.',
        'Yetkisini aşan kararları almaz; uygunsuzluk ve riski derhal amirine bildirir.',
        'Kişisel veri, bilgi güvenliği, iş sağlığı ve güvenliği kurallarına uyar.',
    ]),
]

DEFAULT_DUTIES = [
    'Görev alanına ilişkin süreç adımlarını, onaylı iş akışı ve görev tanımına uygun yürütür.',
    'İşlemlerin zamanında, doğru, kayıtlı ve denetlenebilir biçimde tamamlanmasını sağlar.',
    'Eksiklik, uygunsuzluk ve riskleri kayıt altına alarak yetkili amirine bildirir.',
    'İlgili birimlerle koordinasyon kurar ve süreç kapanış kanıtını oluşturur.',
]


def field(body: str, name: str, default: str = 'İlgili süreç haritaları ve birim iş programında tanımlanan kayıtlar.') -> str:
    for m in FIELD_RE.finditer(body):
        if m.group(1).strip().casefold() == name.casefold():
            value = m.group(2).strip()
            if value:
                return value
    return default


def bullets_for(title: str, body: str) -> list[str]:
    existing = []
    m = re.search(r'(?ms)^\*\*Görevler:\*\*\s*(.*?)(?=^\*\*|^###|\Z)', body)
    if m:
        text = m.group(1).strip()
        existing = [x.strip('- ').strip() for x in text.splitlines() if x.strip()]
    for key, rules in ROLE_RULES:
        if key in title:
            return list(dict.fromkeys(existing + rules))
    return list(dict.fromkeys(existing + DEFAULT_DUTIES))


def compact_source(body: str) -> str:
    lines = []
    for line in body.splitlines():
        if line.strip() and not line.startswith('**Birim:**'):
            lines.append(line.strip())
    return ' '.join(lines)[:1400]


def rebuild(header: str, body: str) -> str:
    title = re.sub(r'^##\s+\d+\.\s+', '', header).strip()
    unit = field(body, 'Birim', 'İlgili organizasyon birimi.')
    purpose = field(body, 'Amaç', f'{title} görev alanındaki işlerin düzenli, izlenebilir ve mevzuata uygun yürütülmesini sağlamak.')
    reporting = field(body, 'Bağlılık', 'İlgili birim sorumlusu veya şube müdürü.')
    processes = field(body, 'Süreç adımları', field(body, 'Süreç adımları ve görevler', 'İlgili süreç haritalarında bu pozisyona atanan adımlar.'))
    inputs = field(body, 'Girdiler', 'Başvuru/talep, kurum görüşü, teknik veri, mevzuat, önceki karar ve birim iş programı.')
    outputs = field(body, 'Çıktılar', 'Kontrol edilmiş kayıt, teknik/operasyonel sonuç, rapor, bildirim ve kapanış kanıtı.')
    authority = field(body, 'Yetki sınırı', 'Kendi görev alanındaki inceleme, kayıt, koordinasyon ve teknik/operasyonel görüşle sınırlıdır; kurul, ihale, kabul veya mali ödeme yetkisi ayrıca verilmedikçe kullanılamaz.')
    kpi = field(body, 'KPI', 'Zamanında tamamlama, ilk seferde doğruluk, tekrar işlem oranı, açık uygunsuzluk ve kayıt tamlığı.')
    duties = bullets_for(title, body)
    duty_md = '\n'.join(f'- {d}' for d in duties)
    source = compact_source(body)
    return f'''{header}\n\n**Birim:** {unit}\n\n**Pozisyonun amacı:** {purpose}\n\n**Organizasyonel bağlılık:** {reporting}\n\n**Vekâlet ve yedekleme:** Yazılı görevlendirilen, gerekli yetkinliğe ve sistem erişimine sahip personel tarafından yürütülür; açık işler, süreler, riskler ve kayıtlar devir tutanağıyla aktarılır.\n\n**Sorumlu olduğu süreçler ve adımlar:** {processes}\n\n### Temel görev ve sorumluluklar\n{duty_md}\n\n### Yetki ve karar sınırları\n- {authority}\n- Mevzuatla başka bir makam veya komisyona verilen karar, onay, yaptırım, kabul ve ödeme yetkisini kullanmaz.\n- Kişisel, ticari veya operasyonel verilere yalnız görev ve rol yetkisi ölçüsünde erişir.\n\n### Süreç girdileri\n{inputs}\n\n### Üretilen çıktılar ve kayıtlar\n{outputs}\n\n### Koordinasyon ilişkileri\n- Bağlı bulunduğu birim ve şube yönetimiyle düzenli iş ve performans takibi yapar.\n- Süreç haritasında görüşü alınan veya bilgilendirilen diğer şube, kurum ve paydaşlarla kayıtlı koordinasyon yürütür.\n- İdari/mali dosya, kurul kararı, hukuk, bilgi işlem, KVKK ve İSG konularında yetkili yapılarla görev sınırları içinde çalışır.\n\n### Kullanılan kayıt ve formlar\n- `12_formlar` içindeki ilgili süreç koduna ve süreç adımına bağlı formlar.\n- EBYS, iş emri, başvuru, karar, kontrol, teslim, kabul, olay, uygunsuzluk ve kapanış kayıtlarından görev alanına uygun olanlar.\n- Kayıt numarası, tarih, sorumlu, ek ve kapanış kanıtı bulunmayan işlem tamamlanmış sayılmaz.\n\n### Performans göstergeleri\n{kpi}\n\n### Mesleki ve davranışsal yetkinlikler\n- Görev alanına ilişkin mevzuat, süreç ve kurumsal doküman bilgisi.\n- Analitik düşünme, kayıt disiplini, sonuç ve hizmet odaklılık.\n- Yazılı ve sözlü iletişim, paydaş koordinasyonu ve problem çözme.\n- Kurumsal sistemleri kullanma, veri güvenliği ve gizlilik farkındalığı.\n- Pozisyonun teknik niteliğine göre gerekli mesleki bilgi ve uygulama yetkinliği.\n\n### Görev ayrılığı ve iç kontrol\n- Talebi oluşturan, teknik kontrolü yapan, onaylayan, kabul eden ve ödeme işlemini yapan roller gerektiğinde farklı kişilerce yürütülür.\n- Kendi hazırladığı işin bağımsız kabul veya mali kontrolünü tek başına yapmaz.\n- Uygunsuzluğu gizlemez; kanıtı, gerekçeyi ve düzeltici faaliyeti kayıt altına alır.\n\n### Kaynak dayanağı\nBu tanımın süreç kapsamı mevcut dosyadaki içerik ile `05_surec_haritalari`, `14_yalin_organizasyon_semasi`, `15_yalin_surec_haritalari` ve `12_formlar` eşleştirmesine dayanır. Önceki metnin özeti: {source}\n\n'''


def process_file(path: Path) -> None:
    text = path.read_text(encoding='utf-8')
    matches = list(SECTION_RE.finditer(text))
    if not matches:
        return
    prefix = text[:matches[0].start()]
    suffix_start = matches[-1].end()
    suffix = text[suffix_start:]
    sections = [rebuild(m.group(1), m.group(2)) for m in matches]
    common = '''## Ortak hükümler\n\n- Tüm pozisyonlar görevlerini yürürlükteki mevzuat, onaylı süreç haritaları, görev ayrılığı ve yetki devri kurallarına uygun yürütür.\n- Süreç kayıtları EBYS veya yetkili kurumsal sistemde tutulur; kişisel ve operasyonel verilere rol bazlı erişilir.\n- Görev devri ve vekâlet yazılı yürütülür; açık iş, süre, risk, belge ve sistem erişimleri devir kaydına bağlanır.\n- Kritik risk, mevzuata aykırılık, çıkar çatışması, bilgi güvenliği olayı ve iş sağlığı-güvenliği tehlikesi gecikmeden amire bildirilir.\n- Bu görev tanımları norm kadro, unvan, atama şartı veya mali yetki ihdas etmez; yürürlüğe alma öncesinde yetkili birimlerce doğrulanır.\n'''
    if '## Ortak hükümler' in suffix:
        suffix = ''
    path.write_text(prefix + ''.join(sections) + common, encoding='utf-8')


def main() -> None:
    for path in FILES:
        process_file(path)

    readme = ROOT / 'README.md'
    text = readme.read_text(encoding='utf-8')
    marker = '## Profesyonel görev tanımı standardı'
    if marker not in text:
        text += f'''\n\n{marker}\n\nHer pozisyon; birim, amaç, bağlılık, vekâlet, sorumlu süreçler, temel görev ve sorumluluklar, yetki sınırları, girdiler, çıktılar, koordinasyon, kayıt/form, KPI, yetkinlik ve görev ayrılığı başlıklarıyla standardize edilmiştir.\n\nKaynaklarda açıkça desteklenmeyen diploma, sertifika, hizmet süresi veya kadro şartları kesin hüküm olarak eklenmemiştir. Bu şartlar yürürlüğe alma aşamasında İnsan Kaynakları, norm kadro ve ilgili mevzuat çerçevesinde belirlenmelidir.\n'''
        readme.write_text(text, encoding='utf-8')


if __name__ == '__main__':
    main()
