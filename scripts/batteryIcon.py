with open("/sys/class/power_supply/BAT0/capacity") as bat:
    perc = int(bat.readline())
    if perc > 90:
        print("")
    elif perc > 65:
        print("")
    elif perc > 45:
        print("")
    elif perc > 25:
        print("")
    else:
        print("")
