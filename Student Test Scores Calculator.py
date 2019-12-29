# Sabrina Turney
# Program Name: Student Test Scores Calculator
# This program serves as an example of the "while" and "for" loops, as well as
# building upon previous program functions (using main, calling modules within
# modules, returning values from modules, and global and locally scoped vars.

def main(): #Define the main function
    #I declare variables here so that the program will run without an issue
    #with local vs. global variable scope. I still call the declareVariables
    #module later.

    endProgram = "no"   #string variable - anything but "no" ends the program
    totalScores = 0.0   #float var for calculations
    averageScores = 0.0 #float again for averages, more calculations
    score = 0           #integer
    number = 0          #integer - number of whole students :)
    counter = 1         #integer - used in for loop in getScores module

    while endProgram == "no":   #First repetition structure!
        #Declare variables module gets called first to "reset" program
        endProgram, totalScores, averageScores, score, number, counter = declareVariables(endProgram, totalScores, averageScores, score, number, counter)
        #Number of students taking the test is returned from getNumber module
        number = getNumber(number)
        #All scores are recieved in getScores module
        totalScores = getScores(totalScores, number, score, counter)
        #The averages of all the test scores are calculated and returned
        averageScores = getAverage(totalScores, number, averageScores)
        #Then the average is printed out in this display module
        printAverage(averageScores)
        #User must decide whether to reset program or quit. If the user enters
        #no, the program loops to the top of the while loop, re-calls all the
        #modules, including all calculations and changes to variables! If the
        #user enters anything but "no", the program exits the loop, and the
        #program is finished!
        endProgram = input("Do you want to end the program? Enter no to process a new set of test scores. ")

def declareVariables(endProgram, totalScores, averageScores, score, number, counter):
    #This module declares all the variables we'll use in the program. Notice how
    #endProgram is automatically set to "no", so the loop will iterate at least
    #once before it can be exited. This ensures our program will run!
    endProgram = "no"
    totalScores = 0.0
    averageScores = 0.0
    score = 0
    number = 0
    counter = 1
    #All these declared variables will be the "reset" state in the while loop.
    #When we return them here, they return to the while loop and start
    #the whole program over in a new iteration.
    return endProgram, totalScores, averageScores, score, number, counter

def getNumber(number):
    #This module is where the user inputs the whole number of students that
    #took the test. Notice the int (everyone is 1 whole person!)
    number = int(input("How many students took the test? "))
    return number

def getScores(totalScores, number, score, counter):
    #Here, we use another repetition structure! This is a for loop, and it
    #takes the range of numbers for the number of students entered in the
    #getNumber module. From zero (where a list starts) to the number of
    #students entered by the user, the user inputs again the test scores
    #for each student. Once the range is reached, the program sets the
    #totalScores equal to all the scores added together, and returns it
    #to the main module. This is our first calculation.
    for counter in range(0, number):
        score = int(input("Enter their score: "))
        totalScores = totalScores + score

    return totalScores

def getAverage(totalScores, number, averageScores):
    #Our second calculation begins here. We reference the previous variables
    #we used to get our total scores and the number of students that took the
    #test, divide the two, and then set that value to the variable
    #averageScores. Breaking the calculations up into two modules makes
    #the program very clear. I love this! We return the average scores to main.
    averageScores = totalScores / number
    return averageScores

def printAverage(averageScores):
    #Here's the breadwinner. This module is nice and simple, and just displays
    #the output to the user with the variable we've just calculated from
    #getAverage in a little print statement. We COULD have put this in our
    #while loop, but it would have become cluttered with all the printing and
    #calculations, where in this module, it's very simple to understand.
    print("The average scores is ", averageScores)
    return 

#Last but not least, we call the main function for the user to run the program.
main()
