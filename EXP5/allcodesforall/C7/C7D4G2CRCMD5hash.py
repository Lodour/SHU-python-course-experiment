#coding:utf-8
## -*- coding : gbk -*-
#CRC32
import zlib
print zlib.crc32('SDIBT')
import binascii
print binascii.crc32('SDIBT')

#MD5_1
import hashlib
md5value=hashlib.md5()
md5value.update('12345')
md5value=md5value.hexdigest()
print md5value
import md5
md5value=md5.md5()
md5value.update('12345')
md5value=md5value.hexdigest()
print md5value

#MD5_2
import hashlib
import os
import sys
fileName = sys.argv[1]
if os.path.isfile(fileName):
    with open(fileName, 'r') as fp:
        lines = fp.readlines()
    data = ''.join(lines)
print(hashlib.md5(data).hexdigest())

#计算文件哈希值
from ssdeep import ssdeep
s = ssdeep()
print s.hash_file(filename) 
