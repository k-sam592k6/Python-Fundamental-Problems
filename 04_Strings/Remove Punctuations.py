sentence = input("Enter sentence: ")
final = ""
for char in sentence:
    if char.isalpha() or char == " ":
        final += char
    else:
        pass

print("Orignal Sentence: ", sentence)
print("Cleaned Sentence: ", final)
