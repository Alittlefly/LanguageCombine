#! usr/bin/env python3
#coding=utf-8

class ResultFormater:
    def __init__(self, languageKey, languageKeys):
        self.lkey = languageKey
        self.languageKeys = languageKeys

    def formatResult(self, keyValues):

        datas = []
        for index in range(0, len(self.languageKeys), 1):
            formatDict = {}
            allKeys = []
            nameKey = self.languageKeys[index]
            outputFileName = self.fileType(nameKey)

            results = []
            for kv in keyValues:

                if not kv.has_key(self.lkey) or not kv.has_key(nameKey):
                    continue

                valueKey = kv[self.lkey]
                value = kv[nameKey]

                if len(value) == 0:
                    # 空值不添加
                    print('enptyValue :' + valueKey + '  ' + nameKey)
                    continue

                shouldUseIndex = False

                if len(valueKey) == 0 or allKeys.__contains__(valueKey):
                    shouldUseIndex = True

                index = list(keyValues).index(kv)
                if shouldUseIndex == False:
                    # 只包含数字
                    newKey = valueKey
                    if str(valueKey).isdigit():
                        newKey = 'key_' + str(valueKey);
                    # result = self.formatStr(newKey, value)
                else:
                    if len(valueKey) == 0:
                        newKey = 'NoneKey_Error_MustChange' + str(index)
                        print(newKey)
                    else:
                        newKey = valueKey + '_' + str(index)
                        print('newKey :' + newKey)

                newKey = newKey.strip().replace(' ', '').replace('\n', '').replace('\t', '')

                result = self.formatStr(newKey, value)

                results.append(result)

                if allKeys.__contains__(valueKey) == False:
                    allKeys.append(valueKey)


            formatDict['name'] = outputFileName
            formatDict['data'] = results
            datas.append(formatDict)
        return  datas

    def fileType(self,key):
        return ""

    def formatStr(self, key, value):
        return ""

class iOSResultFormater(ResultFormater):

    def fileType(self, key):
        return key + '.strings'

    def formatStr(self, key, value):
        return str(key) + ' = "' + str(value) + '";' + '\n'

class AndroidResultFormater(ResultFormater):

    def fileType(self, key):
        return key + '.xml'
    def formatStr(self, key, value):
        return '<string name = "' + str(key) + '">' + str(value) + '</string>' + '\n'

class WebResultFormater(ResultFormater):

    def fileType(self,key):
        return key + '.properties'

    def formatStr(self, key, value):
        return  str(key) + ' = ' + str(value) + '\n'