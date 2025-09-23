names = ["John", "Paul", "George", "Ringo", "John", "John", "Paul"]
counts = {}
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
for key, value in counts.items():
    print(f"{key} -> {value}")