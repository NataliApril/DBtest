'''https://pythonru.com/biblioteki/vvedenie-v-postgresql-s-python-psycopg2'''


import psycopg2
import datetime
from psycopg2 import Error

try:
    conn = psycopg2.connect(dbname="tester", user="tester", password="postgres", host= "77.238.255.81", port="5432")

    # Курсор для выполнения операций с базой данных
    cursor = conn.cursor()
    # Распечатать сведения о PostgreSQL
    print("Информация о сервере PostgreSQL")
    print(conn.get_dsn_parameters(), "\n")
    # Выполнение SQL-запроса
    cursor.execute("SELECT version();")
    # Получить результат
    record = cursor.fetchone()
    print("Вы подключены к - ", record, "\n")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")