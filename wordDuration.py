from convert import convert_text_to_list, split_strings
def calculate_word_durations(text, speaking_rate):
    # Calculate the duration of each word based on the speaking rate
    word_durations = []
    for word in text:
        # Calculate the duration of the word
        duration = (len(word) / (19.575))
        word_durations.append(duration)

    return word_durations
