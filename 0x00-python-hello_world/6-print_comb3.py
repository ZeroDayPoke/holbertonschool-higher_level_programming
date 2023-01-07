#!/usr/bin/python3
for diglett in range(0, 10):
    for dugtrio in range(diglett + 1, 10):
        if diglett == 8 and dugtrio == 9:
            print("{}{}".format(diglett, dugtrio), end="")
        else:
            print("{}{}".format(diglett, dugtrio), end=". ")
