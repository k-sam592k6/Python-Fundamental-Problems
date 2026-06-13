n = int(input("Enter the size of the data: "))


dict_marks = {}
nameslist = []
markslist = []

for i in range (1,n+1):
    names = str(input("Enter Names of Students: "))
    nameslist.append(names)

for j in range (1,n+1):
    marks = float(input("Enter Marks: "))
    markslist.append(marks)


for i, j in range (1,n+1):
    dict_marks[names[i]] = markslist[j]

print("Highest Marks:", max(dict_marks.values()))
print("Lowest Marks: ", min(dict_marks.values()))

print("Average Marks: ", sum(dict_marks.values())/n )

print("\nLeaderboard:")
leaderboard = sorted(dict_marks.items(), key=lambda x: x[1], reverse=True)
for rank, (name, mark) in enumerate(leaderboard, 1):
    print(f"  {rank}. {name} : {mark}")
