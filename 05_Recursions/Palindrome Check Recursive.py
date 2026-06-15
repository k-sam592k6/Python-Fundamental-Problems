def palindrome(s):
    mylist = [char for char in s]

    if len(mylist) < 2:
        return True

    elif mylist[0] != mylist[-1]:
        return False

    else:
        mylist.pop(0)
        mylist.pop(-1)

    return palindrome(mylist)


word = input("Enter word: ")
print(palindrome(word))
