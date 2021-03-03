# --------------Problem 1--------------
# you can write a string as input (lines 4 & 5) or write that In the code (line 6)
with open("file.txt", "w+") as new_file:
    # text_input = input("Enter your text: ")
    # new_file.write(text_input)
    new_file.write("The quick\n brown fox\n jumps over\n the lazy\n dog")
    new_file.seek(0)
    text = new_file.read().split()
    count_character = len(" ".join(text))
    count_words = len(text)
    new_file.seek(0)
    print("Number of lines: ", len(new_file.readlines()), "\nNumber of words: ", count_words,
          "\nNumber of characters: ",
          count_character)
    new_file.close()
# --------------Problem 2--------------
import shutil

source = input("pleas enter the path of your file that you want to copy: ")
detination = input("pleas enter the path of file as detination: ")
operation = shutil.copy(source, detination)
