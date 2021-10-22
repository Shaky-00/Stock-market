import requests
import re
import json
import pandas as pd
import pymysql
import time

# 更新details函数
def update_details():
    cursor = None
    conn = None
    try:
        data = pd.DataFrame()
        for page in range(250):
            new = get_stocks(page)
            data = data.append(new, ignore_index=True)
        li = data
        li.replace(to_replace='-', value=0, inplace=True)

        conn, cursor = get_conn()
        sql = "insert into current_details(code,name,current_price,gains,increase_price,vol,turn_over,PE,high,low,t_open,y_close,total_market,current_market,PBR,update_time) \
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute("TRUNCATE TABLE current_details")
        update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"{time.asctime()}开始更新数据")
        for item in li.iloc:
            tmp = item.tolist()
            tmp.append(update_time)
            cursor.execute(sql, tmp)
        conn.commit()
        print(f"{time.asctime()}已更新最新数据")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)

if __name__ == "__main__":
    update_details()