def genGames(filename: str) -> list[tuple[str]]:
    with open(filename) as f:
        rawGames = f.readlines()
    
    processedGames = []
    for game in rawGames:
        moves = game.split()
        processed = (moves[0], moves[1])
        processedGames.append(processed)
    return processedGames


def handleGamesTier1(gameList: list[tuple[str]]) -> int:
    score = 0
    for game in gameList:
        if game[1].lower() == "x":
            score += 1
            if game[0].lower() == "a":
                score += 3
            if game[0].lower() == "b":
                score += 0
            if game[0].lower() == "c":
                score += 6
       
       
        if game[1].lower() == "y":
            score += 2
            if game[0].lower() == "a":
                score += 6
            if game[0].lower() == "b":
                score += 3
            if game[0].lower() == "c":
                score += 0
       
       
        if game[1].lower() == "z":
            score += 3
            if game[0].lower() == "a":
                score += 0
            if game[0].lower() == "b":
                score += 6
            if game[0].lower() == "c":
                score += 3
       
    
    return score



def handleGamesTier2(gameList: list[tuple[str]]) -> int:
    score = 0
    for game in gameList:
        if game[1].lower() == "x":
            score += 0
            if game[0].lower() == "a":
                score += 3
            if game[0].lower() == "b":
                score += 1
            if game[0].lower() == "c":
                score += 2
       
       
        if game[1].lower() == "y":
            score += 3
            if game[0].lower() == "a":
                score += 1
            if game[0].lower() == "b":
                score += 2
            if game[0].lower() == "c":
                score += 3
       
       
        if game[1].lower() == "z":
            score += 6
            if game[0].lower() == "a":
                score += 2
            if game[0].lower() == "b":
                score += 3
            if game[0].lower() == "c":
                score += 1
       
    
    return score




            
gamesList = genGames("Day2Data.txt")

print(handleGamesTier1(gamesList))

print(handleGamesTier2(gamesList))