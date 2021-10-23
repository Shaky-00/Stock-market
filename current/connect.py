import pymysql

# 连接本地数据库
def get_conn():
    conn = pymysql.connect(host="127.0.0.1", user="root", password="518518", db="stock", charset="utf8")
    cursor = conn.cursor()
    return conn, cursor

# 断开与本地数据库的连接
def close_conn(cursor, conn):
    if cursor:
        cursor.close()
    if conn:
        conn.close()