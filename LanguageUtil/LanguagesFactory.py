#! user/bin/env python3
#coding=utf-8

from LanguageTester import LanguageCreater

'''
    lkey 是 多语言那栏的key
    keys 是 标题栏的多语言的内容. 
'''
lkey = 'Key'
# keys = ['中文', '越南语', 'English', '印尼语', '泰语', '越南语', '马来语']
keys = ['中文', '越南语', 'English', '印尼语', '泰语', '越南语', '马来语' ,'Hindi' ,'Bengali','Telugu', 'Tamil', 'Turkish', 'Arabic']


'''
    表格导出的csv文件
'''
# filePathDir = '/Users/mac/Desktop/Csv_Language/CsvFiles'
# filePathDir = '/Users/mac/Desktop/NewLanguage/CsvFiles'
# filePathDir = '/Users/mac/Desktop/nnn/Csvfiles'
# filePathDir = '/Users/mac/Desktop/Arabic/CreatedLanguage'
# filePathDir = '/Users/mac/Desktop/excels'
filePathDir = '/Users/mac/Documents/Svn/V1.2版本/文案（阿语及精简）'

# filePathDir = testPathDir
'''
    表格转好的文件
'''
# CreatedDir = '/Users/mac/Desktop/Csv_Language/Created_Language'
# CreatedDir = '/Users/mac/Desktop/NewLanguage/Created_Language'
CreatedDir = '/Users/mac/Desktop/nnn/Created_Language'

# CreatedDir = testCreatedDir

'''
    合并的文件
'''
# CombinedDataDir = '/Users/mac/Desktop/Csv_Language/CombineData'
# CombinedDataDir = '/Users/mac/Documents/Svn/Ready产品空间/V1.0版本/文案/CombineData'
# CombinedDataDir = '/Users/mac/Desktop/NewLanguage/CombineData'
# CombinedDataDir = '/Users/mac/Documents/Svn/Ready产品空间/V1.1版本/文案/CombineData'
# CombinedDataDir = '/Users/mac/Documents/Svn/V1.2版本/文案/CombineData'
# CombinedDataDir = '/Users/mac/Documents/Svn/V1.2版本/文案（土语）/CombineData'
CombinedDataDir = '/Users/mac/Documents/Svn/V1.2版本/文案（阿语及精简）/CombineData'

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



