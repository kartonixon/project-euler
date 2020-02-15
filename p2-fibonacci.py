# Project Euler Problem 2
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.


def main():
    sum_even = 0
    a = 1
    b = 2
    while b < 4000000:
        if b % 2 == 0:
            sum_even += b
        temp = b
        b = b + a
        a = temp
    print(sum_even)


if __name__ == '__main__':
    main()
