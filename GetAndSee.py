import json
import re

import pandas as pd
import requests

headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 8.1; PACM00 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044306 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070336) NetType/WIFI Language/zh_CN Process/tools'}


# 从响应头获取cookie
def get_WMID(header):
    set_cookie  = header['Set-Cookie']
    pattern = re.compile(r'WMID=(.*?);', re.S)
    list = re.findall(pattern, set_cookie)
    for i in list:
        if i:
            return i


def getHB(url, wxcookie):
    if '?' in url:
        try:
            url_type = str(url.split('?')[1])
        except:
            print('链接切割失败，获取链接参数失败')
            return None
    else:
        url_type = url
    url = 'https://star.ele.me/hongbao/wpshare?display=json&' + url_type
    url = url.replace("'", '')
    url = url.replace('{', '')
    url = url.replace('}', '')
    # 构造领取cookie
    WXcookie = {'WMID': '', 'whid': ''}
    WXcookie['whid'] = wxcookie
    s = requests.session()
    re2 = s.post(url=url, headers=headers, cookies=WXcookie)
    WXcookie['WMID'] = get_WMID(re2.headers)
    re2 = s.post(url=url, headers=headers, cookies=WXcookie)
    # 此处重构，json解析
    results_html = re2.content.decode('unicode_escape')
    results_html = results_html.replace('"{', '{')
    results_html = results_html.replace('}"', '}')
    results = json.loads(results_html)
    try:
        error_msg = results['result']['msg']
    except:
        error_msg = results['error_msg']
    if len(results['result']) > 8:
            pattern = re.compile(r"第(.*?)个领取的人", re.S)
            luck_number = re.findall(pattern, results['result']['share']['share_title'])[0]
            try:
                friend_info = results['result']['friends_info']
            except:
                print(error_msg)
                return None
            friends_number = len(friend_info)
            print("信息如下：", "最佳位置：", luck_number, '已领人数：', friends_number)
            fri_info = []
            for friend in friend_info:
                hb_info = {}
                hb_info['username'] = friend['username']
                hb_info['amount'] = friend['amount']
                hb_info['is_luck'] = friend['is_luck']
                hb_info['date'] = friend['date']
                fri_info.append(hb_info)
            pad = pd.DataFrame(fri_info, columns=['date', 'is_luck', 'amount', 'username'])
            print(pad)
            print("最佳位置：", luck_number, '已领人数：', friends_number)
            print(error_msg, '\n')
            ret = {}
            ret['luck_number'] = luck_number
            ret['friends_number'] = friends_number
            ret['url'] = url
            return ret


