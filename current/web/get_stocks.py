import pandas as pd
import pymysql

# 连接本地数据库


def get_conn():
    conn = pymysql.connect(host="127.0.0.1", user="root",
                           password="518518", db="stock", charset="utf8")
    cursor = conn.cursor()
    return conn, cursor

# 断开与本地数据库的连接


def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def get_stocks():
    conn, cursor = get_conn()
    sql = "select * from current_details"
    cursor.execute(sql)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=['代码', '名称', '当前价格', '涨幅', '涨价', '总手',
                                        '换手', '市盈', '当日最高', '当日最低', '今日开盘',
                                        '昨日收盘', '总市值', '流通市值', '市净', '更新时间'])
    close_conn(conn, cursor)
    return df


def get_higho_lowg():
    conn, cursor = get_conn()
    sql = "select * from current_details where t_open>y_close and gains<0;"
    cursor.execute(sql)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=['代码', '名称', '当前价格', '涨幅', '涨价', '总手',
                                        '换手', '市盈', '当日最高', '当日最低', '今日开盘',
                                        '昨日收盘', '总市值', '流通市值', '市净', '更新时间'])
    if len(df) == 0:
        df = pd.DataFrame([['-', '-', '-', '-', '-', '-', '-', '-',
                            '-', '-', '-', '-', '-', '-', '-', '-']],
                          columns=['代码', '名称', '当前价格', '涨幅', '涨价', '总手',
                                   '换手', '市盈', '当日最高', '当日最低', '今日开盘',
                                   '昨日收盘', '总市值', '流通市值', '市净', '更新时间'])
    close_conn(conn, cursor)
    return df


def get_rise_limit():
    conn, cursor = get_conn()
    sql = "select * from current_details        \
            where code REGEXP '^30' and name not REGEXP '^C' and gains>19.9   \
            or code REGEXP '^00' and gains>9.9  \
            or code REGEXP '^60' and gains>9.9;"
    cursor.execute(sql)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=['代码', '名称', '当前价格', '涨幅', '涨价', '总手',
                                        '换手', '市盈', '当日最高', '当日最低', '今日开盘',
                                        '昨日收盘', '总市值', '流通市值', '市净', '更新时间'])
    if len(df) == 0:
        df = pd.DataFrame([['-', '-', '-', '-', '-', '-', '-', '-',
                            '-', '-', '-', '-', '-', '-', '-', '-']],
                          columns=['代码', '名称', '当前价格', '涨幅', '涨价', '总手',
                                   '换手', '市盈', '当日最高', '当日最低', '今日开盘',
                                   '昨日收盘', '总市值', '流通市值', '市净', '更新时间'])
    close_conn(conn, cursor)
    return df


def get_drop_limit():
    conn, cursor = get_conn()
    sql = "select * from current_details        \
            where code REGEXP '^30' and name not REGEXP '^C' and gains<-19.9  \
            or code REGEXP '^00' and gains<-9.9  \
            or code REGEXP '^60' and gains<-9.9;"
    cursor.execute(sql)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=['代码', '名称', '当前价格', '涨幅', '涨价', '总手',
                                        '换手', '市盈', '当日最高', '当日最低', '今日开盘',
                                        '昨日收盘', '总市值', '流通市值', '市净', '更新时间'])
    if len(df) == 0:
        df = pd.DataFrame([['-', '-', '-', '-', '-', '-', '-', '-',
                            '-', '-', '-', '-', '-', '-', '-', '-']],
                          columns=['代码', '名称', '当前价格', '涨幅', '涨价', '总手',
                                   '换手', '市盈', '当日最高', '当日最低', '今日开盘',
                                   '昨日收盘', '总市值', '流通市值', '市净', '更新时间'])
    close_conn(conn, cursor)
    return df
