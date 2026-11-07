
# 1. Napisati funkciju get_even_positions(data: tuple) -> tuple koja
# vraća elemente torke koji se nalaze na parnim indeksima (0, 2, 4...).
# Input: (10, 20, 30, 40, 50, 60)
# Output: (10, 30, 50)

test = (10, 20, 30, 40, 50, 60)

def get_even_positions(data):
    data_list = list(data)
    true_data_list = []
    for i in range(0, len(data)):
        if i % 2 == 0:
            true_data_list.append(data_list[i])
    return tuple(true_data_list)

print(get_even_positions(test))





# 2. Napisati funkciju find_exclusive_students(group1: set, group2:set) -> set 
# koja vraća studente koji se nalaze u prvoj grupi, ali ne i u drugoj.

# Input: {'Ana','Marko','Jovan','Milica'},{'Marko','Milica','Petar'}
# Output: {'Ana','Jovan'}

test1 = {'Ana','Marko','Jovan','Milica'}
test2 = {'Marko','Milica','Petar'}

def find_exclusive_students(group1, group2):
    return group1 - group2

print(find_exclusive_students(test1, test2))





# 3. Napisati funkciju clean_tags(text: str) -> str koja obrađuje tekst sa tagovima.
# Potrebno je:
# -Razdvojiti tagove koji su odvojeni karakterom |
# -Ukloniti početne i krajnje razmake svakog taga
# -Sva slova pretvoriti u mala slova
# -Spojiti tagove karakterom -

# Input:' Python | DATA | SQL '
# Output:'python-data-sql'

test = ' Python | DATA | SQL '

def clean_tags(text):
    tags = text.split('|')
    for i in range(0, len(tags)):
        tags[i] = tags[i].strip().lower()
    return '-'.join(tags)

print(clean_tags(test))





# 4. Napisati funkciju count_products(csv_lines: list) -> dict koja analizira porudžbine iz CSV podataka 
# i vraća ukupan broj naručenih proizvoda.
# Svaki red sadrži ime kupca, naziv proizvoda i količinu, razdvojene zarezom. 
# Prvi red predstavlja zaglavlje i treba ga zanemariti.
# Ako se isti proizvod pojavljuje u više redova, sabrati njegove količine.

# Input: ['customer,product,quantity', 'Alice,laptop,2', 'Bob,mouse,3', 'Alice,laptop,1', 'Charlie,keyboard,2','Bob,mouse,1']

# Output: {'laptop': 3, 'mouse': 4, 'keyboard': 2}

test = ['customer,product,quantity', 'Alice,laptop,2', 'Bob,mouse,3', 'Alice,laptop,1', 'Charlie,keyboard,2','Bob,mouse,1']

def count_products(csv_lines):
    product_orders = {}
    for line in csv_lines[1:]:
        product_name = line.split(',')[1]
        product_quantity = line.split(',')[2]
        if product_name in product_orders:
            product_orders[product_name] = str(int(product_orders[product_name]) + int(product_quantity))
        else:
            product = [(product_name, product_quantity)]
            product_orders.update(product)
    return product_orders
        


print(count_products(test))