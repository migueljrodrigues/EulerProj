def divisible(n):
	for i in range(1,21):
		if n % i != 0:
			return False
	return True

var = 2520

print 'wait for it...'

while True:
	if divisible(var):
		print var
		break
	else:
		var += 2