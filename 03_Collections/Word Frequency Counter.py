from collections import Counter

para = input("Enter paragraph: ")
words = para.lower().split()

counter = Counter(words)

print("\nTop 5 most common:")
for rank, (word, count) in enumerate(counter.most_common(5), 1):
    print(f"{rank}. {word:10} : {count}")
