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


print(largest_palindrome_bruteforce())
