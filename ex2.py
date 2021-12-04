class MyZeroDivisionError(ZeroDivisionError):
    def init(self, txt):
        self.txt = txt


if __name__ == '__main__':
    try:
        number_1 = int(input('Введите числитель: '))
        number_2 = int(input('Введите Знаминатель: '))
        if number_2 == 0:
            raise MyZeroDivisionError('нельзя вводить ноль')
    except MyZeroDivisionError as e:
        print(e)
    else:
        result = number_1 / number_2
        print(f'{result}')
