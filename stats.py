def get_word_count(texts):
    to_count = texts.split()
    word_count = 0
    for text in to_count:
        word_count += 1
    return word_count

def get_letter_count(texts):
    to_count = texts.split()
    letters = {}
    for text in to_count:
        text = text.lower()
        for letter in text:
            if letter in letters:
                letters[letter] += 1
                #print(True)
            elif letter not in letters:
                letters[letter]=1
            #print(letter)
    return(letters)
