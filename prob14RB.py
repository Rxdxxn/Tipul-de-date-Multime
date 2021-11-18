def intersection(x,y):
    z=[value for value in x if value in y]
    return z
x=input("Dati primul sir")
y=input("Dati al doilea sir")
print(intersection(x,y))
