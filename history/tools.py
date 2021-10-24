import pandas as pd
import matplotlib.pyplot as plt
import mpl_finance as mpf
import matplotlib.ticker as ticker

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


def manage(df):
    df.loc[:, '涨跌'] = 0
    df['开盘价'] = df['开盘价'].astype('float')
    df['收盘价'] = df['收盘价'].astype('float')
    df['最高价'] = df['最高价'].astype('float')
    df['最低价'] = df['最低价'].astype('float')
    df['成交量'] = df['成交量'].astype('int')
    df['涨跌'] = df['涨跌'].astype('float')

    df['涨跌'] = df['收盘价'] - df.shift(1)['收盘价']
    return df

# 获取某日期区间的所有数据 以dataframe返回
# 预期输入的日期都是开盘日期（！！）
# 调用该函数前可以写一个check_date


def get_interval_data(lst, start_date, end_date):
    start = find_index(lst, 'd', start_date)
    end = find_index(lst, 'd', end_date)
    df = pd.DataFrame(columns=['日期', '开盘价', '收盘价', '最高价', '最低价', '成交量'])

    for i in range(start-1, end+1):
        date = lst[i]['d']
        open_price = lst[i]['o']
        close_price = lst[i]['c']
        high = lst[i]['h']
        low = lst[i]['l']
        vol = lst[i]['v']
        df = df.append([{'日期': date, '开盘价': open_price, '收盘价': close_price,
                       '最高价': high, '最低价': low, '成交量': vol}], ignore_index=True)
        df = manage(df)
    return df[1:]

# 获取近n天的所有数据 以dataframe返回


def get_ndays_data(lst, n):
    length = len(lst)
    df = pd.DataFrame()

    for i in range(length-n-1, length):
        date = lst[i]['d']
        open_price = lst[i]['o']
        close_price = lst[i]['c']
        high = lst[i]['h']
        low = lst[i]['l']
        vol = lst[i]['v']
        df = df.append([{'日期': date, '开盘价': open_price, '收盘价': close_price,
                       '最高价': high, '最低价': low, '成交量': vol}], ignore_index=True)
        df = manage(df)
    return df[1:]


def drawBarChart_vol(df, n):
    date = df['日期'].to_list()
    vol = df['成交量'].to_list()
    positive = df['涨跌'] > 0

    # 对中文编码做处理
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.bar(date, vol, color=df['positive'].map({True: 'g', False: 'r'}))
    plt.title('个股{}日成交量统计'.format(n))
    plt.show()

# 绘制个股K线、均线以及成交量柱状图


def drawStockInfo(df, n):
    figure, (axPrice, axVol) = plt.subplots(2, sharex=True, figsize=(15, 8))
    # K线与均线
    mpf.candlestick2_ochl(ax=axPrice, opens=df['开盘价'], closes=df['收盘价'],
                          highs=df['最高价'], lows=df['最低价'],
                          width=0.75, colorup='red', colordown='green')
    axPrice.set_title("个股K线图和均线")

    if n <= 10:
        axPrice.plot(df['收盘价'].rolling(window=5).mean(),
                     color="red", label="3天均线")
    if n >= 10:
        axPrice.plot(df['收盘价'].rolling(window=5).mean(),
                     color="red", label="5天均线")
    if n >= 15:
        axPrice.plot(df['收盘价'].rolling(window=10).mean(),
                     color="blue", label="10日均线")
    if n >= 25:
        axPrice.plot(df['收盘价'].rolling(window=20).mean(),
                     color="orange", label="20日均线")

    axPrice.legend(loc='best')
    axPrice.set_ylabel("价格（单位：元）")
    axPrice.set_ylim(df['最低价'].min(), df['最高价'].max())
    axPrice.grid(True)
    # 交易量图
    for index, row in df.iterrows():
        if row['涨跌'] > 0:
            axVol.bar(row['日期'], row['成交量']/1000000, width=0.5, color='green')
        else:
            axVol.bar(row['日期'], row['成交量']/1000000, width=0.5, color='red')
    axVol.set_ylabel("成交量（单位：亿手）")
    axVol.set_title("个股成交量")
    axVol.set_ylim(0, df['成交量'].max()/1000000*1.2)
    axVol.xaxis.set_major_locator(ticker.MultipleLocator(5))
    axVol.grid(True)
    for xtick in axVol.get_xticklabels():
        xtick.set_rotation(30)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show
