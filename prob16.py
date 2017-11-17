var = pow(2,1000)
var = str(var)
print var
soma = 0

for i in range(0,len(var)):
	soma += int(var[i])

print soma