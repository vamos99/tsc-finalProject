# Ürün Yönetim Sistemi

Bu proje, ürünlerin yönetimini sağlayan basit bir konsol uygulamasıdır. Kullanıcılar ürün ekleyebilir, silebilir, güncelleyebilir ve listeleyebilirler.

Bu projeyi geliştirirken clean code ve SOLID prensiplerine dikkat ederek kod kalitesini artırmaya çalıştım. Bu prensiplere ve kod kalitesini artırmaya çalışırken GPT-4 ve Claude 3.5 Sonnet'ten yardım aldım. Ayrıca, README dosyasını oluştururken de bu araçlardan faydalandım.

## Proje Yapısı

- `market.py`: Uygulamanın ana dosyası. Uygulamanın çalıştırılması ve ana işlevlerin yönetilmesi burada gerçekleştirilir.
- `product_manager.py`: Ürün yönetimi ile ilgili işlemleri içerir. Ürün ekleme, silme, güncelleme ve listeleme işlemleri burada yapılır.
- `ui_manager.py`: Kullanıcı arayüzü ile ilgili işlemleri içerir. Kullanıcıdan veri alma ve menü gösterme işlemleri burada yapılır.
- `validators.py`: Girdi doğrulama işlemlerini içerir. Ürün fiyatı ve stok miktarının doğrulanması burada yapılır.
- `constants.py`: Sabit değerleri içerir. Dosya yolları gibi sabit değerler burada tanımlanır.
- `data/product.txt`: Ürün verilerinin saklandığı dosya. Ürün bilgileri bu dosyada saklanır.

## Özellikler

- **Ürünleri Listele:** Tüm ürünleri listeler.
- **Ürün Ekle:** Yeni bir ürün ekler.
- **Ürün Sil:** Mevcut bir ürünü siler.
- **Belirli Kategori Ürünlerini Listele:** Belirli bir kategoriye ait ürünleri listeler.
- **Ürün Güncelle:** Mevcut bir ürünü günceller.
- **Çıkış:** Uygulamadan çıkar. `data/product.txt` dosyasını siler.

## Kod Detayları

### market.py

- `Market` sınıfı:
    - `run`: Kullanıcıdan menü seçeneklerini alır ve ilgili işlemleri gerçekleştirir.
    - `list_product`: Ürünleri listeler, isteğe bağlı olarak kategori filtresi uygular.
    - `add_product`: Yeni bir ürün ekler, ürünün mevcut olup olmadığını kontrol eder ve geçerli girişleri doğrular.
    - `delete_product`: Belirtilen ürünü siler.
    - `update_product`: Mevcut bir ürünü günceller.
    - `cleanup`: Uygulama kapatıldığında dosyayı siler.

### product_manager.py

- `ProductManager` sınıfı:
    - `read_products_from_file`: Dosyadan ürünleri okur.
    - `add_product_to_file`: Yeni bir ürünü dosyaya ekler.
    - `delete_product_from_file`: Belirtilen ürünü dosyadan siler.
    - `filter_products_by_category`: Belirli bir kategoriye ait ürünleri filtreler.
    - `print_products`: Ürünleri ekrana yazdırır.
    - `product_exists`: Ürünün mevcut olup olmadığını kontrol eder.

### ui_manager.py

- `UIManager` sınıfı:
    - `display_menu`: Kullanıcıya menü seçeneklerini gösterir ve kullanıcıdan seçim alır.
    - `get_product_details`: Kullanıcıdan ürün bilgilerini alır.
    - `print_with_newline`: Ekrana mesaj yazdırır ve yeni satır ekler.
    - `get_category_filter`: Kullanıcıdan kategori filtresi alır.

### validators.py

- `validate_product_input`: Ürün fiyatı ve stok miktarının doğrulanmasını sağlar. Fiyatın pozitif bir sayı, stok miktarının ise pozitif bir tam sayı olup olmadığını kontrol eder.

### constants.py

- `FILE_NAME`: Ürün verilerinin saklandığı dosyanın yolunu belirtir.
