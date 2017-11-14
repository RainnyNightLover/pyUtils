'''
Created on 2017年11月14日

@author: Administrator
'''
import pymysql

#def getconnection(self):
connection = pymysql.connect(host = "172.16.90.55",
                            user = "root",
                            password = "root",
                            db = "spider",
                            charset = "utf8mb4"
                            )
  #return connection


try:
  #获取会话指针
  with connection.cursor() as cursor:
      #创建sql
    sql = "insert into `toutiaodraftdata`(`title`,`abstract`) values(%s,%s)"
    cursor.execute(sql,("yangxing","hello"))
    connection.commit()
finally:
  connection.close()  