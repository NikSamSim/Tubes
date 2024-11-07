#functions
def swing():
	pass

def fan():
	pass

def mode():
	pass

def turbo():
	pass

def quiet():
	pass

def sleep():
	pass

def timer():
	pass

def set_temperature_up():
    pass
def set_temperature_down():
    pass

def auto():
	pass

def display():
    global swing_status
    global fan_status
    global mode_status
    global turbo_status
    global quiet_status
    global sleep_status
    global timer_status
    global temperature_status
    global auto_status

    print(f"{' STATUS ':=^30}")
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
            pass
        case "swing":
            pass
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
            pass
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


while(True):
    display()
    ask()