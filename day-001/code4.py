##PROJECT OF THE DAY###
#Create a greeting for your program. Ask the user for the city that they grew up in. Ask the user for the name of a pet. Combine the name of their city and pet and show them their band name. The input cursor should show the new line
print("Welcome to the band name generator")
print("Please enter the name of your city in which you grew up in?")
city_name = input()
print("Please enter the name of the pet that you have?")
pet_name = input()
band_name = city_name + " " + pet_name
print("So, according to us, your band name should be " + band_name)