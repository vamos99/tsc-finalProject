def validate_product_input(price, stock):
    try:
        price = float(price)
        if price < 0:
            raise ValueError("Fiyat negatif olamaz.")
        stock = int(stock)
        if stock < 0:
            raise ValueError("Stok miktarı negatif olamaz.")
        return True, price, stock
    except ValueError as e:
        return False, None, str(e)
