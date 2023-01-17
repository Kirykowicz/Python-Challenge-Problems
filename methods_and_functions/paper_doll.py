# Given a string, return a string where for every character in the original there are three characters

def paper_doll(word):
    word_split = []
    for letter in word:
        for i in range(3):
            word_split.append(letter)
    joinded_word = ''.join(word_split)
    print(joinded_word)

paper_doll("Robert")

# Alternate approach

def paper_doll_alternate(word):
    result = ''
    for letter in word:
        result += letter * 3
    return result 

print(paper_doll_alternate("Katie"))