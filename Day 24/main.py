#TODOs:
# Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        print(new_letter)

        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)