#Write a program that repeatedly asks the user to enter product names and prices. Store all of these in a dictionary whose keys are the product names and whose values are the prices. When the user is done entering products and prices, allow them to repeatedly enter a product name and print the corresponding price or a message if the product is not in the dictionary
n = int(input("Enter Number of product you would love to input:"))#Allows user to enter the number of product to add
product_price = {}#defined an empty dictionary to put the product and price

for i in range(n): #initializing a for loop
        product = str(input("Enter the name of the  product  would love to add:"))#Allows the user to enter the name of the product to add
        price = int(input("Enter the price of the product:"))#Allows the user to enter the price of the corresponding product enterede
        product_price[product] = price#set the key and value pair of the dictionary
print("The products and the corresponding price are :",product_price)#prints out the dictionary

product_check = str(input("Enter a product name and i would tell you the price:"))#Allows useo enter a product
if product_check not in product_price:#Check if the product is not already in the dictionary
        print("Such product does not exist")#prints this if it is not in the dictionary
else:
    print("The price of the product is =",product_price[product_check])#print the corresponding price of the product if it is in the dictionary
