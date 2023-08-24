CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name VARCHAR(255) NOT NULL,
    student_reg VARCHAR(255) NOT NULL
);

CREATE TABLE books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_name VARCHAR(255) NOT NULL,
    book_ref VARCHAR(255) NOT NULL,
    author_id INTEGER,

    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

CREATE TABLE authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_name VARCHAR(255) NOT NULL
);

CREATE TABLE borrowed_books (
    borrowed_book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
);

-- insert data to students table
INSERT INTO students (student_name, student_reg) VALUES ('Fauzia Mohammed', '20230587');
INSERT INTO students (student_name, student_reg) VALUES ('John Karanja', '20232658');
INSERT INTO students (student_name, student_reg) VALUES ('Gideon Peter', '20236365');

-- insert data to authors table
INSERT INTO authors (author_name) VALUES ('J.K Rowling');
INSERT INTO authors (author_name) VALUES ('Nelius Wandia');
INSERT INTO authors (author_name) VALUES ('Owino Gilbert');

-- insert data to books table
INSERT INTO books (book_name, book_ref, author_id) VALUES ('Harry Potter', 'HP001', 1);
INSERT INTO books (book_name, book_ref, author_id) VALUES ('Pride', 'PR-56', 2);
INSERT INTO books (book_name, book_ref, author_id) VALUES ('Born a Crime', 'BAC-635', 1);
INSERT INTO books (book_name, book_ref, author_id) VALUES ('Msafiri', 'MSA-214', 3);


-- insert data to borrowed_books table
INSERT INTO borrowed_books (book_id, student_id) VALUES (1, 1);
INSERT INTO borrowed_books (book_id, student_id) VALUES (2, 3);


-- get author of a book
SELECT * FROM books WHERE book_ref = 'HP001';

SELECT authors.author_name, books.book_name
FROM books 
JOIN authors ON books.author_id = authors.author_id
WHERE book_ref = 'PR-56';
