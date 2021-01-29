import pregame
import rungame
import postgame
name = pregame.Pregame()
points = rungame.RunGame()
name, HighAccuracy,points,num = str(name[0]), float(name[1]),int(points[0]),int(points[1])
postgame.PostGame(name,HighAccuracy,points,num)
