import procedures
def Pregame():
    name = input("what's your name?")
    HighScoreLine = procedures.ReadHighScores()
    HighAccuracy = float(HighScoreLine[-4:])
    viewhighscore = input("view high score? Y/N")
    if viewhighscore == "Y" or "y":
        print(HighScoreLine)
    viewguide = input("view pseudocode guide? Y/N")
    if viewguide == "Y" or "y":
        procedures.ReadPseudocodeGuide()
    print("Just a reminder: for all strings, use single quotes around the string answer you give.")
    print("Let's start!")
    return(name, HighAccuracy)
