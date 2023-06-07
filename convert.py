import re

def convert_text_to_list(title, content):
    lines = []
    lines.append(title)

    current_line = ''
    previous_char = ''
    word_count = 0
    for char in content:
        current_line += char
        if char == '\n':
            lines.append(current_line.strip())
            current_line = ''
            word_count = 0
        elif char in ('.', ',', '?', '!', ';', ':') and previous_char not in ('.', '!', '?', ':') and not char.isspace():
            lines.append(current_line.strip())
            current_line = ''
            word_count = 0
        elif char.isspace():
            word_count += 1
            if word_count >= 25:
                lines.append(current_line.strip())
                current_line = ''
                word_count = 0
        previous_char = char
    if current_line.strip():
        lines.append(current_line.strip())
    lines.append("What do you think?")
    lines.append("Write your opinion in the comments!")
    return lines


def split_strings(string_list):
    split_list = []
    for string in string_list:
        words = string.split()
        current_string = ''
        while words:
            current_string += ' ' + words.pop(0)
            if len(current_string.split()) == 16 or not words:
                split_list.append(current_string.strip())
                current_string = ''
    return split_list

def process_text_file(file_path):
    word_list = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespaces
            if line == '':
                word_list.append('')  # Append an empty string for new lines
            else:
                words = line.split()  # Split the line into words
                word_list.extend(words)  # Append the words to the list
    return word_list

def filter_bad_words(text):
    bad_words = ["fuck", "shit", "damn", "ass", "bitch", "bastard", "cunt", "dickhead"]
    filtered_text = text

    for word in bad_words:
        pattern = r"\b" + re.escape(word) + r"(?=\b|[\W_])"
        filtered_text = re.sub(pattern, word[0] + (len(word) - 1) * "*", filtered_text, flags=re.IGNORECASE)

    return filtered_text

'''# Example usage
filename = 'a.txt'  # Replace with the path to your text file
result = convert_text_to_list(filename)
splitResult = split_strings(result)
for line in splitResult:
    print(line)'''