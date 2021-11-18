nume_str=str(input('Introduceti numele:'))
print('Numele introdus este:' + str(nume_str))
res = False
for i in nume_str.split( ):
	if i.istitle( ):
		res = True
		break
print('Este scris corect numele:' + str(res))