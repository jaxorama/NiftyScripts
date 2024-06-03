import string

def load_word_list(file_path):
    with open(file_path, 'r') as file:
        words = [line.strip().lower() for line in file if len(line.strip()) == 5]
    return words

def get_feedback(guess, solution):
    feedback = [''] * 5
    solution_chars = list(solution)
    # First pass: Check for correct positions
    for i in range(5):
        if guess[i] == solution[i]:
            feedback[i] = 'G'  # Green for correct position
            solution_chars[i] = None
    # Second pass: Check for correct characters in wrong positions
    for i in range(5):
        if feedback[i] != 'G':
            if guess[i] in solution_chars:
                feedback[i] = 'Y'  # Yellow for correct character in wrong position
                solution_chars[solution_chars.index(guess[i])] = None
            else:
                feedback[i] = 'B'  # Black for incorrect character
    return ''.join(feedback)

def filter_words(words, guess, feedback):
    filtered_words = []
    for word in words:
        if get_feedback(guess, word) == feedback:
            filtered_words.append(word)
    return filtered_words

def suggest_words(words):
    # Suggest words with diverse characters
    char_frequency = {char: 0 for char in string.ascii_lowercase}
    for word in words:
        for char in set(word):
            char_frequency[char] += 1

    # Rank words by frequency of unique characters
    ranked_words = sorted(words, key=lambda word: sum(char_frequency[char] for char in set(word)), reverse=True)
    return ranked_words[:10]

def main():
    word_list_file = 'word_list.txt'
    words = load_word_list(word_list_file)
    print(f"Loaded {len(words)} words.")

    while True:
        guess = input("Enter your guess (5 letters): ").strip().lower()
        if len(guess) != 5 or not guess.isalpha():
            print("Invalid guess. Please enter a 5-letter word.")
            continue
        
        feedback = input("Enter feedback (G for green, Y for yellow, B for black): ").strip().upper()
        if len(feedback) != 5 or any(c not in 'GYB' for c in feedback):
            print("Invalid feedback. Please enter feedback using G, Y, B.")
            continue

        if feedback == "GGGGG":
            print("Congratulations! You've solved the Wordle!")
            break

        words = filter_words(words, guess, feedback)
        suggestions = suggest_words(words)
        
        if not suggestions:
            print("No more possible words found. Check your inputs.")
            break

        print(f"Suggestions ({len(suggestions)} possible words): {', '.join(suggestions)}")

if __name__ == "__main__":
    main()
