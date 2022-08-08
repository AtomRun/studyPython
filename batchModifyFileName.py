# -*- coding:utf-8 -*-

import os

def modifyFile(dirPath,replaceName,toReplaceName):
    dir = os.walk(dirPath)
    for path,dirList,fileList in dir:
        for fileName in fileList:
            oldFile = os.path.join(path,fileName)
            if replaceName in oldFile:
                newFile = os.path.join(path,fileName.replace(replaceName,toReplaceName))
                if os.path.isfile(oldFile):
                    os.rename(oldFile,newFile)

if __name__=='__main__':
    path = input('请输入路径')
    replaceName = input('请输入需要替换的字符')
    toReplaceName = input('请输入替换为的字符')
    fileDir = 'r'+path
    modifyFile(path,replaceName,toReplaceName)
    print('完成!')