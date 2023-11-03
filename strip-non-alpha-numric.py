import re

def strip_non_alphanumeric_from_ends(input_string):
    # Use a regular expression to remove non-alphanumeric characters from the beginning and end of the string
    stripped_string = re.sub(r'^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$', '', input_string)
    return stripped_string
