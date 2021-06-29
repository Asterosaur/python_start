# Часть 1

num = int(input('Введите число\n'))
string = input('Введите строку\n')

print(num, string)
print('\n***\n')
# Часть 2

seconds = int(input('Введите время в секундах\n'))
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print("%02i:%02i:%02i" % (hours, minutes, seconds))
print('\n***\n')

# Часть 3
n = int(input('Введите число n\n'))
# n + nn + nnn
print(n * 123)
print('\n***\n')

# Часть 4

pos_int = int(input("Введите целое число\n"))

# Идем справа налево
max_digit = pos_int % 10
while pos_int > 0:
    # Берем последнюю цифру
    step = pos_int % 10
    # Сравниваем с текущим максимальным значением
    max_digit = max(max_digit, step)
    # Убираем последний разряд
    pos_int //= 10

print(max_digit)
print('\n***\n')

# Часть 5

income = int(input('Введите значение выручки\n'))
costs = int(input('Введите значение издержек\n'))

gains = income - costs
if gains > 0:
    staff_qty = int(input('Введите количество сотрудников\n'))
    print('Каждый из них получит по' + str(gains / staff_qty))
else:
    print('О НЕТ! ВЫ РАЗОРЕНЫ И ВЫХОДИТЕ В ОКНО КАК В ФИЛЬМЕ РОБОКОП ПОЛА ВЕРХОВЕНА '
          'ТЫСЯЧАДЕВЯТЬСОТВОСЕМЬДЕСЯТЛОХМАТОГО ГОДА ОН ЕЩЕ СНЯЛ ШОУ ГЕЛЗ И ЗВЕЗДЫНЙ ДЕСАНТ КАКОЙ ЖЕ ОН КРУТОЙ '
          'РЕЖИССЕР И ТЕБЕ ЛУЧШЕ ФИЛЬМЫ СМОТРЕТЬ А НЕ БИЗНЕСОМ УПРАВЛЯТЬ НЕУЧ')

print('\n***\n')

# Часть 6
daily_route = float(input('Скольк1о наш спортсмен пробежал за первый день?\n'))
expected_route = float(input('А сколько он должен пробежать в итоге?\n'))
iterator = 1
while daily_route < expected_route:
    iterator += 1
    daily_route *= 1.1

print("на " + str(iterator) + "-й день спортсмен достиг результата — не менее " + str(expected_route) + " км.")
