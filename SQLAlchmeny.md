An example explaining how SQLAlchemy is used at each step:

``` python
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Define the database connection
DATABASE_URI = 'sqlite:///library.db' # path to the database
engine = create_engine(DATABASE_URI, echo=True) # connect to the library database
```
`Import Statements` Import necessary modules from SQLAlchemy. These modules are used to create the database engine, define model classes, and set up relationships.

`Database Connection`
Define the DATABASE_URI which specifies the database type (SQLite in this case) and the database file name (library.db). Create the database engine using the create_engine function, passing in the DATABASE_URI. The echo=True argument enables logging, which is useful for seeing the SQL statements executed.

```python
# Define the Base class for declarative model definition
Base = declarative_base()
```
### Base Class Definition: 
Use the `declarative_base()` function to create a base class (Base) for declarative model definitions. All model classes will inherit from this base class.

```python
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
```
### Model Classes: 
Define two model classes, `Author` and `Book`, that inherit from the `Base` class. These classes represent tables in the database.

*`Author`* class has an id column (primary key) and a name column.

*`books`* is a relationship attribute that defines a one-to-many relationship between `authors` and `books`.

*`Book`* class has an id column (primary key), `title`, `ref`, and `author_id` columns.

*`author_id`* is a foreign key referencing the `id` column of the `authors` table.

*`author`* is a relationship attribute that defines the `back-reference` to the Author class.

``` python
# Create tables
Base.metadata.create_all(engine)
```
- *Create Tables*: 
Use the create_all method of the Base.metadata object to create the database tables defined by the model classes. This step creates the tables in the database based on the model class definitions.
```python
# Create a session
Session = sessionmaker(bind=engine)
session = Session()
```
- *Create a Session*: Create a session using the sessionmaker class. The bind argument is set to the database engine created earlier. This session will be used to interact with the database.
python
Copy code
### Insert data into the database
```
author_jk_rowling = Author(name="J.K. Rowling")
author_george_orwell = Author(name="George Orwell")

book_harry_potter = Book(title="Harry Potter", ref="HP001", author=author_jk_rowling)
book_1984 = Book(title="1984", ref="1984-001", author=author_george_orwell)

session.add_all([author_jk_rowling, author_george_orwell, book_harry_potter, book_1984])
session.commit()
```
- *Insert Data*: Create instances of the Author and Book classes with appropriate data. Use the session's add_all method to add the instances to the session. Calling session.commit() persists the changes to the database.
```python
# Query data from the database
all_authors = session.query(Author).all()
for author in all_authors:
    print(f"Author: {author.name}")
    for book in author.books:
        print(f"- Book: {book.title} (Ref: {book.ref})")
```
- *Query Data*: Use the session's query method to perform a query on the Author class. The all() method fetches all authors from the database. Loop through the authors and their associated books, printing the information.
```python
# Close the session
session.close()
```
- *Close Session*: Close the session to release resources.
This example demonstrates how to create tables, define model classes, establish relationships, insert data, and query data using SQLAlchemy. The ORM features make it easier to work with databases by abstracting away much of the underlying SQL.