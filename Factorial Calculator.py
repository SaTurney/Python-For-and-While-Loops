# Sabrina Turney
# September 17, 2018
# Name of program: Calculating the Factorial of a Number
# Description of program: This program takes a whole number input from the user,
# and then displays that number's factorial.

# Defining the main function
def main():
    #Declaring the variable we're using
    factorial = 1

    #User introduction below, welcoming the user to the program.
    print("Welcome to my factorial calculator!")
    print("Enter a postive whole number, and it will print out the factorial.")

    #Asking for user's input. Using int for a whole number value
    userInput = int(input ("Please enter a number: "))
    
    #Here is where my nested repetition structure begins
    #We begin with an If Else block to check that our input works
    #This block catches negatives before running the program
    if userInput < 0:
       print("Please enter a positive integer.")
       
    #Then if the input works, our repetition structure executes
    #This structure does the calculation to actual find the factorial
    #It takes the user input variable, and multiplies each instance of it until
    #The number is completed in the range (inclusive, so I added +1)
    #Then we assign the completed calculation to "factorial"
    else:
       for number in range(1, userInput + 1):
           factorial = (factorial * number)
           
    #Then we display the output to the user. I make it print the original input.
    print(f"The factorial for {userInput} is \t{factorial}!")

main()
#Last but not least, the main() module is called for the user to start.
