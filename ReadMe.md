# DataBase
## Закон 1
### PK Первичный ключ (PK)
    Первичный ключ (PK)
    Определение: Первичный ключ — это уникальный идентификатор для каждой записи в таблице. Он гарантирует, что каждая запись может быть однозначно идентифицирована.
    Характеристики:
    Уникальность: Ни одна строка не может иметь одинаковое значение Первичного ключа.
    Не допускает NULL: Первичные ключи не могут содержать значения NULL.
    Одиночный или составной: Первичный ключ может состоять из одного столбца (одиночный ключ) или нескольких столбцов (составной ключ).   Определение: Первичный ключ — это уникальный идентификатор записи в таблице. Он должен быть уникальным для каждой записи и не может содержать NULL значения.
        
### FK
    Внешний ключ (FK)
    Определение: Внешний ключ — это столбец (или набор столбцов) в одной таблице, который ссылается на Первичный ключ в другой таблице. Он используется для установления и поддержания связи между данными в двух таблицах.
    Характеристики:
    Ссылочная целостность: Внешние ключи обеспечивают, чтобы значение в одной таблице соответствовало действительной записи в другой таблице.
    Может допускать NULL: Внешние ключи могут содержать значения NULL, если явно не определены как обязательные.
    Каскадные действия: При обновлениях или удалениях действия могут каскадироваться на связанные записи (например, каскадное удаление, каскадное обновление).

## Закон 2
### все данные должны сохраняться и нельзя удалять данные, иначе FK будет терять свой смысл

## Agregate
### условие при котором мі получаем резутьтат только один, максимум, минимум
    Агрегатные функции
        Агрегатные функции используются для выполнения вычислений над набором значений и возврата одного результирующего значения. Примеры таких функций включают:

        MAX() — возвращает максимальное значение из набора.
        MIN() — возвращает минимальное значение из набора.
        SUM() — возвращает сумму всех значений в наборе.
        AVG() — возвращает среднее значение из набора.
        COUNT() — возвращает количество строк в наборе.
        Пример:
        Чтобы получить максимальную зарплату из таблицы Employees (Сотрудники):

        sql
        Копировать код
        SELECT MAX(Salary) 
        FROM Employees;

## Non agrigate
### Appercase
## Lowercase
    Неагрегатные функции
    Неагрегатные функции выполняют операции над отдельными значениями и возвращают результат для каждой строки, к которой применяется функция. Примеры включают:

    UPPER() — преобразует все символы строки в верхний регистр.
    LOWER() — преобразует все символы строки в нижний регистр.
    Пример 1 (UPPER):
    Преобразовать имена сотрудников в верхний регистр:

    sql
    Копировать код
    SELECT UPPER(Name)
    FROM Employees;
    Пример 2 (LOWER):
    Преобразовать имена сотрудников в нижний регистр:

    sql
    Копировать код
    SELECT LOWER(Name)
    FROM Employees;
    Таким образом, агрегатные функции обычно возвращают одно значение на основе группы строк, тогда как неагрегатные функции работают на уровне отдельной строки, возвращая результат для каждой строки в отдельности.

### Group by
    Оператор GROUP BY используется для группировки строк с одинаковыми значениями в определенных столбцах. Он часто используется вместе с агрегатными функциями (например, COUNT(), SUM(), MAX(), MIN(), AVG()) для выполнения вычислений по каждой группе данных.

    SELECT Customer, COUNT(*)
    FROM Customers
    GROUP BY Customer;

### Like
    В SQL оператор LIKE используется для поиска строк, которые соответствуют определенному шаблону в текстовых столбцах. Он позволяет выполнять частичные совпадения строк, что делает его полезным для поиска данных, которые соответствуют определенным критериям.
        Специальные символы в шаблонах:
    % — Заменяет ноль или более любых символов.
    _ — Заменяет один любой символ.

    SELECT CustomerName
    FROM Customers
    WHERE CustomerName LIKE '%mit%';


### Join
    Оператор JOIN в SQL используется для объединения строк из двух или более таблиц на основе логической связи между ними. В основном, эта связь создается через ключи, например, Primary Key и Foreign Key.

    Основные типы JOIN:
    INNER JOIN

    Возвращает только те строки, которые имеют совпадение в обеих объединяемых таблицах.
    LEFT JOIN (или LEFT OUTER JOIN)

    Возвращает все строки из левой таблицы и совпадающие строки из правой таблицы. Если совпадений нет, возвращаются NULL значения для столбцов из правой таблицы.
    RIGHT JOIN (или RIGHT OUTER JOIN)

    Возвращает все строки из правой таблицы и совпадающие строки из левой таблицы. Если совпадений нет, возвращаются NULL значения для столбцов из левой таблицы.
    FULL JOIN (или FULL OUTER JOIN)

    Возвращает все строки, когда есть совпадения в одной из таблиц. Если совпадений нет, возвращаются NULL значения для столбцов из обеих таблиц.
    CROSS JOIN

    Возвращает декартово произведение двух таблиц, т.е. все возможные комбинации строк из обеих таблиц.

        SELECT Orders.OrderID, Customers.CustomerName
    FROM Orders
    INNER JOIN Customers
    ON Orders.CustomerID = Customers.CustomerID;

# SQLite

## con 
    con — Сокращение для Connection (Подключение)
    Описание: con обычно используется как переменная для хранения объекта подключения к базе данных. Этот объект представляет соединение с базой данных SQLite, через которое выполняются запросы.

    Пример:

    python
    Копировать код
    import sqlite3

    # Создание подключения к базе данных
    con = sqlite3.connect('example.db')
    В этом примере con — это объект подключения к базе данных example.db.

## cur
    cur — Сокращение для Cursor (Курсор)
    Описание: cur обычно используется как переменная для хранения объекта курсора. Курсор используется для выполнения SQL-запросов и извлечения данных из базы данных.

    Пример:

    python
    Копировать код
    # Создание курсора
    cur = con.cursor()

    # Выполнение SQL-запроса
    cur.execute('SELECT * FROM users')

    # Извлечение всех результатов
    rows = cur.fetchall()

    for row in rows:
        print(row)
    В этом примере cur — это объект курсора, через который выполняется SQL-запрос и извлекаются результаты.


###  Как они взаимодействуют
    con (Connection) создаёт связь между вашей программой и базой данных.
    cur (Cursor) используется для выполнения SQL-запросов через это подключение и для обработки результатов запросов.
    Закрытие соединения
    Не забудьте закрыть подключение после завершения работы с базой данных, чтобы освободить ресурсы.

    python
    Копировать код
    # Закрытие курсора и подключения
    cur.close()
    con.close()
    Это основные роли переменных con и cur в работе с SQLite.

## CREATE TABLE IF NOT EXISTS
    cur.execute("""
        CREATE TABLE IF NOT EXISTS cars (
            brand TEXT,
            color TEXT,
            year INTEGER
        )
    """)
## Insert INTO cars VALUES
    ef addCar(carBrand, carColor, carYear):

        cur.execute(f"Insert INTO cars VALUES ('{carBrand}', '{carColor}', '{carYear}')")
        con.commit()

    addCar(input("brand"), input("color"), input("year"))

## Delete
## Update
