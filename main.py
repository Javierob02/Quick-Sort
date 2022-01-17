from solve import *

first_line = input().split()
numValues = int(first_line[0])

items = []
for j in range(1, numValues+1):
    parts = input().split()
    items.append(int(parts[0]))

quick_sort(items, 0, len(items)-1)
print(items)