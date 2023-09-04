from about_me import print_name


def calculate_area(base, height):
    return 0.5 * base * height


def bmi_calculator(weight, height):
    return weight / height ** 2


def print_bmi(weight, height):
    bmi = bmi_calculator(weight, height)
    print(f"Vægt: {weight}")
    print(f"Højde: {height}")
    print(f"Din BMI er {bmi}")


def fermat(a, b, c, n):
    theo = a ** n + b ** n == c ** n
    print(theo)
    if n > 2 and theo:
        print("Holy smokes, Fermat was wrong!")
    elif n == 2 and theo:
        print("Yes that does work.")
    else:
        print("No, that doesn't work.")


def calculate_quadratic(a, b, c):
    # Compute the solutions of a quadratic equation
    x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    # Compute the discriminant
    d = b ** 2 - 4 * a * c
    # Checks the discriminant and prints the solutions
    if d < 0:
        print(f"The quadratic equation {a}x^2 + {b}x + {c} = 0 has no real solutions")
    elif d == 0:
        print(f"The quadratic equation {a}x^2 + {b}x + {c} = 0 has the solution x = {x1}")
    else:
        print(f"The quadratic equation {a}x^2 + {b}x + {c} = 0 has the solutions x1 = {x1} and x2 = {x2}")
    return x1, x2

if __name__ == "__main__":
    # print_name("Mads", 24, "Aarhus", 7)
    # print(calculate_area(10, 20))
    # print_bmi(80, 1.8)
    # a = 468750.0
    # b = 1168121.0
    # c = 1175621.0
    # n = 4
    # print(468750**4)
    # fermat(a, b, c, n)
    print(calculate_quadratic(1, 2, 1))

