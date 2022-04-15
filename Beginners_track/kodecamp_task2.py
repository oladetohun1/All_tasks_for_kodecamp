'''A code that Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the entries in the list that are greater than 10 with 10.'''

#initialize the variable 'LIST_numbers' and allow the user to assign a list to it

LIST_numbers = input("Create a list that contains numbers between 1 and 12:")
LIST_numbers = LIST_numbers.split( )
print("You created alist with:",LIST_numbers)


#iterate through the numbers in the list entered by the user

for i in range(len(LIST_numbers)):
    
    #check if the nubers in the list are greater than 10
    
    if LIST_numbers[i] > str(10):
        
        #replace the number that s greater than 10 with 10

        LIST_numbers[i] = str(10)
        
#prnt the result
        
print("The new list gotten after replacing all numbers greater than 10 with 10 is:",LIST_numbers)

