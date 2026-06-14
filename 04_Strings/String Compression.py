string = input("Enter string: ")

result = ""
count = 1

for i in range(1, len(string)):
    if string[i] == string[i-1]:
        count += 1
    else:
        result += str(count) + string[i-1]
        count = 1

result += str(count) + string[-1]

if len(result) < len(string):
    print(f"Compressed      : {result}")
elif len(result) > len(string):
    print(f"Original returned: {string} (compressed '{result}' is longer)")
else:
    print(f"Compressed      : {result} (same length)")
