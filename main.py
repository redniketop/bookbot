def main():
    # Define the path to the file you want to open.
    books = "books/frankenstein.txt"

    try:
        # Attempt to open the file in read mode ('r').
        with open(books, 'r') as f:
            # Read the entire content of the file into the 'content' variable.
            content = f.read()
            # Print the content of the file to the console.
            print(content)
            # Get the number of words in the content.
            num_words = get_num_words(content)
            # Print the number of words found in the document.
            print(f"{num_words} words found in the document")
    except FileNotFoundError:
        # Handle the case where the file is not found.
        print(f"The file {books} does not exist.")
    except Exception as e:
        # Handle any other exceptions that may occur.
        print(f"An error occurred: {e}")
        
def get_num_words(text):
    # Split the text into words and return the number of words.
    words = text.split()
    return len(words)

# If this script is run directly, call the main function.
if __name__ == "__main__":
    main()
