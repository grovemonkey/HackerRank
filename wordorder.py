from collections import Counter
y = input()
lines = []
while True:
    try:
        line = input()
    except EOFError:
        break

    lines.append(line)

counts = Counter(lines)
print(len(counts))
print(" ".join([str(v) for k, v in counts.items()]))
