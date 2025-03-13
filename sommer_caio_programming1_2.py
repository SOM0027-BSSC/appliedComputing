dictionary = {
    "Brand": "Asus",
    "GPU": "Intel 1650",
    "CPU": "Intel Gen 11 i5",
    "RAM": "16Gb DDR4"
}

print("Computer properties:")
for i in dictionary:
    print(f"\t{i}: {dictionary[i]}")

while True:
    delete = input("Enter the property you want to remove: ")
    try:
        dictionary.pop(delete)
        break
    except Exception as e:
        print("Invalid input.")

newProperty = input("Enter the property you would like to add: ")
newValue = input("Enter the value you would like to add: ")

dictionary[newProperty] = newValue

print("Computer properties:")
for i in dictionary:
    print(f"\t{i}: {dictionary[i]}")