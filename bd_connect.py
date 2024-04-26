import psycopg2

conn = psycopg2.connect(dbname="tester", user="tester", password="postgres", host= "77.238.255.81", port="5432")

cur = conn.cursor()

cur.execute('select * from people')

results = cur.fetchall()

for result in results:
    print (result)