def numbers(n: int):
    if n < 0:
        return

    print(n)
    numbers(n-1)


def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    i = (fib(n-1)) + (fib(n-2))
    return i


def power(number: int, n: int) -> int:
    if n == 0:
        return 1

    return number*power(number, n-1)


# def reverse(txt: str) -> str:
#     x = ""
#     x += txt[-1]
#
#
#
#     return x


def factorial(n: int) -> int:
    if n <= 1:
        return 1

    return n * factorial(n-1)


def prime(n: int) -> bool:
    if n <= 3:
        return 1
    # if



# numbers(44)
# print(fib(20))
# print(power(10, power(10, 80)))
# print(reverse('klon'))
# print(factorial(10))
