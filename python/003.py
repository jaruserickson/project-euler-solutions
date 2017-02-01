def is_prime(n):
	#basic is_prime
	#runs in O(n)
	count = 0
	for x in range(2, n + 1):
		if n % x == 0:
			count += 1
	if count > 1:
		return False
	else:
		return True

def largest_pf(n):
	#runs in O(lgn) time (divide and conquer)
	largest, x = 1, 2
	while(x <= n): 
	    #this runs in this order so is_prime(x) will only run when n % x == 0
		if n % x == 0 and is_prime(x):
			if x > largest:
				largest = x
			n //= x 
		x += 1
	return largest


if __name__ == "__main__":
	print(largest_pf(600851475143))