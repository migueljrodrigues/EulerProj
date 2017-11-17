x = 999
y = 999
sol = 0

while x > 101:

	y = 999

	while y > 101:

		var = x * y

		print var

		if var < 100000:
			myMap = map(int,str(var))

			#print str(myMap[0]) + ' ' + str(myMap[4])

			if (myMap[0] == myMap[4]) and (myMap[1] == myMap[3]):
				print var

				if var > sol:
					#print 'nova sol' + str(var)
					sol = var

		else:
			myMap = map(int,str(var))

			print str(myMap[0]) + ' ' + str(myMap[5])

			if (myMap[0] == myMap[5]) and (myMap[1] == myMap[4]) and (myMap[2] == myMap[3]):
				print var

				if var > sol:
					#print 'nova sol' + str(var)
					sol = var

		y -= 1

	x -= 1

print 'Solution ' + str(sol)