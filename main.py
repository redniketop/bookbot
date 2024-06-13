def main():
    # Define the path to the file you want to open.
    # Make sure the path is correct relative to where your script is located.
    books = "books/frankenstein.txt"

    try:
        # Attempt to open the file in read mode ('r').
        # The 'with' statement ensures the file is properly closed after the block of code executes.
        with open(books, 'r') as f:
            # Read the entire content of the file into the 'content' variable.
            content = f.read()
            # Print the content of the file to the console.
            print(content)
    except FileNotFoundError:
        # This block executes if the file specified in 'books' is not found.
        print(f"The file {books} does not exist.")
    except Exception as e:
        # This block executes if any other exception occurs during the file operations.
        print(f"An error occurred: {e}")

# This line checks if the script is being run directly (not imported as a module).
# If true, it calls the main() function to execute the code.
if __name__ == "__main__":
    main()
