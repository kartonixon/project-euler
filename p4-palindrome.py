# Project Euler Problem 4
# Find the largest palindrome made from the product of two 3-digit numbers.


def digits(n):
    d = 0
    i = 0
    while (n % pow(10, i)) != n:
        i += 1
        d += 1
    return d


def isPalindrome(n):
    temp = n
    max_power = digits(n) - 1
    i = 0
    n_reversed = 0
    while n != 0:
        d = int(n/pow(10, max_power - i))
        n_reversed += d*pow(10, i)
        n -= d*pow(10, max_power - i)
        i += 1
    if temp == n_reversed:
        return True
    else:
        return False


def main():
    largest_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if isPalindrome(i*j) and i*j > largest_palindrome:
                largest_palindrome = i*j
    print(largest_palindrome)


if __name__ == '__main__':
    main()
