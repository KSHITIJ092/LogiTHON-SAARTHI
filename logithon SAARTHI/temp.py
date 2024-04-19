import csv
from difflib import SequenceMatcher

# Function to calculate similarity between two strings
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Function to find the most matching question and its response
def find_matching_response(user_input, questions_file):
    max_similarity = 0
    matching_question = None
    matching_response = None

    with open(questions_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            question = row[0]
            response = row[1]
            sim = similarity(user_input.lower(), question.lower())
            if sim > max_similarity:
                max_similarity = sim
                matching_question = question
                matching_response = response

    return matching_question, matching_response

# Example usage
user_input = input("what doing")
questions_file = "my.csv"
matching_question, matching_response = find_matching_response(user_input, questions_file)
print("Matching question:", matching_question)
print("Response:", matching_response)
