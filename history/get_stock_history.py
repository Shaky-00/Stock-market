# 单股历史数据分析
import requests
import re
import json
import pandas as pd

if __name__=='__main__':
    code = "********" # 此处code需要加上前面两个字母例如'sh'/'sz'
    url = "https://quotes.sina.cn/cn/api/jsonp.php/var%20_{}{}=/KC_MarketDataService.getKLineData?symbol={}".format(code,code,code)
    r = requests.get(url)
    r.encoding = 'utf-8'

    replace_str = "/*<script>location.href=\'//sina.com\';</script>*/\nvar _{}{}=(".format(code, code)
    content = r.text.replace(replace_str, "")
    content = content.replace(");","")
    history_dict = json.loads(content)

    # 获取某时间段的全部数据
    start_date = "XXXX-XX-XX"
    end_date = "XXXX-XX-XX"
    if check_index(history_dict, start_date, end_date):
        df_1 = get_interval_data(history_dict, start, end)
    
    # 获取近n天的全部数据
    n = 7
    df_2 = get_ndays_data(history_dict, n)