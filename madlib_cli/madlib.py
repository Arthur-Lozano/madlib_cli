import re

# Print a welcome message to the user, explaining the Madlib process and command line interactions
print(
    "Hello, and welcome to my madlib game.  You will be prompted to put in some words and when finished will receive a generated message"
)


adjective_1 = input("Enter an adjective: ")
adjective_2 = input("Enter an adjective: ")
first_name_1 = input("Enter an adjective: ")
past_tense = input("Enter a past tense verb: ")
first_name_2 = input("Please enter a first name: ")
adjective_3 = input("Please enter an adjective: ")
adjective_4 = input("Please enter an adjective: ")
plural_noun_1 = input("Please enter a noun: ")

large_animal_1 = input("Please enter a large animal: ")
small_animal_1 = input("Please enter a small animal: ")
girls_name_1 = input("Please enter a girls name: ")
adjective_5 = input("Please enter an adjective: ")
plural_noun_2 = input("Please enter a plural noun: ")
adjective_6 = input("Please enter an adjective: ")
plural_noun_3 = input("Please enter a plural noun: ")
num_50 = input("Please enter a number between 1-50: ")
num = input("Please enter a random number: ")
plural_noun_4 = input("Please enter a plural noun: ")
num_2 = input("Please enter a random number: ")
plural_noun_5 = input("Please enter a plural noun: ")


def read_template(n):
    with open(n) as words:
        words_rd = words.read()
        return words_rd


def parse_template(x):
    results = tuple(re.finall(r"\{(A-Za-z0-9`_]+)\}", x))
    user_output = x.replace(results[0], "")
    user_output = user_output.replace(results[2], "")
    return (user_output, results)


def merge(a, b):
    new_line = a.format(b[0], b[1], b[2])
    print(new_line)
    return new_line


with open("mad.txt", "r") as file:
    contents = file.read()

    contents = contents.replace("{Adjective}", adjective_1, 1)
    contents = contents.replace("{Adjective}", adjective_2, 1)
    contents = contents.replace("{A First Name}", first_name_1, 1)
    contents = contents.replace("{Past Tense Verb}", past_tense, 1)
    contents = contents.replace("{A First Name}", first_name_2, 1)
    contents = contents.replace("{Adjective}", adjective_3, 1)
    contents = contents.replace("{Adjective}", adjective_4, 1)
    contents = contents.replace("{Plural Noun}", plural_noun_1, 1)
    contents = contents.replace("{Large Animal}", large_animal_1, 1)
    contents = contents.replace("{Small Animal}", small_animal_1, 1)
    contents = contents.replace("{A Girl's Name}", girls_name_1, 1)
    contents = contents.replace("{Adjective}", adjective_5, 1)
    contents = contents.replace("{Plural Noun}", plural_noun_2, 1)
    contents = contents.replace("{Adjective}", adjective_6, 1)
    contents = contents.replace("{Plural Noun}", plural_noun_3, 1)
    contents = contents.replace("{Number 1-50}", num_50, 1)
    contents = contents.replace("{First Name's}", first_name_2, 1)
    contents = contents.replace("{Number}", num, 1)
    contents = contents.replace("{Plural Noun}", plural_noun_4, 1)
    contents = contents.replace("{Number}", num_2, 1)
    contents = contents.replace("{Plural Noun}", plural_noun_5, 1)


with open("mad.txt_copy.txt", "w") as f:
    f.write(contents)
