def direction(facing, turn):
    compass = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    if facing not in compass or turn % 45 != 0 or -1080 >= turn >= 1080:
        return "Not correct data"
    if abs(turn) > 360:
        times = int(turn / 360)
        turn = turn - 360 * times
    i = compass.index(facing) + int(turn / 45)
    if turn >= 0:
        if i <= 7:
            return compass[i]
        else:
            return compass[i - 8]
    else:
        return compass[i]


a = direction("W", 135)
print(a)
