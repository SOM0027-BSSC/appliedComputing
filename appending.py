try:
    with open("myfile.txt", "a") as f:
        f.write("\nThree")
        f.write("\nFour")
except FileNotFoundError as e:
    print("Please make a 'myfile.txt' file and try again.")