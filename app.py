from flask import Flask, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app) 
import json
from db import *

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    return render_template('zametki.html')

@app.route('/save-note', methods=['POST'])
def save_note():
    data = request.get_json()
    add_note(data['title'], data['content'], data['color'])
    return jsonify({'message': 'Заметка сохранена'})

@app.route('/get-notes')
def get_notes():
    notes = get_all_notes()
    formatted_notes = [{'id': row[0], 'title': row[1], 'content': row[2], 'color': row[3]} for row in notes]
    return jsonify(formatted_notes)

@app.route('/edit-note/<int:note_id>', methods=['PUT'])
def edit_note(note_id):
    updated_data = request.get_json()
    update_note(note_id, updated_data.get('title'), updated_data.get('content'), updated_data.get('color'))
    return jsonify({'message': 'Заметка обновлена'})

@app.route('/delete-note/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    delete_note(note_id)
    return jsonify({'message': 'Заметка удалена'})

if __name__ == '__main__':
    app.run(debug=True)
