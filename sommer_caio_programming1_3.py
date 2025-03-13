ls = ["python", "javascript", "ruby", "c++", "rust", "perl"]

string = "c++"
found = False
for i in ls:
    if i == string:
        found = True
        print(string)
    else:
        print(f"{i} - is not the value we are looking for")

if found:
    print(f"\n{string} found in the list")
else:
    print(f"\n{string} not found in the list")