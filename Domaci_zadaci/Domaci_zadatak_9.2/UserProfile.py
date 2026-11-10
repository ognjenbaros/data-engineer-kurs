# 2.Kreirati klasu UserProfile koja predstavlja profil korisnika.
    # Klasa treba da ima sledeće atribute:
        # username – korisničko ime;
        # email – imejl adresa;
        # city – grad;
        # active – informacija o tome da li je profil aktivan.
    # Prilikom kreiranja objekta, profil treba da bude aktivan.


class UserProfile:
    def __init__(self, username, email, city, active = True):
        self.username = username
        self.email = email
        self.city = city
        self.active = active
    
    # 1.change_email(email: str) -> UserProfile – menja imejl adresu korisnika i vraća objekat.

    def change_email(self, new_email):
        self.email = new_email
        return self
    
    # 2.change_city(city: str) -> UserProfile – menja grad korisnika i vraća objekat.

    def change_city(self, new_city):
        self.city = new_city
        return self
    
    # 3.deactivate() -> UserProfile – deaktivira profil i vraća objekat.

    def deactivate(self):
        self.active = False
        return self
    
    # 4.activate() -> UserProfile – aktivira profil i vraća objekat.

    def activate(self):
        self.active = True
        return self
    
    # 5.display_info() -> None – ispisuje sve informacije o korisniku.

    def display_info(self):
        print(f'Username: {self.username}, email: {self.email}, City: {self.city}, Profile active: {self.active}')