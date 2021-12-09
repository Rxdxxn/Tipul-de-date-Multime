with open('desktop/input.txt', 'r') as f:
  lista1=f.readlines()
print('Numarul	Numele	Prenumele	Nota1	Nota2	Nota3\n',*lista1)
with open('desktop/REZERVA.txt','w') as f:
    for i in lista1:
        f.write(i)
for i in lista1:
    lista2=i.split()
    a=lista2[0]+' '+lista2[1]+' '+lista2[2]
    media=str((float(lista2[3])+float(lista2[4])+float(lista2[5]))/3)
    b=a+' '+media+'\n'
    with open('desktop/OUTPUT.txt','a') as f:
        f.write(b)
with open('desktop/OUTPUT.txt','r') as f:
    lista3=f.readlines()
print('Numarul	Numele	Prenumele	Media',*lista3)