# Project Euler Problem 3
# What is the largest prime factor of the number 600851475143 ?

def isPrime(n):
    factors = 0
    for i in range(1, n+1):
        if n % i == 0:
            factors += 1
    if factors == 2:
        return True
    else:
        return False

def findBiggestPrimeFactor(n):
    biggest_prime_factor = 0
    i = 2
    while (n>1):
        if n % i == 0:
            n = n/i
            if isPrime(i):
                biggest_prime_factor = i
            i = 2
        i += 1
    return biggest_prime_factor



def main():
    n = 600851475143
    print(findBiggestPrimeFactor(n))

if __name__ == '__main__':
    main()
