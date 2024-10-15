from flask import Flask,request
from database import init_db,add_book,get_all_books,search_books,delete_book

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
    return books

@app.route('/search', methods=['GET'])
def search():
    data = request.json
    search_type = data['search_type']
    keyword = data['keyword']
    books = search_books(search_type,keyword)
    return books

@app.route("/delete",methods=['DELETE'])
def delete():
    data = request.json
    name = data['name']
    author = data['author']
    platform = data['platform']
    result = delete_book(name,author,platform)
    return result



if __name__ == "__main__":
    app.run(debug=True)