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

  I originally used a fairly basic algorithm, coupled with some use of the Fundamental Theorem of Arithmetic to achieve the answer, but found that it ran in worst-case `O(n)` time. After some reasearch, I found that the best way of attacking this problem would be via a [Prime Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)-esque algorithm.

  We can search through `x ** 2`, as x increases by 1 starting at the first prime, 2. Whenever we find a divisor, we divide into the number, decreasing our loop interval. The algorithm will terminate once `x ** 2 > n`. If a prime number is found, the number is composite, and we have our largest prime, otherwise our largest prime is the input. Please see [Prime Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) for further explanation.

  NOTE: We don't have to check whether a number is prime when dividing for this algorithm, since (by the Fundamental Theorem of Arithmetic), any composite number is a *composite* of prime numbers, and we are only searching for the largest prime.

  Our worst-case time complexity here is `O(sqrt(n))`. This will occur with any prime number, i.e. 961,748,941 will run in roughly 31,012 steps. 
