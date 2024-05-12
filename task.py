"""
lib.kitabElaveEt("Zamanin kisa tarihi","Stephen Hawking","True")
lib.kitabElaveEt("Masumiyet muzesi","Orhan Pamuk","True")
lib.kitabElaveEt("Yasam nedir","Erwin Schrodinger","True")
lib.kitabElaveEt("Tesla SpaceX ve muhtesem geleceyin pesinde","Ashley Vance","True")
"""


class Kitab():
    def __init__(self,basliq,yazar,status):
        self.basliq=basliq
        self.yazar=yazar
        self.status=status
        
class Kitabxana():

    myList=[]
    def kitabElaveEt(self,basliq,yazar,status):
        kitab=Kitab(basliq,yazar,status)
        self.myList.append([kitab.basliq,kitab.yazar,kitab.status])
        print("kitab elave edildi")
        
    def varOlanKitablar(self):
        for i in self.myList:
            print(i)
        
    def borcVer(self,basliq):
        self.basliq=basliq
        for i in self.myList:
            if i[0]==self.basliq:
                if i[2]=="True":
                    i[2]="False"
                    print("Kitab borc verildi")
                else:
                    print("Bu kitab artiq borc verilib")

    def geriQaytar(self,basliq):
        self.basliq=basliq
        for i in self.myList:
            if i[0]==self.basliq:
                if i[2]=="False":
                    i[2]="True"
                    print("Kitab kitabxanaya geri qaytarildi")      
                else:
                    print("Bu kitab borc verilmeyib")
        
    def borcVerilmisler(self):
        borcList=[]
        for i in self.myList:
            if i[2]=="False":
                borcList.append(i)
        print(borcList)

lib=Kitabxana()
