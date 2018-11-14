import Result
import GetAndSee
import linecache
import ReadFile
import requests


# 将wxcookie换成需要领取的人的cookie  其中wxcookie为必选
wxcookie1 = {'whid':''}  #自己的
wxcookie2 = {'whid':''}  #胖的
wxcookie3 = {'whid':''}  #垃圾的

print('1：饿了么星选透视')
print('2：饿了么星选领取')
print('3：饿了么星选读文件批量透视，给出当前最大的url，将未领取到最大的url写入文件')
print('4：饿了么星选读文件批量透视')

number = input("输入选择：")
number = int(number)
if number == 1 :
    url = input("请输入url：")
    # 透视
    GetAndSee.seeHB(url,True,wxcookie1)
elif number == 2 :
    url = input("请输入url：")
    whoGet = input("谁领取？  1. 自己  2. 胖  3. 垃圾 >>>")
    whoGet = int(whoGet)
    # 领取
    if whoGet == 1 :
        GetAndSee.getHB(url,wxcookie1)
    elif whoGet == 2 :
        GetAndSee.getHB(url, wxcookie2)
    elif whoGet == 3 :
        GetAndSee.getHB(url, wxcookie3)
    else:
        print("无法识别")
    # 透视
    GetAndSee.seeHB(url,True,wxcookie1)
elif number == 3 :
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
            results = GetAndSee.seeHB(urlLine, False,wxcookie1)
            if results != None:
                luckNumber = results['luckNumber']
                friend_info = results['friends_info']
                friendsNumber = len(friend_info)
                # 只提出 未领取到最大的url
                if friendsNumber < luckNumber:
                    # littleUrl.append(urlLine)
                    # 捆绑信息
                    urlInfo.append(luckNumber)
                    urlInfo.append(friendsNumber)
                    urlInfo.append(urlLine)
                    littleUrl.append(urlInfo)
                    if (friendsNumber == luckNumber-1):
                        print('下一个最大的url有：')
                        print(urlLine)
                        GetAndSee.seeHB(urlLine, True,wxcookie1)


    # 将未领取到最大的url的领取信息写入文件
    with open('littleUrlsINFO.txt', 'w') as  littleUrlFile:
        for urlDict in littleUrl:
            # writeLine =
            littleUrlFile.write(' 最大:'+ str(urlDict[0]))
            littleUrlFile.write(' 已领：'+ str(urlDict[1]))
            littleUrlFile.write(' 链接：'+ urlDict[2])

     # 将未领取到最大的url写入文件
    with open('littleUrls.txt', 'w') as  littleUrlFile:
        for urlDict in littleUrl:
            littleUrlFile.write(urlDict[2])

elif number == 4 :
    filePath = 'starUrls.txt'
    lineNumber = ReadFile.getFileLineNumber(filePath)
    # count 计数 表示行数
    for count in range(1,lineNumber+1):
        # line 某一行的内容
        urlLine = linecache.getline(filePath, count)
        # 过滤不合格的url，比如换行  只领取大于5个字符的url
        if len(urlLine) > 5:
            # 透视 当前line内容为url
            print(urlLine)
            GetAndSee.seeHB(urlLine, True,wxcookie1)


else:
    print('输入无法识别')