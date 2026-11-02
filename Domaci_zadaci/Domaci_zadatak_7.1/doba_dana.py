# Određivanje doba dana
# Napisati Python program koji za svaki sat u toku dana
# (od 0 do 23) ispisuje odgovarajuće doba dana:
    
# noć (od 22 do 6 časova),
# jutro (od 6 do 12 časova),
# popodne (od 12 do 18 časova) ili
# veče (od 18 do 22 časa).

# Sačuvati program u fajlu doba_dana.py u lokalnom repozitorijumu 
# naziv_po_želji, a zatim izvršiti commit i push iz VS Code-a.



for hour in range(0, 24):
    if hour >= 6 and hour < 12:
        print(f'{hour} je sati, dobro jutro!')
    elif hour >= 12 and hour < 18:
        print(f'{hour} je sati, popodne je!')
    elif hour >= 18 and hour < 22:
        if hour == 21:
            print(f'{hour} je sat, dobro veče!')
        else:
            print(f'{hour} je sati, dobro veče!')
    else:
        if hour == 0:
            print('Ponoć je, zašto ne spavaš?')
        elif hour == 1: 
            print(f'{hour} je sat, noć je, zašto ne spavaš?')
        elif hour >= 2 and hour <= 4:
            print(f'{hour} je sata, noć je, zašto ne spavaš?')
        else:
            print(f'{hour} je sati, noć je, zašto ne spavaš?')





