num = int(input("Enter a number: "))

armstrong_numbers = []

for num in range(1, num + 1):

    digits = [int(digit) for digit in str(num)]
    num_digits = len(digits)

    armstrong_sum = 0

    for digit in digits:
        armstrong_sum += digit ** num_digits

    if armstrong_sum == num:
        armstrong_numbers.append(num)

print("Armstrong numbers up to", num, ":")
print(*armstrong_numbers)
