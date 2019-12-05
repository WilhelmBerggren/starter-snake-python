d = {"turn": 21, "game": {"id": "9e97a607-1359-4fb1-bd1e-a91c13c8f3c0"}, "board": {"food": [{"y": 3, "x": 12}, {"y": 14, "x": 6}, {"y": 12, "x": 10}, {"y": 13, "x": 11}, {"y": 12, "x": 7}, {"y": 6, "x": 8}, {"y": 6, "x": 13}, {"y": 3, "x": 1}, {"y": 5, "x": 3}, {"y": 4, "x": 2}], "width": 15, "snakes": [{"body": [{"y": 5, "x": 0}, {"y": 4, "x": 0}, {"y": 3, "x": 0}], "health": 79, "id": "9d9138c9-f6c2-4607-b95b-9adcdc934553", "name": "Test"}], "height": 15}, "you": {"body": [{"y": 5, "x": 0}, {"y": 4, "x": 0}, {"y": 3, "x": 0}], "health": 79, "id": "9d9138c9-f6c2-4607-b95b-9adcdc934553", "name": "Test"}}

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


if __name__ == "__main__":
    print(isFree("right", d) == True)