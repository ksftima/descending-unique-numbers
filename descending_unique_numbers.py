def get_unique_numbers():
    """
    Prompts the user for a list of numbers, then outputs unique numbers
    in descending order.
    """
    try:
        # Prompt and convert input to integers
        numbers = list(map(int, input('Enter a list of numbers separated by spaces: ').split()))
        
        # Get the unique numbers and sort them in descending order
        unique_numbers = sorted(set(numbers), reverse=True)
        
        print("Unique numbers in descending order:", unique_numbers)

    except ValueError:
        print("Incorrect input. Please enter only numbers separated by spaces.")

# Call the function
get_unique_numbers()