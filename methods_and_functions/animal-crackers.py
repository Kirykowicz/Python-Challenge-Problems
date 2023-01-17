def animal_crackers(text):
    split_text = text.lower().split()
    return split_text[0][0] == split_text[1][0]
       

print(animal_crackers('Robert rirykowicz')) 