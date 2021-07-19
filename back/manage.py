import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

query_create_table_rooms = '''
    CREATE TABLE rooms (
        id INTEGER PRIMARY KEY
        ,name VARCHAR(200) NOT NULL
    )
'''


query_create_table_rooms_data = '''
    CREATE TABLE rooms_data (
        id INTEGER PRIMARY KEY
        ,room_id INTEGER NOT NULL
        ,description VARCHAR(1000) NOT NULL
        ,audio VARCHAR(1000) NOT NULL
        ,photo VARCHAR(300) NOT NULL
    )
'''


rooms = [
    ('Гобеленовая гостиная',),
    ('Спальня княгини',),
    ('Большая ротонда',),
    ('Синяя гостиная',),
    ('Красная гостиная',),
    ('Зелёная гостиная',),
    ('Танцевальный зал',),
]

rooms_data = [
    (1, '', '', ''),
    (2, '', '', ''),
    (3, '', '', ''),
    (4, '', '', ''),
    (5, '', '', ''),
    (6, '', '', ''),
    (7, '', '', ''),
]

query_add_rooms = '''
    INSERT INTO rooms
    (name) VALUES (?)
'''

query_add_rooms_data = '''
    INSERT INTO rooms_data
    (room_id, description, audio, photo)
    VALUES
    (?, ?, ?, ?)
'''

cursor.execute(query_create_table_rooms)
cursor.execute(query_create_table_rooms_data)

cursor.executemany(
    query_add_rooms,
    rooms
).executemany(
    query_add_rooms_data,
    rooms_data
)

conn.commit()