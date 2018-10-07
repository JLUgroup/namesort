#coding: utf-8

#class Readname(object):

#    def readname(self)
"""
此脚本将文本文件中的姓名提取出来写入‘nameout.txt’文件中存为一列。现版本要求不能出现一个字的姓名，
以及只有两字姓名中可以出现空格。可以处理没有空格的英文姓名。

由于不确定文本文件的编码形式，所以需要引入‘chardet’模块来判断。若无chardet模块可通过
‘pip install chardet’命令安装。若确定文件编码为某编码，如utf-8编码，可取消引入chardet
模块。

运行方式：现版本程序需将所有姓名文件置于同一文件夹下（无其它不相关文件），之后将此程序文件
置于同一文件夹下运行即可。若姓名文件以其它方式储存，可对程序进行进一步升级。
"""     
import chardet
import os,sys,re

if os.access('nameout.txt', os.F_OK):      # check file nameout.txt if exist then delete
    os.remove('nameout.txt')

files = os.listdir(os.getcwd())            # make a filename list of current workspace
nameout = open('nameout.txt', mode='w')    # create a file nameout.txt in write-only mode
namelist = []


for filename in files:

    if filename == 'namesort.py':          # make the object except main program
        continue
    
    namefile = open(filename,mode = 'r')   # open one file and prepare to check and sort
    coding = chardet.detect(namefile.read(200))['encoding']
    namefile.seek(0,0)                     # check encode type
   # print coding
   # exit()
    for names in namefile:
        namestore = []
        names = names.decode(coding)       # decode the chinese character in files
        names = names.split()              # split the names by blank space
        for name in names:
            if len(name) == 1:
                namestore.append(name)     # store the single character
            else:
                if name in namelist:
                    pass
                else:
                     nameout.write(name.encode('utf-8'))
                     nameout.write('\n')   # write normal names in nameout
                     namelist.append(name) # add name to list in order to check duplicate

        if len(namestore) == 0 :
            pass
        elif (len(namestore)%2) == 0:
            for i in range(0,len(namestore), 2):
                name = namestore[i] + namestore[i+1]
                if name in namelist:       # link single character to double-character name
                    pass
                else:
                    nameout.write(name.encode('utf-8'))
                    nameout.write('\n')    # write the result to nameout
                    namelist.append(name)
        else:
            print 'error'

    namefile.close()


nameout.close()                            # close the in and out files


