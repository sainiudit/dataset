import re

def extract_phrases_in_quotes(input_sentence):
    # Define a regular expression pattern to match phrases within double quotes
    pattern = r'"(.*?)"'
    
    # Use re.findall to find all matching phrases in the input sentence
    matches = re.findall(pattern, input_sentence)
    
    return matches

# Example usage:
input_sentence = 'This is a "sample sentence" with "multiple phrases" in quotes.'
phrases_in_quotes = extract_phrases_in_quotes(input_sentence)
print(phrases_in_quotes)
