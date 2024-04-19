import re

# Dictionary of replacements
replacements = {
    r"\bu\b": "you",
    r"\bur\b": "your",
    r"\bwe've\b": "we have",
    r"\b2\b": "to",
    r"\b4\b": "for",
    r"\bc\b": "see",
    r"\bplz\b": "please",
    r"\bthx\b": "thanks",
    r"\bmsg\b": "message",
    r"\bgr8\b": "great",
    r"\bpls\b": "please",
    r"\btho\b": "though",
    r"\bu'll\b": "you will",
    r"\bim\b": "I'm",
    r"\bnt\b": "not",
    r"\bda\b": "the",
    r"\b2day\b": "today",
    r"\b2moro\b": "tomorrow",
    r"\bdnt\b": "don't",
    r"\bgonna\b": "going to",
    r"\br\b":"are"
    # Add more replacements as needed
}

def replace_shortcuts(sentence):
    for pattern, replacement in replacements.items():
        sentence = re.sub(pattern, replacement, sentence, flags=re.IGNORECASE)
    return sentence


# sentence = "ur gonna do what?"
# updated_sentence = replace_shortcuts(sentence)
# print("Original sentence:", sentence)
# print("Updated sentence:", updated_sentence)
