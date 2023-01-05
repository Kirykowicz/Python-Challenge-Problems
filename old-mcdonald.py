def old_mcdonald(name):
    first_letter = name[0]
    inbetween = name[1:3]
    rest = name[3:]


    return first_letter.capitalize() + inbetween + rest.capitalize()

print(old_mcdonald('robert'))