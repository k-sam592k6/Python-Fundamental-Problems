rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):        
    for space in range(1, rows - i + 1):
        print(end='  ')              

    mylist = []                      
    r = 1                            
    
    while r <= i:                    
        mylist.append(r)
        r += 1
    
    r = i - 1                        
    while r >= 1:                    
        mylist.append(r)
        r -= 1

    print(*mylist)                   
