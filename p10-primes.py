# Project Euler Problem 10
# Find the sum of all the primes below two million

import math


def is_prime(n):
    factors = 2
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            factors += 1
        if factors > 2:
            break
    if factors == 2:
        return True
    else:
        return False


def sum_of_primes(n):
    prime_sum = 0
    for i in range(2, n+1):
        if is_prime(i):
            prime_sum += i
    return prime_sum


def main():
    print(sum_of_primes(2000000))


if __name__ == '__main__':
    main()