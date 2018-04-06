import re
import os
from bs4 import BeautifulSoup
import shutil

  
if __name__=='__main__':
    sourceDirPath="jlbsczw"
    fileNames=os.listdir(sourceDirPath)
    goalFilepath = sourceDirPath+"_"+"LiTitle.txt"
    file_object = open(goalFilepath,'w')
    for i in range(8,126):
        fileName = "第 {0} 部分".format(i)
        InforStr= '''<a href="{0}/{1}" class="list-group-item ">[经典]{2} </a>
                  '''.format(sourceDirPath,fileName+".html","第 {0} 部分".format(i))

        file_object.write(InforStr)

    file_object.close( )
  
    print("Job is OK")
