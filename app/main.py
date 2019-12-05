import json
import os
import random
import bottle
import snake

from api import ping_response, start_response, move_response, end_response

@bottle.route('/')
def index():
    return '''
    Battlesnake documentation can be found at
       <a href="https://docs.battlesnake.io">https://docs.battlesnake.io</a>.
    '''

@bottle.route('/static/<path:path>')
def static(path):
    """
    Given a path, return the static file located relative
    to the static folder.

    This can be used to return the snake head URL in an API response.
    """
    return bottle.static_file(path, root='static/')

@bottle.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return ping_response()

@bottle.post('/start')
def start():
    data = bottle.request.json

    """
    TODO: If you intend to have a stateful snake AI,
            initialize your snake state here using the
            request's data if necessary.
    """
    print(json.dumps(data))

    color = "#00FF00"

    return start_response(color)


def isFree(direction, data):
    posY = data["you"]["body"][0]["y"]
    posX = data["you"]["body"][0]["x"]
    newY = posY + 0
    newX = posX + 0

    if direction == "up":
        newY = posY - 1
    if direction == "down":
        newY = posY + 1

    if direction == "left":
        newX = posX - 1
    if direction == "right":
        newX = posX + 1

    print({"dir": direction})
    print({"posX" : posX, "newx": newX})
    print({"posy" : posY, "newy": newY})

    width = data["board"]["width"]

    if newY > width or newY < 0 or newX > width or newX < 0:
        print("bad direction: " + direction)
        return False

    for part in data["you"]["body"]:
        if part["y"] == newY:
            return False
        if part["x"] == newX:
            return False



    return True

@bottle.post('/move')
def move():
    data = bottle.request.json

    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
    print(json.dumps(data))

    directions = ['up',
    'left',
    'down',
    'right',
    'up',
    'up',
        'left',
        'down',
        'right',
    'up',
        'up',
            'left',
            'down',
            'right',
        'up',
            'up',
                'left',
                'down',
                'right',
            'up',
                'up',
                    'left',
                    'down',
                    'right',
                'up',
                    'up',
                        'left',
                        'down',
                        'right',
                    'up',
                        'up',
                            'left',
                            'down',
                            'right',
                        'up',
                            'up',
                                'left',
                                'down',
                                'right',
                            'up',
                                'up',
                                    'left',
                                    'down',
                                    'right',
    ]
    return move_response(directions[data["turn"]])

    for d in ["up", "down", "left", "right"]:
        if isFree(d, data) == True:
            print("chose direction: " + d)
            return move_response(d)


@bottle.post('/end')
def end():
    data = bottle.request.json

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    print(json.dumps(data))

    return end_response()

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
