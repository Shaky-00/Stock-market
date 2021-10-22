# 更新details函数
def update_details():
    cursor = None
    conn = None
    try:
        for page in range(250):
            new = get_stocks(page)
            data = data.append(new, ignore_index=True)
        li = data
        conn, cursor = get_conn()
        sql = "insert into current_details(code,name,current_price,gains,increase_price,vol,turn_over,PE,high,low,t_open,y_close,total_market,current_market,PBR) \
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute("TRUNCATE TABLE current_details")
        print(f"{time.asctime()}开始更新数据")
        for item in li.iloc:
            cursor.execute(sql, item.tolist())
        conn.commit()
        print(f"{time.asctime()}已更新最新数据")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)