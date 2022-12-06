# Volunteer Management Program by Sana Asraf

"""
This program has been created to manage a list of volunteers for an event. With five functions, it allows the user to
add names to the volunteer list and to remove them. Additionally, it allows the user to view the shifts worked by
every volunteer. In the case of this program and event, there are 2 possible shifts and the first five volunteers
listed will work the morning shift (8am-4pm) and the rest will work the evening shift (4pm-10pm).
* In this program however, the names and shifts are fixed and cannot be interchanged amongst each other. However,
for future projects, on a more complex and bigger scale, this can be implemented. * (ie, for this program and
event, every volunteer will be working the shift assigned to them without change or modification)
Apart from this, this program also helps set up an allowance plan for the volunteers, and it is listed as one of the programs functions.
And finally, with the help of the "random" module, this program also chooses a random volunteer from the list to work
an extra shift.

"""

# title
print("hello!")
print("---------------------------------\nVOLUNTEER MANAGEMENT FOR AN EVENT\n---------------------------------")


# below are the lists that contain information about the initial names of the volunteers and available shifts

volunteer_names = ["Betty", "Augustine", "Inez", "James", "Dorothea", "Este", "Taylor", "Joe", "Stephen", "Drew",
                   "Tim", "Cory", "Arushi", "Aria"]
shifts = ["8AM- 4PM", "4PM-10PM"]


# below is the code for displaying the names of volunteers before the choice menu for reference

print("       Volunteer Names    \n       ***************")
i = 1
for name in volunteer_names:   # for loop to display names individually
    print("        " + str(i) + "." + " " + str(name))  # for every loop, a new employee and a new number is displayed
    i = i + 1


# below is a main function that serves to show a display menu, that allows the user to choose within a few options. this function will be prevalent throughout the whole program.

def main():
    print("------------------\nCHOICES- choose the corresponding number to make a selection\n1: Add names to the volunteer list\n2: Review names and shifts\n3: Review the payment plan for the volunteers\n4: See which random volunteer will be working an extra shift\n5: Remove a volunteer")

    while True:
        choice = input("-------------------\nEnter choice number\nor press any other key to exit the program:\n") # input for choice

# according to the choice, the if/elif/else statements decide on which function to display to the user
        if choice == "1":
            addname()

        elif choice == "2":
            namesandshift()

        elif choice == "3":
            paymentplan()

        elif choice == "4":
            randomvolunteer()

        elif choice == "5":
            removevolunteer()

        else:
            print("\nThank you!")
            break


# below is a function to add new names to the volunteer list

def addname():
    print("\n---------\nADD NAMES\n---------")
    namesagain = "Y"
    while namesagain == "Y" or namesagain == "y":  # specifying condition for displaying the input again with a while loop. this comes in handy when there are several volunteer names that must be added
        EnterName = input("Enter the name of the new volunteer: ")
        print("The names of the volunteers are: ")
        volunteer_names.append(EnterName)  # "append" adds name to the end of the list
        for name in volunteer_names:
            print(name)
        namesagain = input("Enter Y/y to input a new name. Enter any other key to exit selection: ")


# below is a function to distribute shifts

def namesandshift():
    print("___________________________________________________________")
    Choosing = input("To see all volunteers and their shifts, press Q to continue\nTo see a particular volunteer and their shift, press W to continue\n*(if you wish to exit this selection, press E)*: ")

# choosing Q or W lets the user go on with the selection. Whereas E exits the program with a "thankyou message" and any other character will prompt the user to try again.

    if Choosing == "Q":  # to see all names and shifts
        print("\nNAMES AND SHIFTS\n")
        for name in volunteer_names:
            if name in volunteer_names[0:5]:
                print(name + ":", shifts[0])

            else:
                print(name + ":", shifts[1])

    elif Choosing == "E":  # to exit
        print("Thank you!")




    elif Choosing == "W":  # to see individual names and shifts
        while Choosing == "W":
            Name = input("Input the name whose shift you wish to view: ")
            if Name in volunteer_names[0:5]:

                print("\n", Name, ":", shifts[0], "\n")

                Choosing = input("Enter W to review another name and shift\nor enter any other key to exit this selection: ")

            elif Name not in volunteer_names:

                print("\nInvalid Name")
                Choosing = input("\nEnter W to try again\nor enter any other key to exit this selection: ")




            else:
                print("\n", Name, ":", shifts[1], "\n")
                Choosing = input("Enter W to review another name and shift\nor enter any other key to exit this selection: ")


        else:  # in the case tht any other character is selected
            print("\nInvalid input, try again!\n")
            namesandshift()  # runs the function again



# Payment plan for each shift

def paymentplan():
    # as volunteers are usually paid a certain amount of allowance for food, this function allows you to input the total amount of budget for the same and distribute it among the volunteers.
    # example: total budget is 300 dollars and there are 5 volunteers. each volunteer receives 60 dollars.
    print("------------------------------------------------------------")
    # Utilizing the try and except function, in the case of errors. Try will take in and process all the valid inputs. Whereas, in this program, in the case of a value error in the initial input, it will send in another prompt instead of running into an error
    try:  # for all valid inputs
        Allowance_in_Dollars = float(input("Enter total allowance/payment budget for all the volunteers in dollars: "))

        allowancepervolunteer = (Allowance_in_Dollars)/len(volunteer_names)  # distribution
        print("There are", len(volunteer_names), "volunteers and a total budget of", str(Allowance_in_Dollars), " dollars. Each volunteer will receive", allowancepervolunteer, "dollars as allowance for their work during their shift.")
    except ValueError:   # ValueError is utilized in the case that the initial input cannot be converted to a float value
        totryagain = input("Invalid input. To try again, press W, or to exit, press any other key: ")
        if totryagain == "W":
            paymentplan()
        else:
            print("\nThank you!")


# Choosing a random volunteer for an extra shift

def randomvolunteer():
    import random

    volunteerindex = random.randrange(len(volunteer_names))  # specifying the range to choose the volunteer from

    randomvolunteer = volunteer_names[volunteerindex]  # finalizing the  random volunteer

    print("\n-------------\n" + randomvolunteer + " will be working an extra hour and will be paid overtime.")



# below is a function to remove names from the volunteer list

def removevolunteer():
    print("\n---------\nREMOVE NAMES\n---------")
    leavenames = "Y"
    while leavenames == "Y" or leavenames == "y":  # specifying condition for displaying the input again with a while loop. this comes in handy when there are several volunteer names that must be removed
        Name = input("Enter the name of the volunteer you wish to remove: ")
        if Name in volunteer_names:
            volunteer_names.remove(Name)  # "remove" removes volunteer names
            print("\nUpdated list:\n ")
            for person in volunteer_names:
                print(person)

            leavenames = input("To remove another name, choose Y/y: ")

        else:
            leavenames = input("Name is not on list. choose Y/y to try again: ")  # in the case the name is not in the list due to a spelling error or anything of sort

# main function that gives the user a range of options to choose from throughout the program. shows up after each selection until the user decides to exit.
main()


