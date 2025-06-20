# Q2.py

def read_lines(filename: str) -> list[str]:
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

def main():
    filename = input("Enter the file name: ")
    lines = read_lines(filename)
    print(f"Number of lines: {len(lines)}")

if __name__ == "__main__":
    main()
