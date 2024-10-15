from flask import Flask,request
from database import init_db,add_book,get_all_books,search_books

app = Flask(__name__)


def initialize():
    init_db()

initialize()

@app.route('/add_book', methods=['POST'])
def new_entry():
    data = request.json
    name = data['name']
    author = data['author']
    platform = data['platform']
    result = add_book(name, author,platform)  
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


if __name__ == "__main__":
    app.run(debug=True)