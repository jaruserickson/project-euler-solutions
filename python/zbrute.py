#DISCLAIMER:
# this file is for testing purposes only, as well as to display the effect good
# computer science can have on software.

def brute001(upper_bound):
	#this works, but runs in time O(n). gross.
	total = 0

	for i in range(upper_bound):
		if i % 3 == 0:
			total = total + i
		elif i % 5 == 0:
			total = total + i

	return total

#==========================================

def brute002(n):
	# basic recursive fibonacci function... O(2^n)
	if n == 0: return 0
	elif n == 1: return 1
	else: return brute002(n - 1) + brute002(n - 2)


def brute002_total(n):
	# fibonacci function ran n times == O(n * 2^n) time!!
	total = 0

	for i in range(n):
		this_fib = brute002(i)
		if this_fib % 2 == 0:
			total = total + this_fib

	return total

#==========================================

if __name__ == "__main__":
	print("Project Euler by BRUTE FORCE:")
	print("001:", brute001(1000))
	print("002:", brute002_total(34))