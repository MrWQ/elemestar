import json
import re


# 从返回的html中正则出result字典
def getResultDict(html):
    results = {'luckNumber':'','friends_info':''}
    pattern = re.compile(r"<script (.*?)</script></html>",re.S)
    resultdict = re.findall(pattern,html)
    # print(resultdict)
    pattern = re.compile(r"init(.*?);\n",re.S)
    resultdict = re.findall(pattern,resultdict[0])
    resultdict = resultdict[1]

    length = len(resultdict)
    resultdict = resultdict[1:length - 1]
    resultdict = resultdict.replace('","conflict_activity"', ',"conflict_activity"')
    resultdict = resultdict.replace('"use_condition":"', '"use_condition":')
    try:
        resultdict = json.loads(resultdict)
    except Exception as e:
        print(e)
    error_no = resultdict['error_no']
    if error_no == 20007:
        error_msg = resultdict['error_msg']
    elif error_no == 0:
        error_msg = resultdict['result']['msg']
    # 对于出错代号的处理
    # error_no == 0 表示正确 4表示红包过期
    if error_no == 3 or error_no == 4 or error_no == 5555:
        error_msg = '红包已过期'
        return None
    else:
        try:
            resultdict = resultdict['result']
            # 获取到领取的人的信息
            friends_info = resultdict['friends_info']
            results['friends_info'] = friends_info
        except:
            print("Result.py：代号出错，应该是更改了")

    share_title = resultdict['share']['share_title']
    pattern = re.compile(r"第(.*?)个领取的人", re.S)
    luck_temp_number = re.findall(pattern,share_title)[0]
    if '~' in luck_temp_number:
        luck_temp_number = luck_temp_number.split('~')[0]
    else:
        pass
    luckNumber = luck_temp_number
    # # 获取的到luckNumber并转为int
    # luckNumber = int(luck_temp_number)
    results['luckNumber'] = luckNumber
    results['error_msg'] = error_msg
    # 返回字典
    return results

# 从响应头获取cookie
def get_WMID(header):
    set_cookie  = header['Set-Cookie']
    pattern = re.compile(r'WMID=(.*?);', re.S)
    list = re.findall(pattern, set_cookie)
    for i in list:
        if i:
            return i
# 从响应头获取cookie
def get_WMST(header):
    set_cookie  = header['Set-Cookie']
    pattern = re.compile(r'WMST=(.*?);', re.S)
    list = re.findall(pattern, set_cookie)
    for i in list:
        if i:
            return i

# 提取有效url
# def get_URL(urls):
#     pattern = re.compile(r'\?(.*?)https', re.S)
#     list = re.findall(pattern, urls)
#     if len(list)>1:
#         for i in list:
#             if i:
#                 return i
#     else:
#         return list

# if __name__=='__main__':

