def get_book_text(url):
    text = open(url, 'r', encoding='utf-8').read()
    return text

def get_word_count(url):
    text = get_book_text(url)
    words = text.split()
    return len(words)

def character_count(url):
    data = {}
    text = get_book_text(url)
    words = text.lower()
    for char in words:
        if char.isascii():
            if char in data:
                data[char] += 1
            else:
                data[char] = 1

    return data

def print_report(url):
    count = character_count(url)
    words = get_word_count(url)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("------------ Word Count ------------")
    print(f"Found {words} total words")
    print("------------ Character Count ------------")
    for char, count in count.items():
        print(f"{char}: {count}")
    print("============ END ============")


  