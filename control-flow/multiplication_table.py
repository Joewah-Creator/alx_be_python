# Ask the user for a number and print its multiplication table (1 to 10).

def main():
    # Prompt user for input and save in variable 'number'
    number = int(input("Enter a number to see its multiplication table: "))

    # Use a for loop to generate the table from 1 to 10
    for i in range(1, 11):  # range(1, 11) → numbers 1 through 10
        product = number * i
        print(f"{number} * {i} = {product}")

if __name__ == "__main__":
    main()
