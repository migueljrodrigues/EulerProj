#NOT FINISHED
matrix = []

x = 20
y = 20
x += 1
y += 1
matrix = [[1] * (x)]
anterior = [1] * (x)
coiso = []
#print anterior
#print sum(anterior[:5])
for i in range(0,x):
	for j in range(0,y):
		#print j
		if j == 0:
			coiso.append(1)
		else:
			coiso.append(sum(anterior[:j+1]))
		#print coiso
	matrix.append(coiso)
	anterior = coiso
	coiso = []

print(anterior)
