import random

def rands():
	return (random.randint(1,900))

def getMN():
	m = rands()
	n = rands()
	while m <= n:
		m = rands()
		n = rands()
	return [m,n]

while True:

	l = getMN()

	m = l[0]
	n = l[1]

	a = m**2 - n**2
	b = m*n*2
	c = m**2 + n**2

	#print str(a+b+c)

	if (a+b+c == 1000):
		break

print str(a) + ' ' + str(b) + ' ' + str(c)
print str(a*b*c)


