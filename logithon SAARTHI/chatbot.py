
import enchant
import csv
from shot_cut_remove import replace_shortcuts

def correct_sentence(sentence):
    d = enchant.Dict("en_US")
    corrected_words = []

    for word in sentence.split():
        if not d.check(word):  # Check if the word is misspelled
            suggestions = d.suggest(word)
            if suggestions:
                corrected_word = suggestions[0]  # Choose the first suggestion
            else:
                corrected_word = word  # If no suggestions found, keep the word as it is
        else:
            corrected_word = word  # If the word is spelled correctly, keep it as it is

        corrected_words.append(corrected_word)
        print(' '.join(corrected_words))

    return ' '.join(corrected_words)


def load_responses(file_path):
    responses = {}
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            if len(row) >= 2:  # Check if the row has at least two elements
                responses[row[0].strip()] = row[1].strip()  # Strip whitespace
    return responses

def chatbot(responses,user_input):
    print("Chatbot: Hi there! How can I assist you today?")
    user_input = user_input.strip()  # Remove .lower() method
    user_input = replace_shortcuts(user_input)
    print("replace_shortcuts",user_input)
    user_input = correct_sentence(user_input)
    if user_input == 'exit':
        print("Chatbot: Goodbye!")
    response = responses.get(user_input, "I'm sorry, I don't understand that.")
    return response

if __name__ == "__main__":
    file_path = "my.csv"  
    responses = load_responses(file_path)
    chatbot(responses)
