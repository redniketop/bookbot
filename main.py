def main():
    books = "books/frankenstein.txt"  # Adjust the path as needed

    try:
        with open(books, 'r') as f:
            content = f.read()
            print(content)  # This will print the content of the file
    except FileNotFoundError:
        print(f"The file {books} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
