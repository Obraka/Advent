import os
import re

def multichecka(raw):
    games = {}
    legal = 0
    cubepower = 0
    for line in raw:
        # Get Game ID by searching for the first number (not digit):
        gameid = int(re.findall(r"[0-9]+",line)[0])
        # Remove the Game information
        line = re.sub(r"^(.+\: )", "", line)

        # Store the games 
        games[gameid] = line.split(";")

    for gameid in range(1, len(games)+1):
        maxred = 0
        maxblue = 0
        maxgreen = 0

        for round in range(len(games[gameid])):

            red = 0
            blue = 0
            green = 0
            try:
                # Find colors and number before that color 
                green = int((re.findall(r"(\d+) (green)",games[gameid][round])[0][0]))
            except:
                pass
            try:
                blue = int((re.findall(r"(\d+) (blue)",games[gameid][round])[0][0]))
            except:
                pass
            try:
                red = int((re.findall(r"(\d+) (red)",games[gameid][round])[0][0]))
            except:
                pass

                 
            # Check if current numbers are high score, if so, save as high score
            if (green >= maxgreen):
                maxgreen=green
            if (red >= maxred):
                maxred=red
            if (blue >= maxblue):
                maxblue=blue

        # Check if game is legal
        rulered = 12
        rulegreen = 13
        ruleblue = 14
        # Task one, find valid rounds
        if not(maxred > rulered or maxblue > ruleblue or maxgreen >  rulegreen):
            legal = legal + gameid
    
        # Task two, calculate cubepower
        cubepower += maxred * maxblue * maxgreen

    answer = []
    answer.append(legal)
    answer.append(cubepower)


    return answer

def main():
    file = os.path.dirname(os.path.realpath(__file__))
    file += "\input223"

    with open(file) as inputfile:
        raw = [line.rstrip() for line in inputfile]  
    print("Task 1:", multichecka(raw)[0])      
    print("Task 2:", multichecka(raw)[1])      

main()