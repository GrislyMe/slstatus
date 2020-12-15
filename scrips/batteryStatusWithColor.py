with open("/sys/class/power_supply/BAT0/capacity") as bat:
    perc = int(bat.readline())
    if perc > 50:
        print(u"\u001b[32;1m %s%%" % perc)
    elif perc > 25:
        print(u"\u001b[33;1m %s%%" % perc)
    else:
        print(u"\u001b[31;1m %s%%" % perc)
