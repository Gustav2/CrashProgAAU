from math import factorial, sin, pi


def print_nums():
    for i in range(1000):
        if i % 5 == 0 and i % 7 == 0:
            print(i)


def print_num_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end=" ")
        print()


def harmonic_sum(n):
    if n == 1:
        return 1
    else:
        return 1 / n + harmonic_sum(n - 1)


def fizzbuzz(n):
    for i in range(n):
        buzz_str = ""
        if i % 3 == 0:
            buzz_str += "Fizz"
        if i % 5 == 0:
            buzz_str += "Buzz"
        if buzz_str == "":
            buzz_str = str(i)

        print(buzz_str)


def ackermann_func(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann_func(m - 1, 1)
    else:
        return ackermann_func(m - 1, ackermann_func(m, n - 1))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def taylor_sin(x, n):
    if n == 0:
        return x
    else:
        return taylor_sin(x, n - 1) + ((-1)**n * x**(2*n + 1)) / factorial(2*n + 1)


def abolute_error(x, n):
    return abs(sin(x) - taylor_sin(x, n))

if __name__ == "__main__":
    # print_num_table()
    # print(harmonic_sum(10))
    # fizzbuzz(100)
    # print(ackermann_func(3, 4))
    # print(gcd(12, 8))
    print(taylor_sin(pi/4, 10))
    print(abolute_error(pi/4, 10))