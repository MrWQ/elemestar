import linecache
import os
import GetAndSee


# 将wxcookie换成需要领取的人的cookie  其中wxcookie为必选
wxcookie1 = {'whid': '0%3D', 'flag': '自己'} #自己的

wxcookie = []
wxcookie.append(wxcookie0)
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
    GetAndSee.getHB(url, wxcookie7['whid'])
elif number == 2:
    who = ''
    for counter in range(len(wxcookie)):
        who = who + str(counter) + '.' + wxcookie[counter]['flag'] + '  '
    whoGet = input("谁领取？ " + who + '>>>')
    whoGet = int(whoGet)
    # 领取
    if whoGet >=0 and whoGet < len(wxcookie):
        url = input("请输入url：")
        GetAndSee.getHB(url, wxcookie[whoGet]['whid'])
    else:
        print("无法识别")
elif number == 3:
    file_path = 'starUrls.txt'
    little_urls = []  # 统计未领取到最大的url，写入文件时用
    little_urls_info = []    # 统计未领到最大的url 和 领取信息
    url_list = linecache.getlines(file_path)
    # 去重复
    formatList = []
    for url in url_list:
        if url not in formatList:
            formatList.append(url)
        url_list = formatList
    for url in url_list:
        if len(url) > 5:
            url = url.replace('\n', '')
            url = url.replace('\t', '')
            url = url.replace('\r', '')
            results = GetAndSee.getHB(url, wxcookie7['whid'])
            if results:
                if int(results['luck_number']) > int(results['friends_number']):
                    little_urls.append(url)
                    little_urls_info.append(results)
    # 获取当前文件夹路径
    currentPath = os.path.dirname(os.path.realpath(__file__))
    # 将未领取到最大的url的领取信息写入文件
    with open(currentPath + '/littleUrlsINFO.txt', 'w') as little_url_info_file:
        for url_info in little_urls_info:
            little_url_info_file.write(str(url_info) + '\n')
     # 将未领取到最大的url写入文件
    filePath2 = currentPath + '/' + file_path
    with open(filePath2, 'w') as little_url_file:
        for url in little_urls:
            little_url_file.write(str(url) + '\n')

else:
    print('输入无法识别')