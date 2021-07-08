

def add_sum(stash=0, *args):
    for arg in map(str,args):
        if arg.isdigit():
            stash+=float(arg)
        elif arg=="x":
            print("Финальный результат:", stash)
            return(stash)
    print("Промежуточный результат:", stash)
    add_sum(stash, *input("Введите слагаемые через пробел, символ «X» завершит подсчёт:").split(" "))

def main():
    add_sum()

main()




