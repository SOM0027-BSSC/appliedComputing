try:
    with open("myfile.txt", "r") as f:
        f = f.readlines()
        for i in f:
            print(i, end="")
except FileNotFoundError as e:
    print("Please make a 'myfile.txt' file and try again.")