print("Finding factorial of a Number :\n") 
num=int(input("Enter the number: "))
fact = 1
if (num<0) :
    print ("Not defined ")
else:
    while (num>0):
        fact=fact*num
        num = num - 1
print(fact)

print("Finding the number of digits in a given number :")
print("One way :\n")
n= input("Enter the number: ")
print(len(n)) 
print("The other way :\n")
num=abs(int(input("Enter the number :")))
digits = 1
while (num > 9) :
    num = num // 10
    digits = digits + 1
print(digits) 
print("Writing reverse of digits :\n")
n=int(input("Enter the number:"))
absn = abs(n)
rev = absn % 10
absn = absn // 10 
while (absn >0):
    r = absn % 10
    absn = absn // 10
    rev = rev *10 +r 
if (n>=0):
    print (rev)
else:
    print(rev -2*rev) 