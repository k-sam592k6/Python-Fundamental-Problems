votes = input("Enter votes (space separated): ").split()

vote_dict = {}
for name in votes:
    if name not in vote_dict:
        vote_dict[name] = votes.count(name)

print("\n--- Vote Count ---")
for name in vote_dict:
    print(f"{name:10}: {vote_dict[name]}")

winner = ""
highest = 0
for name in vote_dict:
    if vote_dict[name] > highest:
        highest = vote_dict[name]
        winner = name

print(f"------------------")
print(f"Winner  : {winner} 🎉")
