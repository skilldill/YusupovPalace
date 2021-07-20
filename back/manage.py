import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

query_create_table_rooms = '''
    CREATE TABLE rooms (
        id INTEGER PRIMARY KEY
        ,name VARCHAR(200) NOT NULL
        ,preview VARCHAR(300) NOT NULL
    )
'''


query_create_table_rooms_data = '''
    CREATE TABLE rooms_data (
        id INTEGER PRIMARY KEY
        ,room_id INTEGER NOT NULL
        ,name VARCHAR(200) NOT NULL
        ,description VARCHAR(1000) NOT NULL
        ,audio VARCHAR(1000) NOT NULL
        ,photo VARCHAR(300) NOT NULL
    )
'''


rooms = [
    ('Гобеленовая гостиная', '/static/room1.png'),
    ('Спальня княгини', '/static/room2.png'),
    ('Большая ротонда', '/static/room3.png'),
    ('Синяя гостиная', '/static/room4.png'),
    ('Красная гостиная', '/static/room5.png'),
    ('Зелёная гостиная', '/static/room6.png'),
    ('Танцевальный зал', '/static/room7.png'),
]

rooms_data = [
    (1, 'Гобеленовая гостиная', '', '', '/static/room1.png'),
    (2, 'Спальня княгини', '', '', '/static/room2.png'),
    (3, 'Большая ротонда', '', '', '/static/room3.png'),
    (4, 'Синяя гостиная', '', '', '/static/room4.png'),
    (5, 'Красная гостиная', '', '', '/static/room5.png'),
    (6, 'Зелёная гостиная', '', '', '/static/room6.png'),
    (7, 'Танцевальный зал', '', '', '/static/room7.png'),
]

query_add_rooms = '''
    INSERT INTO rooms
    (name, preview) 
    VALUES 
    (?, ?)
'''

query_add_rooms_data = '''
    INSERT INTO rooms_data
    (room_id, name, description, audio, photo)
    VALUES
    (?, ?, ?, ?, ?)
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