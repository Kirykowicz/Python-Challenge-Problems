def old_mcdonald(name):
    name[0] = name[0].capitalize()
    name[3] = name[3].capitalize()
    return name

example = old_mcdonald('robert')

print(example)