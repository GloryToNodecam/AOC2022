import re
box_stack = [['D', 'L', 'J', 'R', 'V', 'G', 'F'], ['T' ,'P', 'M', 'B', 'V', 'H', 'J', 'S'], ['V', 'H', 'M','F', 'D', 'G', 'P','C'],\
    ['M', 'D', 'P', 'N', 'G', 'Q'], ['J', 'L', 'H', 'N', 'F'], ['N', 'F', 'V', 'Q', 'D', 'G', 'T', 'Z'], ['F', 'D', 'B', 'L'],\
        ['M', 'J', 'B', 'S', 'V', 'D', 'N'], ['G', 'L', 'D']]

def getMoves(filename) -> list[list[int]]:
    moveList = []
    with open(filename) as f:
        for line in f:
            moveList.append([int(s) for s in re.findall(r'\d+', line)])
    return moveList

def doMovesDumb(moveList: list[list[int]]):
    for move in moveList:
        for _ in range(move[0]):
            box_stack[move[2] - 1].append(box_stack[move[1] - 1].pop())\
                
                
def doMovesSmart(moveList: list[list[int]]):
    for move in moveList:
        temp_stack = []
        for _ in range(move[0]):
            temp_stack.append(box_stack[move[1] - 1].pop())
        for _ in range(len(temp_stack)):
            box_stack[move[2] - 1].append(temp_stack.pop())

def readBoxes():
    message = ''
    for stack in box_stack:
        message += stack.pop()
    print(message)
    

moveList = getMoves("DataInputs\Day5Data.txt")


doMovesSmart(moveList)

readBoxes()