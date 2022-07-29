dic_list = [
    {'name': 'Brian', 'age': 30, 'score': 50},
    {'name': 'Alice', 'age': 18, 'score': 100},
    {'name': 'Mary', 'age': 18, 'score': 70},
    {'name': 'Bob', 'age': None, 'score': 60},
    {'name': 'Charlie', 'age': None, 'score': 50},
]

# Noneを含むソート
print(sorted(dic_list, key=lambda dic: (dic['age'] is None, dic['age'], dic['score'])))
