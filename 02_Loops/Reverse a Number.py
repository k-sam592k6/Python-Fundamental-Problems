n = int(input("Enter a number: "))

reverse_num = 0

while n >0 :
    reverse_num = reverse_num * 10 + (n%10)
    n = n//10

print(reverse_num)
