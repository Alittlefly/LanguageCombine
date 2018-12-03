#! usr/bin/env python3
#coding=utf-8

import xlrd

class FileReader:
    def __init__(self):
        pass

class MyExcelReader(FileReader):
    def __init__(self,path):
        self.filePath = path

    def readExcel(self):
        tupleInfos = []

        workbook = xlrd.open_workbook(self.filePath)
        names = workbook.sheet_names()
        for name in names:
            keyValues = []
            sheet = workbook.sheet_by_name(name)
            sheetKeys = sheet.row_values(0)
            # 有效列 即Key的长度
            sheetRowCount = sheet.nrows
            sheetColConnt = sheet.ncols

            print(name)
            # 读取每行的数据
            for row in range(1,sheetRowCount,1):
                rowValues = sheet.row_values(row);
                keyValue = {}

                for col in range(0, sheetColConnt, 1):
                    key = str(sheetKeys[col]).encode('utf-8')
                    value = str(rowValues[col]).encode('utf-8')
                    keyValue[key] = value

                keyValues.append(keyValue)
            # print(keyValues)
            name = str(name).encode('utf-8')
            tupleInfos.append((keyValues, name))
        return tupleInfos

if __name__ == '__main__':
    path = '/Users/mac/Desktop/excels/aaa.xlsx'
    reader = MyExcelReader(path)
    infos = reader.readExcel()
    print(infos)