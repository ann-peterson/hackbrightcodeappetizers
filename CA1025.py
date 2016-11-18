def eat_it():
	print "Eat it!"


def main():
	choice = raw_input("Should you eat that bacon? Answer 'yes' or 'no'.").lower()
	if choice == "yes":
		frolick = raw_input("Do you want to feel like angels are frolicking on your taste buds? Yes or no.")
		if frolick == "yes":
			print eat_it()
		elif frolick == "no":
			print "You've clearly never tasted bacon."
			print eat_it()
		else:
			print "Are afraid bacon is going to kill you?"
			kill = raw_input("Are you a coward?")
			if kill == "yes":
				print eat_it()

	#elif choice == lower("no"):




if __name__ == '__main__':
	main()
