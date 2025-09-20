# Utilize while loops and nested for loops to draw a simple text-based pattern 

def main(): # Prompt user for the size of the pattern
    size = int(input("Enter the size of the pattern: "))

    row = 0

    while row < size:
        for col in range(size): # Print asterisk without moving to a new line
            print("*", end="")
        print()
        
        # Increment row counter
        row += 1

if __name__ == "__main__":
    main()
