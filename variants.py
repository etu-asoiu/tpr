# -*- coding: utf-8 -*-
import os

for i in range(141):
    srcFileName = "%d.pdf" % i
    dirName = "%03d" % i
    if os.path.isfile(srcFileName):
        # Если каталога не существует => создаём его
        if not os.path.isdir(dirName):
            os.makedirs(dirName)
        dstFileName = dirName + "/" + srcFileName
        if not os.path.isfile(dstFileName):
            os.rename(srcFileName, dstFileName)
