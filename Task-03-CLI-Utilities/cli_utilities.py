from pathlib import Path


def word_count(file_path):
    text = Path(file_path).read_text(encoding="utf-8")
    return len(text.split())


def file_size(file_path):
    path = Path(file_path)
    return path.stat().st_size


def show_help():
    print("\nCLI Utilities")
    print("1. Count words in a file")
    print("2. Check file size")
    print("3. Exit")


def main():
    while True:
        show_help()
        choice = input("Choose an option: ")

        if choice == "1":
            file_name = input("Enter file path: ")
            try:
                count = word_count(file_name)
                print(f"Word count: {count}")
            except FileNotFoundError:
                print("File not found. Please check the path.")

        elif choice == "2":
            file_name = input("Enter file path: ")
            try:
                size = file_size(file_name)
                print(f"File size: {size} bytes")
            except FileNotFoundError:
                print("File not found. Please check the path.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
