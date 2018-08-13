#! usr/bin/env python3
#coding=utf-8

import csv

class CsvReader:
    def __init__(self,filePath):
        self.path = filePath


    def fileInfos(self):
        fileInfo = []
        with open(self.path,'r') as f:
            dictReader = csv.DictReader(f)
            for row in dictReader:
                fileInfo.append(row)
        return fileInfo

