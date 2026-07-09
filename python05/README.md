# Python05

## 📖 Genel Bakış

Bu modülde Python'un ileri seviye **Nesne Yönelimli Programlama (Object-Oriented Programming - OOP)** özellikleri üzerinde çalışıldı. Amaç; sürdürülebilir, genişletilebilir ve okunabilir yazılımlar geliştirebilmek için soyut sınıflar, kalıtım, protokoller, tip ipuçları ve veri işleme mimarilerini öğrenmektir.

Bu projede farklı veri tiplerini işleyen bir **Data Pipeline (Veri İşleme Hattı)** geliştirildi. Gelen veriler uygun işlemcilere yönlendirilir, doğrulanır, depolanır ve istenilen formatta dışarı aktarılır.

---

# 📚 Öğrenilen Kavramlar

## 1. Nesne Yönelimli Programlama (OOP)

Nesne yönelimli programlama; kodu sınıflar ve nesneler üzerinden organize etmeyi sağlayan bir programlama yaklaşımıdır.

Temel amaçları:

* Kod tekrarını azaltmak
* Okunabilirliği artırmak
* Bakımı kolaylaştırmak
* Genişletilebilir yazılımlar geliştirmek

Bu modülde OOP'nin dört temel prensibi üzerinde çalışıldı:

* Encapsulation (Kapsülleme)
* Inheritance (Kalıtım)
* Polymorphism (Çok Biçimlilik)
* Abstraction (Soyutlama)

---

## 2. Class (Sınıf) ve Object (Nesne)

**Class**, nesnelerin özelliklerini ve davranışlarını tanımlayan şablondur.

**Object**, bu şablondan oluşturulan örnektir.

Örneğin:

* `DataProcessor` bir sınıftır.
* `NumericProcessor()` ise bu sınıftan türetilen bir nesnedir.

---

## 3. Inheritance (Kalıtım)

Kalıtım, bir sınıfın başka bir sınıfın özelliklerini ve metotlarını devralmasını sağlar.

Bu projede:

* `DataProcessor`

  * `NumericProcessor`
  * `TextProcessor`
  * `LogProcessor`

şeklinde bir kalıtım yapısı kurulmuştur.

Avantajları:

* Ortak kod tek yerde yazılır.
* Kod tekrarını azaltır.
* Yeni processor eklemek kolaylaşır.

---

## 4. Abstract Class (Soyut Sınıf)

Soyut sınıflar doğrudan nesne oluşturmak için değil, diğer sınıflara temel oluşturmak için kullanılır.

Python'da `abc.ABC` kullanılarak oluşturulur.

Görevleri:

* Ortak değişkenleri tanımlamak
* Ortak metotları sağlamak
* Alt sınıfların belirli metotları yazmasını zorunlu kılmak

---

## 5. Abstract Method

Alt sınıfların mutlaka implement etmesi gereken metotlardır.

Bu projede:

* `validate()`
* `ingest()`

metotları abstract olarak tanımlanmıştır.

Bu sayede her processor kendi doğrulama ve veri ekleme mantığını yazmak zorundadır.

---

## 6. Type Hinting

Type Hinting, değişkenlerin ve fonksiyon parametrelerinin beklenen veri tiplerini belirtmek için kullanılır.

Örnek:

* `int`
* `str`
* `list[int]`
* `dict[str, str]`

Avantajları:

* Kod okunabilirliğini artırır.
* IDE desteğini güçlendirir.
* Hataların erken fark edilmesini sağlar.

---

## 7. typing.Any

Bazı fonksiyonlar her veri tipini kabul edebilir.

Bu durumda:

`typing.Any`

kullanılır.

Örneğin `validate()` metodu başlangıçta her türlü veriyi kabul eder ve daha sonra uygunluğunu kontrol eder.

---

## 8. Protocol

Protocol, sınıfların aynı davranışı göstermesini sağlayan bir arayüzdür.

Bu projede:

* CSVPlugin
* JSONPlugin

aynı `process_output()` metodunu implement eder.

Böylece DataStream hangi plugin'in kullanıldığını bilmeden çalışabilir.

---

## 9. Duck Typing

Python'da önemli olan nesnenin hangi sınıftan geldiği değil, gerekli davranışlara sahip olmasıdır.

Bir sınıf gerekli metotları içeriyorsa kullanılabilir.

Protocol yapısı bu mantığı destekler.

---

## 10. Polymorphism (Çok Biçimlilik)

Aynı isimdeki metotların farklı sınıflarda farklı davranış göstermesidir.

Örneğin:

* NumericProcessor.validate()
* TextProcessor.validate()
* LogProcessor.validate()

Hepsi aynı metodu kullanır fakat farklı veri tiplerini işler.

---

## 11. Encapsulation (Kapsülleme)

Sınıf içerisindeki verilerin doğrudan değiştirilmesini engeller.

Projede:

* `_storage`
* `_rank`
* `_total_processed`

değişkenleri kapsüllenmiştir.

---

## 12. isinstance()

Verinin beklenen tipte olup olmadığını kontrol etmek için kullanılır.

Bu projede:

* Sayısal veri kontrolü
* String kontrolü
* Dictionary kontrolü
* Liste kontrolü

için kullanılmıştır.

---

## 13. Exception Handling

Geçersiz veri geldiğinde sistem hata üretir.

Örneğin:

* ValueError
* IndexError

Bu sayede hatalı veriler pipeline'a eklenmez.

---

## 14. Plugin Mimarisi

Export işlemi doğrudan DataStream içerisinde yazılmamıştır.

Bunun yerine plugin sistemi oluşturulmuştur.

Yeni bir export formatı eklemek için yalnızca yeni bir plugin yazmak yeterlidir.

Bu yaklaşım yazılımı genişletilebilir hale getirir.

---

# 🏗 Proje Mimarisi

```text
                     DataStream
                          │
          ┌───────────────┼───────────────┐
          │               │               │
          ▼               ▼               ▼
 NumericProcessor   TextProcessor   LogProcessor
          │               │               │
          └───────────────┼───────────────┘
                          │
                    İşlenmiş Veriler
                          │
               ┌──────────┴──────────┐
               ▼                     ▼
          CSVPlugin             JSONPlugin
```

Bu yapı sayesinde:

* DataStream yalnızca yönlendirme yapar.
* Processor sınıfları yalnızca veri işlemekten sorumludur.
* Plugin sınıfları yalnızca çıktıyı üretir.

Her sınıf tek bir sorumluluğa sahiptir (**Single Responsibility Principle**).

---

# 🔄 Veri Akışı

```text
Gelen Veri
     │
     ▼
validate()
     │
     ▼
ingest()
     │
     ▼
_storage
     │
     ▼
output()
     │
     ▼
CSV / JSON Plugin
```

---

# 📦 Sınıfların Görevleri

## DataProcessor

Temel soyut sınıftır.

Görevleri:

* validate()
* ingest()
* output()
* get_stats()

---

## NumericProcessor

Sayısal verileri işler.

Kabul ettiği tipler:

* int
* float
* list[int]
* list[float]

---

## TextProcessor

Metinsel verileri işler.

Kabul ettiği tipler:

* str
* list[str]

---

## LogProcessor

Log kayıtlarını işler.

Kabul ettiği tipler:

* dict[str, str]
* list[dict[str, str]]

---

## DataStream

Pipeline'ın merkezidir.

Görevleri:

* Processor kaydetmek
* Veriyi uygun processor'a yönlendirmek
* İstatistikleri göstermek
* Export işlemini başlatmak

---

## CSVPlugin

İşlenmiş verileri CSV formatında dışarı aktarır.

---

## JSONPlugin

İşlenmiş verileri JSON formatında dışarı aktarır.

---

# 📁 Proje Yapısı

```text
python05/
│
├── ex00/
├── ex01/
├── ex02/
│   ├── data_pipeline.py
│   ├── DataProcessor
│   ├── NumericProcessor
│   ├── TextProcessor
│   ├── LogProcessor
│   ├── DataStream
│   ├── CSVPlugin
│   └── JSONPlugin
│
└── README.md
```

---

# 🎯 Bu Modülde Kazanılan Beceriler

* Nesne yönelimli programlama prensiplerini uygulamak
* Soyut sınıflar oluşturmak
* Abstract metotlar kullanmak
* Kalıtım yapıları kurmak
* Polymorphism mantığını uygulamak
* Protocol ile ortak arayüz tasarlamak
* Type Hinting kullanarak okunabilir kod yazmak
* Farklı veri tiplerini doğrulamak
* Plugin tabanlı genişletilebilir mimari geliştirmek
* Sorumlulukları sınıflar arasında doğru şekilde dağıtmak
* Daha temiz, modüler ve sürdürülebilir Python kodu geliştirmek
