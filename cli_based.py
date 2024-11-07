#functions
def power():
    global power_status
    global power_warning
    print(f"Current power status: {power_status}")
    power_status = input("Enter your changes: ")
    if(power_status == "0"):
        power_status = "Off"
    elif(power_status == "off"):
        power_status = "Off"
    elif(power_status == "Off"):
        power_status = "Off"
    elif(power_status == "1"):
        power_status = "On"
    elif(power_status == "on"):
        power_status = "On"
    elif(power_status == "On"):
        power_status = "On"
    
    else:
        print("Wrong input.")
        power()
    
    if(power_status == "On"):
        power_warning = ""
    
def power_check():
    global power_warning
    if(power_status == "Off"):
        print(f"Your power is off, cannot continue command.")
        power_warning = "<- This needs to be on."
        return False
    
    power_warning = ""
    return True

def swing():
    global swing_status
    status = power_check()
    if(not status):
        return False
    
    print(f"Current swing status: {swing_status}")
    swing_status = input("Enter your changes: ")
    if(swing_status == "0"):
        swing_status = "Off"
    elif(swing_status == "off"):
        swing_status = "Off"
    elif(swing_status == "Off"):
        swing_status = "Off"
    elif(swing_status == "1"):
        swing_status = "On"
    elif(swing_status == "on"):
        swing_status = "On"
    elif(swing_status == "On"):
        swing_status = "On"
    else:
        print("Wrong input.")
        swing()

#TODO finish defining this function
def fan():
    global fan_status
    options = ["Low", "Medium", "High"]
    print(f"Current fan status  : {fan_status}")
    print(f"What you can choose : Low Medium High")
    print(f"Current temperature: {temperature_status}")
    temp_fan_status = input("Enter your changes: ")
    try:
        temp_fan_status = int(temp_fan_status)
    except ValueError:
        if(temp_fan_status == "up"):
            temp_fan_status = temperature_status+1
        elif(temp_fan_status == "down"):
            temp_fan_status = temperature_status-1
        else:
            print("Wrong input.")
            set_temperature()
            return False

def mode():
	global power_status

def turbo():
	global power_status

def quiet():
	global power_status

def sleep():
	global power_status

def timer():
	global power_status

def set_temperature():
    global temperature_status
    status = power_check()
    if(not status):
        return False
    
    print(f"Current temperature: {temperature_status}")
    temp_temperature_status = input("Enter your changes: ")
    try:
        temp_temperature_status = int(temp_temperature_status)
    except ValueError:
        if(temp_temperature_status == "up"):
            temp_temperature_status = temperature_status+1
        elif(temp_temperature_status == "down"):
            temp_temperature_status = temperature_status-1
        else:
            print("Wrong input.")
            set_temperature()
            return False

    temperature_status = temp_temperature_status

def auto():
	global power_status

def display():
    global power_status
    global swing_status
    global fan_status
    global mode_status
    global turbo_status
    global quiet_status
    global sleep_status
    global timer_status
    global temperature_status
    global auto_status
    
    global warning_power

    print(f"{' STATUS ':=^30}")
    print(f"{"Power":<15}: {power_status:<10} {power_warning}")
    print(f"{"Swing":<15}: {swing_status}")
    print(f"{"Fan":<15}: {fan_status}")
    print(f"{"Mode":<15}: {mode_status}")
    print(f"{"Turbo":<15}: {turbo_status}")
    print(f"{"Quiet":<15}: {quiet_status}")
    print(f"{"Sleep":<15}: {sleep_status}")
    print(f"{"Timer":<15}: {timer_status}")
    print(f"{"Temperature":<15}: {temperature_status}")
    print(f"{"Auto":<15}: {auto_status}")
    print(f"{"":=<30}")
    
def ask():
    global power_status
    global swing_status
    global fan_status
    global mode_status
    global turbo_status
    global quiet_status
    global sleep_status
    global timer_status
    global temperature_status
    global auto_status
    
    command = input("What do you want to change? ")
    match command:
        case "power":
            power()
        case "swing":
            swing()
        case "fan":
            pass
        case "mode":
            pass
        case "turbo":
            pass
        case "quiet":
            pass
        case "sleep":
            pass
        case "timer":
            pass
        case "temperature":
            set_temperature()
        case "auto":
            pass
        case "exit":
            pass

power_status = "Off"
swing_status = "Off"
fan_status = "Low"
mode_status = "Normal"
turbo_status = "Off"
quiet_status = "Off"
sleep_status = "Off"
timer_status = "Off"
temperature_status = 23
auto_status = "Off"

power_warning = ""

while(True):
    display()
    ask()