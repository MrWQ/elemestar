import linecache
import os

import GetAndSee
import GetAndSee
import ReadFile

# 将wxcookie换成需要领取的人的cookie  其中wxcookie为必选
wxcookie7 = {'whid':'%3D'} #自己的


wxcookie = []
wxcookie.append([0])
wxcookie.append(wxcookie1)
wxcookie.append(wxcookie2)
wxcookie.append(wxcookie3)
wxcookie.append(wxcookie4)
wxcookie.append(wxcookie5)
wxcookie.append(wxcookie6)
wxcookie.append(wxcookie7)

print('1：饿了么星选领取来透视')
print('2：饿了么星选领取')
print('3：饿了么星选读文件批量透视')

number = input("输入选择：")
number = int(number)
if number == 1:
    url = input("请输入url：")
    GetAndSee.getHB(url, wxcookie7, True)
elif number == 2:
    url = input("请输入url：")
    whoGet = input("谁领取？  1. 自己   2. 垃圾   3. 胖    4.二   5.三的  6.立神  7.翻译>>>")
    whoGet = int(whoGet)
    # 领取
    if whoGet >0 and whoGet <8:
        GetAndSee.getHB(url, wxcookie[whoGet], True)
    else:
        print("无法识别")
elif number == 3:
    filePath = 'starUrls.txt'
    lineNumber = ReadFile.getFileLineNumber(filePath)
    littleUrl = []  #统计未领取到最大的url，写入文件时用
    # count 计数 表示行数
    for count in range(1,lineNumber+1):
        urlInfo = []  #捆绑信息，将最大数，朋友数目，url捆绑起来
        # line 某一行的内容
        urlLine = linecache.getline(filePath, count)
        # 过滤不合格的url，比如换行  只领取大于5个字符的url
        if len(urlLine) > 5:
            # 透视 当前line内容为url
            results = GetAndSee.getHB(urlLine, wxcookie7, False)
            if results != None:
                try:
                    luckNumber = int(results['luckNumber'])
                except:
                    print('最佳手气数字转换为int失败')
                friend_info = results['friends_info']
                friendsNumber = len(friend_info)
                # 只提出 未领取到最大的url
                if friendsNumber < luckNumber:
                    # 捆绑信息
                    urlInfo.append(luckNumber)
                    urlInfo.append(friendsNumber)
                    urlInfo.append(urlLine)
                    littleUrl.append(urlInfo)
                    # 去重复
                    formatList = []
                    for id in littleUrl:
                        if id not in formatList:
                            formatList.append(id)
                    littleUrl = formatList

    # 获取当前文件夹路径
    currentPath = os.path.dirname(os.path.realpath(__file__))

    # 将未领取到最大的url的领取信息写入文件
    with open(currentPath + '\\' + 'littleUrlsINFO.txt', 'w') as littleUrlFile:
        for urlDict in littleUrl:
            # writeLine =
            littleUrlFile.write(' 最大:'+ str(urlDict[0]))
            littleUrlFile.write(' 已领：'+ str(urlDict[1]))
            littleUrlFile.write(' 链接：'+ urlDict[2])

     # 将未领取到最大的url写入文件
    filePath2 = currentPath + '\\' +filePath
    with open(filePath2, 'w') as  littleUrlFile:
        for urlDict in littleUrl:
            littleUrlFile.write(urlDict[2])

else:
    print('输入无法识别')