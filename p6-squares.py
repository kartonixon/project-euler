# Project Euler Problem 6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sum_of_squares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i * i
    return sum


def square_of_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum*sum


def main():
    print(abs(sum_of_squares(100)-square_of_sum(100)))


if __name__ == '__main__':
    main()
