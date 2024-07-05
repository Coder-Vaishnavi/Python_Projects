# Temperature Converter using Python :

# Function definitions
def fahrenheit(c):
    return (c * 9 / 5) + 32

def celsius(f):
    return (f - 32) * 5 / 9

# Main Program
while True:
    # Menu
    print("\n===== Temperature Converter =====")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("0. To Exit")
    
    # Choice from user
    choice = input("Enter Your Choice: ")
    
    # Convert from Celsius to Fahrenheit
    if choice == "1":
        c = float(input("Enter Celsius Temperature: "))
        print("The Fahrenheit temperature is:", fahrenheit(c))
    
    # Convert from Fahrenheit to Celsius
    elif choice == "2":
        f = float(input("Enter Fahrenheit Temperature: "))
        print("The Celsius temperature is:", celsius(f))
        
    # To Exit the Program 
    elif choice == "0":
        print("Exited the program.")
        break
    
    # For Invalid choice
    else:
        print("Invalid choice. Please enter 1, 2, or 0 to exit.")
