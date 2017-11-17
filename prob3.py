def eh_inteiro(n):
	return (n - int(n)) == 0

def primes(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

num = 600851475143#				tem de dar 13 ou mais com o 143 600851475143
num2 = float(num)
final = num

prime_list = primes(int(num**0.5))

for var in prime_list:
	print var

	res = float(num2/var)

	if eh_inteiro(res):
		print str(var) + ' primo e inteiro'
		final = var

	var += 1

print "res final = " + str(final)