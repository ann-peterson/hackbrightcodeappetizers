# write a function that takes this list and returns a dictionary with the name of the food as the key and the price as the value

menu_list = ["food : hotdog, price : 5.50", "food : burger, price : 9.50", 
			"food : fries, price : 4.00", "food : shake, price : 5.00"]





# split at ":"
# split at ","
def list_to_dict():
	food_dict = {}
	for item in menu_list:
		split_string = item.split(",")
		#print split_string
		food = split_string[0].split(":")
		#print food
		price = split_string[1].split(":")
		#print price
		food_dict[food[1]] = price[1]
		return food_dict
		
	
#print food_dict


		#print menu_list


# menu_list[0]

#print menu_list


# def main():
# 	menu = menu_to_dict(MENU_LIST)
# 	for name, 
