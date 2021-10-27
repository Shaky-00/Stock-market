import pandas as pd
from connect import get_conn, close_conn
import tools


def get_stocks():
    conn, cursor = get_conn()
    sql = "select * from current_details"
    cursor.execute(sql)
    results = cursor.fetchall()
    data = pd.DataFrame(results, columns=['代码', '名称', '当前价格', '涨幅', '涨价', '总手',
                                          '换手', '市盈', '当日最高', '当日最低', '今日开盘',
                                          '昨日收盘', '总市值', '流通市值', '市净', '更新时间'])
    close_conn(cursor, conn)
    return data


if __name__ == "__main__":
    # 获取当前大盘全部信息
    df = get_stocks()

    # 操作区...
    # example
    stock_detail = tools.get_stock_info(600000)
    print(stock_detail)

    rise_num, drop_num = tools.get_rise_drop_num()
    print("当前涨的股票有{}支".format(rise_num))
    print("当前跌的股票有{}支".format(drop_num))
