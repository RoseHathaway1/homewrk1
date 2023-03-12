n = int(input('Введите высоту шоколадки'))
m = int(input('Введите ширину шоколадки'))
k = int(input('Введите колличество долек'))
if k<n*m and (k%n==0 or k%m==0):
    print ('Yes')
else:
    print ('No')