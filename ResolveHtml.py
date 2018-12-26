from html.parser import HTMLParser

class houseDebet(HTMLParser):

    debetlistcur=[]

    debetlist=[]
    
    is_dd=False
    def __init__(self):
        HTMLParser.__init__(self)
        self.debetlist=[]
    
    def handle_starttag(self,tag,attrs):
        #print(tag)
        if tag=="dd":
            self.is_dd=True
        #pass
    
    def handle_endtag(self,tag):
       # print(tag)
        if tag=="dd":
            self.is_dd=False
            self.debetlist.append(self.debetlistcur[:])
            self.debetlistcur.clear()

    def handle_data(self,data):
       # print(data)
        if self.is_dd and len(data.strip())>0:
            self.debetlistcur.append(data.strip())
         #   if len(self.debetlistcur)==5:
    
    def outputResult(self):
        for ele in self.debetlist:
            print(ele)

if __name__ =="__main__":
    house=houseDebet()
    house.feed(r"""<dd> 
    <div>333</div>
    <div>1113.12</div>
    <div>11.93</div>
    <div>1101.19</div>
    <div>3303.57</div>
    <div class="clear"></div>
</dd>
<dd>
    <div>336</div>
    <div>1104.17</div>
    <div>2.98</div>
    <div>1101.19</div>
    <div>0.00</div>
    <div class="clear"></div>
</dd>""")
    house.outputResult()