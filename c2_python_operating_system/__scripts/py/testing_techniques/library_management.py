#!/usr/bin/env python3

class Library:
    def __init__(self):
        self.collection = []
    
    def add_book(self, book_title):
        self.collection.append(book_title)
    
    def has_book(self, book_title):
        return book_title in self.collection
