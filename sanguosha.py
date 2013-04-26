'''
Manual Sanguosha Card Recorder!
Better to use iPython to do interaction!

Created on Apr 19, 2013

@author: fatestudio
'''
# num: 'A' to 'K';
# suit: 's': spade, 'h': heart, 'c': club, 'd': diamond;
# name: 'Juedou', 'Wugufengdeng', etc...;
# category: 'equip', 'basic', 'magic';

def checkCardInput(strs):   
    if(len(strs) != 4):
        print('len(strs): ' + str(len(strs)) + ' is not 4!')
        return False
    elif(strs[0] != 'A' and strs[0] != 'J' and strs[0] != 'Q' and strs[0] != 'K'
         and strs[0] != '10' and strs[0] >= '9' and strs[0] <= '2'):
        print("strs[0]: " + strs[0] + " not in 'A' to 'K'!")
        return False
    elif(strs[1] != 's' and strs[1] != 'h' and strs[1] != 'c' and strs[1] != 'd'):
        print("strs[1]: " + strs[1] + " not in 's', 'h', 'c', 'd'!")
        return False
    elif(strs[3] != 'E' and strs[3] != 'B' and strs[3] != 'M'):
        print("strs[3]: " + strs[3] + " not in 'E', 'B', 'M'!")
        return False
    
    return True

    
class Card:
    def __init__(self, strs): # initialize Card from a string array
        # check input
        if(not checkCardInput(strs)):
            print("check failed, exit!")
            exit(0)
        self.num = strs[0]
        self.suit = strs[1]
        self.name = strs[2]
        self.category = strs[3]
    
    def showNum(self):
        print(self.num)
    
    def showSuit(self):
        print(self.suit)
        
    def showName(self):
        self.name
    
    def showCategory(self):
        self.category
        
    
class Cards:
    allcards = []
    restcards = []
    
    def __init__(self):     # add all cards into allcards[]
        self.allcards.append(['A', 's', 'Juedou', 'M'])
        self.allcards.append(['A', 's', 'Shandian', 'M'])
        self.allcards.append(['A', 's', 'Gudingdao', 'E'])
        
        self.allcards.append(['A', 'h', 'Wanjianqifa', 'M'])
        self.allcards.append(['A', 'h', 'Taoyuanjieyi', 'M'])
        self.allcards.append(['A', 'h', 'Wuxiekeji', 'M'])
        
        self.allcards.append(['A', 'c', 'Juedou', 'M'])
        self.allcards.append(['A', 'c', 'Zhugeliannu', 'E'])
        self.allcards.append(['A', 'c', 'Baiyinshizi', 'E'])
        
        self.allcards.append(['A', 'd', 'Juedou', 'M'])
        self.allcards.append(['A', 'd', 'Zhugeliannu', 'E'])
        self.allcards.append(['A', 'd', 'Zhuqueyushan', 'E'])
        
        self.allcards.append(['2', 's', 'Baguazhen', 'E'])
        self.allcards.append(['2', 's', 'Cixiongshuanggujian', 'E'])
        self.allcards.append(['2', 's', 'Tengjia', 'E'])
        self.allcards.append(['2', 's', 'Hanbingjian', 'E'])
        
        self.allcards.append(['2', 'h', 'Shan', 'B'])
        self.allcards.append(['2', 'h', 'Shan', 'B'])
        self.allcards.append(['2', 'h', 'Huogong', 'M'])
        
        self.allcards.append(['2', 'c', 'Sha', 'B'])
        self.allcards.append(['2', 'c', 'Baguazhen', 'E'])
        self.allcards.append(['2', 'c', 'Tengjia', 'E'])
        self.allcards.append(['2', 'c', 'Renwangdun', 'E'])
        
        self.allcards.append(['2', 'd', 'Shan', 'B'])
        self.allcards.append(['2', 'd', 'Shan', 'B'])
        self.allcards.append(['2', 'd', 'Tao', 'B'])
        
        self.allcards.append(['3', 's', 'Guohechaiqiao', 'M'])
        self.allcards.append(['3', 's', 'Shunshouqianyang', 'M'])
        self.allcards.append(['3', 's', 'Jiu', 'B'])
        
        self.allcards.append(['3', 'h', 'Tao', 'B'])
        self.allcards.append(['3', 'h', 'Wugufengdeng', 'M'])
        self.allcards.append(['3', 'h', 'Huosha', 'B'])
        
        self.allcards.append(['3', 'c', 'Sha', 'B'])
        self.allcards.append(['3', 'c', 'Guohechaiqiao', 'M'])
        self.allcards.append(['3', 'c', 'Jiu', 'B'])
        
        self.allcards.append(['3', 'd', 'Shan', 'B'])
        self.allcards.append(['3', 'd', 'Shunshouqianyang', 'M'])
        self.allcards.append(['3', 'd', 'Tao', 'B'])
        
        self.allcards.append(['4', 's', 'Guohechaiqiao', 'M'])
        self.allcards.append(['4', 's', 'Shunshouqianyang', 'M'])
        self.allcards.append(['4', 's', 'Leisha', 'B'])
        
        self.allcards.append(['4', 'h', 'Tao', 'B'])
        self.allcards.append(['4', 'h', 'Wugufengdeng', 'M'])
        self.allcards.append(['4', 'h', 'Huogong', 'M'])
        
        self.allcards.append(['4', 'c', 'Sha', 'B'])
        self.allcards.append(['4', 'c', 'Guohechaiqiao', 'M'])
        self.allcards.append(['4', 'c', 'Bingliangcunduan', 'M'])
        
        self.allcards.append(['4', 'd', 'Shan', 'B'])
        self.allcards.append(['4', 'd', 'Shunshouqianyang', 'M'])
        self.allcards.append(['4', 'd', 'HUosha', 'B'])
        
        self.allcards.append(['5', 's', 'Qinglongyanyuedao', 'E'])
        self.allcards.append(['5', 's', 'Jueying', 'E'])
        self.allcards.append(['5', 's', 'Leisha', 'B'])
        
        self.allcards.append(['5', 'h', 'Qilinggong', 'E'])
        self.allcards.append(['5', 'h', 'Chitu', 'E'])
        self.allcards.append(['5', 'h', 'Tao', 'B'])
        
        self.allcards.append(['5', 'c', 'Sha', 'B'])
        self.allcards.append(['5', 'c', 'Dilu', 'E'])
        self.allcards.append(['5', 'c', 'Leisha', 'B'])
        
        self.allcards.append(['5', 'd', 'Shan', 'B'])
        self.allcards.append(['5', 'd', 'Guanshifu', 'E'])
        self.allcards.append(['5', 'd', 'Huosha', 'B'])
        
        self.allcards.append(['6', 's', 'Lebusishu', 'M'])
        self.allcards.append(['6', 's', 'Qinggangjian', 'E'])
        self.allcards.append(['6', 's', 'Leisha', 'B'])
        
        self.allcards.append(['6', 'h', 'Tao', 'B'])
        self.allcards.append(['6', 'h', 'Lebusishu', 'M'])
        self.allcards.append(['6', 'h', 'Tao', 'B'])
        
        self.allcards.append(['6', 'c', 'Sha', 'B'])
        self.allcards.append(['6', 'c', 'Lebusishu', 'M'])
        self.allcards.append(['6', 'c', 'Leisha', 'B'])
        
        self.allcards.append(['6', 'd', 'Sha', 'B'])
        self.allcards.append(['6', 'd', 'Shan', 'B'])
        self.allcards.append(['6', 'd', 'Shan', 'B'])
        
        self.allcards.append(['7', 's', 'Sha', 'B'])
        self.allcards.append(['7', 's', 'Nanmanruqin', 'M'])
        self.allcards.append(['7', 's', 'Leisha', 'B'])
        
        self.allcards.append(['7', 'h', 'Tao', 'B'])
        self.allcards.append(['7', 'h', 'Wuzhongshengyou', 'M'])
        self.allcards.append(['7', 'h', 'Huosha', 'B'])
        
        self.allcards.append(['7', 'c', 'Sha', 'B'])
        self.allcards.append(['7', 'c', 'Nanmanruqin', 'M'])
        self.allcards.append(['7', 'c', 'Leisha', 'B'])
        
        self.allcards.append(['7', 'd', 'Sha', 'B'])
        self.allcards.append(['7', 'd', 'Shan', 'B'])
        self.allcards.append(['7', 'd', 'Shan', 'B'])
        
        self.allcards.append(['8', 's', 'Sha', 'B'])
        self.allcards.append(['8', 's', 'Sha', 'B'])
        self.allcards.append(['8', 's', 'Leisha', 'B'])
        
        self.allcards.append(['8', 'h', 'Tao', 'B'])
        self.allcards.append(['8', 'h', 'Wuzhongshengyou', 'M'])
        self.allcards.append(['8', 'h', 'Shan', 'B'])
        
        self.allcards.append(['8', 'c', 'Sha', 'B'])
        self.allcards.append(['8', 'c', 'Sha', 'B'])
        self.allcards.append(['8', 'c', 'Leisha', 'B'])
        
        self.allcards.append(['8', 'd', 'Sha', 'B'])
        self.allcards.append(['8', 'd', 'Shan', 'B'])
        self.allcards.append(['8', 'd', 'Shan', 'B'])
        
        self.allcards.append(['9', 's', 'Sha', 'B'])
        self.allcards.append(['9', 's', 'Sha', 'B'])
        self.allcards.append(['9', 's', 'Jiu', 'B'])
        
        self.allcards.append(['9', 'h', 'Tao', 'B'])
        self.allcards.append(['9', 'h', 'Wuzhongshengyou', 'M'])
        self.allcards.append(['9', 'h', 'Shan', 'B'])
        
        self.allcards.append(['9', 'c', 'Sha', 'B'])
        self.allcards.append(['9', 'c', 'Sha', 'B'])
        self.allcards.append(['9', 'c', 'Jiu', 'B'])
        
        self.allcards.append(['9', 'd', 'Sha', 'B'])
        self.allcards.append(['9', 'd', 'Shan', 'B'])
        self.allcards.append(['9', 'd', 'Jiu', 'B'])
        
        self.allcards.append(['10', 's', 'Sha', 'B'])
        self.allcards.append(['10', 's', 'Sha', 'B'])
        self.allcards.append(['10', 's', 'Bingliangcunduan', 'M'])
        
        self.allcards.append(['10', 'h', 'Sha', 'B'])
        self.allcards.append(['10', 'h', 'Sha', 'B'])
        self.allcards.append(['10', 'h', 'Huosha', 'B'])
        
        self.allcards.append(['10', 'c', 'Sha', 'B'])
        self.allcards.append(['10', 'c', 'Sha', 'B'])
        self.allcards.append(['10', 'c', 'Tiesuolianhuan', 'M'])
        
        self.allcards.append(['10', 'd', 'Sha', 'B'])
        self.allcards.append(['10', 'd', 'Shan', 'B'])
        self.allcards.append(['10', 'd', 'Shan', 'B'])
        
        self.allcards.append(['J', 's', 'Shunshouqianyang', 'M'])
        self.allcards.append(['J', 's', 'Wuxiekeji', 'M'])
        self.allcards.append(['J', 's', 'Tiesuolianhuan', 'M'])
        
        self.allcards.append(['J', 'h', 'Sha', 'B'])
        self.allcards.append(['J', 'h', 'Wuzhongshengyou', 'M'])
        self.allcards.append(['J', 'h', 'Shan', 'B'])
        
        self.allcards.append(['J', 'c', 'Sha', 'B'])
        self.allcards.append(['J', 'c', 'Sha', 'B'])
        self.allcards.append(['J', 'c', 'Tiesuolianhuan', 'M'])
        
        self.allcards.append(['J', 'd', 'Shan', 'B'])
        self.allcards.append(['J', 'd', 'Shan', 'B'])
        self.allcards.append(['J', 'd', 'Shan', 'B'])
        
        self.allcards.append(['Q', 's', 'Guohechaiqiao', 'M'])
        self.allcards.append(['Q', 's', 'Zhangbashemao', 'E'])
        self.allcards.append(['Q', 's', 'Tiesuolianhuan', 'M'])
        
        self.allcards.append(['Q', 'h', 'Tao', 'B'])
        self.allcards.append(['Q', 'h', 'Guohechaiqiao', 'M'])
        self.allcards.append(['Q', 'h', 'Shan', 'B'])
        self.allcards.append(['Q', 'h', 'Shandian', 'M'])
        
        self.allcards.append(['Q', 'c', 'Jiedaosharen', 'M'])
        self.allcards.append(['Q', 'c', 'Wuxiekeji', 'M'])
        self.allcards.append(['Q', 'c', 'Tiesuolianhuan', 'M'])
        
        self.allcards.append(['Q', 'd', 'Tao', 'B'])
        self.allcards.append(['Q', 'd', 'Fangtianhuaji', 'E'])
        self.allcards.append(['Q', 'd', 'Huogong', 'M'])
        self.allcards.append(['Q', 'd', 'Wuxiekeji', 'M'])
        
        self.allcards.append(['K', 's', 'Nanmanruqin', 'M'])
        self.allcards.append(['K', 's', 'Dawan', 'E'])
        self.allcards.append(['K', 's', 'Wuxiekeji', 'M'])
        
        self.allcards.append(['K', 'h', 'Shan', 'B'])
        self.allcards.append(['K', 'h', 'Zhuahuangfeidian', 'E'])
        self.allcards.append(['K', 'h', 'Wuxiekeji', 'M'])
        
        self.allcards.append(['K', 'c', 'Jiedaosharen', 'M'])
        self.allcards.append(['K', 'c', 'Wuxiekeji', 'M'])
        self.allcards.append(['K', 'c', 'Tiesuolianhuan', 'M'])
        
        self.allcards.append(['K', 'd', 'Sha', 'B'])
        self.allcards.append(['K', 'd', 'Zixin', 'E'])
        self.allcards.append(['K', 'd', 'Hualiu', 'E'])
        
        self.restcards = list(self.allcards)
        
    def qRestcards(self):
        showCards(self.restcards)   
        
    def qAllcards(self):
        showCards(self.allcards)
    
    def qEquip(self):
        ans = []
        for i in range(len(self.restcards)):
            if(self.restcards[i][3] == 'E'):
                ans.append(self.restcards[i])
        showCards(ans)
        
    def qMagic(self):
        ans = []
        for i in range(len(self.restcards)):
            if(self.restcards[i][3] == 'M'):
                ans.append(self.restcards[i])
        showCards(ans)
        
    def qBasic(self):
        ans = []
        for i in range(len(self.restcards)):
            if(self.restcards[i][3] == 'B'):
                ans.append(self.restcards[i])        
        showCards(ans)

    def q(self, name):
        name = name[0].upper() + name[1:]
        ans = []
        for i in range(len(self.restcards)):
            if(name in self.restcards[i][2]):
                ans.append(self.restcards[i])
        showCards(ans)
        
    def refreshCards(self):
        self.restcards = list(self.allcards)
    
    def removeCard(self, strs):
        checkCardInput(strs)
        if(not checkCardInput(strs)):
            print("check failed, exit!")
            exit(0)
        
        for i in range(len(self.restcards)):
            if(strs[0] == self.restcards[i][0] and strs[1] == self.restcards[i][1] and 
               strs[2] == self.restcards[i][2] and strs[3] == self.restcards[i][3]):
                self.restcards.remove(strs)
                return True
        
        print("Cannot find " + strs)
        return False

    def a(self, name): # do it reversely! Compare to r!
        name = name[0].upper() + name[1:]
        rests = []
        for i in range(len(self.restcards)):
            if(name in self.restcards[i][2]):
                rests.append(self.restcards[i])
                
        alls = []
        for i in range(len(self.allcards)):
            if(name in self.allcards[i][2]):
                alls.append(self.allcards[i])
        
        for i in range(len(rests)):
            for j in range(len(alls)):
                if(rests[i] == alls[j]):
                    alls.pop(j)
                    break
        
        if(len(alls) == 0):
            print("No card in this name: " + name + " can be added!")
            return False
        else:
            showCards(alls)
            idx = input("Enter the index to add: ")
            self.restcards.append(alls[idx])
            print("After add:")
            cards.qName(name)
            return True
        
            
    def r(self, name): # find all rest cards with this name, then select and delete one of them
        name = name[0].upper() + name[1:]
        rests = []
        for i in range(len(self.restcards)):
            if(name in self.restcards[i][2]):
                rests.append(self.restcards[i])

        if(len(rests) == 0):
            print("No card in this name: " + name + " can be removed!")
            return False
        else:
            showCards(rests)
            idx = input("Enter the index to remove: ")
            self.restcards.remove(rests[idx])
            print("After remove:")
            cards.qName(name)
            return True                

def showCards(arrs):
    print(len(arrs))
    cols = 2
    for i in range(len(arrs)):
        print(str(i) + ': ' + str(arrs[i]) + ' '), 
        if((i + 1) % cols == 0):
            print
    if(len(arrs) % cols != 0):
        print
        

cards = Cards()
#cards.qEquip()
#cards.qBasic()        
# cards.qMagic()     
# cards.removeCard(['A', 's', 'Juedou', 'M'])
# cards.removeCard(['K', 'c', 'Tiesuolianhuan', 'M'])
# cards.qMagic()
# cards.refreshCards()
# cards.qMagic()
# cards.q("guohe")
# cards.r("guohe")
# cards.r("guohe")
# cards.a("guohe")
