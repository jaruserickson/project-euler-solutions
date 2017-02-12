
def largest_palindrome_bruteforce():
    lst = []
    for number in range(100,1000):
        for num in range(100,1000):
            #cast as string to make it easier to check if its a palindrome
            if is_palindrome(str(number * num)):
                lst.append(number * num)
    return max(lst)

#checks if n is a palindrome
def is_palindrome(n):
    new = ""
    for i in range(len(n)-1, -1, -1):
        new += n[i]
    if new == n:
        return True
    return False


#print(largest_palindrome_bruteforce())

#This solution is much faster, it starts from the largest possible products of two 3 digits numbers
#It checks if product is a palindrome, and if it is, it sees if there are two 3 digits numbers that give that product
def palindrome_efficient():
    for product in range(998001, 0, -1):
        if is_palindrome(str(product)):
            for mult in range(999, 0 , -1):
                if product / mult == int(product / mult) and len(str(int(product / mult))) == 3:
                    return product

print(palindrome_efficient())
