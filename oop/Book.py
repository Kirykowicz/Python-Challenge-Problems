class Book():

    def __init__(self, title, author, pages=0):
        self.title = title 
        self.author = author
        self.pages = pages 

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages 

    def __del__(self):
        print(f"{self.title} has been deleted")


book1 = Book('The greatest book of all time', 'Robert Kirykowicz', 317)

print(book1)
print(len(book1))

del book1

