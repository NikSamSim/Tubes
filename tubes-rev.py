# Bikin AC

import tkinter as tk
import tkinter.messagebox
import tkinter.ttk
import sys

#function
#TODO define the functions
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
    global temperature
    temperature += 1
    temperature_text.set(f"{temperature}\N{DEGREE SIGN}")
    temperature_number.configure(text=temperature_text.get())
    
def set_temperature_down():
    global temperature
    temperature -= 1
    temperature_text.set(f"{temperature}\N{DEGREE SIGN}")
    temperature_number.configure(text=temperature_text.get())

def auto():
	pass

#Main program
power = False
pilihan = ''
temperature = 0


# initializing window
root = tk.Tk()
frm_top = tk.Frame(root)
frm_top.grid()


# Displaying temperature and such
frm1 = tk.Frame(frm_top, height=500, width=500, bg="red")
frm1.grid(row=0, column=0)

temperature_display = tk.Frame(frm_top, height=500, width=500, bg = "green")
temperature_display.grid(row=0, column=1)


temperature_text = tk.StringVar()
temperature_text.set(f"{temperature}\N{DEGREE SIGN}")

temperature_number = tk.ttk.Label(temperature_display, text=temperature_text.get())
temperature_number.grid(row=0,column=0)
temperature_number.configure(font=("Calibri", 100))

#buttons
frm_button = tk.Frame(root, bg="magenta")
frm_button.grid()


def switch_power():
    global power
    power = not power
    
power_button = tk.ttk.Button(frm_button, text="POWER", command=switch_power)
power_button.grid(row=0, column=0)

swing_button = tk.ttk.Button(frm_button, text="SWING", command=swing)
swing_button.grid(row=0, column=1)

fan_button = tk.ttk.Button(frm_button, text="FAN", command=fan)
fan_button.grid(row=1, column=0)

mode_button = tk.ttk.Button(frm_button, text="MODE", command=mode)
mode_button.grid(row=1, column=1)

turbo_button = tk.ttk.Button(frm_button, text="TURBO", command=turbo)
turbo_button.grid(row=2, column=0)

quiet_button = tk.ttk.Button(frm_button, text="QUIET", command=quiet)
quiet_button.grid(row=2, column=1)

sleep_button = tk.ttk.Button(frm_button, text="SLEEP", command=sleep)
sleep_button.grid(row=3, column=0)

timer_button = tk.ttk.Button(frm_button, text="TIMER", command=timer)
timer_button.grid(row=3, column=1)

temperature_up_button = tk.ttk.Button(frm_button, text="UP", command=set_temperature_up)
temperature_up_button.grid(row=4, column=0)

temperature_down_button = tk.ttk.Button(frm_button, text="DOWN", command=set_temperature_down)
temperature_down_button.grid(row=4, column=1)

# while(True):
# 	if(power == True):
# 		print("power on.")
# 		pilihan = input("Mau masukin apa: ")
# 		match pilihan:
# 			case 'swing':
# 				swing()
# 			case 'fan':
# 				fan()
# 			case 'mode':
# 				mode()
# 			case "turbo":
# 				turbo()
# 			case 'quiet':
# 				quiet()
# 			case 'sleep':
# 				sleep()
# 			case 'timer':
# 				timer()
# 			case 'atur suhu':
# 				atur_suhu()
# 			case "auto":
# 				auto()
# 			case _:
# 				print("Wrong input!")
# 	else:
# 		print("Power off.")

root.mainloop()