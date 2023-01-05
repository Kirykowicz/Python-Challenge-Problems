def master_yoda(text):
    split_text = text.split()
    split_text.reverse()
    return ' '.join(split_text)

print(master_yoda('reverse this string'))