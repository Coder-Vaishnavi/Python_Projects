#Basic Calculator using Function :

# Functions for arithmetic operations
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error! Zero division Error"
    else:
        return x / y

# Main program
calculate = True

# Display Menu
while calculate:
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print(".............................")
    
# Take user choice
    choice = int(input("Enter your choice (1/2/3/4):"))
    
# Inputs from user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(".............................")
    
# Operation based on user choice
    if choice == 1:
        print("Addition is :", add(num1, num2))
    elif choice == 2:
        print("Subtraction is :", sub(num1, num2))
    elif choice == 3:
        print("Multiplication is :", mul(num1, num2))
    elif choice == 4:
        print("Division is :", div(num1, num2))
    else:
        print("Invalid input")
    
# if user want to calculate more
    user_choice = input("Do you want to calculate more? (YES/NO): ").strip().lower()    
    if user_choice != "yes":
        calculate = False
        print("Thank You!")