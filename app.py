from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Файл для хранения текста
TEXT_FILE = 'saved_text.txt'

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/save-text', methods=['POST'])
def save_text():
    text = request.json['text']
    with open(TEXT_FILE, 'w') as f:
        f.write(text)
    return jsonify({'message': 'Текст успешно сохранён!'})

@app.route('/get-text')
def get_text():
    try:
        with open(TEXT_FILE, 'r') as f:
            saved_text = f.read()
        return jsonify({'text': saved_text})
    except FileNotFoundError:
        return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)
