def reverse_string(s, index):

    if index < 0:
        return ""

    return s[index] + reverse_string(s, index - 1)


word = input("Enter word: ")

print(reverse_string(word, len(word) - 1))
