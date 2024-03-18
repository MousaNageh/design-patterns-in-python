class Book:
    def __init__(self, title):
        self.title = title

class BookCollection:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def __iter__(self):
        return BookCollectionIterator(self)


class BookCollectionIterator:
    def __init__(self, book_collection: BookCollection):
        self._book_collection = book_collection
        self._index = 0
    
    def __next__(self):
        if self._index < len(self._book_collection.books):
            book = self._book_collection.books[self._index]
            self._index += 1
            return book
        else:
            raise StopIteration

# Example usage
if __name__ == "__main__":
    book_collection = BookCollection()
    book_collection.add_book(Book("Design Patterns"))
    book_collection.add_book(Book("The Pragmatic Programmer"))
    book_collection.add_book(Book("Clean Code"))
    
    for book in book_collection:
        print(book.title)