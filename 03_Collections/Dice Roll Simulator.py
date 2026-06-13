import random
count = 0

frequency = []

while count <1000:
    a = random.randint(1,6)
    b = random.randint(1,6)
    sum_required = a + b
    count += 1
    frequency.append(sum_required)

print("Dice Roll Simulator")
print("-------------------")
for i in range(2, 13):
    bars = '*' * (frequency.count(i) // 10)
    print(f"{i:2} |{bars}")







