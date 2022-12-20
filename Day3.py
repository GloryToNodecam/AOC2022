def getBackpacks(filename: str) -> list[tuple[str]]:
    with open(filename) as f:
        rawBags = f.readlines()
    return rawBags

def getCommonItems(rawBags: list[str]) -> list[str]:
    commonItems = []
    processedBags = []
    for bag in rawBags:
        splitter = len(bag) // 2
        newBag = (bag[:splitter], bag[splitter:])
        processedBags.append(newBag)
    
    
    for bag in processedBags:
        for char in bag[0]:
            if char in bag[1]:
                commonItems.append(char)
                break
    return commonItems


def getBadges(bags: list[str]) -> list[str]:
    badgeList = []
    for index in range(0, len(bags), 3):
        for char in bags[index]:
            if char in bags[index + 1] and char in bags[index + 2]:
                badgeList.append(char)
                break
    return badgeList


def getItemsPrio(items: list[str]) -> int:
    total = 0
    for item in items:
        if item.isupper():
            total += ord(item) - 38
        elif item.islower():
            total += ord(item) - 96
    return total


backpacks = getBackpacks("Day3Data.txt")

commonItems = getCommonItems(backpacks)

itemPrio = getItemsPrio(commonItems)

badges = getBadges(backpacks)

badgePrio = getItemsPrio(badges)

print(itemPrio)


print(badgePrio)