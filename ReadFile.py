import linecache


# 获取文件行数
def getFileLineNumber(filePath):
    fileLineNumber = len(linecache.getlines(filePath))
    return fileLineNumber

if __name__ == '__main__':
    # 读文件获取特定行
    filePath = 'starUrls.txt'
    line = linecache.getline(filePath, 5)
    # print(linecache.getlines(filePath))
