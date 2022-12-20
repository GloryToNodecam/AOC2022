from __future__ import annotations

class Range:
    
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        
    def contains(self, other: Range) -> bool:
        return (self.start <= other.start and self.end >= other.end) or (other.start <= self.start and other.end >= self.end)
    
    def overlaps(self, other: Range) -> bool:
        return (other.start <= self.start <= other.end) or (other.start <= self.end <= other.end) \
            or (self.start <= other.start <= self.end) or (self.start <= other.end <= self.end)


def getPairs(filename: str) -> list[tuple[str]]:
    pairList = []
    with open(filename) as f:
        for line in f:
            pair = line.split(',')
            pairList.append((pair[0], pair[1]))
    return pairList   


def getRanges(pairs: list[tuple[str]]) -> list[tuple[Range]]:
    rangeList = []
    for pair in pairs:
        elfOne = pair[0].split('-')
        elfTwo = pair[1].split('-')
        rangeOne = Range(int(elfOne[0]), int(elfOne[1]))
        rangeTwo = Range(int(elfTwo[0]), int(elfTwo[1]))
        rangeList.append((rangeOne, rangeTwo))
    return rangeList


def getContainments(pairs: list[tuple[Range]]) -> int:
    total = 0
    for pair in pairs:
        total += pair[0].contains(pair[1])
    return total


def getOverlaps(pairs: list[tuple[Range]]) -> int:
    total = 0
    for pair in pairs:
        total += pair[0].overlaps(pair[1])
    return total    



def main():
    pairList = getPairs("DataInputs\Day4Data.txt")
    # pairList = getPairs("DataInputs\Day4TestData.txt")
    pairRanges = getRanges(pairList)
    print(getContainments(pairRanges))
    print(getOverlaps(pairRanges))
    
    

main()