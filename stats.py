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

def sort_on(character_counts):
    return character_counts["num"]

def sorted_list(character_counts_item):
    dict_list = []
    for character_count in character_counts_item:
        ordered = character_counts_item[character_count]
        char_dict = {"char":character_count , "num":ordered}
        dict_list.append(char_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
    


     


    

