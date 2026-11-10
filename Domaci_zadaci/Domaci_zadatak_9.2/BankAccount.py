# 1.Kreirati klasu BankAccount koja predstavlja bankovni račun.
    # Klasa treba da ima sledeće atribute:
        # owner – ime vlasnika računa;
        # balance – trenutno stanje na računu.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # 1.deposit(amount: float) -> BankAccount – uvećava stanje na
    # računu za zadati iznos. Ako je iznos pozitivan, izvršava uplatu.
    # Vraća objekat nad kojim je metoda pozvana.
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self
    

    # 2.withdraw(amount: float) -> BankAccount – umanjuje stanje
    # na računu za zadati iznos. Isplata se izvršava samo ako je
    # iznos pozitivan i ako na računu ima dovoljno novca. Vraća
    # objekat nad kojim je metoda pozvana.

    def withdraw(self, amount):
        if amount > 0 and self.balance > amount:
            self.balance -= amount
        return self


    # 3.display_balance() -> None – ispisuje trenutno stanje na računu.

    def display_balance(self):
        return self.balance
    

    def __repr__(self):
        return f'Bank Account \nOwner: {self.owner} \nBalance: {self.balance}'