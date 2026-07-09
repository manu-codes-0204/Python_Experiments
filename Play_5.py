print("Problems using for loop : ")
print("\n 1.Finding the factorial of a number : ")
n=int(input('Enter a number : '))
fact=1
if (n<0):
    print('NOT DEFINED ')
else:
    for i in range (n,1,-1) : 
        fact = fact * i 
    print(fact)
print ("\n 2.Finding the number of digits in a number:")
n=int(input("Enter the number :"))
N=str(n)
digits = 0
for c in N :
    digits = digits + 1
print(digits)
print("\n 3.Reversing the digits in a given number : ")
n= int(input("Enter the number :"))
N=str(abs(n))
rev=''
for c in N :
    rev = c + rev 
if (n>=0):
    print (rev)
else:
    print("-"+rev)
print("\n 4.Finding wether the given number is a palindrome or not :")
n=int(input("Enter the number :"))
N=str(abs(n))
rev=''
for c in N :
    rev = c + rev 
if (n>=0):
    print(rev)
else:
    print("-"+ rev )
if (n == int(rev)):
    print("It is a palindrome ")
else: 
    print("It is not a palindrome ")
