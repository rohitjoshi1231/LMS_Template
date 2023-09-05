class BookDetails:
    def __init__(self, book_id: int, book_name: str, author_name: list):
        self.book_id = book_id
        self.book_name = book_name
        self.author_name = author_name

    def add_book(self):
        if all([self.book_id, self.book_name, self.author_name]):
            # Add book in database
            return 'book added successfull'
        else:
            return 'Write all Required Fields'
