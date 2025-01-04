class UIManager:
    @staticmethod
    def print_with_newline(message=""):
        if message:
            print(message)
        print()

    @staticmethod
    def display_menu():
        menu_options = {
            "1": "Ürünleri Listele",
            "2": "Ürün Ekle",
            "3": "Ürün Sil",
            "4": "Belirli Kategori Ürünlerini Listele",
            "5": "Ürün Güncelle",
            "6": "Çıkış"
        }
        print()
        print("\n".join([f"{key}) {value}" for key, value in menu_options.items()]))
        print()
        return input("Seçiminiz: ")

    @staticmethod
    def get_product_details():
        UIManager.print_with_newline()
        details = {
            'name': input("Ürün adı: "),
            'category': input("Kategori: "),
            'price': input("Fiyat: "),
            'stock': input("Stok miktarı: ")
        }
        UIManager.print_with_newline()
        return details

    @staticmethod
    def get_category_filter():
        UIManager.print_with_newline()
        category = input("Hangi kategori ürünlerini görmek istiyorsunuz? ")
        UIManager.print_with_newline()
        return category
