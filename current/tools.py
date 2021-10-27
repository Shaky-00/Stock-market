# 一些功能性的接口函数（数据库查询/分析）
from connect import get_conn, close_conn
import pandas as pd
import traceback


# 1. 获取代码为code的股票行情信息
def get_stock_info(code):
    cursor = None
    conn = None
    conn, cursor = get_conn()
    sql = "select * from current_details where code='%s'"
    cursor.execute(sql, code)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=['代码', '名称', '当前价格', '涨幅', '涨价', '总手',
                                        '换手', '市盈', '当日最高', '当日最低', '今日开盘',
                                        '昨日收盘', '总市值', '流通市值', '市净', '更新时间'])
    close_conn(conn, cursor)
    return df


# 2. 获取当前涨停的所有股票信息
def get_rise_limit():
    cursor = None
    conn = None
    conn, cursor = get_conn()
    sql = "select * from current_details    \
        where code REGEXP '^30' and name not REGEXP '^C' and gains>19.9 \
        or code REGEXP '^00' and gains>9.9  \
        or code REGEXP '^60' and gains>9.9;"
    cursor.execute(sql)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=['代码', '名称', '当前价格', '涨幅', '涨价', '总手',
                                        '换手', '市盈', '当日最高', '当日最低', '今日开盘',
                                        '昨日收盘', '总市值', '流通市值', '市净', '更新时间'])
    if len(df) == 0:
        df = pd.DataFrame([['-', '-', '-', '-', '-', '-', '-',
                            '-', '-', '-', '-', '-', '-', '-',
                            '-', '-']], columns=['代码', '名称', '当前价格', '涨幅',
                                                 '涨价', '总手', '换手', '市盈',
                                                 '当日最高', '当日最低', '今日开盘',
                                                 '昨日收盘', '总市值', '流通市值',
                                                 '市净', '更新时间'])

    close_conn(conn, cursor)
    return df


# 3. 获取当前跌停的所有股票信息
def get_drop_limit():
    cursor = None
    conn = None
    conn, cursor = get_conn()
    sql = "select * from current_details        \
            where code REGEXP '^30' and name not REGEXP '^C' and gains<-19.9     \
            or code REGEXP '^00' and gains<-9.9  \
            or code REGEXP '^60' and gains<-9.9;"
    cursor.execute(sql)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=['代码', '名称', '当前价格', '涨幅', '涨价', '总手',
                                        '换手', '市盈', '当日最高', '当日最低', '今日开盘',
                                        '昨日收盘', '总市值', '流通市值', '市净', '更新时间'])
    if len(df) == 0:
        df = pd.DataFrame([['-', '-', '-', '-', '-', '-', '-',
                            '-', '-', '-', '-', '-', '-', '-',
                            '-', '-']], columns=['代码', '名称', '当前价格', '涨幅',
                                                 '涨价', '总手', '换手', '市盈',
                                                 '当日最高', '当日最低', '今日开盘',
                                                 '昨日收盘', '总市值', '流通市值',
                                                 '市净', '更新时间'])
    close_conn(conn, cursor)
    return df


# 4. 获取大盘涨跌股数
def get_rise_drop_num():
    cursor = None
    conn = None
    conn, cursor = get_conn()
    sql_rise = "select * from current_details where gains>0;"
    sql_drop = "select * from current_details where gains<0;"
    rise_num = cursor.execute(sql_rise)
    drop_num = cursor.execute(sql_drop)

    close_conn(conn, cursor)
    return rise_num, drop_num
