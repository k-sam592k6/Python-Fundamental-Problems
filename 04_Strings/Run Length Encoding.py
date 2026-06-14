string = input("Enter string: ") 

result = ""

count = 1
for i in range(1, len(string)):
    if string[i] == string[i-1]:
        count +=1 
    else:
        result += str(count) + string[i-1]
        count = 1

result += str(count) + string[-1]
print(result)

decoded = ""
i = 0
while i < len(result):
    count = int(result[i])
    char = result[i+1]
    decoded += char * count
    i += 2
print(decoded)
