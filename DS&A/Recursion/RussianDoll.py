def openRussianDoll(doll, i = 1):
    if doll == 1:
        print("All dolls are open")
    else:
        print("Opened doll #", i, sep="")
        openRussianDoll(doll-1, i + 1)

openRussianDoll(10)