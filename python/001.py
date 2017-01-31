def mult3or5(upper_bound):
	#this is constant time O(1).
	#get counts
	COUNT_3 = upper_bound // 3
	COUNT_5 = upper_bound / 5

	#get overlap
	COUNT_15 = COUNT_5//3

	#get sums
	fifteens = 15 * ((COUNT_15 * (COUNT_15 + 1)) / 2)
	fives = 5 * ((COUNT_5 * (COUNT_5 - 1)) / 2)
	threes = 3 * ((COUNT_3 * (COUNT_3 + 1)) / 2)

	return int(fives + threes - fifteens)


#min_mode version of O(1) algorithm
def min_mult(UB):
	return int(5 * (UB / 5 * ((UB / 5) - 1)) / 2)\
					+ (3 * (UB // 3 * ((UB // 3) + 1)) / 2)\
					- (15 * (UB / 5 // 3 * ((UB / 5 // 3) + 1)) / 2))


if __name__ == "__main__":
	print("algo main:", mult3or5(1000))
	print("min_mode:", min_mult(1000))