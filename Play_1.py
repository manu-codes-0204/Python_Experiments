r=int(input("Enter the radius :"))
area=3.14*r*r 

print("For a circle :\nThe area  is",area)

l=int(input("Enter the length:"))
b=int(input("Enter the breadth :"))
if l!=b :
    print("RECTANGLE")
if l==b:
    print("SQUARE") 

Rectangle={
        "area": l*b,
        "perimeter":2*(l+b)
}
Square={
    "area":l*l ,
    "perimeter":4*l
}
if l!=b:
    print("For a rectangle :\narea=",Rectangle["area"],"\nperimeter=",Rectangle["perimeter"] )
if l==b:
    print("for a square :\narea=",Square["area"],"\nperimeter=",Square["perimeter"]) 