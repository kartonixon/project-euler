# Project Euler Problem 7
# What is the 10 001st prime number?


def is_prime(n):
    factors = 1
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            factors += 1
        if factors > 2:
            break
    if factors == 2:
        return True
    else:
        return False


def nth_prime_number(n):
    counter = 0
    number = 0
    while n != counter:
        number += 1
        if is_prime(number):
            counter += 1
    return number


def main():
    print(nth_prime_number(10001))


if __name__ == '__main__':
    main()
