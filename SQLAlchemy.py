from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Define the database connection
DATABASE_URI = 'sqlite:///library.db'
engine = create_engine(DATABASE_URI, echo=True)

# Define the Base class for declarative model definition
Base = declarative_base()

# Define Author and Book classes
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, Sequence('author_id_seq'), primary_key=True)
    name = Column(String)

    books = relationship('Book', back_populates='author')

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, Sequence('book_id_seq'), primary_key=True)
    title = Column(String)
    ref = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship('Author', back_populates='books')

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert data into the database
author_jk_rowling = Author(name="J.K. Rowling")
author_george_orwell = Author(name="George Orwell")

book_harry_potter = Book(title="Harry Potter", ref="HP001", author=author_jk_rowling)
book_1984 = Book(title="1984", ref="1984-001", author=author_george_orwell)

session.add_all([author_jk_rowling, author_george_orwell, book_harry_potter, book_1984])
session.commit()

# Query data from the database
all_authors = session.query(Author).all()
for author in all_authors:
    print(f"Author: {author.name}")
    for book in author.books:
        print(f"- Book: {book.title} (Ref: {book.ref})")

# Close the session
session.close()
