num = int(input("Enter the number of rows: "))
shapes = input(
    "1. Right Triangle\n"
    "2. Inverted Triangle\n"
    "3. Diamond\n"
    "4. Hollow Square\n"
    "Choose a shape: "
).lower()


def righttriangle(n):
    for i in range(1, n + 1):
        print("*" * i)


def invertedtriangle(n):
    for i in range(n, 0, -1):
        print("*" * i)


def diamond(n):
    # Upper half
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

    # Lower half
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))


def hollowsquare(n):
    print("*" * n)

    for i in range(n - 2):
        print("*" + " " * (n - 2) + "*")

    if n > 1:
        print("*" * n)


if shapes == "right triangle":
    righttriangle(num)

elif shapes == "inverted triangle":
    invertedtriangle(num)

elif shapes == "diamond":
    diamond(num)

elif shapes == "hollow square":
    hollowsquare(num)

else:
    print("Check spelling")
