#Supacharn Kaowanan Section-1 653380026-4

import pytest
from main import User
from main import Book

def test_register_user(db_session):
    newUser = User(username = "TestUser",fullname = "CoolUser",has_book = True)
    db_session.add(newUser)
    db_session.commit()

    User = db_session.query(User).filter_by(username="TestUser").first()
    assert User is not None
    assert User.username == "TestUser"

def test_remove_user(db_session):
    newUser2 = User(username = "TestUser2",fullname = "CoolUser",has_book = True)
    db_session.add(newUser2)
    db_session.commit()

    db_session.delete(newUser2)
    db_session.commit()

    DeletedUser = db_session.query(User).filter_by(username="TestUser2").first()
    assert DeletedUser is None

def test_register_book(db_session):
    newBook = Book(title = "Book1",firstauthor = "Author",isbn = "isbn")
    db_session.add(newBook)
    db_session.commit()

    Book = db_session.query(Book).filter_by(title="Book1").first()
    assert Book is not None
    assert Book.title == "Book1"

def test_remove_user(db_session):
    newBook2 = User(title = "Book2",firstauthor = "Author2",isbn = "isbn2")
    db_session.add(newBook2)
    db_session.commit()

    db_session.delete(newBook2)
    db_session.commit()

    DeletedBook = db_session.query(Book).filter_by(title="Book2").first()
    assert DeletedBook is None


