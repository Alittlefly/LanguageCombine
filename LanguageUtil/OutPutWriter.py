#! usr/bin/env python3
#coding=utf-8

import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class OutPutWriter:
    def makeOutPutDir(self,dirPath):
        if False == os.path.exists(dirPath):
            os.makedirs(dirPath)

    def write(self, data, fileName):
        outPutPath = self.dirPath + '/' + fileName
        fo = open(outPutPath, 'w',)
        fo.writelines(data)
        fo.close()

class IOSOutPutWriter(OutPutWriter):
    def __init__(self,fileDir):
        self.dirPath = fileDir + '/' + 'iOS'
        self.makeOutPutDir(self.dirPath)


class AndroidOutPutWiter(OutPutWriter):
    def __init__(self,fileDir):
        self.dirPath = fileDir + '/' + 'Android'
        self.makeOutPutDir(self.dirPath)

class WebOutPutWriter(OutPutWriter):
    def __init__(self,fileDir):
        self.dirPath = fileDir + '/' + 'Web'
        self.makeOutPutDir(self.dirPath)