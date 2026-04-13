from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'books.json'

def load_books():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_books(books):
    with open(DATA_FILE, 'w') as f:
        json.dump(books, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/api/books', methods=['POST'])
def add_book():
    books = load_books()
    book_data = request.json
    
    new_book = {
        'id': len(books) + 1,
        'title': book_data['title'],
        'author': book_data['author']
    }
    books.append(new_book)
    save_books(books)
    return jsonify(new_book), 201