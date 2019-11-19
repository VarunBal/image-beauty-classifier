import psycopg2 as pg
import numpy as np
import struct

conn = pg.connect(database="testdb", user="postgres", password="root", host="localhost", port="5432")

db_cur = conn.cursor()

def create_table():
    try:
        db_cur.execute("CREATE TABLE URLS(ID TEXT PRIMARY KEY NOT NULL,URL TEXT NOT NULL);")
        conn.commit()
        print('table created')
    except Exception as e:
        print(e)
        conn.rollback()

def drop_table():
    try:
        db_cur.execute("DROP TABLE URLS")
        conn.commit()
        print('table dropped')
    except Exception as e:
        print(e)
        conn.rollback()

def insert_url(pic_id,url,is_pro):
    try:
        db_cur.execute("INSERT INTO URLS(ID,URL,IS_PRO) VALUES(%s,%s,%s);",(pic_id,url,is_pro))
        conn.commit()
        print('url inserted')
    except Exception as e:
        print(e)
        conn.rollback()

def select_url():
    try:
        db_cur.execute("SELECT URL,IS_PRO FROM URLS;")
        data = db_cur.fetchall()
        return data
    except Exception as e:
        print(e)

def close_conn():
    conn.close()

def main():
    create_table()
    db_cur.execute("SELECT URL FROM URLS;")
    data = db_cur.fetchall()
    print('data length:',len(data))
    conn.close()

if __name__ == '__main__':
    main()
