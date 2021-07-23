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
        ,description VARCHAR(10000) NOT NULL
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
    (1, 'Гобеленовая гостиная', 
        '''
            Князья Юсуповы славились европейским уровнем культуры и неограниченным
            финансовыми возможностями, позволявшими не только следовать последней моде,
            но и задавать тон в аристократической среде. Но неизменным в парадных апартаментах
            дворца на Мойке оставалось то, что позволило севтскому хроникёру в 1846 году назвать
            их "чертогами изящества и вкуса". 
            Сегодня во дворце остались всего три интерьера Б. Симона: Гобеленовая гостиная. Интерьер Б. 
            СимонаЗал Антонио Виги и Комната коронации. Гобеленовая гостиная оформляется симметрично 
            Зимнему саду с правой стороны вестибюля». Гобеленовая гостиная появилась во дворце как помещение, 
            «предназначенное» специально для гобелена «Дети-садовники», подаренного Наполеоном I князю, 
            а также для трех фламандских шпалер из серии «Охота Мелиагра». Таким образом, и гобелен, 
            и шпалеры стали «главными героями» помещения. Для того, чтобы подчеркнуть теплоту красок 
            гобелена и шпалер, Б. Симон расписал гипсовые стены гостиной под темное дерево. «Стены сделаны не из ореха, 
            - сказано в источнике, - лишь низ стен облицован ореховыми панелями, верхняя же часть украшена лепкой 
            и тонирована под орех».  Забегая вперед, скажем, что эти шедевры были переданы 
            в Эрмитаж, а их место заняли копии.
        '''
    , '', '/static/room1.png'),
    (2, 'Спальня княгини', 
        '''
            Князья Юсуповы славились европейским уровнем культуры и неограниченным
            финансовыми возможностями, позволявшими не только следовать последней моде,
            но и задавать тон в аристократической среде. Но неизменным в парадных апартаментах
            дворца на Мойке оставалось то, что позволило севтскому хроникёру в 1846 году назвать
            их "чертогами изящества и вкуса". 
            Сегодня во дворце остались всего три интерьера Б. Симона: Гобеленовая гостиная. Интерьер Б. 
            СимонаЗал Антонио Виги и Комната коронации. Гобеленовая гостиная оформляется симметрично 
            Зимнему саду с правой стороны вестибюля». Гобеленовая гостиная появилась во дворце как помещение, 
            «предназначенное» специально для гобелена «Дети-садовники», подаренного Наполеоном I князю, 
            а также для трех фламандских шпалер из серии «Охота Мелиагра». Таким образом, и гобелен, 
            и шпалеры стали «главными героями» помещения. Для того, чтобы подчеркнуть теплоту красок 
            гобелена и шпалер, Б. Симон расписал гипсовые стены гостиной под темное дерево. «Стены сделаны не из ореха, 
            - сказано в источнике, - лишь низ стен облицован ореховыми панелями, верхняя же часть украшена лепкой 
            и тонирована под орех».  Забегая вперед, скажем, что эти шедевры были переданы 
            в Эрмитаж, а их место заняли копии.
        '''
    , '', '/static/room2.png'),
    (3, 'Большая ротонда', 
        '''
            Князья Юсуповы славились европейским уровнем культуры и неограниченным
            финансовыми возможностями, позволявшими не только следовать последней моде,
            но и задавать тон в аристократической среде. Но неизменным в парадных апартаментах
            дворца на Мойке оставалось то, что позволило севтскому хроникёру в 1846 году назвать
            их "чертогами изящества и вкуса". 
            Сегодня во дворце остались всего три интерьера Б. Симона: Гобеленовая гостиная. Интерьер Б. 
            СимонаЗал Антонио Виги и Комната коронации. Гобеленовая гостиная оформляется симметрично 
            Зимнему саду с правой стороны вестибюля». Гобеленовая гостиная появилась во дворце как помещение, 
            «предназначенное» специально для гобелена «Дети-садовники», подаренного Наполеоном I князю, 
            а также для трех фламандских шпалер из серии «Охота Мелиагра». Таким образом, и гобелен, 
            и шпалеры стали «главными героями» помещения. Для того, чтобы подчеркнуть теплоту красок 
            гобелена и шпалер, Б. Симон расписал гипсовые стены гостиной под темное дерево. «Стены сделаны не из ореха, 
            - сказано в источнике, - лишь низ стен облицован ореховыми панелями, верхняя же часть украшена лепкой 
            и тонирована под орех».  Забегая вперед, скажем, что эти шедевры были переданы 
            в Эрмитаж, а их место заняли копии.
        '''
    , '', '/static/room3.png'),
    (4, 'Синяя гостиная', 
        '''
            Князья Юсуповы славились европейским уровнем культуры и неограниченным
            финансовыми возможностями, позволявшими не только следовать последней моде,
            но и задавать тон в аристократической среде. Но неизменным в парадных апартаментах
            дворца на Мойке оставалось то, что позволило севтскому хроникёру в 1846 году назвать
            их "чертогами изящества и вкуса". 
            Сегодня во дворце остались всего три интерьера Б. Симона: Гобеленовая гостиная. Интерьер Б. 
            СимонаЗал Антонио Виги и Комната коронации. Гобеленовая гостиная оформляется симметрично 
            Зимнему саду с правой стороны вестибюля». Гобеленовая гостиная появилась во дворце как помещение, 
            «предназначенное» специально для гобелена «Дети-садовники», подаренного Наполеоном I князю, 
            а также для трех фламандских шпалер из серии «Охота Мелиагра». Таким образом, и гобелен, 
            и шпалеры стали «главными героями» помещения. Для того, чтобы подчеркнуть теплоту красок 
            гобелена и шпалер, Б. Симон расписал гипсовые стены гостиной под темное дерево. «Стены сделаны не из ореха, 
            - сказано в источнике, - лишь низ стен облицован ореховыми панелями, верхняя же часть украшена лепкой 
            и тонирована под орех».  Забегая вперед, скажем, что эти шедевры были переданы 
            в Эрмитаж, а их место заняли копии.
        '''
    , '', '/static/room4.png'),
    (5, 'Красная гостиная', 
        '''
            Князья Юсуповы славились европейским уровнем культуры и неограниченным
            финансовыми возможностями, позволявшими не только следовать последней моде,
            но и задавать тон в аристократической среде. Но неизменным в парадных апартаментах
            дворца на Мойке оставалось то, что позволило севтскому хроникёру в 1846 году назвать
            их "чертогами изящества и вкуса". 
            Сегодня во дворце остались всего три интерьера Б. Симона: Гобеленовая гостиная. Интерьер Б. 
            СимонаЗал Антонио Виги и Комната коронации. Гобеленовая гостиная оформляется симметрично 
            Зимнему саду с правой стороны вестибюля». Гобеленовая гостиная появилась во дворце как помещение, 
            «предназначенное» специально для гобелена «Дети-садовники», подаренного Наполеоном I князю, 
            а также для трех фламандских шпалер из серии «Охота Мелиагра». Таким образом, и гобелен, 
            и шпалеры стали «главными героями» помещения. Для того, чтобы подчеркнуть теплоту красок 
            гобелена и шпалер, Б. Симон расписал гипсовые стены гостиной под темное дерево. «Стены сделаны не из ореха, 
            - сказано в источнике, - лишь низ стен облицован ореховыми панелями, верхняя же часть украшена лепкой 
            и тонирована под орех».  Забегая вперед, скажем, что эти шедевры были переданы 
            в Эрмитаж, а их место заняли копии.
        '''
    , '', '/static/room5.png'),
    (6, 'Зелёная гостиная', 
        '''
            Князья Юсуповы славились европейским уровнем культуры и неограниченным
            финансовыми возможностями, позволявшими не только следовать последней моде,
            но и задавать тон в аристократической среде. Но неизменным в парадных апартаментах
            дворца на Мойке оставалось то, что позволило севтскому хроникёру в 1846 году назвать
            их "чертогами изящества и вкуса". 
            Сегодня во дворце остались всего три интерьера Б. Симона: Гобеленовая гостиная. Интерьер Б. 
            СимонаЗал Антонио Виги и Комната коронации. Гобеленовая гостиная оформляется симметрично 
            Зимнему саду с правой стороны вестибюля». Гобеленовая гостиная появилась во дворце как помещение, 
            «предназначенное» специально для гобелена «Дети-садовники», подаренного Наполеоном I князю, 
            а также для трех фламандских шпалер из серии «Охота Мелиагра». Таким образом, и гобелен, 
            и шпалеры стали «главными героями» помещения. Для того, чтобы подчеркнуть теплоту красок 
            гобелена и шпалер, Б. Симон расписал гипсовые стены гостиной под темное дерево. «Стены сделаны не из ореха, 
            - сказано в источнике, - лишь низ стен облицован ореховыми панелями, верхняя же часть украшена лепкой 
            и тонирована под орех».  Забегая вперед, скажем, что эти шедевры были переданы 
            в Эрмитаж, а их место заняли копии.
        '''
    , '', '/static/room6.png'),
    (7, 'Танцевальный зал', 
        '''
            Князья Юсуповы славились европейским уровнем культуры и неограниченным
            финансовыми возможностями, позволявшими не только следовать последней моде,
            но и задавать тон в аристократической среде. Но неизменным в парадных апартаментах
            дворца на Мойке оставалось то, что позволило севтскому хроникёру в 1846 году назвать
            их "чертогами изящества и вкуса". 
            Сегодня во дворце остались всего три интерьера Б. Симона: Гобеленовая гостиная. Интерьер Б. 
            СимонаЗал Антонио Виги и Комната коронации. Гобеленовая гостиная оформляется симметрично 
            Зимнему саду с правой стороны вестибюля». Гобеленовая гостиная появилась во дворце как помещение, 
            «предназначенное» специально для гобелена «Дети-садовники», подаренного Наполеоном I князю, 
            а также для трех фламандских шпалер из серии «Охота Мелиагра». Таким образом, и гобелен, 
            и шпалеры стали «главными героями» помещения. Для того, чтобы подчеркнуть теплоту красок 
            гобелена и шпалер, Б. Симон расписал гипсовые стены гостиной под темное дерево. «Стены сделаны не из ореха, 
            - сказано в источнике, - лишь низ стен облицован ореховыми панелями, верхняя же часть украшена лепкой 
            и тонирована под орех».  Забегая вперед, скажем, что эти шедевры были переданы 
            в Эрмитаж, а их место заняли копии.
        '''
    , '', '/static/room7.png'),
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