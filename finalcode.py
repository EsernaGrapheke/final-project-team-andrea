from time import sleep
def drawMatriz(matriz):
    for row in matriz:
        for column in row:
            print(column, end='')
        print()
    sleep(0.5)
def copyMatrix(matriz):
    matrizcopied = [[]]
    for row in matriz:
        matrizcopied.append([])
        for column in row:
            matrizcopied[-1].append(column)
    return matrizcopied
def copyList(lista):
    listCopied = []
    for element in list:
        listCopied.append(element)
    return listCopied
def checkIfNextToSolution(matriz, ycoordinate, xcoordinate):
    """
    Check if the current position is next to the solution
    :param matriz: any 2D matrix of any size
    :param xcoordinate: the x coordinate of the current position
    :param ycoordinate: the y coordinate of the current position
    :return: True if the current position is next to the solution, False otherwise
    """
    if matriz[xcoordinate][ycoordinate - 1] == 'S' or \
            matriz[xcoordinate - 1][ycoordinate] == 'S' or \
            matriz[xcoordinate][ycoordinate + 1] == 'S' or \
            matriz[xcoordinate + 1][ycoordinate] == 'S':
        return True
    else:
        return False
labyrinth = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
             ['x', ' ', 'x', ' ', ' ', ' ', ' ', 'x'],
             ['x', ' ', 'x', 'x', ' ', 'x', ' ', 'x'],
             ['x', ' ', 'x', 'x', ' ', 'x', ' ', 'x'],
             ['x', 'x', 'x', 'x', ' ', 'x', ' ', 'x'],
             ['x', 'E', ' ', ' ', ' ', ' ', 'S', 'x'],
             ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
PathUp = False
PathRight = False
PathLeft = False
PathDown = False
numberOfpaths = 0
row = 0
while row < len(labyrinth):
    column = 0
    while column < len(labyrinth[0]):
        if labyrinth[row][column] == "E":
            erow = row
            ecolumn = column
        column += 1
    row += 1
currentlx = ecolumn
currently = erow
while checkIfNextToSolution(labyrinth, currentlx, currently) is False:
    PathLeft = False
    PathUp = False
    PathRight = False
    PathDown = False
    if labyrinth[currently -1][currentlx] == " ":
        PathUp = True
        numberOfpaths += 1
    elif labyrinth[currently][currentlx +1] == " ":
        PathRight = True
        numberOfpaths += 1
    elif labyrinth[currently +1][currentlx] == " ":
        PathDown = True
        numberOfpaths += 1
    elif labyrinth[currently][currentlx -1] == " ":
        PathLeft = True
        numberOfpaths += 1
    if PathUp:
        labyrinth[currently -1][currentlx] = "."
        currently -= 1
    elif PathRight:
        labyrinth[currently][currentlx + 1] = "."
        currentlx += 1
    elif PathDown:
        labyrinth[currently + 1][currentlx] = "."
        currently += 1
    elif PathLeft:
        labyrinth[currently][currentlx - 1] = "."
        currentlx -= 1
if checkIfNextToSolution (labyrinth, currentlx, currently) is True:
    print ("You have arrived at the finish line ")
    print ("It took", numberOfpaths, "steps to reach the exit")
drawMatriz(labyrinth)