def ReadHighScores():
    with open("HighScores.txt", "r") as f:
        lines = f.read().splitlines()
        HighScoreLine = lines[-1]
    f.close()
    return(HighScoreLine)

def ReadPseudocodeGuide():
    file = open("pseudocodeguide.txt", "r")
    lines = file.readlines()
    for line in lines:
        print(line)
    file.close()

def ReadWords():
    file = open("words.txt", "r")
    words = [word.strip() for word in file]
    file.close()
    return(words)
