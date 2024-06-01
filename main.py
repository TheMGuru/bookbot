def main():
    path_to_book = "books/frankenstein.txt"
    text = get_text(path_to_book)
    num_of_words = num_words(text)
    print(f"{num_of_words} words found in text.")
    chars_dict = char_count(text)
    chars_dict_sorted = sorted(filter(lambda item: item[0].isalpha(), chars_dict.items()), reverse=True, key=lambda item: item[1])
    for c, n in chars_dict_sorted:
        print(f"The {c} character was found {n} times")
    print("--- End report ---")


def get_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()

def num_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars  

if __name__ == "__main__":
    main()