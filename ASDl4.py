def list_to_edgers(N):
    max = N[0][0]
    for i in N:
        for j in i:
            if j > max:
                max = j
    edgers1 = [[0 for i in range(max)] for i in range(max)]
    for i in range(len(N)):
        edgers1[N[i][0] - 1][N[i][1] - 1] = 1
    edgers2 = []
    for i in range(len(edgers1)):
        t = []
        for j in range(len(edgers1[i])):
            if (edgers1[i][j] == 1):
                t.append(j + 1)
        edgers2.append(t)
    return edgers2

N1 = [[1, 3], [1, 2], [2, 3], [3, 4]]
N2 = [[1, 3], [1, 2], [2, 3], [3, 4], [3, 1], [2, 1], [3, 2], [4, 3]]
edgers1 = list_to_edgers(N1)
edgers2 = list_to_edgers(N2)
print("ориентированный граф")
for i in range(len(edgers1)):
    print(f"{i + 1} -> {edgers1[i]}", end='\n')
print()
print("неориентированный граф")
for i in range(len(edgers2)):
    print(f"{i + 1} -> {edgers2[i]}", end='\n')
print()