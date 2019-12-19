def main():
    print('Количество команд: ', end='')
    n_str = input()
    n = int(n_str) if n_str else 0
    while 1:
        print('Напишите 1, чтобы узнать, сколько есть вариантов распределить первые три места. Напишите 2, чтобы узнать, сколько вариантов есть распределить все места : ')
        x = input()
        if  x == '1': 
            f3(n)
            return
        if x == '2':
            all(n)
            return
        if x != '1' and x != '2':
            print('Ошибка ввода, выберите пожалуйста "1" или "2"')

def f3(n):
    n = factorial(n) / factorial(n - 3)
    print(str(n))

def all(n):
    n = factorial(n)
    print(str(n))

def factorial(n):
    fac = 1
    while n > 1:
        fac *= n
        n -= 1
    return int(fac)


main()