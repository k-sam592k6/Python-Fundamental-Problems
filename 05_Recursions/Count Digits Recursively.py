def count_digits(n):

    count = 0

    if n <10:
        return 1 
    
    else:
        n = n // 10
        count += 1 + count_digits(n)
        

    return count

n = int(input("Enter the number "))
print(count_digits(n))
