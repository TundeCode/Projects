# Babatunde Fakolujo
# CSC 100 -Spring 2023
# Programming Project Design
# Due 5/2/23
#

# For this project I will be using code from lab 5

# Program Title: Airline Scheduling Program


# Project Description:
# The program will have information about flights from Providence, RI to Orlanado
# It will ask different question to the user about flights

# Ask user for File
def openFile():
    goodFile = False
    while not goodFile:
        fname = input("Please enter a file name: ")
        try:
            inFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid file name try again ...")
    return inFile


# This Function gets all the information from the File
def getData():
    infile = openFile()

    airList = []
    flightnumList = []
    departList = []
    arrivalList = []
    pricesList = []

    line = infile.readline()

    while line != "":
        line = line.strip()
        airline, flightNumber, depart, arrive, price = line.split(",")

        airList.append(airline)
        flightnumList.append(flightNumber)
        departList.append(depart)
        arrivalList.append(arrive)
        pricesList.append(price)

        line = infile.readline()

    infile.close()
    return airList, flightnumList, departList, arrivalList, pricesList
#Where the user will chose the options
def getChoice():
    while True:
        print("")
        print("Please choose one of the following options:")
        print("1 -- Find flight information by airline and flight number")
        print("2 -- Find flights shorter than a specified duration")
        print("3 -- Find the cheapest flight by a given airline")
        print("4 -- Find flight departing after a specified time")
        print("5 -- Find the average price of all flights")
        print("6 -- Write a file with flights sorted by departure time")
        print("7 -- Quit")
        OK = False
        while OK == False:
            try:
                choice = int(input("Choice ==> "))
                if choice < 1 or choice > 7:
                    print("Entry must be between 1 and 7")
                else:
                    return choice
            except ValueError:
                print("Entry must be a number")

#This function will find if the inputted flight and number that the user entered is valid
def findFlight(airList,flightnumList,departList,arrivalList,pricesList):
    #Makes sure the user flight is on the list
    print("")
    OK = False
    while not OK:
        airline = input("Enter airline name : ")
        if airline in airList:
            OK = True
        else:
            print("Invalid input -- try again")

    #Make sure flight number is true
    found = False
    while not found:
        try:
            flightNumber = input("Enter flight number: ")
            if flightNumber in flightnumList:
                found = True
            else:
                print("Invalid input -- try again")
        except ValueError:
            print("Invalid input -- try again")

    #Gets the information
    for i in range(len(airList)):
        if airList[i] == airline and flightnumList[i] == flightNumber:
            print("")
            print("The flight that meets your criteria is:")
            print("")
            print("AIRLINE FLT# DEPART ARRIVE PRICE")
            print( airList[i],""  "",flightnumList[i],""  "", departList[i],""  "", arrivalList[i],""  "", pricesList[i])


#Converts times used for function SortFLight
#Code help received from office hours
def timeConversion(time):
    hours,mins = time.split(":")
    hours = int(hours)
    mins = int(mins)
    hours = hours * 60
    total = hours+ mins
    return total






def findShortFlight(airList,flightnumList,departList,arrivalList,pricesList):
    # empty list to store the flights that meet requirements
    flightList = []
    # maximum duration set to None
    print("")
    maxDur = None
    while maxDur is None:
        try:
           
            maxDur = int(input("Enter maximum duration (in minutes): "))
        except ValueError:
            print("Entry must be a number")
    # loop through every flight in list
    for i in range(len(departList)):
        # convert hh:mm format to min
        departHours,departMinutes = departList[i].split(':')
        departHours = int(departHours)
        departMinutes = int(departMinutes)
        departTime = departHours * 60 + departMinutes

        # convert arrival time format to min
        arrivalHours,arrivalMinutes = arrivalList[i].split(':')
        arrivalHours = int(arrivalHours)
        arrivalMinutes = int(arrivalMinutes)
        arrivalTime = arrivalHours * 60 + arrivalMinutes

        # calculate the duration
        flightDur = arrivalTime - departTime

        if flightDur <= maxDur:
            #if no flight have been printed yet , printed yet
            if not flightList:
                print(" ")
                print("The flights that meet your criteria are:")
                print("")
                print("AIRLINE  FLT#   DEPART ARRIVE  PRICE")
            # add the flight to the list of matching flights
            flightList.append((airList[i], flightnumList[i], departList[i], arrivalList[i], pricesList[i]))

    # print the list of matching flights, or a message if no flights meet the criteria
    if not flightList:
        print("")
        print("No flights meet your criteria")
    else:
        for flight in flightList:
            print(flight[0].ljust(8), flight[1].ljust(4), flight[2].rjust(8),flight[3].rjust(7),str(flight[4]).rjust(6))
            
#Finds the cheapest flight 
def findCheapestFlight(airList,flightnumList,departList,arrivalList,pricesList):
    #  variables to keep track of cheapest flight
    index = 0 
    cheapest = pricesList[0]
    lowest = float('inf')
    airline = ""

# Prompt user to enter airline name and validate input
    print("")
    while True:
        airline = input("Enter airline name: ")
        if airline in airList:
            break
        else:
            print("Invalid input -- try again")

    # Iterate through each flight in the lists for the specified airline    
    for i in range(len(pricesList)):
        if airList[i] == airline:
            price = int(pricesList[i].replace("$",""))
            if price < lowest:
            # Update lowest price and index of cheapest flight
                lowest = price
                index = i

                # Print information for the cheapest flight found
                print(" ")
                print("The flight that meets your criteria is:")
                print(" ")
                print("AIRLINE  FLT#   DEPART   ARRIVE   PRICE")
                print(airList[i].ljust(8), flightnumList[i].ljust(4), departList[i].rjust(8),arrivalList[i].rjust(7),str(pricesList[i]).rjust(8))
    
    

#This function is used to find the average price
def findAverage(pricesList):
    total = 0
    count = 0
    for price in pricesList:
        #remove leading/trailing whitespace and dollar sign
        price = price.strip().replace('$', '')  
        total += int(price)
        count += 1
    average = total / count 
    print("The average price is $", round(average,2))
    
def isValidTime(time):
    try:
        # Split the time string into hours and minutes
        hours, mins = time.split(":")
    # Check that the hours and minutes are two digits long
        if len(hours) != 2 or len(mins) != 2:
            return False

    # Convert hours and minutes to integers
        hours = int(hours)
        mins = int(mins)

        # Check that hours and minutes are in valid rang
        if hours < 0 or hours > 24 or mins < 0 or mins > 60:
            return False
    except ValueError:
        return False
    return True

def findDepartAfterTime(airList, flightnumList, departList, arrivalList, pricesList):
    # Prompt user to enter earliest departure time and validate input
    print("")
    departTime = input("Enter earliest departure time: ")
    while not isValidTime(departTime):
        departTime = input("Invalid time - Try again ")
    print(" ")

    # Counter variable to keep track of how many flights meet the criteria
    counter = 0

    # Iterate through each flight in the lists
    for i in range(len(departList)):

     # Check if the flight departs after the specified departure time
        if timeConversion(departList[i]) > timeConversion(departTime):

    # If this is the first flight that meets the criteria, print header row
            if counter == 0:
                print("The flights that meet your criteria are:")
                print("")
                print("AIRLINE  FLT#   DEPART ARRIVE  PRICE")

    # Increment counter and print flight information
            counter += 1
            print(airList[i].ljust(8), flightnumList[i].ljust(4), departList[i].rjust(8),arrivalList[i].rjust(7),str(pricesList[i]).rjust(4))

    # If no flights meet the criteria, print message
    if counter == 0:
        print("")
        print("No flights meet your criteria")

def SortFlight(airList, flightnumList, departList, arrivalList, pricesList):
    with open('time-sorted-flights.csv', 'w') as fname:
        indexList = []
#append each index of departlist in indexList
        for a in range(len(departList)):
            indexList.append(a)

        for b in range(0,len(departList)):
            temp = 0
            indexTemp = 0

   # make it so it start the  element but the first index 
            for i in range(1,len(departList)):
                temp = departList[i]
                indexTemp =indexList[i]

               #Used code from homework 6  and using bubble sort
                if timeConversion(departList[i]) < timeConversion(departList[i-1]):       
                    departList[i] = departList[i-1]
                    departList[i-1] = temp
                    indexList[i] = indexList[i-1]
                    indexList[i-1] = indexTemp

        for c in range(len(indexList)):
            fname.write(str(airList[indexList[c]]) + "," + str(flightnumList[indexList[c]]) + "," + str(departList[c]) + "," + str(arrivalList[indexList[c]]) + "," + str(pricesList[indexList[c]]) + "\n")
    print("")
    print("Sorted data has been written to file: time-sorted-flights.csv")




def main():
    airList, flightnumList, departList, arrivalList, pricesList = getData()
    choice = getChoice()
    while choice != 7:
        if choice == 1:
            findFlight(airList,flightnumList,departList,arrivalList,pricesList)
            choice = getChoice()
        elif choice == 2:
            findShortFlight(airList,flightnumList,departList,arrivalList,pricesList)
            choice = getChoice()
        elif choice == 3:
             findCheapestFlight(airList,flightnumList,departList,arrivalList,pricesList)
             choice = getChoice()
        elif choice == 4:
            findDepartAfterTime(airList, flightnumList, departList, arrivalList, pricesList)
            choice = getChoice()
        elif choice == 5:
            findAverage(pricesList)
            choice = getChoice()
        elif choice == 6:
            SortFlight(airList,flightnumList,departList,arrivalList,pricesList)
            choice = getChoice()           
    else:
         print("Thank you for flying with us")
      





