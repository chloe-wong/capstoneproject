import questiongenerator
import random

word, character, question = "","",""
floatnum = 0.0
num1, num2 = 0,0

def RunGame():
    global points
    points = 0
    numquestions = int(input("input number of questions to attempt"))
    for x in range(numquestions):
        currentquestion = questiongenerator.QuestionGenerator()
        currentanswer = questiongenerator.AnswerGenerator()
        print(currentquestion)
        useranswer = input("what is the answer?")
        if useranswer == currentanswer:
            points = points + 1
            print("correct!")
        else:
            print("wrong, the answer is:", currentanswer)
        print("You have",points,"points")
    return(points,numquestions)