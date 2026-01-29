import art

print(art.logo)

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


calculator={'+':add, '-':subtract, '*':multiply, '/':divide}


first=float(input("Enter your first number: "))
operator=input("Enter your operator (+,-,*,/): ")
second=float(input("Enter your second number: "))

next="yes"
while next=="yes":
    ans=calculator[operator](first,second)
    print(f"{first}{operator}{second} = {ans}")
    first=ans
    next=input("do you want to continue (yes/no) to operate on the result: ")
    if next=="no":
        break
    second=float(input("Enter your second number: "))
    operator = input("Enter your operator (+,-,*,/): ")