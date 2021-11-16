A=set(input('dati elementele multimii A:').split())
for a in A:
    if ((ord(a)>65)or(ord(a)<90)):
        break
B=set(input('dati elementele multimii B:').split())
for b in B:
        if ((ord(b)>65)or(ord(b)<90)):
            break
else:
    print('Introduceti doar litere mari!')
print("Reuniunea multimilor:",A.union(B))
print("Intersectia multimilor:",A.intersection(B))
print("Diferenta multimilor:",A.difference(B))
print("Diferenta multimilor:",B.difference(A))

