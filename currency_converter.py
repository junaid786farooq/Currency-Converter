print("Welcome to the currency converter that converts rupees to US dollars.")

# Function to convert rupees to dollars
def convert_rupees_to_dollars(rupees):
    return rupees * 0.0036

# Main function to handle user interaction
def main():
    while True:

        try:
            # Prompt user to enter an amount in rupees and covert it to dollars
            rupees = float(input("Enter the amount in rupees RS: "))
            dollars = convert_rupees_to_dollars(rupees)
            print(f"RS {rupees} is ${dollars:.2f} dollars.")

            # Nested while loop
            while True:
                # Ask the user if they want to perform another conversion
                another_conversion =  input("Do you want to convert another amount (yes/no): ").strip().lower()
                if another_conversion == "yes":
                    break
                elif another_conversion == "no":
                    print("Thank you for using the currency converter.")
                    return
                else:
                    print(f"Invalid option: '{another_conversion}'. Please enter 'yes' or 'no' only.")
            
        except ValueError:
            print("Error: Please enter a numeric value!")

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()
