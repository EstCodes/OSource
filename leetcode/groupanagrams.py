from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

d: defaultdict[str, list] = defaultdict(list)

for i in words:
    print(sorted(i))
    print(''.join(sorted(i)))

    d[''.join(sorted(i))].append(i)

print(d)
