'''
Created on 2017年11月14日

@author: Administrator
'''
#strncmp(sStr1,sStr2,n)
#strncmp(sStr1,sStr2,n)
#strcpy(sStr1,sStr2)
from _operator import eq
from filecmp import cmp
from operator import le


sStr1 = '2017-09'
sStr2 = '2017-08'
print(le(sStr1,sStr2))


