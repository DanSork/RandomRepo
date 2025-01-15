grid = [
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
]



print("Plant your treasure somewhere")


for row in grid:
    print(row)
    
row = int(input("Choose a row (1-3): "))
column = int(input("Choose a column (1-3): "))

grid[row-1][column-1] ='X'


for row in grid:
    print(row)