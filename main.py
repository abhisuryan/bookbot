
def count_chars(content):
    char_count = {}
    line = [x.split(" ") for x in content.split("\n")]
    for i in line:
        for j in i:
            if j != '':
                for k in j:
                    l = k.lower()
                    if l in char_count.keys():
                        char_count[l] += 1
                    else:
                        char_count[l] = 1
    return char_count


def count_words(content):
    lines = [x.split(" ") for x in content.split("\n")]
    count = 0
    for i in lines:
        for j in i:
            if j!='':
                count+=1
    return count


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    print("\n")
    char_count = count_chars(file_contents)
    for key in char_count:
        print(f"The {key} character was found {char_count[key]} times")
    print("--- End report ---")

main()