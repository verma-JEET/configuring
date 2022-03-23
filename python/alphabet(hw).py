ch= input("Enter any character: ")
if ch.isnumeric():
    print("Entered character is a number")
    if int(ch)==0:
        print("\n"+ch,"Is ZERO")
    elif int(ch)>0:
        print("\n"+ch,"Is a positive number")
    else:
        print("\n"+ch,"Is a negative number")
elif ch.isalpha():
    print("Entered character is Alphabet")
    if ch.isupper():
        print("\n"+ch,"Is a UPPERCASE ALPHABET")
    else:
        print("\n"+ch,"IS a LOWERCASE ALPHABET") 
else:
    print("\n"+ch,"Is a special character")
