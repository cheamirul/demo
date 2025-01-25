import psycopg2

con = psycopg2.connect(dbname="studentdb", user="postgres", password="blk30416", host="localhost", port="5433")
print(con)