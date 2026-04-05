class Product:
    name: str
    code: int
    count: int
    price: int
    def __init__(self, name: str, code: int, count: int, price: int):
        self.name = name
        self.code = code
        self.count = count
        self.price = price
    def get_info(self) -> str:

        return f"Товар: {self.name}, Код: {self.code}, Количество: {self.count}, Цена: {self.price} руб."
    
    def update_quantity(self, amount: int) -> None:

        if amount >= 0:
            self.count = amount
            print(f"Количество товара '{self.name}' обновлено. Новое количество: {self.count}")
        else:
            print("Ошибка: количество не может быть отрицательным")
    
    def update_price(self, price: int) -> None:

        if price > 0:
            self.price = price
            print(f"Цена товара '{self.name}' обновлена. Новая цена: {self.price} руб.")
        else:
            print("Ошибка: цена должна быть положительной")

class Warehouse:
    
    def __init__(self):

        self.products = []
    
    def add_product(self, product: Product) -> None:
   
        # Проверяем, нет ли уже товара с таким кодом
        for existing_product in self.products:
            if existing_product.code == product.code:
                print(f"Ошибка: товар с кодом {product.code} уже существует на складе")
                return
        
        self.products.append(product)
        print(f"Товар '{product.name}' успешно добавлен на склад")
    
    def remove_product_by_code(self, code: int) -> None:
    
        for i, product in enumerate(self.products):
            if product.code == code:
                removed_product = self.products.pop(i)
                print(f"Товар '{removed_product.name}' с кодом {code} удален со склада")
                return
        
        print(f"Ошибка: товар с кодом {code} не найден на складе")
    
    def print_all_products(self) -> None:

        if not self.products:
            print("Склад пуст")
            return
        
        print("\n" + "="*60)
        print("СПИСОК ТОВАРОВ НА СКЛАДЕ:")
        print("="*60)
        
        for product in self.products:
            print(product.get_info())
        
        print("="*60)
        print(f"Всего товаров: {len(self.products)}")
        print()
        
    