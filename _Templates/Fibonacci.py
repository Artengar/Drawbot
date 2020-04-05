#This script provides the Fibonacci numbers for a desired amount of steps

amountOfSteps = 10

#Do the work
def fibonacci(amountOfSteps):
    currentNumber = 1
    previousNumber = 1
    olderNumber = 1
    for step in range(amountOfSteps):
        if step != 0 and step != 1:
            olderNumber = previousNumber
            previousNumber = currentNumber
            currentNumber += olderNumber
        print(currentNumber)

fibonacci(amountOfSteps)




