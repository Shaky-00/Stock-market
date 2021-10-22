# 对于某特定股的一些操作函数

def find_index(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1

def check_index(lst, start, end):
    index1 = find_index(lst, 'd', start)
    index2 = find_index(lst, 'd', end)
    if index1 != -1 and index2 != -1:
        return True
    else:
        return False

# 获取某日期区间的所有数据 以dataframe返回
# 预期输入的日期都是开盘日期（！！）
# 调用该函数前可以写一个check_date
def get_interval_data(lst, start_date, end_date):
    start = find_index(lst, 'd', start_date)
    end = find_index(lst, 'd', end_date)
    df = pd.DataFrame(columns = ['日期','开盘价','收盘价','最高价','最低价','成交量'])

    for i in range(start, end+1):
        date = lst[i]['d']
        open_price = lst[i]['o']
        close_price = lst[i]['c']
        high = lst[i]['h']
        low = lst[i]['l']
        vol = lst[i]['v']
        df = df.append([{'日期':date, '开盘价':open_price, '收盘价':close_price, '最高价':high, '最低价':low, '成交量':vol}], ignore_index=True)
    return df

# 获取近n天的所有数据 以dataframe返回
def get_ndays_data(lst, n):
    length = len(lst)
    df = pd.DataFrame()

    for i in range(length-7, length):
        date = lst[i]['d']
        open_price = lst[i]['o']
        close_price = lst[i]['c']
        high = lst[i]['h']
        low = lst[i]['l']
        vol = lst[i]['v']
        df = df.append([{'日期':date, '开盘价':open_price, '收盘价':close_price, '最高价':high, '最低价':low, '成交量':vol}], ignore_index=True)
    return df