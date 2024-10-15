from flask import Flask,request
import sqlite3
from database import init_db,add_book,get_all_books,search_books,update_book_status

app = Flask(__name__)


def initialize():
    init_db()

initialize()

@app.route('/add_book', methods=['POST'])
def new_entry():
    data = request.json
    name = data['name']
    author = data['author']
    status = data['status']
    platform = data['platform']
    result = add_book(name, author, status,platform)  
    return result 
        

@app.route('/view',methods=['GET'])
def view_all():
    books = get_all_books()
    return {'books':books}

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    search_type = data['search_type']
    keyword = data['keyword']
    books = search_books(search_type,keyword)
    return {'books':books}

@app.route('/update_book', methods=['POST'])
def update_book_status_api():
    data = request.json
    book_id = data['id']
    new_status = data['status']
    
    result = update_book_status(book_id, new_status)  
    return result 


if __name__ == "__main__":
    app.run(debug=True)