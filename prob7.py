def eh_primo(n):
	for i in range(3, n):
		if n % i == 0:
			return False
	return True

a = 1
n = 2

while a != 10001:

	n += 1
	
	myMap = map(int,str(n))
	#print myMap
	wvar = myMap[len(myMap)-1]
	#print wvar

	if wvar == 5 or wvar == 0 or wvar == 2:
		continue

	if eh_primo(n):
		a += 1
		print str(n) + ' eh o ' + str(a) + ' esimo primo' 

print n