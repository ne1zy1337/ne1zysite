from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Создаем приложение Flask
app = Flask(__name__)

# Конфигурация подключения к базе данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Подключаем SQLAlchemy
db = SQLAlchemy(app)

# Модель для заметок
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)

    def __repr__(self):
        return f'<Note {self.title}>'

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    notes = Note.query.all()  # Получение всех заметок из базы данных
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    title = request.form.get('title')
    content = request.form.get('content')
    
    note = Note(title=title, content=content)
    db.session.add(note)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    note = Note.query.filter_by(id=note_id).first_or_404()
    
    if request.method == 'POST':
        note.title = request.form.get('title')
        note.content = request.form.get('content')
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('edit_note.html', note=note)

@app.route('/delete_note/<int:note_id>')
def delete_note(note_id):
    note = Note.query.filter_by(id=note_id).first_or_404()
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


