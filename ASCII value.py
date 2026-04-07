ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter only one character.")
else:
    print("ASCII value:", {ord(ch)})

    if ch.isalpha():
        print("It is an alphabet.")
    elif ch.isdigit():
        print("It is a digit.")
    else:
        print("It is a special character.")