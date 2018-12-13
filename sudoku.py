from random import randint


grid = [[0]*9 for n in range(9)]


def printGrid():
    i = 1
    print("+-------+-------+-------+")
    for row in grid:
        print ("|" , *row[:3], "|", *row[3:6],"|", *row[6:10], "|")
        if i % 3 == 0:
            print ("+-------+-------+-------+")
        i+=1


def isNumPossible(row, col, randomNumber):
    numberIsPossible = 1
    i = 0
    while i < 9:
        if grid[row][i] == randomNumber:  # sprawdzanie wiersza
            numberIsPossible = 0
        if grid[i][col] == randomNumber:  # sprawdzanie kolumny
            numberIsPossible = 0
        i += 1
        if row % 3 == 0:
            if col % 3 == 0:
                if randomNumber == grid[row + 1][col + 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row + 1][col + 2]:
                    numberIsPossible = 0
                if randomNumber == grid[row + 2][col + 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row + 2][col + 2]:
                    numberIsPossible = 0
            if col % 3 == 1:
                if randomNumber == grid[row + 1][col + 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row + 1][col - 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row + 2][col + 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row + 2][col - 1]:
                    numberIsPossible = 0
            if col % 3 == 2:
                if randomNumber == grid[row + 1][col - 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row + 1][col - 2]:
                    numberIsPossible = 0
                if randomNumber == grid[row + 2][col - 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row + 2][col - 2]:
                    numberIsPossible = 0
        if row % 3 == 1:
            if col % 3 == 0:
                if randomNumber == grid[row - 1][col + 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row - 1][col + 2]:
                    numberIsPossible = 0
                if randomNumber == grid[row + 1][col + 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row + 1][col + 2]:
                    numberIsPossible = 0
            if col % 3 == 1:
                if randomNumber == grid[row - 1][col + 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row - 1][col - 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row + 1][col + 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row + 1][col - 1]:
                    numberIsPossible = 0
            if col % 3 == 2:
                if randomNumber == grid[row - 1][col - 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row - 1][col - 2]:
                    numberIsPossible = 0
                if randomNumber == grid[row + 1][col - 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row + 1][col - 2]:
                    numberIsPossible = 0
        if row % 3 == 2:
            if col % 3 == 0:
                if randomNumber == grid[row - 1][col + 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row - 1][col + 2]:
                    numberIsPossible = 0
                if randomNumber == grid[row - 2][col + 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row - 2][col + 2]:
                    numberIsPossible = 0
            if col % 3 == 1:
                if randomNumber == grid[row - 1][col + 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row - 1][col - 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row - 2][col + 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row - 2][col - 1]:
                    numberIsPossible = 0
            if col % 3 == 2:
                if randomNumber == grid[row - 1][col - 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row - 1][col - 2]:
                    numberIsPossible = 0
                if randomNumber == grid[row - 2][col - 1]:
                    numberIsPossible = 0
                if randomNumber == grid[row - 2][col - 2]:
                    numberIsPossible = 0
    return numberIsPossible


def fillGrid():
    row = 0
    col = 0
    while row < 9:
        while col < 9:
            randomNumber = randint(1, 9)
            numberIsPossible = isNumPossible(row,col,randomNumber)
            if numberIsPossible == 0:
                if numberOfGuesses > 20:
                    z = 0
                    while z < 9:
                        grid[row][z] = "0"
                        z+=1
                        col = 0

                numberOfGuesses += 1
            if numberIsPossible == 1:
                grid[row][col] = randomNumber
                col += 1
                numberOfGuesses = 0
        row +=1
        col = 0

fillGrid()
printGrid()
input()  # sprawienie by okienko z tablica nie zginelo