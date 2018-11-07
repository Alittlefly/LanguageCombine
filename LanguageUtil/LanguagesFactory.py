#! user/bin/env python3
#coding=utf-8

from LanguageTester import LanguageCreater

'''
    lkey 是 多语言那栏的key
    keys 是 标题栏的多语言的内容. 
'''
lkey = 'Key'
keys = ['中文', '越南语', '英文', '印尼语', '泰语', '越南语', '马来语' ]

'''
    表格导出的csv文件
'''
# filePathDir = '/Users/mac/Desktop/Csv_Language/CsvFiles'
filePathDir = '/Users/mac/Desktop/NewLanguage'

testPathDir = './../Ready'

# filePathDir = testPathDir
'''
    表格转好的文件
'''
# CreatedDir = '/Users/mac/Desktop/Csv_Language/Created_Language'
CreatedDir = '/Users/mac/Desktop/NewLanguage/Created_Language'
testCreatedDir = './../ReadyCreated'

# CreatedDir = testCreatedDir

'''
    合并的文件
'''
CombinedDataDir = '/Users/mac/Desktop/Csv_Language/CombineData'
# CombinedDataDir = '/Users/mac/Documents/Svn/Ready产品空间/V1.0版本/文案/CombineData'
# CombinedDataDir = '/Users/mac/Desktop/NewLanguage/CombineData'
CombinedDataDir = '/Users/mac/Documents/Svn/Ready产品空间/V1.1版本/文案/CombineData'
testCombinedDir = './../ReadyCombineData'

# CombinedDataDir = testCombinedDir


class lanugagefac:
    def create(self):
        '''
            creater 代码毋需修改
        '''
        creater = LanguageCreater(lkey, keys)
        creater.configCsvFiles(filePathDir)
        creater.configCreatedDir(CreatedDir)
        creater.configCombinedDataDir(CombinedDataDir)
        creater.creatAppUsedFilesWithDirs()
        creater.creatCombinefile()



