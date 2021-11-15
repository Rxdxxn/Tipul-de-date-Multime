#Problema 11
import itertools
from itertools import combinations, chain
def submultimile(m, x):
	return list(map(set, itertools.combinations(m, x)))
def submultimile(m, y):
	return list(map(set, itertools.combinations(m, y)))
def submultimile(m, z):
	return list(map(set, itertools.combinations(m, z)))
m = {'A', 'B', 'C', 'D'}
x = 1
y = 2 
z = 3
print("Submultimile cu lungimea 1->",submultimile(m, x))
print("Submultimile cu lungimea 2->",submultimile(m, y))
print("Submultimile cu lungimea 3->",submultimile(m, z))
print("Submultimile cu lungimea 4->",m)