def get_word_count(texts):
    to_count = texts.split()
    word_count = 0
    for text in to_count:
        word_count += 1
    return word_count