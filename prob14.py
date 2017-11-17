def evenodd(lista,n):
	lista.append(n)
	if n == 1:
		return lista
	else:
		return evenodd(lista,n/2) if n%2 == 0 else evenodd(lista,n*3+1)

num_max_tam = 0
max_tam = 0
lista = []

#TODO save vars to avoid repetition
for i in range(2,1000000):
	var = i
	#print i 
	res = evenodd(lista,var)

	if len(res) > max_tam:
		max_tam = len(res)
		#print max_tam
		#print res
		num_max_tam = res[0]
		#print num_max_tam
	lista = []

print num_max_tam
