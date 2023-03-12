n =int(input('Введите колличество сделаных журавликов: '))
if n%6!=0:
    print('Решения нет')
else:
    a =int(n/6)
    b =int((n/6)*4)
    c =int(n/6)
print(a, b, c)
