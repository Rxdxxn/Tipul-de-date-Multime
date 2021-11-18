nume=str(input('Introduceti numele:'))
print('Numele introdus este:' + str(nume))
res = False

for i in nume.split():
    if ord(str(i[0]))>=65 and ord(str(i[0]))<=90 and i.istitle() and ord(str(i[-1]))>=97 and ord(str(i[-1]))<=122:
        res = True
print('Este scris corect numele:' + str(res))
