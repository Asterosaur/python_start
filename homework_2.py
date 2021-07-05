# 1
my_list = [1, "Two", True, 4.0, complex(1, 1)]

print(my_list)
for i, elem in enumerate(my_list):
    print(f"Элемент №{i + 1} является экземпляром {type(elem)}")

# 2

my_list = input("\n Введите элементы списка через пробел: \n").split(" ")
for i, elem in enumerate(my_list):
    if len(my_list) > 1 and i % 2 == 0 and i + 1 < len(my_list):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)

# 3

month = int(input("\n Введите номер месяца: \n")) % 12
seasons = ["нулябрь",
           "зима", "зима",
           "весна", "весна", "весна",
           "лето", "лето", "лето",
           "осень", "осень", "осень",
           "зима"]
print(f"\n Список говорит, что у вас на дворе {seasons[month]}")

seasons = {0: "нулябрь",
           1: "зима", 2: "зима",
           3: "весна", 4: "весна", 5: "весна",
           6: "лето", 7: "лето", 8: "лето",
           9: "осень", 10: "осень", 11: "осень",
           12: "зима"}

print(f"\n Словарь говорит, что у вас на дворе {seasons[month]}")

# 4
print("\nВведите слова через пробел: \n")
# my_list =
for el in input().split(" "):
    print(f"{el[0:9]}")

# 5
my_list = [7, 5, 3, 3, 2]
elem = int(input("\n Вводи новый элемент рейтинга: \n"))

my_list.append(elem)
my_list.sort()
my_list.reverse()

print(my_list)

# 6
goods = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]
result = dict()
for product in goods:
    for elem in product:
        if type(elem) == dict:
            for item in elem.items():
                if result.get(item[0]) == None:
                    result.update({item[0]:item[1]})
                else:
                    result[item[0]] = f"{result[item[0]]}, {item[1]}"

print(result)
