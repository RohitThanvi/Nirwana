def load_scores(filename):
    scores = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    name = parts[0]
                    try:
                        score = int(parts[1])
                        scores.append((name, score))
                    except ValueError:
                        pass
    except FileNotFoundError:
        print("No scores file found. Starting fresh.")
    return scores

def save_scores(filename, scores):
    with open(filename, 'w') as file:
        for name, score in scores:
            file.write(f"{name},{score}\n")

def add_score(scores):
    name = input("Enter name: ")
    try:
        score = int(input("Enter score: "))
        scores.append((name, score))
        print("Score added!")
    except ValueError:
        print("Invalid score. Must be a number.")

def show_top_n(scores):
    try:
        n = int(input("Enter how many top scores to show: "))
        sorted_scores = sort_scores(scores)
        print("\nTop Scores:")
        for i in range(min(n, len(sorted_scores))):
            print(f"{sorted_scores[i][0]} - {sorted_scores[i][1]}")
    except ValueError:
        print("Please enter a valid number.")

def sort_scores(scores):

    sorted_scores = scores[:]
    for i in range(len(sorted_scores)):
        for j in range(i+1, len(sorted_scores)):
            if sorted_scores[j][1] > sorted_scores[i][1]:
                sorted_scores[i], sorted_scores[j] = sorted_scores[j], sorted_scores[i]
    return sorted_scores

def main():
    filename = "scores.txt"
    scores = load_scores(filename)

    while True:
        print("\nMenu:")
        print("1. Show Top N Scores")
        print("2. Add New Score")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_top_n(scores)
        elif choice == '2':
            add_score(scores)
            save_scores(filename, scores)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
