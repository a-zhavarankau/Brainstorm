import pprint
n = 4

m = []
# Prepare 'wave' for the rows
for i in range(2*n-1):
    m.append([])
    for j in range(2*n-1):
        row = (n-1)-abs(n-1-i)
        col = 1
        m[i].append(row)


# pprint.pprint(m)
for row in m:
    for element in row:
        print(element, end=" ")
    print()
