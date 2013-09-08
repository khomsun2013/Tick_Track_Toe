hum = [-1,-1,-1] # constant value of human
com = [1,1,1]  # constant value of human

class MoveInfo(object):

    def __init__(self,move,value,board):
        self.m = move # m = move
        self.v = value # v = value
        self.b = board # b = board of tries
    def isEmpty(self,n):
        return (b[n]==0)
    def isFull(self):
        i = 1
        while( i < 10):
            if (b[i] == 0): return False
            i = i + 1
        return True
    def place(self,n,p):
        b[n] = p
    def unplace(self,n):
        b[n] = 0
    def checkGame(self): 
        if ((b[1:4]==hum)or(b[4:7]==hum)or(b[7:10]==hum)
           or([b[1],b[4],b[7]]==hum)or([b[2],b[5],b[8]]==hum)or([b[3],b[6],b[9]]==hum)    
           or([b[1],b[5],b[9]]==hum)or([b[3],b[5],b[7]]==hum)):return -1
        if ((b[1:4]==com)or(b[4:7]==com)or(b[7:10]==com)
           or([b[1],b[4],b[7]]==com)or([b[2],b[5],b[8]]==com)or([b[3],b[6],b[9]]==com)    
           or([b[1],b[5],b[9]]==com)or([b[3],b[5],b[7]]==com)):return 1
        return 0
    def immComWin(self):
        if ((b[1:4]==com)or(b[4:7]==com)or(b[7:10]==com)
           or([b[1],b[4],b[7]]==com)or([b[2],b[5],b[8]]==com)or([b[3],b[6],b[9]]==com)    
           or([b[1],b[5],b[9]]==com)or([b[3],b[5],b[7]]==com)):
            return MoveInfo(0,1,b)
        else:
            return 
    def immHumWin(self):        
        if ((b[1:4]==hum)or(b[4:7]==hum)or(b[7:10]==hum)
           or([b[1],b[4],b[7]]==hum)or([b[2],b[5],b[8]]==hum)or([b[3],b[6],b[9]]==hum)    
           or([b[1],b[5],b[9]]==hum)or([b[3],b[5],b[7]]==hum)):
            return MoveInfo(0,-1,b)
        else:
            return 
    def findComMove(self):
        value = 1
        best = 1
        if (self.isFull()):
            value = 0
        else:
            quickWin = self.immComWin()
            if (quickWin != None):
                return quickWin
            else:
                value = -1
                i = 1
                while(i < 10):
                    if (self.isEmpty(i)):
                        self.place(i,1)
                        respon = self.findHumMove().v
                        self.unplace(i)
                        if (respon > value):
                            value = respon
                            best = i
                    i = i + 1
        return MoveInfo(best, value, b)
    def findHumMove(self):
        value = 1
        best = 1
        if (self.isFull()):
            value = 0
        else:
            quickWin = self.immHumWin()
            if (quickWin != None):
                return quickWin
            else:
                value = 1
                i = 1
                while(i < 10):
                    if (self.isEmpty(i)):
                        self.place(i,-1)
                        respon = self.findComMove().v
                        self.unplace(i)
                        if (respon < value):
                            value = respon
                            best = i
                    i = i + 1
        return MoveInfo(best, value, b)
    
def display():
    i = 1
    while(i < 10):
        c = b[i]
        if (b[i] == -1):
            c = 'O'
        elif (b[i] == 1):
            c = 'X'
        else:
            c = ' '
        if ((i % 3) != 0):
            print c,'  ',
        else:
            print c
        i = i + 1
    print
    
done = False # Game over = True
turn = True  # Human = True, Computer = False
b = [0]*10
mi = MoveInfo(1,0,b)
while(not done):
    if (turn):
        n = int(input("Human Select --> (1 to 9) : "))
        while(b[n]!=0):
              n = int(input("Human Select --> (1 to 9) : "))
        b[n] = -1
        turn = False
    else:
        n = mi.findComMove().m;
        print "Computer Select : ",n
        b[n] = 1
        turn = True
    display()
    if (mi.checkGame() == -1):
        print("Cool!! You're win")
        done = True
    if (mi.checkGame() == 1):
        print("Sorry!! You're lost")
        done = True
    if ((mi.checkGame() == 0)and(mi.isFull())):
        print("Draw!! Let's try again")
        done = True
    
