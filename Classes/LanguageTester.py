#! user/bin/env python3
#coding=utf-8

import os
from Csv_Reader import CsvReader
from OutPutWriter import IOSOutPutWriter
from OutPutWriter import AndroidOutPutWiter
from OutPutWriter import WebOutPutWriter

from ReusltFormater import iOSResultFormater
from ReusltFormater import AndroidResultFormater
from ReusltFormater import WebResultFormater


class LanguagePaths:
    def filepaths(self, list_name, path):
        for file in os.listdir(path):
            file = os.path.join(path,file)
            if os.path.isdir(file):
                self.filepaths(list_name,file)
            else:
                list_name.append(file)


class LanguageCreater:
    def __init__(self,lkey,keys):
        self.lkey = lkey
        self.keys = keys

    def configCreatedDir(self, createddir):
        self.createddir = createddir

    def configCsvFiles(self, filePathDir):
        self.filePathDir = filePathDir

    def configCombinedDataDir(self, combinedDataDir):
        self.combinedDataDir = combinedDataDir



    def createAppUsedLanguageFile(self,filePath):
        fileName = os.path.basename(filePath)
        fileDir = os.path.splitext(fileName)
        fileNameWithoutExt = fileDir[0]
        OutPutDir = self.createddir + '/' + fileNameWithoutExt

        reader = CsvReader(filePath)
        print('start :' + filePath)
        keyValues = reader.fileInfos()

        lkey = self.lkey
        keys = self.keys

        print('--------------------ios-------------------------')
        iosFormater = iOSResultFormater(lkey, keys)
        iosWriter = IOSOutPutWriter(OutPutDir)
        iosReuslts = iosFormater.formatResult(keyValues)
        for dict in iosReuslts:
            data = dict['data']
            name = dict['name']
            iosWriter.write(data, name)

        print('--------------------android---------------------')
        androidFromater = AndroidResultFormater(lkey, keys)
        androidResults = androidFromater.formatResult(keyValues)
        androidWriter = AndroidOutPutWiter(OutPutDir)

        for dict in androidResults:
            data = dict['data']
            name = dict['name']
            androidWriter.write(data, name)

        print('--------------------web-------------------------')

        webFromater = WebResultFormater(lkey, keys)
        webResults = webFromater.formatResult(keyValues)
        webWriter = WebOutPutWriter(OutPutDir)

        for dict in webResults:
            data = dict['data']
            name = dict['name']
            webWriter.write(data, name)

    def creatAppUsedFilesWithDirs(self):
        CsvFiles = []
        LanguagePaths().filepaths(CsvFiles,self.filePathDir)
        for path in CsvFiles:
            if path.endswith('.csv'):
                self.createAppUsedLanguageFile(path)

    def groupsPaths(self, paths, ext):
        group = []
        for path in paths:
            if path.endswith(ext):
                group.append(path)
        return group

    def makecombinefile(self, filepaths, combineOutPutPath, ext):

        keypaths = {}

        for filepath in filepaths:
            filename = os.path.basename(filepath)
            filenamekey = os.path.splitext(filename)[0]

            if not keypaths.has_key(filenamekey):
                keypaths.setdefault(filenamekey)
                keypaths[filenamekey] = []

            filenamekeyvalues = keypaths[filenamekey]
            filenamekeyvalues.append(filepath)
            keypaths[filenamekey] = filenamekeyvalues

        for key in keypaths.keys():
            grouppaths = keypaths[key]
            combinfilepath = combineOutPutPath + key + ext
            if not os.path.exists(combinfilepath):
                dirpath = os.path.dirname(combinfilepath)
                if not os.path.exists(dirpath):
                    os.makedirs(dirpath)

            fo = open(combinfilepath, 'w')

            for path in grouppaths:
                # print(path)
                pathkeyfile = open(path, 'r')
                data = pathkeyfile.readlines()
                fo.writelines(data)
                pathkeyfile.close()
            fo.close()

    def combinIos(self):


        print('-----------------------combin--------------------')
        allfiles = []
        LanguagePaths().filepaths(allfiles,self.createddir)
        return allfiles

    def creatCombinefile(self):

        allfiles = self.combinIos()

        iosExt = '.strings'
        androidExt = '.xml'
        webExt = '.properties'

        iosPaths = self.groupsPaths(allfiles, iosExt)
        androidPaths = self.groupsPaths(allfiles, androidExt)
        webPaths = self.groupsPaths(allfiles, webExt)

        iosCombinePath = self.combinedDataDir + '/iOS/'
        androidCombinePath = self.combinedDataDir + '/Android/'
        webCombinePath = self.combinedDataDir + '/Web/'

        self.makecombinefile(iosPaths, iosCombinePath, iosExt)
        self.makecombinefile(androidPaths, androidCombinePath, androidExt)
        self.makecombinefile(webPaths, webCombinePath, webExt)

























