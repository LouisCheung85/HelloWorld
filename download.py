import os
import urllib.request
import time
import re

def GetTextData():
    curpath=os.path.split(os.path.realpath(__file__))[0]
    txtfile=os.path.join(curpath,"abc.txt")
    list1=[]
    with open(txtfile,"r",encoding="UTF-8") as txt:
        for l in txt:
            list1.append(l.strip())            
        txt.close()    
    return list1

def downloadImage():

   folder= os.path.join(os.path.split(os.path.realpath(__file__))[0],"images")

   if(os.path.exists(folder)==False):
       os.makedirs(folder)   
 
   images=GetTextData()
   imageSite="http://192.168.145.23:8085/content/images/thumbs/"
   num=1
   total=str(len(images))
   for im in images:

       print("downloading："+str(num)+"/"+total)
       num+=1

       if re.match('\s+|NULL',im.split("\t")[1]):
            continue

       picId="{:0>7}".format(im.split("\t")[1])

       seoName=im.split("\t")[2]

       productNumber=im.split("\t")[3]

       imageName=None

       if re.match('\s+|NULL',seoName) or seoName=="":
           imageName=picId+".jpeg"
       else:            
           imageName=picId+"_"+seoName+".jpeg"                          
      

       if os.path.exists(os.path.join(folder,productNumber+".jpeg")):
          continue

       try:
           urllib.request.urlretrieve(imageSite+imageName,os.path.join(folder,productNumber+".jpeg"))
            # pass
       except Exception as exe:
           print(exe)
           continue

       time.sleep(0.5)
    
if __name__=="__main__":
  downloadImage()

