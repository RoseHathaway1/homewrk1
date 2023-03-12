n =int(input('Введите номер билета: '))
a =0
b =0
while n >=1000:
    c =n%10
    n =n//10
    a =a+c
else:
    print('a')
while n>0:
    c=n%10
    n=n//10
    b=b+c
else:
    print('b')
if a==b:
    print('Yes')
else:
    print('No')
