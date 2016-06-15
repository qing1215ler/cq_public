#coding=utf-8
import zipfile
import os,sys
import shutil

apkFile=sys.argv[1]
channel=sys.argv[2]
apk=apkFile.split('.apk')[0]

empty_file='xx.txt'
f=open(empty_file,'w')
f.close()

destfile='./%s_%s.apk'%(apk,channel)
shutil.copy(apkFile,destfile)
zipped = zipfile.ZipFile(destfile,'a',zipfile.ZIP_DEFLATED)
empty_channel_file="META-INF/{channelname}".format(channelname=channel)
zipped.write(empty_file,empty_channel_file)
zipped.close()