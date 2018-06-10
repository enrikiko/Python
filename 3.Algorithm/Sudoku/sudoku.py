sudoku=[[8,1,3,0,0,2,0,0,9],
        [7,0,6,4,1,3,5,8,2],
        [0,2,5,0,0,0,0,0,0],
        [0,8,0,0,5,0,9,0,3],
        [2,0,9,8,0,6,1,0,7],
        [3,0,1,0,2,0,0,6,0],
        [0,0,0,0,0,0,8,1,0],
        [0,0,0,2,8,5,0,0,6],
        [5,0,0,9,0,0,0,7,0]]


def solveSudoku(sudoku):
    for row in range(sudoku.__len__()):
        for col in range(sudoku[row].__len__()):
            if sudoku[row][col] == 0:
                possible = [9,8,7,6,5,4,3,2,1]
                if 0 <= row <= 2:
                    x = 0
                elif 3 <= row <= 5:
                    x = 1
                elif 6 <= row <= 8:
                    x = 2
                if 0 <= col <= 2:
                    y = 0
                elif 3 <= col <= 5:
                    y = 1
                elif 6 <= col <= 8:
                    y = 2
                for log in range(3*x, 3*(x+1)):
                    for lat in range(3*y, 3*(y+1)):
                        if sudoku[log][lat] in possible:
                            possible.remove(sudoku[log][lat])
                for i in range(9):
                    if sudoku[row][i] in possible:
                        possible.remove(sudoku[row][i])
                    if sudoku[i][col] in possible:
                        possible.remove(sudoku[i][col])
                if possible.__len__() == 1:
                    sudoku[row][col]=possible[0]
    printSudoku(sudoku)

def evil(sudoku):
    for row in range(sudoku.__len__()):
        for col in range(sudoku[row].__len__()):
            if sudoku[row][col] == 0:
                if 0 <= row <= 2:
                    x = 0
                elif 3 <= row <= 5:
                    x = 1
                elif 6 <= row <= 8:
                    x = 2
                if 0 <= col <= 2:
                    y = 0
                elif 3 <= col <= 5:
                    y = 1
                elif 6 <= col <= 8:
                    y = 2
                checkElement(sudoku,row,col,x,y)
    printSudoku(sudoku)

def checkElement(sudoku,row,col,x,y):
    checkSquare(sudoku,row,col,x,y)
    # checkRow(sudoku,row,col)
    # checkCol(sudoku,row,col)

def checkSquare(sudoku,row,col,x,y):
    certain=0
    listPossibleNumber=[]
    for number in range(1,10):
        listPossibleNumber.insert(0,number)
    for log in range(3*x, 3*(x+1)):
        for lat in range(3*y, 3*(y+1)):
            if sudoku[log][lat] in listPossibleNumber:
                listPossibleNumber.remove(sudoku[log][lat])
    for number in listPossibleNumber:
        certain=0
        for log in range(3*x, 3*(x+1)):
            for lat in range(3*y, 3*(y+1)):
                if log!=row or lat!=col:
                    certainly=False
                    for element in range(9):
                        if sudoku[log][element]==number:
                            certainly=True
                        elif sudoku[element][lat]==number:
                            certainly=True
                    if certainly==True:
                        certain = certain + 1
        if certain==8:
            sudoku[row][col] = number

    # for element in range(9):
    #     if number ==  sudoku[log][element]:
    #         certain=True
    #     if number ==  sudoku[element][lat]:
    #         certain=True

# def checkRow(sudoku,row,col):
#     for i in range(1,10)
#
# def checkCol(sudoku,row,col):
#     for i in range(1,10)


def printSudoku(sudoku):
    for row in sudoku:
        print(row)
    print("\n")


def isSolved(sudoku):
    for row in sudoku:
        for num in row:
            if num == 0:
                print('Not solved')
                return False
    print('Solved!')
    return True

# printSudoku(sudoku)
# isSolved(sudoku)
solveSudoku(sudoku)
evil(sudoku)
solveSudoku(sudoku)
evil(sudoku)
solveSudoku(sudoku)
evil(sudoku)
solveSudoku(sudoku)
evil(sudoku)
# print(sudoku[0][0])
