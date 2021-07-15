from itertools import count, cycle

my_list = []

for i in count(int(input("введите целое число меньше 13: "))):
    print(i)
    my_list.append(i)
    if i >= 13:
        break

step = 0
for el in cycle(my_list):
    print(el)
    step += 1
    if step > 100:
        break
