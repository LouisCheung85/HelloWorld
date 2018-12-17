class ca(object):
    
    def __init__(self):
      self.Data=[]

    def add(self,list):
      self.Data.extend(list)

    def out(self):
       for i in self.Data:
           print(i)

if __name__=="__main__":
    c =ca()

    c.add([1,2,5])

    c.add([7,8,6])

    c.out()

    print(c.Data)

