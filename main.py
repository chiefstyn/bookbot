def main():
    file_path = "books/frankenstein.txt"

    with open(file_path) as f:
        file_contents = f.read()      ## up to this line reads the file and stores it in file_contents
        characters = count_characters(file_contents) ##How to call on the count characters function we created 
        word_count = count_words(file_contents) ## call on the count words function
        

    char_list = create_char_list(characters) ## call on the create cahracter list function
    char_list.sort(reverse=True, key=sort_on)


    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words in document")
    for char_dict in char_list:      ##need to loop through the character list, to find each of the character dictionaries made
        char = char_dict["char"] 
        num = char_dict["num"]
        if  char.isalpha(): ##makes it so only alphabetical characters are displayed
            print(f"The {char} character was found {num} times")
    print(f"--- End report ---")


def count_words(file_contents): ## function made to count the number of words in the book
    word_count = file_contents.split() ## .split breaks up string into single pieces
    return len(word_count) ## len will tell us the length of the split pieces

def count_characters(file_contents):
    characters = {}  ## createss characters dictionary
    
    for char in file_contents: ## looks through each character in the file contents
        char = char.lower() ## counts all uppercase letters as lower case
        if char in characters: ##checks if we've seen the character before
            characters[char] += 1 ## if a char exists in the dictionary we add a count to it // dictionary[key]
        else: 
            characters[char] = 1 ## if the char does not exist we add it to the dictionary
    return(characters)


            
def sort_on(characters):       ## sort is a key function that tells python to compare the characters dictionaries to their num value
    return characters["num"]

def create_char_list(characters):
    char_list = [] ## creates an empty list to store the new dictionaries
    for char, count in characters.items(): ## .items is a method used to get keys and values from a dictionary at the same time
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)
    return char_list

    


    


main()
