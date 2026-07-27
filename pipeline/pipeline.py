import csv
import psycopg
import os

from dotenv import load_dotenv
load_dotenv()

password = os.getenv("password")

data = []

with open('source\\source.csv', mode = 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    # print(csv_reader.dialect)
    
    for row in csv_reader:
        data.append(row)

data = data[1:]

with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password=password,
) as connection:

    with connection.cursor() as cursor:

        query = "insert into target1 values (%s, %s, %s)" \
        " on conflict (id) " \
        "do update set name = excluded.name, grade = excluded.grade"
        cursor.executemany(query, data)
        connection.commit()