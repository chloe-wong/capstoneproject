def PostGame(name,HighAccuracy, points,num):
    accuracy = int(round((points/num)*100,1))
    print("Your final score is",points,"with percentage accuracy",accuracy)
    linetoadd = name + " " + str(points) + " " + str(accuracy)
    f = open("Scores.txt", "a")
    f.write(linetoadd)
    f.close()
    if accuracy >= HighAccuracy:
        print("new high accuracy!")
        f = open("HighScores.txt","a")
        f.write(linetoadd)
        f.close()
    print("thank you for playing", name, "!")
