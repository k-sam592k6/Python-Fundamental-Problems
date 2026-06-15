sentence = input("Enter sentence: ").lower().split()

freq = {}
for word in sentence:
    freq[word] = sentence.count(word)

duplicates = {}
for word, count in freq.items():
    if count > 1:
        duplicates[word] = count

if len(duplicates) == 0:
    print("No duplicates!")
else:
    print("Duplicate words:")
    for word, count in duplicates.items():
        print(f"{word:10}: {count} times")
