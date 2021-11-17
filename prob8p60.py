A=set(input('dati elementele multimii A:'))
B=set(input('dati elementele multimii B:'))
a=set()
b=set()
for i in A:
    if ord(str(i))>=48 and ord(str(i))<=57 :
        a.add(int(i))
for i in B:
    if ord(str(i))>=48 and ord(str(i))<=57 :
        b.add(int(i))
print("Reuniunea multimilor:",a.union(b))
print("Intersectia multimilor:",a.intersection(b))
print("Diferenta multimilor:",a.difference(b))
print("Diferenta multimilor:",b.difference(a))


