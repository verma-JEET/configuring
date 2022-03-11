length = int(input("Enter the length of the Password : "))
import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbol = "!@#$%^&*()_+-=[]{}/\<>;:,.|"
all = lower + upper + number + symbol
password = "".join(random.sample(all,length))
print("Your Generated PAssword is : ",password)