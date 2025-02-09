import os

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]


# [{'name': 'plane', 'num': 10}, {'name': 'car', 'num': 7}, {'name': 'boat', 'num': 2}]

def count_characters(text):
    # First count the characters into a dictionary
    char_count = {}
    lower_text = text.lower()
    for char in lower_text:
        if char.isalpha():  # Only count letters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    # Then convert to list of dictionaries
    char_list = []
    for char, num in char_count.items():
        char_list.append({"char": char, "num": num})
    
    return char_list


def main():
    # Dynamically determine the absolute path
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "books", "frankenstein.txt")

    with open(file_path) as f:
        file_contents = f.read()
        
        # Print report header
        print("--- Begin report of books/frankenstein.txt ---")
        
        # Count and print words
        words = file_contents.split()
        print(f"{len(words)} words found in the document\n")
        
        # Get and sort character counts
        characters = count_characters(file_contents)
        characters.sort(reverse=True, key=sort_on)  # Sort in descending order
        
        # Print character counts
        for char in characters:
            print(f"The '{char['char']}' character was found {char['num']} times")

main()