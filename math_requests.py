from math import sin, cos, factorial


def make_sum(number1, number2):
    result = number1 + number2
    return result


def make_mult(number1, number2):
    return number1 * number2


def make_pow(number, power):
    return number ** power


def make_sinus(number):
    return sin(number)


def make_scaled_sinus(radians, scale=1):
    return scale * sin(radians)


def make_transformed_cosinus(
        radians, scale=1, shift=0):
    return scale * cos(radians) + shift


def make_number_of_combinations(
        amount, combination_size=1):
    return (factorial(amount) /
            factorial(combination_size) /
            factorial(amount - combination_size))


def make_binomial(x, a=1, b=0, c=0):
    return a * x * x + b * x + c


def make_binom2(x, **kwargs):
    return (kwargs.get('a', 1) * x ** 2 +
            kwargs.get('b', 0) * x +
            kwargs.get('c', 0))


def sum_all(*args):
    result = 0
    for argument in args:
        result += argument
    return result


def mult_all(*args):
    result = 1
    for argument in args:
        result *= argument
    return result


if __name__ == '__main__':
    print(make_sum(100, 500))
    print(make_mult(100, 500))
    print(make_pow(11, 3))
    print(make_sinus(5))
    print(make_scaled_sinus(5))
    print(make_scaled_sinus(5), 2)

    print(make_transformed_cosinus(5))
    print(make_transformed_cosinus(5, shift=2))
    print(make_transformed_cosinus(5, 2, 2))
    print(make_number_of_combinations(10))
    print(make_number_of_combinations(10, 3))
    print(make_binomial(5))
    print(make_binomial(5, b=2))
    print(make_binomial(5, 2, -2, 8))
    print(make_binom2(5, a=2, b=-2, c=0))

    print(sum_all(1, 10, 100, 500))
    print(sum_all(*range(100)))
    print(mult_all(1, 10, 100, 500))
    print(mult_all(*range(10, 13)))
