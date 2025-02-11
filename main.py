def main() :
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count(file_contents)} words found in the document\n")
        count = count_characters(file_contents)
        for key in count:
            if key.isalpha() == True :
                print(f"The '{key}' character was found {count[key]} times")
        print("--- End Report ---")

def word_count(string) :
    words = string.split()
#    print(len(words))
    return len(words)

def count_characters(string) :
    lower_string = string.lower()
    count = {}
    for j in lower_string:
        if (j in count)==True :
            count[j] += 1
        else :
            count[j] = 1
#    print(count)
    return count

main()

