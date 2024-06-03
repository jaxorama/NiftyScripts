import sys

def load_word_list(file_path):
    with open(file_path, 'r') as file:
        words = [line.strip().lower() for line in file if len(line.strip()) >= 4]
    return words

def is_valid_word(word, letters, center_letter):
    return center_letter in word and all(char in letters for char in word)

def is_pangram(word, letters):
    return all(char in word for char in letters)

def find_spelling_bee_words(words, letters, center_letter):
    valid_words = []
    pangrams = []
    
    for word in words:
        if is_valid_word(word, letters, center_letter):
            valid_words.append(word)
            if is_pangram(word, letters):
                pangrams.append(word)
    
    return valid_words, pangrams

def main():
    if len(sys.argv) != 4:
        print("Usage: python spelling_bee_solver.py <path_to_word_list> <letters> <center_letter>")
        print("Example: python spelling_bee_solver.py word_list.txt abcdefg a")
        return
    
    word_list_file = sys.argv[1]
    letters = sys.argv[2].lower()
    center_letter = sys.argv[3].lower()
    
    if len(center_letter) != 1 or center_letter not in letters:
        print("The center letter must be one of the letters provided.")
        return
    
    words = load_word_list(word_list_file)
    valid_words, pangrams = find_spelling_bee_words(words, letters, center_letter)
    
    if valid_words:
        print(f"Found {len(valid_words)} valid words:")
        for word in sorted(valid_words, key=len, reverse=True):
            print(word)
    else:
        print("No valid words found.")
    
    if pangrams:
        print("\nPangrams:")
        for word in sorted(pangrams, key=len, reverse=True):
            print(word)
    else:
        print("\nNo pangrams found.")

if __name__ == "__main__":
    main()
