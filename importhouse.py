import mysql.connector
import ResolveHtml
import os

def insertData(data=[]):
  mydb = mysql.connector.connect(
    host="47.104.237.7",
    user="louis",
    passwd="Aa@111111",
    database="test_db",
    auth_plugin='mysql_native_password'
  )
  
  cur=mydb.cursor()

  sql="Insert into HouseDebet(Stage,Total,Interest,Capital,Remain) values(%s,%s,%s,%s,%s)"

  values=[]

  for d in data:
    values.append(d)

  cur.executemany(sql,values)

  mydb.commit()
  mydb.close()

def gethtmlData():
    curpath=os.path.split(os.path.realpath(__file__))[0]
    txtfile=os.path.join(curpath,"new 2.html")
    with open(txtfile,"r",encoding="UTF-8") as txt:
       content= txt.read(-1)           
       txt.close()   
       return content 

if __name__=="__main__":
  houseDebet=ResolveHtml.houseDebet()
  houseDebet.feed(gethtmlData())
  listData=houseDebet.getResult()
  insertData(listData)


    
  




