highscore_path = "highscores.txt"

def get_highscores():
    with open(highscore_path, "r") as file:
        result = file.read()
    
    result = result.split("\n")

    result = [x for x in result if x != ""]
    
    return result

def modify_highscore(difficulty, newScore):
    highscores = get_highscores()
    highscores[difficulty - 1] = newScore
    
    highscoreText = ""
    for score in highscores:
        highscoreText += str(score) + "\n"

    with open(highscore_path, "w") as file:
        file.write(highscoreText)