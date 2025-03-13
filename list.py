ls = ["python", "javascript", "ruby", "c++", "rust", "perl"]

def printls():
    for i in range(0, len(ls)):
        print(f"{i}: {ls[i]}")


printls()
removeItemIndex = -1
while removeItemIndex > 5 or removeItemIndex < 0:
    try:
        removeItemIndex = int(input("Enter the index of the item to remove: "))
        notInt = False
    except ValueError:
        print("Please enter a number")
        notInt = True
    if (removeItemIndex > 5 or removeItemIndex < 0) and not notInt:
        print("Invalid index. Please enter a number between 0 and 5 (inclusive)")
ls.pop(removeItemIndex)
newItem = input("Enter an item to add: ")
ls.append(newItem)
printls()