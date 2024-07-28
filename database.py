import sqlite3
import os

def create_database():
    if os.path.exists('film_equipment.db'):
        return

    conn = sqlite3.connect('film_equipment.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS equipment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL,
            price REAL NOT NULL,
            availability BOOLEAN NOT NULL
        )
    ''')

    sample_data = [
        ('Camera Model X', 1000, 1),
        ('Camera Model Y', 1200, 0),
        ('Lens Model Z', 300, 1),
        ('Microphone Model A', 150, 1),
        ('Tripod Model B', 75, 1)
    ]
    cursor.executemany('INSERT INTO equipment (item, price, availability) VALUES (?, ?, ?)', sample_data)
    
    conn.commit()
    conn.close()

def check_availability(item_name):
    conn = sqlite3.connect('film_equipment.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM equipment WHERE item LIKE ?', (f'%{item_name}%',))
    record = cursor.fetchone()
    
    conn.close()
    
    if record:
        return {
            'item': record[1],
            'price': record[2],
            'availability': bool(record[3])
        }
    return None

def get_available_items():
    conn = sqlite3.connect('film_equipment.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT item, price FROM equipment WHERE availability=1')
    records = cursor.fetchall()
    
    conn.close()
    
    return [{'item': record[0], 'price': record[1]} for record in records]
