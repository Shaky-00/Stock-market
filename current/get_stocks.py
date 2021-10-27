import requests
import json
import pandas as pd


def get_stocks(page):
    url = "http://42.push2.eastmoney.com/api/qt/clist/get?  \
            cb=jQuery11240574199433107409_1590886830210&pn={0}    \
            &pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2 \
            &invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&   \
            fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,  \
            f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152 \
            &_=1590886830256".format(page)
    r = requests.get(url)
    r.encoding = 'utf-8'
    content = r.text.replace("jQuery11240574199433107409_   \
                                1590886830210", "")
    content = content.replace(";", "")
    content = content[1:-1]
    content_dict = json.loads(content)

    size = len(content_dict.get('data').get('diff'))
    data_new = pd.DataFrame()
    for i in range(size):
        code = content_dict.get('data').get('diff')[i].get('f12')
        name = content_dict.get('data').get('diff')[i].get('f14')
        current_price = content_dict.get('data').get('diff')[i].get('f2')
        gains = content_dict.get('data').get('diff')[i].get('f3')
        increase_price = content_dict.get('data').get('diff')[i].get('f4')
        vol = content_dict.get('data').get('diff')[i].get('f5')
        turn_over = content_dict.get('data').get('diff')[i].get('f8')
        PE = content_dict.get('data').get('diff')[i].get('f9')
        high = content_dict.get('data').get('diff')[i].get('f15')
        low = content_dict.get('data').get('diff')[i].get('f17')
        t_open = content_dict.get('data').get('diff')[i].get('f16')
        y_close = content_dict.get('data').get('diff')[i].get('f18')
        total_market = content_dict.get('data').get('diff')[i].get('f20')
        current_market = content_dict.get('data').get('diff')[i].get('f21')
        PBR = content_dict.get('data').get('diff')[i].get('f23')
        data_new = data_new.append([[code, name, current_price, gains,
                                   increase_price, vol, turn_over, PE,
                                   high, low, t_open, y_close,
                                   total_market, current_market, PBR]],
                                   ignore_index=True)
    return data_new
