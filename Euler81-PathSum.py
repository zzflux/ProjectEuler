#Project Euler problem #81
#Path sum: two ways
#Status: solved

FILENAME = "e81-Matrix.txt"
#FILENAME = "e81Test.txt"

def solvePath(grid):
    values = [[None] * len(grid) for _ in range(len(grid[0]))]
    values[-1][-1] = grid[-1][-1]
    #print(values)
    for r in range(len(grid) - 2, -1, -1):
        values[r][-1] = values[r+1][-1] + grid[r][-1]
        #print(values[r][-1], "=", values[r+1][-1], "+", grid[r][-1])
    #print(values)
    for c in range(len(grid[0]) - 2, -1 , -1):
        values[-1][c] = values[-1][c+1] + grid[-1][c]
    #print(values)
    for r in range(len(grid) - 2, -1, -1):
        for c in range(len(grid[0]) - 2, -1, -1):
            values[r][c] = min([values[r+1][c], values[r][c+1]]) + grid[r][c]
    #print()
    #print(values)
    return values[0][0]


if __name__ == "__main__":
    with open(FILENAME) as file:
        gr = [[int(num) for num in line.split(',')] for line in file]
        print("Answer:", solvePath(gr))

#done
