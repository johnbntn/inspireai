import re

def remove_credit(text):
    # This pattern matches a quote (anything in quotation marks)
    # followed by a dash or em-dash and then any text until the end of the line
    pattern = r'(".*?").*$'
    return re.sub(pattern, r'\1', text, flags=re.MULTILINE)

# Read the input file
with open('input.txt', 'r') as file:
    content = file.read()

# Remove credits
cleaned_content = remove_credit(content)

# Write the result to a new file
with open('output.txt', 'w') as file:
    file.write(cleaned_content)

print("Credits removed successfully. Check 'output.txt' for the result.")