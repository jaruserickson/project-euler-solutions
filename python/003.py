def largest_pf(n):
	#runs in O(sqrt(n)) time
	x, largest = 2, 1
	while x ** 2 < n: 
		# runs as many times as can be divided by the prime.
		while n % x == 0:
			if x > largest:
				largest = x
			n //= x 
		x += 1
	return largest if largest > n else n


if __name__ == "__main__":
	print(largest_pf(600851475143))
	print(largest_pf(8))
	print(largest_pf(5))
	print(largest_pf(24))
	#print(largest_pf(961748941))