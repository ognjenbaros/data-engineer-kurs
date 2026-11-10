# 3.Kreirati klasu Product koja predstavlja proizvod u prodavnici.
    # Klasa treba da ima sledeće atribute:
        # name – naziv proizvoda;
        # price – cena proizvoda;
        # quantity – količina proizvoda na stanju.
    
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    # 1.change_price(new_price: float) -> Product 
    # menja cenu proizvoda ako je nova cena pozitivna. Vraća objekat.

    def change_price(self, new_price):
        if new_price >= 0:
            self.price = new_price
        return self
    

    # 2.add_stock(amount: int) -> Product 
    # povećava količinu proizvoda na stanju za zadati iznos ako je iznos pozitivan. Vraća objekat.

    def add_stock(self, amount):
        if amount > 0:
            self.quantity += amount
        return self


    # 3.sell(amount: int) -> Product
    # umanjuje količinu proizvoda na stanju ako ima dovoljno proizvoda i ako je količina pozitivna. Vraća objekat.

    def sell(self, amount):
        if amount >= 0 and self.quantity >= amount:
            self.quantity -= amount
        return self


    # 4.display_info() -> None – ispisuje informacije o proizvodu.

    def display_info(self):
        print(f'Product name: {self.name}, Quantity: {self.quantity}, Price: {self.price}')