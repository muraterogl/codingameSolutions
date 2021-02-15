grid = []

#Creating grid while checking row errors
for i in range(9):
    row = [*map(int,input().split())]
    if len(row) == len(set(row)):
        grid.append(row)
    else:
        print("false")
        exit()

#Checking column errors
for i in range(9):
    column = []
    for j in range(9):
        column.append(grid[j][i])
    
    if len(set(column)) != 9:
        print("false")
        exit()

#Checking subgrid errors
for i in range(0,9,3):
    for j in range(0,9,3):
        subgrid = []

        for k in range(i, i+3):
            for l in range(j, j+3):
                subgrid.append(grid[k][l])

        if len(set(subgrid)) != 9:
            print("false")
            exit()

print("true")
 
