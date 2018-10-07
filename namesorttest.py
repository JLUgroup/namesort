# coding: utf-8
import chardet
        
        
path = 'namelist.txt'
namefile = open(path,mode = 'rb')
        
names = namefile.readline()
print names
print chardet.detect(names)#.decode('utf-8').encode('utf-8'))
#names = names.decode("gb2312")
        #f = lookhan.decode(names)
        #names = lookhan.encode(names)

names = names.decode('utf-8')#.encode('')
        #b=names.unicode(names,"gb2312")
test = open('test.txt', 'w')
test.write(names)
print test.read()
names = names.split()
namesutf8 = []
i=0
for name in names:
    i=i+1
            #namesutf8.append(name.encode('utf-8'))
#    print name,len(name),i#,chardet.detect(name.encode('gbk'))
            #print name.encode('utf-8'),len(name.encode('utf-8'))
        #print names,type(names),len(names)
        #print namesutf8
        #print chardet.detect(names)

        #print f
namefile.close()
