class Donation:
    def __init__(self,lan = "en"):
        self.dodo = []
        self.lan = lan
    def add(self,name,money):
        self.dodo.append({"name":name,"many":money})
    def delete(self,name):
        for item in self.dodo:
            if item["name"] == name:
                itemmoney = item["many"]
                self.dodo.remove({"name":name,"many":itemmoney})
                return
        if self.lan == "en":
            print("No sponsored user with that name")
        elif self.lan == "ko":
            print("그 이름을 가진 후원한 유저는 없습니다")
    def print(self,greeting = "Sponsor List------",order = "Number"):
        print(greeting)
        j=0
        for i in self.dodo:
            if self.lan == "en":
                if order == "Number":
                    print(str(j+1)+"."+self.dodo[j]["name"]+" "+str(self.dodo[j]["many"])+"$")
                else:
                    print(order+self.dodo[j]["name"]+" "+str(self.dodo[j]["many"])+"$")
            if self.lan == "ko":
                if order == "Number":
                    print(str(j+1)+"."+self.dodo[j]["name"]+"님 "+str(self.dodo[j]["many"])+"원")
                else:
                    print(order+self.dodo[j]["name"]+"님 "+str(self.dodo[j]["many"])+"원")
                
            j = j + 1

