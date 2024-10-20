from decimal import Decimal, getcontext, ROUND_HALF_UP


def calculate_pi(prec: int) -> Decimal:
    getcontext().prec = prec + 5
    C = 426880 * Decimal(10005).sqrt()
    M = Decimal(1)
    L = Decimal(13591409)
    X = Decimal(1)
    K = Decimal(6)
    S = L
    for k in range(1, prec):
        M = (M * (K**3 - 16 * K)) / (k**3)
        L += 545140134
        X *= -262537412640768000
        term = (M * L) / X
        S += term
        if term == 0:
            break
        K += 12
    pi = C / S
    return pi


def sine(x: Decimal, terms: int) -> Decimal:
    getcontext().prec += 2
    x_power = x
    factorial = Decimal(1)
    sin_x = x
    sign = -1
    for i in range(3, terms * 2, 2):
        x_power *= x * x
        factorial *= i * (i - 1)
        term = x_power / factorial
        sin_x += sign * term
        sign *= -1
        if term == 0:
            break
    getcontext().prec -= 2
    return +sin_x


def cosine(x: Decimal, terms: int) -> Decimal:
    getcontext().prec += 2
    x_power = Decimal(1)
    factorial = Decimal(1)
    cos_x = Decimal(1)
    sign = -1
    for i in range(2, terms * 2, 2):
        x_power *= x * x
        factorial *= i * (i - 1)
        term = x_power / factorial
        cos_x += sign * term
        sign *= -1
        if term == 0:
            break
    getcontext().prec -= 2
    return +cos_x


def precise_rounding(x: Decimal, digits: int) -> Decimal:
    if x.is_zero():
        return Decimal(0)
    else:
        _, digits_tuple, exponent = x.as_tuple()
        adjusted_exponent = exponent + len(digits_tuple) - digits
        quantize_exp = Decimal("1e{}".format(adjusted_exponent))
        return x.quantize(quantize_exp, rounding=ROUND_HALF_UP)


def arb_tangent(A: int, precision: int) -> str:
    getcontext().prec = precision + 10

    pi = calculate_pi(getcontext().prec)

    angle_rad = (A * pi) / Decimal(200)

    terms = precision + 5
    sin_x = sine(angle_rad, terms)
    cos_x = cosine(angle_rad, terms)

    tan_x = sin_x / cos_x
    tan_x = precise_rounding(tan_x, precision)
    tan_str = "{0}".format(tan_x.normalize())

    if "." in tan_str:
        integer_part, fractional_part = tan_str.split(".")
        significant_digits = len(integer_part.lstrip("-") + fractional_part)
    else:
        integer_part = tan_str.lstrip("-")
        significant_digits = len(integer_part)

    if significant_digits < precision:
        zeros_needed = precision - significant_digits
        if "." in tan_str:
            tan_str += "0" * zeros_needed
        else:
            tan_str += "." + "0" * zeros_needed

    return tan_str


if __name__ == "__main__":
    A = Decimal(int(input()))
    precision = int(input())

    tan = arb_tangent(A, precision)
    print(tan)
