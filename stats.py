def number_of_words(text):
    return len(text.split())

def num_characters(text):
    count = {}
    lowercase = text.lower()
    for character in lowercase:
        if character in count:
            count[character] += 1
        else:
            count[character] = 1
    return count




    

