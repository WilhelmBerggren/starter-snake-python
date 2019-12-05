import json


def getDir(data):
    width = data.board.width
    turn = data.turn

    posY = data.you.body[0]
    posX = data.you.body[1]

    
    directions = ['up', 'left', 'right', 'down']


    """direction = random.choice(directions)"""

    direction = directions[turn % 2]


    

    return direction