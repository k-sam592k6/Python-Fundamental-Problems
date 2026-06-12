import random


score = 0

for i in range(1,11):
    a1 = random.randint(1,100)
    a2 = random.randint(1,100)
    print(f"{a1} X {a2} = ?")
    answer = int(input(""))
    if answer == a1 * a2:
        score += 1
    else:
        print("Wrong!" "Correct Answer", a1*a2)

print(score)
