import re
import os
from bs4 import BeautifulSoup
import shutil

  
if __name__=='__main__':
    sourceDirPath="20180324"
    fileNames=os.listdir(sourceDirPath)
    goalFilepath = sourceDirPath+"_"+"LiTitle.txt"
    file_object = open(goalFilepath,'w',encoding='utf8')
    for fileName in fileNames:
        strFile=sourceDirPath+"/"+fileName
        textHtml=open(strFile,'r',encoding='utf8')
        InforStr= '''<a href="{0}/{1}" class="list-group-item ">[]{2} </a>
                  '''.format(sourceDirPath,fileName,fileName.split('.')[0])

        file_object.write(InforStr+'\n')

    file_object.close( )
  
    print("Job is OK")
