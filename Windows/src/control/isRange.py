def in_range(x, y, i):
    if (x + i) > 7 or (y + i) > 7:
        print("Fora de alcance")
        return False
    elif (x - i) < 0 or (y + i) > 7:
        print("Fora de alcance")
        return False
    elif (x + i) > 7 or (y - i) < 0:
        print("Fora de alcance")
        return False
    elif (x - i) < 0 or (y - i) < 0:
        print("Fora de alcance")
        return False

    return True
