import sys

width = 0
radius = 0
PI = 3.14159  #Define the variable PI
i = 0
num = 0

#Print the menu of calculations
print("Calculations")
print("\n1. Calculate area of a square")
print("\n2. Calculate area of a circle")
print("\n3. Display palindromes up to 1,000")
print("\n4. Exit")

x = int(input("\nEnter an option: "))  #Declares the variable x and asks the user to define the input value

#Function to calculate the area of a circle
def areaCircle(radius):
    return PI * (radius * radius)

#Function to calculate the area of a square    
def areaSquare(width):
    return width * width

#Function to print all palindromes
def isPalindrome(num):
    str(num)
    reverse = ""
    for i in str(num):
        reverse += str(i)
    return str(reverse)
       
#
if (x == 1):
    print("\n**** Area of a square ****") 
    print("\nEnter width of square (cm): ")
    width = int(input("Enter the width of the circle: "))
    print("\nThe area of a square of " + str(width) + "cm = " + str(areaSquare(width)) + "cm squared")
elif (x == 2):
    print("\n**** Area of a circle ****")
    print("Enter radius of circle (cm): ")
    radius = float(input("Enter the radius of the circle: "))
    print("The area of a circle of " + str(radius) + "cm = " + str(areaCircle(radius)) + "cm squared")
elif (x ==3):
    print("\n**** Palindromes ****")
    for i in range (0,1001):
        if (isPalindrome(i)):   #Calls the isPalindrome function to check the number is a palindrome
            print(i)            #If the number is a palindrome it prints the number to screen
            
elif (x == 4):
    print("\nGoodbye!")
    quit
    
    

else:
    print("Invalid Option")
    
           

        


