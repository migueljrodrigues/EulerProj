sum_squares = 0
squares_sum = 0

for i in range(1,101):
	sum_squares += i**2

	squares_sum += i

print sum_squares
print squares_sum

print str(squares_sum**2 - sum_squares)