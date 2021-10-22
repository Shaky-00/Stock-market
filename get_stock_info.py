# 获取代码为code的股票行情信息
def get_stock_info(code):
    cursor = None
    conn = None
    try:
        conn, cursor = get_conn()
        sql = "select * from current_details where code='%d'"
        cursor.execute(sql, code)
        results = cursor.fetchall()
        df = pd.DataFrame(results, columns=['代码','名称','当前价格','涨幅', '涨价','总手','换手','市盈',
                            '当日最高','当日最低','今日开盘','昨日收盘','总市值','流通市值','市净'])
        return df
    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)