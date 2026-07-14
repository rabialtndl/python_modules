# Python Import Laboratuvarı

Bu repo, Python'ın import (içe aktarma) mekanizmalarını, modül çözümleme (module resolution) sürecini ve paket hiyerarşisini test etmek için oluşturulmuş bir laboratuvar ortamıdır. 

Projeyi 4 temel aşamada ele alıyoruz. Aşağıda her bir yapının teknik detaylarını ve neden bu şekilde kurgulandıklarını bulabilirsiniz.

## 1. `__init__.py` ve Paket Yönetimi (The Alembic)
Python'da bir klasörün standart bir dizin (directory) değil, bir paket (package) olarak algılanması için içine `__init__.py` dosyası eklenir. Bu dosya, paket ilk kez import edildiğinde çalışan başlatma (initialization) betiğidir.

* **Kapsülleme (Encapsulation):** `__init__.py` içinde `__all__` listesi tanımlayarak dışarıya hangi fonksiyonların açılacağını (public API) belirleriz. `__all__ = ["create_air"]` dediğimizde, paketi kullanan biri gizli tutmak istediğimiz `create_earth` fonksiyonuna doğrudan erişemez.
* **Namespace Temizliği:** `import elements` kullandığınızda tüm modül belleğe alınır ve namespace kirliliği yaratmaz (`elements.create_fire()` şeklinde çağrılır). `from elements import create_fire` kullandığınızda ise fonksiyon doğrudan yerel namespace'e dahil olur. Hızlıdır ama isim çakışması (name collision) riski taşır.

## 2. Alias Kullanımı (Distillation)
Modül hiyerarşisi derinleştikçe, kullanıcıların fonksiyonlara erişmesi zorlaşabilir. `__init__.py` bu noktada bir köprü (gateway) görevi görür.

* **Paket Seviyesinde Alias:** `alchemy/potions.py` içindeki `healing_potion` fonksiyonunu `__init__.py` içerisinde `from .potions import healing_potion as heal` şeklinde dışarı açtık. Bu sayede kullanıcı, uzun uzun modül yolunu yazmak yerine doğrudan `alchemy.heal()` diyerek asıl fonksiyona erişebilir. Geliştirici deneyimi (DX) açısından kritik bir yöntemdir.

## 3. Mutlak (Absolute) ve Göreli (Relative) İçe Aktarmalar
Paket içi bağımlılıkları yönetmenin iki yolu vardır. İkisi de kullanım senaryosuna göre tercih edilmelidir.

* **Mutlak İçe Aktarma (Absolute Import):** 
  `from alchemy.potions import strength_potion`
  Arama işlemine daima projenin kök dizininden (`sys.path` üzerinden) başlar. Okunabilirliği çok yüksektir ve kodun nereden geldiği nettir. Paket dışından bir modül çağırılıyorsa mutlak import kullanmak zorunludur.
  
* **Göreli İçe Aktarma (Relative Import):**
  `from ..elements import create_air`
  Mevcut dosyanın konumunu referans alır. `.` mevcut dizini, `..` bir üst dizini ifade eder. Proje içindeki klasör isimleri değişse bile (örneğin `alchemy` klasörünün adını `magic` yapsanız bile) kod kırılmaz. Ancak bu dosyayı doğrudan `python recipes.py` şeklinde çalıştırırsanız (top-level script olarak), relative import hata verir. Göreli importlar sadece paket içi yapılarda çalışır.

## 4. Döngüsel Bağımlılık (Circular Dependency / Avoid the Explosion)
Projelerde en sık karşılaşılan ve çözümü en can sıkıcı olan mimari sorunlardan biridir. 

`A modülü` `B modülünü` import edip, `B modülü` de aynı anda `A modülünü` dosyanın en başında (top-level) import etmeye kalktığında oluşur. Python, modüllerin yüklenmesini bitiremediği için sonsuz bir döngüye girmek yerine `ImportError: cannot import name ... from partially initialized module` hatası fırlatır (dark_spellbook örneğinde olduğu gibi).

**Nasıl Çözülür?**
1. **Yerel İçe Aktarma (Local/Inline Import):** Import ifadesini dosyanın başına değil, fonksiyonun içine taşımak. Bu projede `light_spellbook.py` içinde yaptığımız gibi. Böylece import işlemi, dosya okunduğunda değil, fonksiyon ilk çağrıldığında çalışır (Lazy loading).
2. **Mimariyi Yeniden Kurmak:** İki modülün birbirine kesin ihtiyacı varsa, paylaştıkları ortak mantığı üçüncü bir `C modülüne` taşıyıp, ikisinin de o modülden beslenmesini sağlamak (Büyük projelerde en temiz çözümdür).