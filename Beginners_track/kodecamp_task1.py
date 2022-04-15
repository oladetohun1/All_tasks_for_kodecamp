temp = float(input("Enter a temperature value :"))
unit = str(input("What unit is the temp currently in?\n Please type in Celsius or Fahrenheit:"))
F = 9*(temp)/5 + 32
C = 5*(temp - 32)/9
if unit == "Fahrenheit":
    print("The value of" ,str(temp) + unit ,"is :" ,str(C)+"Celsius")
elif unit == "Celsius":
    print("The value of" ,str(temp) + unit ,"is :" ,str(F)+"Fahrenheit")
