import sqlite3

def init_db():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            color TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_note(title, content, color):
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute('INSERT INTO notes (title, content, color) VALUES (?, ?, ?)', (title, content, color))
    conn.commit()
    conn.close()

def get_all_notes():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute('SELECT * FROM notes')
    rows = c.fetchall()
    conn.close()
    return rows

def update_note(id, title=None, content=None, color=None):
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    query = 'UPDATE notes SET '
    values = []
    if title is not None:
        query += 'title=?, '
        values.append(title)
    if content is not None:
        query += 'content=?, '
        values.append(content)
    if color is not None:
        query += 'color=?, '
        values.append(color)
    query = query[:-2] + ' WHERE id=?'
    values.append(id)
    c.execute(query, tuple(values))
    conn.commit()
    conn.close()

def delete_note(id):
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute('DELETE FROM notes WHERE id=?', (id,))
    conn.commit()
    conn.close()
