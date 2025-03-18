from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Путь к файлу для хранения текста
TEXT_FILE_PATH = 'saved_text.txt'

@app.route('/')
def index():
    return render_template('zametki.html')

@app.route('/save', methods=['POST'])
def save_text():
    data = request.get_json()
    with open(TEXT_FILE_PATH, 'w') as file:
        file.write(data['text'])
    return jsonify({'message': 'Текст успешно сохранён!'})

@app.route('/load')
def load_text():
    try:
        with open(TEXT_FILE_PATH, 'r') as file:
            text = file.read()
        return jsonify({'text': text})
    except FileNotFoundError:
        return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)
