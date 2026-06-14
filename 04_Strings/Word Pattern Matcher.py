pattern = list(input("Enter pattern: ").lower())
string = input("Enter string: ").lower().split()

if len(pattern) != len(string):
    print("False ✗ — length mismatch!")
else:
    pattern_to_word = {}
    word_to_pattern = {}

    for i in range(len(pattern)):
        p = pattern[i]
        w = string[i]

        if p in pattern_to_word and pattern_to_word[p] != w:
            print("False ✗ — string does not follow the pattern!")
            break
        if w in word_to_pattern and word_to_pattern[w] != p:
            print("False ✗ — string does not follow the pattern!")
            break

        pattern_to_word[p] = w
        word_to_pattern[w] = p

    else:
        print("True ✓ — string follows the pattern!")
