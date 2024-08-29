import sqlite3

# Создание подключения к базе данных
con = sqlite3.connect("cars.db")

# Создание курсора
cur = con.cursor()

# Выполнение запроса для получения информации о таблицах
res = cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(res.fetchone())  # Получаем одну строку результата


cur.execute("""
    CREATE TABLE IF NOT EXISTS cars (
        brand TEXT,
        color TEXT,
        year INTEGER
    )
""")


def addCar(carBrand, carColor, carYear):

    cur.execute(f"Insert INTO cars VALUES ('{carBrand}', '{carColor}', '{carYear}')")
    con.commit()

addCar(input("brand"), input("color"), input("year"))


res = cur.execute("Select * FROM cars")
for i in res.fetchall():
    print(i)


    

# # Выполнение запроса для вставки данных
# cur.execute("""
#     INSERT INTO cars (make, color, year) VALUES
#         ('Volvo', 'red', 2017),
#         ('Kia', 'green', 2020)
# """)

# # Сохранение изменений
# con.commit()

# Закрытие курсора и подключения
cur.close()
con.close()
