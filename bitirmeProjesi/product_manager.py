import os

class ProductManager:
    def __init__(self, file_name):
        self.file_name = file_name
        os.makedirs(os.path.dirname(self.file_name), exist_ok=True)
        self.file_handle = None
        self._open_file()

    def _open_file(self):
        if self.file_handle is None or self.file_handle.closed:
            self.file_handle = open(self.file_name, "a+")

    def close_file(self):
        if self.file_handle and not self.file_handle.closed:
            self.file_handle.close()

    def read_products_from_file(self):
        self.file_handle.seek(0)
        lines = self.file_handle.readlines()
        valid_lines = []
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 4:
                valid_lines.append(line)
        return valid_lines

    def filter_products_by_category(self, lines, category_filter):
        filtered_products = []
        for line in lines:
            try:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    product_name, category, price, stock = parts
                    if not category_filter or category_filter.lower() == category.lower():
                        filtered_products.append((product_name, category, price, stock))
            except:
                continue
        return filtered_products

    def print_products(self, products):
        if not products:
            print("Gösterilecek ürün yok.")
            return
        
        print("Ürünler:")
        for i, product in enumerate(products, start=1):
            try:
                product_name, category, price, stock = product
                print(f"{i}) Ad: {product_name}, Kategori: {category}, Fiyat: {price} TL, Stok: {stock}")
            except:
                continue

    def add_product_to_file(self, product_name, category, price, stock):
        try:
            with open(self.file_name, "a") as file:
                file.write(f"{product_name},{category},{price},{stock}\n")
        except Exception as e:
            print(f"Ürün eklenemedi: {e}")

    def delete_product_from_file(self, lines, index):
        removed_product = lines.pop(index).strip()
        try:
            with open(self.file_name, "w") as file:
                file.writelines(lines)
            return removed_product
        except Exception as e:
            print(f"Ürün silinemedi: {e}")
            return None

    def product_exists(self, product_name):
        lines = self.read_products_from_file()
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue
            existing_product_name, _, _, _ = parts
            if existing_product_name.lower() == product_name.lower():
                return True
        return False
