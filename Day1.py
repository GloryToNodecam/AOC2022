

# reads the list of calories per elf into a list


def getCalList(filename: str) -> list[str]:
    calList = []
    elfCalCurr = []
    with open(filename) as f:
        for line in f:
            if line == "\n":
                if not len(elfCalCurr) == 0:
                    calList.append(elfCalCurr)
                elfCalCurr = []
            else:
                elfCalCurr.append(line)
    return calList

#takes a list of all the calorie numbers carried by each elf and adds them together, 
# replaces the value present in the input list

def calcCal(calList: list[str]) -> None: 
    for i, elf in enumerate(calList):
        tempVal = 0
        for calNum in elf:
            tempVal += int(calNum)    
        calList[i] = tempVal


ElfList = getCalList("Day1Data.txt")
calcCal(ElfList)

print("The highest Calorie carrying elf has:")
print(max(ElfList))
print("calories")

ElfList.sort()

print("The top 3 elves have:")
print(ElfList[-1] + ElfList[-2] + ElfList[-3])
print("calories between them.")