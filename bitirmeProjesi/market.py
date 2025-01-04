import os
from product_manager import ProductManager
from ui_manager import UIManager
from validators import validate_product_input
from constants import FILE_NAME

class Market:
    def __init__(self):
        self.product_manager = ProductManager(FILE_NAME)
        self.ui_manager = UIManager()

    def cleanup(self):
        self.product_manager.close_file()
        if os.path.exists(self.product_manager.file_name):
            self.ui_manager.print_with_newline(f"{self.product_manager.file_name} dosyası silindi.")
            os.remove(self.product_manager.file_name)

    def list_product(self, category_filter=None):
        try:
            lines = self.product_manager.read_products_from_file()
            if not lines:
                self.ui_manager.print_with_newline("Hiç ürün yok.")
            else:
                filtered_products = self.product_manager.filter_products_by_category(lines, category_filter)
                self.product_manager.print_products(filtered_products)
        except IOError as e:
            self.ui_manager.print_with_newline(f"Ürünler listelenemedi: {e}")

    def add_product(self):
        try:
            product_details = self.ui_manager.get_product_details()
            if self.product_manager.product_exists(product_details['name']):
                self.ui_manager.print_with_newline("Bu ürün zaten mevcut.")
                return

            is_valid, price, stock = validate_product_input(product_details['price'], product_details['stock'])
            
            if not is_valid:
                self.ui_manager.print_with_newline("Fiyat bir sayı olmalı ve stok miktarı bir tam sayı olmalı.")
                return

            self.product_manager.add_product_to_file(
                product_details['name'], 
                product_details['category'],
                price,
                stock
            )
            self.ui_manager.print_with_newline(f"{product_details['name']} eklendi.")
        except IOError as e:
            self.ui_manager.print_with_newline(f"Ürün eklenemedi: {e}")

    def delete_product(self):
        try:
            lines = self.product_manager.read_products_from_file()
            if not lines:
                self.ui_manager.print_with_newline("Hiç ürün yok.")
                return

            filtered_products = self.product_manager.filter_products_by_category(lines, None)
            self.product_manager.print_products(filtered_products)
            
            try:
                index = int(input("Silmek istediğiniz ürün numarasını girin: ")) - 1
                if 0 <= index < len(lines):
                    parts = lines[index].strip().split(",")
                    if len(parts) != 4:
                        self.ui_manager.print_with_newline("Geçersiz ürün formatı.")
                        return
                    removed_product = self.product_manager.delete_product_from_file(lines, index)
                    if removed_product:
                        self.ui_manager.print_with_newline(f"{removed_product.split(',')[0]} silindi.")
                else:
                    self.ui_manager.print_with_newline("Geçersiz ürün numarası.")
            except ValueError:
                self.ui_manager.print_with_newline("Geçersiz giriş.")
        except IOError as e:
            self.ui_manager.print_with_newline(f"Ürün silinemedi: {e}")

    def get_available_categories(self):
        lines = self.product_manager.read_products_from_file()
        categories = set()
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 4:
                categories.add(parts[1])  
        return sorted(list(categories))

    def update_product(self):
        try:
            lines = self.product_manager.read_products_from_file()
            if not lines:
                self.ui_manager.print_with_newline("Hiç ürün yok.")
                return

            self.product_manager.print_products(self.product_manager.filter_products_by_category(lines, None))
            self.ui_manager.print_with_newline()

            try:
                index = int(input("Güncellemek istediğiniz ürün numarasını girin: ")) - 1
                if 0 <= index < len(lines):
                    parts = lines[index].strip().split(",")
                    if len(parts) != 4:
                        self.ui_manager.print_with_newline("Geçersiz ürün formatı.")
                        return
                    product_name, category, price, stock = parts
                    self.ui_manager.print_with_newline(f"Mevcut Bilgiler: Ad: {product_name}, Kategori: {category}, Fiyat: {price} TL, Stok: {stock}")
                    new_name = input(f"Yeni Ad ({product_name}): ") or product_name
                    new_category = input(f"Yeni Kategori ({category}): ") or category
                    new_price = input(f"Yeni Fiyat ({price}): ") or price
                    new_stock = input(f"Yeni Stok ({stock}): ") or stock

                    is_valid, new_price, new_stock = validate_product_input(new_price, new_stock)
                    
                    if not is_valid:
                        self.ui_manager.print_with_newline("Fiyat bir sayı olmalı ve stok miktarı bir tam sayı olmalı.")
                        return

                    lines[index] = f"{new_name},{new_category},{new_price},{new_stock}\n"
                    with open(self.product_manager.file_name, "w") as file:
                        file.writelines(lines)
                    self.ui_manager.print_with_newline(f"{new_name} güncellendi.")
                else:
                    self.ui_manager.print_with_newline("Geçersiz ürün numarası.")
            except ValueError:
                self.ui_manager.print_with_newline("Geçersiz giriş.")
        except IOError as e:
            self.ui_manager.print_with_newline(f"Ürün güncellenemedi: {e}")

    def run(self):
        while True:
            choice = self.ui_manager.display_menu()
            
            if choice == "1":
                self.list_product()
                self.ui_manager.print_with_newline()
            elif choice == "2":
                self.add_product()
                self.ui_manager.print_with_newline()
            elif choice == "3":
                self.delete_product()
                self.ui_manager.print_with_newline()
            elif choice == "4":
                categories = self.get_available_categories()
                category_index_map = {}
                if categories:
                    self.ui_manager.print_with_newline("Mevcut Kategoriler:")
                    for i, cat in enumerate(categories, start=1):
                        print(f"{i}) {cat}")
                        category_index_map[str(i)] = cat
                    self.ui_manager.print_with_newline()
                selection = input("Hangi kategoriyi görmek istiyorsunuz? ")
                chosen_category = category_index_map.get(selection, None)
                if chosen_category:
                    self.list_product(category_filter=chosen_category)
                else:
                    self.ui_manager.print_with_newline("Geçersiz kategori seçimi.")
                self.ui_manager.print_with_newline()
            elif choice == "5":
                self.update_product()
                self.ui_manager.print_with_newline()
            elif choice == "6":
                self.ui_manager.print_with_newline("Çıkış yapıldı.")
                self.cleanup()
                self.ui_manager.print_with_newline()
                break
            else:
                self.ui_manager.print_with_newline("Geçersiz seçim.")
                self.ui_manager.print_with_newline()

if __name__ == "__main__":
    market = Market()
    market.run()