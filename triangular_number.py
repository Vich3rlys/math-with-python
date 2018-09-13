# author : vicherlys
from math import sqrt,floor
p,n,t,d=print, input("Entrez un nombre : "),lambda x : (((sqrt((8*x)+1))-1)/2),False
while not d:
 try:
  n = int(n)
  d = True
 except ValueError as _:
	 n = input("Entrez un nombre valide: ")
r=t(n)
if r-floor(r) == 0:
 p("%d est le nombre triangulaire n* %d"%(n,r))
else:
 p("%d n'est pas un nombre triangulaire"%(n))
