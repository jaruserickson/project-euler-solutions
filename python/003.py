def largest_pf(n):
	#runs in O(nlgn) time (divide and conquer optimization)
	x, largest = 2, 1
	while x ** 2 < n: 
	    #this runs in this order so is_prime(x) will only run when n % x == 0
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