import requests,re,json

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
    try:
        resultdict = json.loads(resultdict)
    except Exception as e:
        print(e)
    error_no = resultdict['error_no']
    if error_no == 4:
        # results['friends_info'] = '当前红包已过期'
        return None
    else:
        resultdict = resultdict['result']
        # 获取到领取的人的信息
        friends_info = resultdict['friends_info']
        results['friends_info'] = friends_info

    share_title = resultdict['share']['share_title']
    pattern = re.compile(r"第(.*?)个领取的人", re.S)
    # 获取的到luckNumber并转为int
    luckNumber = int(re.findall(pattern,share_title)[0])
    results['luckNumber'] = luckNumber
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

