###     John Gavigan        CMPSC 101           03/29/2024
measure = 0.0
count = 0
list1 = []
list2 = []
list3 = []
masterList = []
userVal = ""
userVal3 = 0
userInput = "add"

print("This program records ingredients for recipes. You will be prompted to enter different commands including: ")
print("Enter: \"add\" to add an ingredient to the current recipe or to begin a new recipe after saving.")
print("Enter: \"remove\" to remove an ingredient from your current recipe.")
print("Enter \"save\" to save the recipe.")
print("Enter \"stop\" to terminate the program.\n")

while (userInput != "stop"):
    if (userInput == "add"): # ADD INGREDIENT '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        userVal = str(input("Please enter ingredient name: "))
        list1.append(userVal)
        measure = float(input("Please enter ingredient measurement: "))
        list2.append(measure)
        userVal = str(input("Please enter measurement unit: "))
        list3.append(userVal)

        print(list2[count], list3[count], "of", list1[count] +".\nIs this correct (y/n)?") #confirm addition
        userVal = str(input(":"))
        if userVal == "y":
            count += 1
        elif userVal == "n":
            list1.remove(list1[count])
            list2.remove(list2[count])
            list3.remove(list3[count])
        userInput = str(input("Enter: 1. \"add\" 2. \"remove\" 3. \"save\" 4. \"stop\": ")) #receive next direction

    elif (userInput == "remove"): # REMOVE INGREDIENT ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        userVal3 = int(input("Enter number of ingredient to remove.\n(Example: if carrots is the first ingredient in the list, enter 1, second enter 2,...)\n: "))
        userVal3 -= 1
        print(list1[userVal3], "removed.")
        list1.remove(list1[userVal3])
        list2.remove(list2[userVal3])
        list3.remove(list3[userVal3])
        userVal3 = 0
        count -= 1
        print(len(list1), "ingredients remaining.\n")
        userInput = str(input("Enter: 1. \"add\" 2. \"remove\" 3. \"save\" 4. \"stop\": ")) #receive next direction

    elif userInput == "save": # SAVE RECIPE ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        userVal = str(input("Enter recipe name: "))
        userVal = ("-----------------------------------------------------\n" + userVal + "\n-----------------------------------------------------")
        masterList.append(userVal)                          
        for i in range(count):
            print(list2[i], list3[i], "of", list1[i])
            userVal = (str(list2[i]) + " " + list3[i] + " of " + list1[i])
            masterList.append(userVal)
        list1 = []
        list2 = []
        list3 = []
        count = 0
        userInput = str(input("Enter: 1. \"add\" 2. \"stop\": ")) #receive next direction

# Display all recipes --------------------------------------------------------------
for i in range(len(masterList)):
    print(masterList[i], end="\n")
print()
exit1 = input("Enter any key to quit program: ")
