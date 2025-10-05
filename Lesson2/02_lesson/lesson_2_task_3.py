from math import ceil


def square(x):
    s = x**2
    return s


x = float(input("Длина стороны квадрата: "))
result = square(x)
rounded = ceil(result)
print(f"Площадь квадрата: {rounded}")

