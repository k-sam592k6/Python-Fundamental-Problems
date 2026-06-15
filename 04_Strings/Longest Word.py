sentence = [word for word in input("Enter Sentence: ").split()]

max_length = max(len(item) for item in sentence)

for i in range(len(sentence)):

    if len(sentence[i]) == max_length:
        print(f"Longest Word: {sentence[i]} ({max_length} charechters)") 
        break
    
    else:
        pass
