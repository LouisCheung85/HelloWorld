import mysql.connector
import ResolveHtml
import os

def insertData(data=[]):
  mydb = mysql.connector.connect(
    host="192.168.145.93",
    user="root",
    passwd="Aa111111",
    database="jiaoshi_2_new"
  )
  
  cur=mydb.cursor()

  sql="Insert into HouseDebet(Stage,Total,Interest,Capital,Remain) values(%s,%s,%s,%s,%s)"

  values=[]

  for d in data:
    values.append(d)

  cur.executemany(sql,values)

  mydb.commit()

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


    
  




