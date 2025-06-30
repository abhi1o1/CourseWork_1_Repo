import sysclear







def decimal_to_hex(decimal_value):
    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hexadecimal = ""
    num = decimal_value

    print(f"Converting the Decimal Value {num} to Hex...")

    while num != 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16

    print(f"Hexadecimal representation is: {hexadecimal}")
    return hexadecimal  # Return the hexadecimal value for testing

if __name__ == "__main__":
    # Check if an argument is provided
    if len(sys.argv) < 2:
        print("Error: No input argument provided. Please provide a decimal integer.")
        sys.exit(1)  # Exit with error status

    # Try to convert the input to integer and handle non-integer inputs
    try:
        decimal_value = int(sys.argv[1])
        if decimal_value < 0:
            print("Error: Please provide a non-negative integer.")
            sys.exit(1)
        decimal_to_hex(decimal_value)
    except ValueError:
        print("Error: Invalid input. Please provide a valid integer.")
        sys.exit
