a = pow(-2, 31)
b = pow(2, 31) -1


def ans(n):
    sign = 0
    if n < 0:
        n = abs(n)
        sign = 1
    result = 0
    while n:
        result = result*10 + n%10
        n = int(n / 10)
    
    if sign:
        result = 0 - result
    if result < a or result > b:
        return 0
    else:
        return result

print(ans(-123))


# add negative sign to a positive number
    # negative = 0 - positive

# add positive sign to a negative number
    # positive = abs(negative)

# reverse a string
    # str_rever = given_str[::-1]

# add last digit of a number to another number
    # result = result*10 + n%10
    # n = int(n / 10)
