

def fib(numb, current=2, a=0, b=1):
    current += 1
    if current < numb:
        fib(numb, current, b, a + b)
    elif current == numb:
        print('Число Фиббоначи номер {} - это'.format(numb), a + b)


def correct_input():
    while True:
        try:
            number = int(input())
            if number == 0:
                print('Конец')
                break
            elif number <= 2:
                print('Число Фиббоначи номер {} - это'.format(number), number - 1)
                break
            elif number >= 25:
                print('Слишком большое число, попробуйте ещё раз')
            else:
                return number
        except:
            print('Что-то пошло не так, попробуйте другое число, чтобы выйти введите 0')


fib(correct_input())
