#Names

studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]

#Oringin
print("Original student names with last name Evans:")
for name in studentNames:
    full_name = name + " Evans"
    print(full_name)

#Add
new_name = input("\nPlease enter a new name to add to the list: ")
studentNames.append(new_name)


print("\nUpdated student names with last name Evans:")
for name in studentNames:
    full_name = name + " Evans"
    print(full_name)
