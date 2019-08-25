import requests

import Result

headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 8.1; PACM00 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044306 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070336) NetType/WIFI Language/zh_CN Process/tools'}


# 透视
# def seeHB(url,printInfo,wxcookie):
#     s = requests.session()
#     re2 = s.post(url=url, headers=headers, cookies=wxcookie)
#
#     resultHtml = re2.content.decode('unicode_escape')
#     # resultHtml = re2.content.decode()
#
#     results = Result.getResultDict(resultHtml)
#     if results != None:
#         # 如果标志位为ture 打印信息
#         if printInfo == True:
#             luckNumber = results['luckNumber']
#             friend_info =  results['friends_info']
#             friendsNumber = len(friend_info)
#             print('最佳手气位置：' ,luckNumber)
#             print("当前已领取人数：" ,friendsNumber)
#             print("朋友信息如下：")
#             print('姓名'.rjust(10) ,'红包'.rjust(20))
#             for friend in friend_info:
#                 # print(friend)
#                 print(friend['username'].rjust(10) ,str(friend['amount']).rjust(20))
#         else:
#             return results
#     else:
#         print('当前红包已过期')
#         return  None
#     领取
def getHB(url, wxcookie, printInfo):
    # 构造领取cookie
    WXcookie = {'WMID': '',
                'whid': '',
                'WMST': ''
                }
    s = requests.session()
    re2 = s.post(url=url, headers=headers, cookies=wxcookie)
    WXcookie['WMID'] = Result.get_WMID(re2.headers)
    WXcookie['WMST'] = Result.get_WMST(re2.headers)
    WXcookie['whid'] = wxcookie['whid']
    # 领取
    re2 = s.post(url=url, headers=headers, cookies=WXcookie)
    resultHtml = re2.content.decode('unicode_escape')
    results = Result.getResultDict(resultHtml)
    if results != None:
#         # 如果标志位为ture 打印信息
        if printInfo == True:
            luckNumber = results['luckNumber']
            friend_info =  results['friends_info']
            error_msg = results['error_msg']
            friendsNumber = len(friend_info)
            print('最佳手气位置：' ,luckNumber)
            print("当前已领取人数：" ,friendsNumber)
            print("朋友信息如下：")
            print('姓名'.rjust(10) ,'红包'.rjust(20))
            for friend in friend_info:
                print(friend['username'].rjust(10) ,str(friend['amount']).rjust(20))
            print(error_msg)
        else:
            return results
    else:
        print('当前红包已过期,获取红包信息失败')
        return None

