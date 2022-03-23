#step 1 :- create an empty list named beatles;
beatles=[]
print("Step 1:", beatles)

# step 2 :-use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
beatles.append("john lennon")
beatles.append("paul mccartney")
beatles.append("george")
beatles.append("pete")
print("Step 2:", beatles)

# step 3:-use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best; 
for i in range(2):
    add=input("Enter the name to add in list :")
    beatles.append(add)
print("Step 3:", beatles)

# step 4 :- use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
del beatles[5]
del beatles[4]
print("Step 4:", beatles)

# step 5 :- use the insert() method to add Ringo Starr to the beginning of the list.
beatles.insert(0, "starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))