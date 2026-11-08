
# 19. Написати функцију get_header(path: str) -> list која враћа заглавље CSV фајла
# Користити csv.reader и next()
# Input: 'data/raw/teams.csv'
# Output: ['team', 'city', 'points']

import csv
test_path = './teams.csv'
def get_header(path):
    with open(path, 'r') as f:
        header = next(csv.reader(f))
        return header

# Output:   ['team', 'city', 'points']





# 20. Написати функцију read_rows(path: str) -> list која враћа све редове CSV фајла без
# заглавља, као листу листи
# Користити csv.reader
# Input: 'data/raw/teams.csv'
# Output: [['FK Jedinstvo', 'Bela Palanka', '34'], ['FK Radnički', 'Niš', '41'],
# ['FK Rakovica', 'Beograd, Rakovica', '28'], ['FK Sloga', 'Kraljevo', '19']]

import csv
test_path = './teams.csv'

def read_rows(path):
    with open(path, 'r') as f:
        reader = csv.reader(f)
        lines = []
        for row in reader:
            lines.append(row)
        return lines[1:]

print(read_rows(test_path))

# Output: [['FK Jedinstvo', 'Bela Palanka', '34'], ['FK Radnički', 'Niš', '41'], ['FK Rakovica', 'Beograd, Rakovica', '28'], ['FK Sloga', 'Kraljevo', '19']]





# 21. Написати функцију total_points(path: str) -> int која враћа збир бодова свих тимова
# Користити csv.DictReader
# Input: 'data/raw/teams.csv'
# Output: 122

import csv
test_path = './teams.csv'

def total_points(path):
    with open(path, 'r') as f:
        teams = list(csv.DictReader(f))
        points = [int(t['points']) for t in teams]
        return sum(points)

print(total_points(test_path))

# Output: 122





# 22. Написати функцију write_rows(path: str, rows: list) -> None која листу листи уписује у CSV
# фајл
# Input: 'data/processed/people.csv', [['name', 'age'], ['Ana', 20], ['Marko', 22]]
# Садржај фајла након позива:
# name,age
# Ana,20
# Marko,22


import csv
test_path = './new_file.csv'
test_rows = [['name', 'age'], ['Ana', 20], ['Marko', 22]]

def write_rows(path, rows):
    with open(path, 'a') as f:
        csv.writer(f).writerows(rows)
    
print(write_rows(test_path, test_rows))

# Output: new_file.csv ->  name,age
#                          Ana,20
#                          Marko,22

# Napomena: svesno sam koristio append,
# tako da imam više upisa u taj .csv fajl 



# 23. Написати функцију write_dicts(path: str, rows: list) -> None која листу речника уписује у
# CSV фајл
# Користити csv.DictWriter; заглавља су кључеви првог речника
# Input: 'data/processed/people.csv', [{'name': 'Ana', 'age': 20}, {'name':
# 'Marko', 'age': 22}]
# Садржај фајла након позива:
# name,age
# Ana,20
# Marko,22

import csv
test_path = './people.csv'
test_rows = [{'name': 'Ana', 'age': 20}, {'name':'Marko', 'age': 22}]

def write_dicts(path, rows):
    with open(path, 'w') as f:
        header = []
        for row in test_rows[:1]:
            for info in row:
                header.append(info)
        writer = csv.DictWriter(f, fieldnames = header)
        writer.writeheader()
        writer.writerows(test_rows)
    

write_dicts(test_path, test_rows)


# Output: people.csv ->   name,age
#                         Ana,20
#                         Marko,22


