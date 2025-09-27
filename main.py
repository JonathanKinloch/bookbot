from stats import character_count
from stats import word_count
import sys 

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1]

def main():
    book_text = get_book_text(path)
    char_counts = character_count(book_text)

    stats = []
    for ch, num in char_counts.items():
        stats.append({"character": ch, "character_count": num})
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words.")
    print("----------- Character Count ----------")
    sorted_stats = sorted(stats, key=sort_on, reverse=True)
    for item in sorted_stats:
        if item["character"].isalpha():
            print(f'{item["character"]}: {item["character_count"]}')

    

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def sort_on(item):
    return item["character_count"]

    

main()





