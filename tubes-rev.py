# Bikin AC

#function
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

def atur_suhu():
	pass

def auto():
	pass

#Main program
power = 'off'
pilihan = ''

print("hello world!")

while(True):
	power = input("Masukkan power: ")
	if(power == 'on'):
		pilihan = input("Mau masukin apa: ")
		match pilihan:
			case 'swing':
				swing()
			case 'fan':
				fan()
			case 'mode':
				mode()
			case "turbo":
				turbo()
			case 'quiet':
				quiet()
			case 'sleep':
				sleep()
			case 'timer':
				timer()
			case 'atur suhu':
				atur_suhu()
			case "auto":
				auto()
			case _:
				print("Wrong input!")
	else:
		print("Power off.")
		break
     