import random
number = random.randint(1,100)

choice = int(input("Guess!: "))
guess_count = 0

while choice != number:

    guess_count += 1

    if choice > number and (choice - number) >10:
        print("Too High!")
    elif choice > number :
        print("High")

    if choice < number and (number - choice) < 10:
        print("Too Low!")
    elif choice < number:
        print("Low")

    if choice == number:
        print(f"Correct! You got it in {guess_count} attempts!")
        break
