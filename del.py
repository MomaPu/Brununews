import psycopg2

# Установите соединение с базой данных
conn = psycopg2.connect(database="postgres", user="postgres", password="228778", host="127.", port="5333")
cur = conn.cursor()

# Удалите таблицу
cur.execute("DROP TABLE Article CASCADE;")

# Зафиксируйте изменения
conn.commit()

# Закройте соединение
cur.close()
conn.close()

