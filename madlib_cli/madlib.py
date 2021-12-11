# Print a welcome message to the user, explaining the Madlib process and command line interactions
print(
    "Hello, and welcome to my madlib game.  You will be prompted to put in some words and when finished will receive a generated message"
)


adjective_1 = input("Enter an adjective: ")
adjective_2 = input("Enter an adjective: ")
# first_name_1 = input("Enter an adjective: ")
# past_tense = input("Enter a past tense verb: ")
# first_name_2 = input("Please enter a first name: ")
# adjective_3 = input("Please enter an adjective: ")
# adjective_4 = input("Please enter an adjective: ")
# plural_noun_1 = input("Please enter a noun: ")

# large_animal_1 = input("Please enter a large animal: ")
# small_animal_1 = input("Please enter a small animal: ")
# girls_name_1 = input("Please enter a girls name: ")
# adjective_5 = input("Please enter an adjective: ")
# plural_noun_2 = input("Please enter a plural noun: ")
# adjective_6 = input("Please enter an adjective: ")
# plural_noun_3 = input("Please enter a plural noun: ")
# num_50 = input("Please enter a number between 1-50: ")
# num = input("Please enter a random number: ")
# plural_noun_4 = input("Please enter a plural noun: ")
# num_2 = input("Please enter a random number: ")
# plural_noun_5 = input("Please enter a plural noun: ")


with open("mad.txt") as file:
    print(file.read())
