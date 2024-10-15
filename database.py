import sqlite3

def init_db():
    conn = sqlite3.connect('tracker.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, name TEXT, author TEXT, status TEXT, platform TEXT)")
    conn.commit()
    conn.close()

def add_book(name,author,status,platform):
    try:
        conn = sqlite3.connect('tracker.db')
        c = conn.cursor()

        # Check if the book already exists
        c.execute("SELECT * FROM books WHERE name = ? AND author = ? AND platform = ?", (name, author,platform))
        existing_book = c.fetchone()

        if existing_book:
            print(f"Duplicate book found: {name} by {author} in {platform} mode")
            return {"error": "Duplicate book entry."}  

       
        c.execute("INSERT INTO books (name, author, status, platform) VALUES (?, ?, ?, ?)", (name, author, status,platform))
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


def update_book_status(book_id, new_status):
    try:
        conn = sqlite3.connect('tracker.db')
        c = conn.cursor()
        
        
        c.execute("UPDATE books SET status = ? WHERE id = ?", (new_status, book_id))
        conn.commit()
        
        if c.rowcount == 0:
            return {"error": "Book not found."} 
        
        return {"message": "Book status updated successfully!"}  
    except sqlite3.Error as e:
        print(f"An error occurred while updating the book status: {e}")
        return {"error": str(e)}  
    finally:
        conn.close()
