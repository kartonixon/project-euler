# Project Euler Problem 9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product abc


def pythagorean(a,b,c):
    if a*a + b*b == c*c:
        return True
    else:
        return False


def product_of_triplet(n):
    aa = 0
    bb = 0
    cc = 0
    for a in range(1, n):
        for b in range(1, n):
            c = n-a-b
            if pythagorean(a, b, c):
                aa = a
                bb = b
                cc = c
                break
    product = aa*bb*cc
    return product


def main():
    print(product_of_triplet(1000))


if __name__ == '__main__':
    main()