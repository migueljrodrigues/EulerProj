from math import floor, sqrt

def fac(n):
    step = lambda x: 1 + (x<<2) - ((x>>1)<<1)
    maxq = long(floor(sqrt(n)))
    d = 1
    q = n % 2 == 0 and 2 or 3 
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return q <= maxq and [q] + fac(n//q) or [n]

def res(lista):
	#print lista
	data = 1
	coiso = {}
	for i in lista:
		coiso[i] = lista.count(i)
		
	#print coiso
	for a,b in coiso.items():
		data *= (b+1)
	return data

primo = 1
factor = 1

var = res(fac(primo))

while var < 500:
	factor += 1
	primo += factor

	var = res(fac(primo))

print "solution " + str(primo)