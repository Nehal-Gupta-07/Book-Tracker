import sqlite3

def init_db():
    conn = sqlite3.connect('tracker.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, name TEXT, author TEXT, platform TEXT)")
    conn.commit()
    conn.close()

def add_book(name,author,platform):
    try:
        conn = sqlite3.connect('tracker.db')
        c = conn.cursor()
        c.execute("SELECT * FROM books WHERE name = ? AND author = ? AND platform = ?", (name, author,platform))
        existing_book = c.fetchone()

        if existing_book:
            print(f"Duplicate book found: {name} by {author} in {platform} mode")
            return {"error": "Duplicate book entry."}  

       
        c.execute("INSERT INTO books (name, author, platform) VALUES (?, ?, ?)", (name, author,platform))
        conn.commit()
        return {"message": "Book added successfully!"}  
    except sqlite3.Error as e:
        print(f"An error occurred while adding the book: {e}")
        return {"error": str(e)} 
    finally:
        conn.close()

def get_all_books():
    conn = sqlite3.connect('tracker.db')
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    conn.close()
    return books

def search_books(search_type, keyword):
    conn = sqlite3.connect('tracker.db')
    c = conn.cursor()
    query = f"SELECT * FROM books WHERE {search_type} LIKE ?"
    c.execute(query, ('%' + keyword + '%',))
    books = c.fetchall()
    conn.close()
    return books

def  delete_book(name, author, platform):
    try:
        conn = sqlite3.connect('tracker.db')
        c =  conn.cursor()
        c.execute("SELECT * FROM books WHERE name = ? AND author = ? AND platform = ?",(name,author,platform))
        existing_book = c.fetchone()
        if existing_book:
            c.execute("DELETE FROM books WHERE name = ? AND author = ? AND platform = ?", (name,author,platform))
            conn.commit()
            return  {"message": "Book deleted successfully!"}  
        else:
            return {"error": "Book not found."}
    except sqlite3.Error as e:
        print(f"An error occurred while deleting the book: {e}")
        return {"error": str(e)}
    finally:
        conn.close()






