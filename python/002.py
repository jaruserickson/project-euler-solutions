def even_fib(n):
	total = 2
	prior, even = 1, 2
	while even <= n:
		prior, even = (2 * even + prior), (3 * even + 2 * prior)
		if even <= n:
			total += even
	return total

if __name__ == "__main__":
	print("algo main:", even_fib(4000000))
