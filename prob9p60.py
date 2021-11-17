A=set(input('dati elementele multimii A:'))
B=set(input('dati elementele multimii B:'))
a=set()
b=set()
for i in A:
    if ord(str(i))>=65 and ord(str(i))<=90 :
        a.add(i)
for i in B:
    if ord(str(i))>=65 and ord(str(i))<=90 :
        b.add(i)
print("Reuniunea multimilor:",a.union(b))
print("Intersectia multimilor:",a.intersection(b))
print("Diferenta multimilor:",a.difference(b))
print("Diferenta multimilor:",b.difference(a))


