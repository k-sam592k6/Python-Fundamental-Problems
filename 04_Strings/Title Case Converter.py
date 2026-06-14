string = input("Enter string: ").split()
small_words = ['a', 'an', 'the', 'in', 'on', 'at', 
               'by', 'for', 'and', 'but', 'or', 'of']

capitaliselist = []
a = string[0].capitalize()
capitaliselist.append(a)


for i in range (1,len(string)):
    if string[i] in small_words:
        capitaliselist.append(string[i])
    else:
        b = string[i].capitalize()
        capitaliselist.append(b)

print(*capitaliselist, sep=" ")
