names = ['Alice', 'Bob', 'Cindy', 'Dani']
roster = input().split()
for name in names:
    if name not in roster:
        print(name)
        break
