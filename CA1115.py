# Your job is to write a Python program that converts the percentage 
# grade to a letter grade. (Download the file as a .txt)

# read class_grades.txt


with open('class_grades.txt') as my_file:
    grades  = my_file.readlines()
    for num in grades:
    	num = int(num)
    	if num >= 90:
    		print num, "A"
    	elif num >= 80 and num <= 89:
    		print num, "B"
  #   	elif num >= 70 and num <= 79:
  #   		print num, "C"
		# elif num >= 60 and num <= 69:
    		#print num, "D"  
		#else:
    		#print num, "F"  
	    
    # make grades an int
    # strip invisibles off
    # write conditional - if num is between 90 and 100 it's an A....

    print grades
    # for item in grades:

