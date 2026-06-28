n=int(input("Enter the  number:")) 
if (n % 2 == 0):
    print("Even")
else:
    print("Odd") 

m=int(input("\nEnter the number :"))
if (m % 5 == 0 ):
    if (m % 10 == 0):
        print("ENDS WITH ZERO")
if (m % 5 == 0):
    if (m % 10 != 0):
        print("ENDS WITH FIVE")
else:
    print("Other")

l=int(input("\nEnter the marks :"))
if l>=90 :
    print("Grade A")
elif l>=80 and l<90:
    print("Grade B")
elif l>=70 and l<80 :
    print("Grade C")
elif l >=60 and l<70 :
    print("Grade D") 
elif l>=0 and l<60 :
    print("Grade E")
else:
    print("Invalid input")


