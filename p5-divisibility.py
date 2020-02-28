# Project Euler Problem 5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def is_divisible(n):
    for i in range(1, 21):
        if not n % i == 0:
            return False
    return True


def main():
    n = 0
    ok = False
    while not ok:
        n += 20
        if is_divisible(n):
            ok = True
    print(n)


if __name__ == '__main__':
    main()
