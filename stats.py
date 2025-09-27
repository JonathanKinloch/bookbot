def character_count(book_text):
    count = {}
    for characters in book_text:
        char = characters.lower()
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def word_count(book_text): 
    num_words = len(book_text.split())  
    return num_words