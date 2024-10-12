import re

# Define the regex pattern
pattern = r'[“"“](.*?)[”"”].*$'

# Read from the input file
with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.readlines()

# Process each line and apply the regex substitution
with open('output.txt', 'w', encoding='utf-8') as file:
    for line in text:
        modified_line = re.sub(pattern, r'\1', line)
        file.write(modified_line)