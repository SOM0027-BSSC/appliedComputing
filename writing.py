try:
    with open("myfile.txt", "w") as f:
        f.write("Five")
        f.write("\nSix")
except FileNotFoundError as e:
    print("Please make a 'myfile.txt' file and try again.")