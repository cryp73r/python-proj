# discrete logarithm is the inverse of modular exponentiation
def discrete_logarithm(a, b, m):
    # we try all the values of the exponent one by one until we find it
    c = 1

    # if b^c mod m = a it means we find the right c exponent
    while pow(b, c) % m != a:
        # if the exponent is not right we consider the next one
        c = c + 1

    return c


# modular exponentiation: we just have to use the formula (b^c) mod m
def modular_exponentiation(b, c, m):
    return pow(b, c) % m


if __name__ == '__main__':
    # this is a good trapdoor-function (Diffie-Hellman algorithm)
    print(modular_exponentiation(5, 948603, 9048610007))
    print(discrete_logarithm(3668993056, 5, 9048610007))
