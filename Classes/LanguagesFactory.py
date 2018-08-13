#! user/bin/env python3
#coding=utf-8

from LanguageTester import LanguageCreater

'''
    lkey 是 多语言那栏的key
    keys 是 标题栏的多语言的内容. 
'''
lkey = 'Key'
keys = ['中文', '越南语', '英文', '印尼语', '泰语', '越南语', '马来语'  ,'tester']

'''
    表格导出的csv文件
'''
filePathDir = '/Users/mac/Desktop/Csv_Language/CsvFiles'
'''
    表格转好的文件
'''
CreatedDir = '/Users/mac/Desktop/Csv_Language/Created_Language'
'''
    合并的文件
'''
CombinedDataDir = '/Users/mac/Desktop/Csv_Language/CombineData'






'''
    creater 代码毋需修改
'''
creater = LanguageCreater(lkey, keys)
creater.configCsvFiles(filePathDir)
creater.configCreatedDir(CreatedDir)
creater.configCombinedDataDir(CombinedDataDir)
creater.creatAppUsedFilesWithDirs()
creater.creatCombinefile()