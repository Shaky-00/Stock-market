import requests
import re
import json
import pandas as pd

def get_stocks(page):
    url = "http://42.push2.eastmoney.com/api/qt/clist/get?cb=jQuery11240574199433107409_1590886830210&pn={0}&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1590886830256".format(page)
    r = requests.get(url)
    r.encoding = 'utf-8'
    content = r.text.replace("jQuery11240574199433107409_1590886830210", "")
    content = content.replace(";", "")
    content = content[1:-1]
    content_dict = json.loads(content)
    
    try:
        size = len(content_dict.get('data').get('diff'))
        data_new = pd.DataFrame(columns=['代码','名称','当前价格','涨幅', '涨价','总手','换手','市盈',
                            '当日最高','当日最低','今日开盘','昨日收盘','总市值','流通市值','市净'])
        for i in range(size):
            code = content_dict.get('data').get('diff')[i].get('f12')
            name = content_dict.get('data').get('diff')[i].get('f14')
            current_price = content_dict.get('data').get('diff')[i].get('f2') # 当前价格
            gains = content_dict.get('data').get('diff')[i].get('f3') # 涨幅
            increase_price = content_dict.get('data').get('diff')[i].get('f4') # 涨的价格
            vol = content_dict.get('data').get('diff')[i].get('f5') # 总手
#             price = content_dict.get('data').get('diff')[i].get('f6') # 价格
            turn_over = content_dict.get('data').get('diff')[i].get('f8') # 换手
            PE = content_dict.get('data').get('diff')[i].get('f9') # 市盈
            high = content_dict.get('data').get('diff')[i].get('f15') # 当日最高
            low = content_dict.get('data').get('diff')[i].get('f17') # 当日最低
            t_open = content_dict.get('data').get('diff')[i].get('f16') # 今日开盘
            y_close = content_dict.get('data').get('diff')[i].get('f18') # 昨日收盘
            total_market = content_dict.get('data').get('diff')[i].get('f20') # 总市值
            current_market = content_dict.get('data').get('diff')[i].get('f21') # 流通市值
            PBR = content_dict.get('data').get('diff')[i].get('f23') # 市净
            
            data_new = data_new.append([{"代码":code, "名称":name, "当前价格":current_price, "涨幅":gains,
                                        "涨价":increase_price, "总手":vol, "换手":turn_over, "市盈":PE, 
                                        "当日最高":high, "当日最低":low, "今日开盘":t_open, "昨日收盘":y_close,
                                        "总市值":total_market, "流通市值":current_market, "市净":PBR}], ignore_index=True)
        return data_new
    except:
        pass
    
    
data = pd.DataFrame(columns=['代码','名称','当前价格','涨幅', '涨价','总手','换手','市盈',
                            '当日最高','当日最低','今日开盘','昨日收盘','总市值','流通市值','市净'])
for page in range(250):
    new = get_stocks(page)
    data = data.append(new, ignore_index=True)