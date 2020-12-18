with open("/sys/class/power_supply/BAT0/capacity") as bat:
    perc = int(bat.readline())
    if perc > 90:
        print("", end = "")
    elif perc > 65:
        print("", end = "")
    elif perc > 45:
        print("", end = "")
    elif perc > 25:
        print("", end = "")
    else:
        print("", end = "")

with open("/sys/class/power_supply/BAT0/status") as status:
    current = status.readline().split()
    if current[0] != "Discharging":
        print("  ﮣ", perc)
    else:
        print(" ")
