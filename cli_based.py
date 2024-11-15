import time

#functions
def power():
    """
    This function changes power to on/off based on user's command
    """
    global power_status
    global power_warning
    print(f"Current power status: {power_status}")
    temp_power_status = input("Enter your changes: ") # using temp variable to avoid accessing the main variable directly
    if(temp_power_status == "0"):
        temp_power_status = "Off"
    elif(temp_power_status == "off"):
        temp_power_status = "Off"
    elif(temp_power_status == "Off"):
        temp_power_status = "Off"
    elif(temp_power_status == "1"):
        temp_power_status = "On"
    elif(temp_power_status == "on"):
        temp_power_status = "On"
    elif(temp_power_status == "On"):
        temp_power_status = "On"
    
    else:
        print("Wrong input.")
        power()
    
    power_status = temp_power_status
    
    if(power_status == "On"):
        power_warning = ""
    
def power_check():
    """
    This function checks whether the power is on or off when the user tries to execute other functions.
    If power is off, the process will terminate and asks the user to turn on the power.
    """
    global power_warning
    if(power_status == "Off"):
        print(f"Your power is off, cannot continue command.")
        power_warning = "<- This needs to be on."
        return False
    
    power_warning = ""
    return True

def swing():
    """
    This function changes swing to on/off based on user's command
    """
    global swing_status
    
    # checks power status
    status = power_check()
    if(not status):
        return False
    
    print(f"Current swing status: {swing_status}")
    temp_swing_status = input("Enter your changes: ") # using temp variable to avoid accessing the main variable directly
    if(temp_swing_status == "0"):
        temp_swing_status = "Off"
    elif(temp_swing_status == "off"):
        temp_swing_status = "Off"
    elif(temp_swing_status == "Off"):
        temp_swing_status = "Off"
    elif(temp_swing_status == "1"):
        temp_swing_status = "On"
    elif(temp_swing_status == "on"):
        temp_swing_status = "On"
    elif(temp_swing_status == "On"):
        temp_swing_status = "On"
    else:
        print("Wrong input.")
        swing()
        
    swing_status = temp_swing_status

def fan():
    """
    This function changes fan speed to low/medium/high based on user's command
    """
    global fan_status
    
    # checks power status
    status = power_check()
    if(not status):
        return False
    
    options = ["Low", "Medium", "High"]
    print(f"Current fan status  : {fan_status}")
    print(f"What you can choose : Low Medium High")
    temp_fan_status = input("Enter your changes: ") # using temp variable to avoid accessing the main variable directly
    try:
        temp_fan_status = int(temp_fan_status)
    except ValueError:
        if(temp_fan_status == "low"):
            temp_fan_status = options[0]
        elif(temp_fan_status == "medium"):
            temp_fan_status = options[1]
        elif(temp_fan_status == "high"):
            temp_fan_status = options[2]
        else:
            print("Wrong input.")
            fan()
            return False
    else:
        if(temp_fan_status == 1 or temp_fan_status == 0):
            temp_fan_status = options[0]
        elif(temp_fan_status == 2):
            temp_fan_status = options[1]
        elif(temp_fan_status == 3):
            temp_fan_status = options[2]
        else:
            print("Wrong input.")
            fan()
            return False
    
    fan_status = temp_fan_status

def mode():
    """
    This function changes mode to the listed options based on user's input
    """
    global mode_status
    
    status = power_check()
    if(not status):
        return False

    options = ["Cool", "Dry", "Fan", "Turbo", "Quiet", "Sleep", "Auto"]
    print(f"Current mode status: {mode_status}")
    print(f"What you can choose: ", end="")
    for op in options:
        print(f"{op} ", end="")
    print()
    # using temp variable to avoid accessing the main variable directly
    temp_mode_status = input("Enter your changes: ").lower() 
    
    try:
        temp_mode_status = int(temp_mode_status)
    except ValueError:
        if(temp_mode_status == "cool"):
            temp_mode_status = options[0]
        elif(temp_mode_status == "dry"):
            temp_mode_status = options[1]
        elif(temp_mode_status == "fan"):
            temp_mode_status = options[2]
        elif(temp_mode_status == "turbo"):
            temp_mode_status = options[3]
        elif(temp_mode_status == "quiet"):
            temp_mode_status = options[4]
        elif(temp_mode_status == "sleep"):
            temp_mode_status = options[5]
        elif(temp_mode_status == "auto"):
            temp_mode_status = options[6]
        else:
            print("Wrong input.")
            mode()
            return False
    else:
        if(temp_mode_status >=0 and temp_mode_status <= len(options)):
            if(temp_mode_status == 0):
                temp_mode_status = options[0]
            else:
                temp_mode_status = options[temp_mode_status-1]
        else:
            print("Wrong input.")
            mode()
            return False
    
    mode_status = temp_mode_status

def timer():
    # This function sets a timer to automatically turn off
    # the power after a specified duration in minutes.
    global power_status, timer_status
    status = power_check()
    if (not status):
        return False
        
    print(f"Current timer status: {timer_status}")
    duration_minutes = int(input("Enter timer duration in minutes: "))
    timer_status = f"{duration_minutes} min"
    print(f"Timer set for {duration_minutes} minutes.")
    # Wait for the specified duration
    time.sleep(duration_minutes * 60) # Converts minutes to seconds
    # After time is up, turn off power and reset timer
    power_status = "Off"
    timer_status = "Off"
    print("Timer ended. Power has been turned off automatically.")
    return True
    
def set_temperature():
    global temperature_status
    status = power_check()
    if(not status):
        return False
    
    print(f"Current temperature: {temperature_status}")
    temp_temperature_status = input("Enter your changes: ") # using temp variable to avoid accessing the main variable directly
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

def display():
    global power_status
    global swing_status
    global fan_status
    global mode_status
    global timer_status
    global temperature_status
    
    global warning_power

    print(f"{' STATUS ':=^30}")
    print(f"{"Power":<15}: {power_status:<10} {power_warning}")
    print(f"{"Swing":<15}: {swing_status}")
    print(f"{"Fan":<15}: {fan_status}")
    print(f"{"Mode":<15}: {mode_status}")
    print(f"{"Timer":<15}: {timer_status}")
    print(f"{"Temperature":<15}: {temperature_status}")
    print(f"{"":=<30}")
    
def ask():
    global power_status
    global swing_status
    global fan_status
    global mode_status
    global timer_status
    global temperature_status
    
    command = input("What do you want to change? ")
    match command:
        case "power":
            power()
        case "swing":
            swing()
        case "fan":
            fan()
        case "mode":
            mode()
        case "timer":
            timer() 
        case "temperature":
            set_temperature()
        case "exit":
            return False
    
    return True

power_status = "Off"
swing_status = "Off"
fan_status = "Low"
mode_status = "Normal"
timer_status = "Off"
temperature_status = 23

power_warning = ""

while(True):
    display()
    status = ask()
    if(not status):
        print(f"Program terminated.")
        break
