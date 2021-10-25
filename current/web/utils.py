import time
from get_stocks import get_conn, close_conn
def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年","月","日")

def get_rise():
    conn, cursor = get_conn()
    sql = "select * from current_details        \
                where code REGEXP '^30' and name not REGEXP '^C' and gains>19.9     \
                or code REGEXP '^00' and gains>9.9  \
                or code REGEXP '^60' and gains>9.9;"
    num = cursor.execute(sql)

    close_conn(conn, cursor)
    return str(num)

def get_drop():
    conn, cursor = get_conn()
    sql = "select * from current_details        \
                where code REGEXP '^30' and name not REGEXP '^C' and gains<-19.9     \
                or code REGEXP '^00' and gains<-9.9  \
                or code REGEXP '^60' and gains<-9.9;"
    num = cursor.execute(sql)

    close_conn(conn, cursor)
    return str(num)

if __name__ == "__main__":
    print(get_rise())