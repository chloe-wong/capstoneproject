import random
import procedures
floatnum = 0.0
word, character,question,command = "","","",""
num1, num2 = 0, 0
CharacterList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
CommandList = ["LEFT", "RIGHT", "MID", "ONECHAR", "LENGTH", "LCASE", "UCASE", "TO_UPPER", "TO_LOWER", "NUM_TO_STRING", "STRING_TO_NUM", "INT", "ASC"]
def QuestionGenerator():
    global character
    global floatnum
    global question
    global word
    global num1, num2
    global command
    command = random.choice(CommandList)
    if (command == "LCASE") or (command == "UCASE") or (command == "ASC"):
        character = random.choice(CharacterList)
        if command == "UCASE":
            character = character.lower()
        question = command + "(" + "'" + character + "'" + ")"
    elif (command == "NUM_TO_STRING") or (command == "STRING_TO_NUM") or (command == "INT"):
        floatnum = round(random.uniform(0,100000), random.randint(1,5))
        if command == "STRING_TO_NUM":
            question = command + "(" + "'" + str(floatnum) + "'" + ")"
        else:
            question = command + "(" + str(floatnum) + ")"
    else:
        words = procedures.ReadWords()
        word = random.choice(words)
        if (command == "TO_UPPER") or (command == "TO_LOWER") or (command == "LENGTH"):
            if command == "TO_LOWER":
                word = word.upper()
            question = command + "(" + "'" + word + "'" + ")"
        else:
            num1 = random.randint(1, len(word)-1)
            if command == "MID":
                num2 = random.randint(num1+1,len(word))
                question = command + "(" + "'" + word + "'" + "," + str(num1) + "," + str(num2) + ")"
            else:
                question = command + "(" + "'" + word + "'" + "," + str(num1) + ")"
    return(question)


def AnswerGenerator():
    if command == "TO_UPPER": answer = "'" + word.upper() + "'"
    elif command == "TO_LOWER":answer = "'" + word.lower() + "'"
    elif command == "LCASE":answer = "'" + character.lower() + "'"
    elif command == "UCASE":answer = "'" + character.upper() + "'"
    elif command == "ASC":answer = ord(character)
    elif command == "LENGTH":answer = len(word)
    elif command == "NUM_TO_STRING":answer = "'" + str(floatnum) + "'"
    elif command == "STRING_TO_NUM":answer = floatnum
    elif command == "INT":answer = round(floatnum)
    elif command == "LEFT":answer = "'" + word[0:num1] + "'"
    elif command == "RIGHT":answer = "'" + word[-num1:] + "'"
    elif command == "ONECHAR":answer = "'" + word[num1-1]+ "'"
    elif command == "MID":answer = "'" + word[num1 - 1:num2] + "'"
    return(str(answer))


