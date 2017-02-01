# Logic for Project Euler Solutions!

# 001
## Multiples of 3 and 5
[Question](https://projecteuler.net/problem=1) | [Code](https://github.com/jaruserickson/project-euler-solutions/blob/master/python/001.py)

  - The modulo between two numbers intersects every x times y numbers (for the two numbers x and y).  
  - The number of multiples of 5 less than 1000 is then equal to `1000 / 5` (- 1 for 1000).  
  - The number of multiples of 3 less than 1000 is then equal to `1000 // 3`.  

  ![chart](https://github.com/jaruserickson/project-euler-solutions/blob/master/img/chart.png?raw=true "001 chart")  

  these counts include overlap, so we need to begin by calculating the number of overlapping multiples (i.e. `3*5 = 15` [multiples of 15])  
  
  this is simply `COUNT_5//3)` (or `COUNT_3//5`).

  we need to calculate sums for each total now.  
    to get the sums we simply use the series `1 + 2 + 3 + ... + n = n(n+1)/2`  
    (i.e. first 3 multiples of 5 `= 5x1 + 5x2 + 5x3 = 5 x (1 + 2 + 3)`)

  since 1000 is a multiple of 5, and we don't want to include it, we'll use `n(n-1)/2` for 5.

  then simply return `mult of 5 + mult of 3 - mult of 15` to get the total.

# 002
## Even Fibonacci numbers
[Question](https://projecteuler.net/problem=2) | [Code](https://github.com/jaruserickson/project-euler-solutions/blob/master/python/002.py)

  I took a look at this one and came up with a pretty simple algorithm pretty quickly. Using Binet's formula, I could've just looped by increments of 3 to sum even fibonacci numbers. (every 3rd fibonacci number is even.)

  But rather, I decided to take it a step further and make it a tad bit faster, removing division and sqrt from the algorithm. 

  The solution is up to some basic math.

  ![math](https://github.com/jaruserickson/project-euler-solutions/blob/master/img/math.png?raw=true "002 math")

  This then means for each loop, we'll have a prior (f_n-1) and an even number (f_n). We need to start with 1, 2 as prior and even respectively.

  The algorithm will then run until even is >= 4,000,000 (or whatever input).

  This algorithm runs (generally) in the same time an algorithm with the golden ratio runs, however it runs much *much* faster than the brute force algorithm that uses the recursive definition of a fibonacci number.

  THEREFORE: This will run in `O(n/3)`, or `O(n)`, but is what i believe is the fastest possible algorithm without using Binet's formula at 12 iterations (per 33 even fibonacci numbers < 4000000). It doesn't iterate over any odd Fibonacci numbers.

# 003
## Largest prime factor
[Question](https://projecteuler.net/problem=3) | [Code](https://github.com/jaruserickson/project-euler-solutions/blob/master/python/003.py)

  With this question, I found it pretty hard to come up with a solution that wasn't even *kind of* brute force-y, so I ended up keeping the brute force, and just improve it.

  I found that divide-and-conquer would be the best way of attacking the problem. Every time I found a number that would divide into the input, run an algorithm that runs in `O(n)` that checks if it's prime. If so, set the largest number to this number, and divide the input by said number (without permanently mutating the input - thanks python!).

  The time complexity is kind of odd for this one, since the `O(n)` `is_prime` algorithm only runs 4 or 5 times for the input specified. I took the time complexity by nature of the algorithm.

  This ends up running in `O(lgn)`, due to its divide-and-conquer nature. The input decreases in size every so often. 
