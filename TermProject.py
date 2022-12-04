##code 
import pymysql

connect = pymysql.connect(host='192.168.230.3',user='jpark', password='1234', db='Termpro', port=4567, charset='utf8',)

cur = connect.cursor()