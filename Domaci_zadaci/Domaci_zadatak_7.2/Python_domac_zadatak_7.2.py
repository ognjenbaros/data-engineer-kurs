

# 0.1. Napisati program kojim se prevodi temperatura iz Celzijusove skale u Farenhajtovu skalu,
# ako je odgovaraju´ca formula oblika T [◦F] = T [◦C] · 1.80 + 32. Na ulazu se unosi vrednost
# temperature u stepenima Celzijusa (realan broj) a ispisuje se vrednost temperature u stepenima
# Farenhajta.


def c_to_f(temperature):
    print(f'Temperature is {temperature * 1.8 +32} degrees Fahrenheit')

c_to_f(30)





# 0.2. Napisati program koji za uneti redni broj dana u nedelji (od 1 do 7) ispisuje naziv tog
# dana (ponedeljak - nedelja). Ukoliko je unet broj koji nije izmed¯u 1 i 7, ispisati Pogresan
# unos.


def day_in_week(day):
    if day is None or day < 1 or day > 7:
        print('Wrong entry')
    elif day == 1:
        print('Monday')
    elif day == 2:
        print('Tuesday')
    elif day == 3:
        print('Wednesday')
    elif day == 4:
        print('Thursday')
    elif day == 5:
        print('Friday')
    elif day == 6:
        print('Saturday')
    elif day == 7:
        print('Sunday')


days = [1, 2, 3, 4, 5, 6, 7]

for day in days:
    day_in_week(day)





# 0.3. Napisati program koji raˇcuna najve´ci negativni element u listi.


from math import inf
list = [1, 4, -5, 12, 0, 1, -14, -1, -2]

def max_negative(numbers):
    max_neg = float(-inf)
    for num in numbers:
        if num < 0 and num > max_neg:
            max_neg = num
    return max_neg

print(max_negative(list))





# 0.5. Napisati program koji raˇcuna broj parnih elemenata date liste

list = [-1, 4, -5, 12, -2, 1]

def count_even(numbers):
    counter = 0
    for num in numbers:
        if num % 2 == 0:
            counter = counter + 1
    return counter

print(count_even(list))





# 0.6. Napisati program koji raˇcuna sume elemenata liste celih brojeva koji su deljivi sa 2 
# odnosno sa 3.

# Ako smatramo da sabiramo elemente koji su deljivi sa 2 ili sa 3
# Druga opcija bi bila da se sabiraju samo elementi liste koji su deljivi i sa 2 i sa 3, tj 6


list1 = [-7, 12, 0, 18, -3, 5, 20, -10, 9, 14]
list2 = [-4, 7, 0, -2, 9, 3, -5, 6, 1, 10]

def sum_div2_div3(numbers):
    sum = 0
    for num in numbers:
        if num % 2 == 0 or num % 3 == 0:
            sum += num
    return sum

print(sum_div2_div3(list1))
print(sum_div2_div3(list2))