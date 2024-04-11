import json
from difflib import get_close_matches

# Load the dictionary data
with open('data.json') as f:
    data = json.load(f)

def get_definition(word):
    # Convert the word to lowercase
    word = word.lower()

    # Check if the word is in the dictionary
    if word in data:
        return data[word]

    # If the word is not in the dictionary, check for close matches
    elif len(get_close_matches(word, data.keys())) > 0:
        # Get the closest match
        closest_match = get_close_matches(word, data.keys())[0]

        # Ask the user if they meant the closest match
        yn = input(f"Did you mean '{closest_match}' instead? Enter Y if yes, or N if no: ")

        # If the user confirms the closest match, return the definition
        if yn.upper() == "Y":
            return data[closest_match]

        # If the user doesn't confirm the closest match, inform them that the word doesn't exist
        elif yn.upper() == "N":
            return "The word doesn't exist. Please double check it."

        # If the user's input is invalid, inform them that the input was not understood
        else:
            return "We didn't understand your entry."

    # If there are no close matches, inform the user that the word doesn't exist
    else:
        return "The word doesn't exist. Please double check it."

# Get the word from the user
word = input("Enter word: ")

# Print the definition or the appropriate message
print(get_definition(word))