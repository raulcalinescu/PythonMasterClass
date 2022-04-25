def multiply():
    res = 10 * 4
    return res


print(multiply())


def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()


def sentence_palindrome(sentence):
    string = ""
    for char in sentence:
        if str.isalpha(char):
            string += char
    return is_palindrome(string)


def fibonacci(n):
    """
    Return the `n`th Fibonacci number, for positive `n`.
    """
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0
    result = None
    for f in range(n-1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
    return result


def fizz_buzz(num: int) -> str:
    """
   Play Fizz buzz
   :param num: The number to check.
   :return: 'fizz' if the number is divisible by 3.
       'buzz' if it's divisible by 5.
       'fizz buzz' if it's divisible by both 3 and 5.
       The number, as a string, otherwise.
   """
    if num % 3 == 0 and num % 5 == 0:
        return "fizz buzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)


# test for numbers from 1 to 100
for i in range(1, 5):
    print(fizz_buzz(i))


def factorial(n: int) -> int:
    """
    This function calculates the factorial of a given `n` integer.
    :param n:
    :return: n!
    """
    if n == 0:
        return 1
    res = 1
    for f in range(n-1):
        res *= n
        n -= 1
    return res


for i in range(3):
    print("{0} {1}".format(i, factorial(i)))


def sum_numbers(*args: float) -> float:
    """
    This function calculates the sum of its args
    :param args:
    :return: res
    """
    # return sum(args)
    res = 0
    for a in args:
        res += a
    return res


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        #else:
        print('{0} is not a valid number'.format(temp))


# MAIN DRIVER
print(get_integer("Type number here: "))
print(sentence_palindrome("I am 1 ma "))
print(sum_numbers(1, 2, 3))

