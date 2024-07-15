"""make_me_rich.py"""

import yfinance as yf
import time
import datetime
from colorama import Fore

bot_rich = 0 # price of your earnings
striking_Rate = 1.82 # percentage must be wrritten as decimal.
tickers = yf.Tickers('HG=F GBPUSD=X CNY=X') # your currencies
array_data = [0.0]*200
count = 0
first_time = 0
tradable = False

date = datetime.datetime.now()
date = str(date)

print(Fore.WHITE+"\n𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡")
print(Fore.LIGHTBLACK_EX+"▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅")
print(Fore.LIGHTWHITE_EX+" \n 钱 ","⇛ Make_me_rich.py   ⇛ BY: isa pečurević   ⇛ Time: ",date)
print(Fore.WHITE+'')

yen = tickers.tickers['CNY=X'].history(period ="1mo", interval="1d")
yen = str(yen)
yen = yen[2324:-32] # You may need remove some bytes to get gurrent price of YUAN
yen = float(yen)

for i in range(20):
    buy = False
    sell = False
    counter = 8
    price = []
    s = tickers.tickers['HG=F'].history(period="1d",interval="1m")
    s = str(s)
    f = open("stock_price.txt", "w")
    f.write(s)
    with open("stock_price.txt", "r") as f:
        for line in f:
            price.append(line.rstrip("\n"))

    cu1 = [price[counter]]
    cu1 = str(cu1) # close
    cu1 = cu1[53:-30]
    cu1 = float(cu1)

    cuv1 = [price[counter]]
    cuv1 = str(cuv1) # volume
    cuv1 = cuv1[64: -20]
    cuv1 = float(cuv1)

    cu1L = [price[counter]]
    cu1L = str(cu1L) # Low
    cu1L = cu1L[44: -42]
    cu1L = float(cu1L)

    cu1H = [price[counter]]
    cu1H = str(cu1H) # High
    cu1H = cu1H[36: -49]
    cu1H = float(cu1H)

    cu1O = [price[counter]]
    cu1O = str(cu1O) # open
    cu1O = cu1O[29: -57]
    cu1O = float(cu1O)

    counter = counter+1 # counter

    cu2 = [price[counter]]
    cu2 = str(cu2)
    cu2 = cu2[53:-30]
    cu2 = float(cu2)

    cuv2 = [price[counter]]
    cuv2 = str(cuv2) # volume
    cuv2 = cuv2[64: -20]
    cuv2 = float(cuv2)

    cu2L = [price[counter]]
    cu2L = str(cu2L) # Low
    cu2L = cu2L[44: -42]
    cu2L = float(cu2L)

    cu2H = [price[counter]]
    cu2H = str(cu2H) # High
    cu2H = cu2H[36: -49]
    cu2H = float(cu2H)

    cu2O = [price[counter]]
    cu2O = str(cu2O) # open
    cu2O = cu2O[29: -57]
    cu2O = float(cu2O)

    counter = counter+1 # counter
    
    cu3 = [price[counter]]
    cu3 = str(cu3)
    cu3 = cu3[53:-30]
    cu3 = float(cu3)

    cuv3 = [price[counter]]
    cuv3 = str(cuv3)
    cuv3 = cuv3[64: -20]
    cuv3 = float(cuv3)

    cu3L = [price[counter]]
    cu3L = str(cu3L) # Low
    cu3L = cu3L[44: -42]
    cu3L = float(cu3L)

    cu3H = [price[counter]]
    cu3H = str(cu3H) # High
    cu3H = cu3H[36: -49]
    cu3H = float(cu3H)

    cu3O = [price[counter]]
    cu3O = str(cu3O) # open
    cu3O = cu3O[29: -57]
    cu3O = float(cu3O)

    counter = counter+1 # counter

    cu4 = [price[counter]]
    cu4 = str(cu4)
    cu4 = cu4[53:-30]
    cu4 = float(cu4)

    cuv4 = [price[counter]]
    cuv4 = str(cuv4)
    cuv4 = cuv4[64: -20]
    cuv4 = float(cuv4)

    cu4L = [price[counter]]
    cu4L = str(cu4L) # Low
    cu4L = cu4L[44: -42]
    cu4L = float(cu4L)

    cu4H = [price[counter]]
    cu4H = str(cu4H) # High
    cu4H = cu4H[36: -49]
    cu4H = float(cu4H)

    cu4O = [price[counter]]
    cu4O = str(cu4O) # open
    cu4O = cu4O[29: -57]
    cu4O = float(cu4O)

    counter = counter+1 # counter
    
    cu5 = [price[counter]]
    cu5 = str(cu5)
    cu5 = cu5[53:-30]
    cu5 = float(cu5)

    cuv5 = [price[counter]]
    cuv5 = str(cuv5)
    cuv5 = cuv5[64: -20]
    cuv5 = float(cuv5)

    cu5L = [price[counter]]
    cu5L = str(cu5L) # Low
    cu5L = cu5L[44: -42]
    cu5L = float(cu5L)

    cu5H = [price[counter]]
    cu5H = str(cu5H) # High
    cu5H = cu5H[36: -49]
    cu5H = float(cu5H)

    cu5O = [price[counter]]
    cu5O = str(cu5O) # open
    cu5O = cu5O[29: -57]
    cu5O = float(cu5O)
    time.sleep(5)

    date = datetime.datetime.now()
    date = str(date)

    array_data[count] = cu5

    if (first_time > 1) and (array_data[count-1] != cu5): 
        tradable = True

    if tradable == True:
        if (cuv5 > cuv4) and (cuv4 > cuv3) and (cuv2 > cuv1):
            print(Fore.LIGHTBLACK_EX+"🖳",str(date),Fore.WHITE+"▼ SOLD! 'HG=F' stock for:",Fore.RED+"",round(cu5*yen,3),"¥")
            sell = True
            buy = False
        elif (cu5 >= cu4) and (cu5 >= cu3) or (cu5 >= cu2) and (cu5 >= cu1):
            print(Fore.LIGHTBLACK_EX+"🖳",str(date),Fore.WHITE+"▼ SOLD! 'HG=F' stock for:",Fore.RED+"",round(cu5*yen,3),"¥")
            sell = True
            buy = False
        elif (cuv5 < cuv4) and (cuv4 < cuv3) and (cuv2 < cuv1):
            print(Fore.LIGHTBLACK_EX+"🖳",str(date),Fore.WHITE+"BOUGHT! 'HG=F' stock for:",Fore.GREEN+"",round(cu5*yen,3),"¥ ▲")
            buy = True
            sell = False
        elif (cuv5 > cuv4) and (cuv4 > cuv3) and (cuv2 > cuv1):
            print(Fore.LIGHTBLACK_EX+"🖳",str(date),Fore.WHITE+"▼ SOLD! 'HG=F' stock for:",Fore.RED+"",round(cu5*yen,3),"¥")
            buy = True
            sell = False
        elif ((cu1O > cu1) and (cu2O > cu2) and (cu3O > cu3)) or ((cu2O > cu2) and (cu4O > cu4) and (cu5O > cu5)):
            print(Fore.LIGHTBLACK_EX+"🖳",str(date),Fore.WHITE+"BOUGHT! 'HG=F' stock for:",Fore.GREEN+"",round(cu5*yen,3),"¥")
            buy = True
            sell = False
        elif ((cu1O < cu1) and (cu2O < cu2) and (cu3O < cu3)) or ((cu2O < cu2) and (cu4O < cu4) and (cu5O < cu5)):
            print(Fore.LIGHTBLACK_EX+"🖳",str(date),Fore.WHITE+"SOLD! 'HG=F' stock for:",Fore.RED+"",round(cu5*yen,3),"¥ ▼",)
            sell = True
            buy = True
        elif (cuv5 > cuv4) and (cuv5 > cuv3):
            print(Fore.LIGHTBLACK_EX+"🖳",str(date),Fore.WHITE+"SOLD! 'HG=F' stock for:",Fore.RED+"",round(cu5*yen,3),"¥ ▼",)
            sell = True
            buy = False
        elif (cuv5 < cuv4) and (cuv5 < cuv3) and (cuv5 < cuv2) and (cuv5 < cuv1):
            print(Fore.LIGHTBLACK_EX+"🖳",str(date),Fore.WHITE+"BOUGHT! 'HG=F' stock for:",Fore.GREEN+"",round(cu5*yen,3),"¥ ▲")
            buy = True
            sell = False
        elif ((cu5O >= cu5) and (cu4O >= cu4)) or ((cu3O >= cu3) and (cu4O >= cu4)):
            print(Fore.LIGHTBLACK_EX+"🖳",str(date),Fore.WHITE+"SOLD! 'HG=F' stock for:",Fore.RED+"",round(cu5*yen,3),"¥ ▼",)
            sell = True
            buy = False
        elif (cuv5 < cuv4) and (cu4O < cu5O) and (cu5L < cu4L): 
            print(Fore.LIGHTBLACK_EX+"🖳",str(date),Fore.WHITE+"BOUGHT! 'HG=F' stock for:",Fore.GREEN+"",round(cu5*yen,3),"¥ ▲")
            buy = True
            sell = False
        elif (cu5L < cu3L) and (cu5L < cu2L) and (cu5L < cu1L):
            print(Fore.LIGHTBLACK_EX+"🖳",str(date),Fore.WHITE+"BOUGHT! 'HG=F' stock for:",Fore.GREEN+"",round(cu5*yen,3),"¥ ▲")
            buy = True
            sell = False
        elif (cu5O > cu5):
            print(Fore.LIGHTBLACK_EX+"🖳",str(date),Fore.WHITE+"SOLD! 'HG=F' stock for:",Fore.RED+"",round(cu5*yen,3),"¥",)
            sell = True
            buy = False
        else:
            buy = False
            sell = False
        
        if (sell == True) and (buy == False) and (array_data[count-1] > array_data[count]):
            bot_rich = bot_rich + (array_data[count-1]*yen*striking_Rate)
            print(Fore.LIGHTGREEN_EX+"💰 ",Fore.LIGHTBLACK_EX+"BOT Made:",Fore.WHITE+ str(round(bot_rich,3)),Fore.LIGHTGREEN_EX+"≈ ¥",Fore.WHITE+str(round(bot_rich*0.1096,3)),Fore.LIGHTGREEN_EX+"≈ £",Fore.WHITE+str(round(bot_rich*0.14,3)),Fore.LIGHTGREEN_EX+"≈ $")
        elif (sell == False) and (buy == True) and (array_data[count-1] < array_data[count]):
            bot_rich = bot_rich + (array_data[count-1]*yen*striking_Rate)
            print(Fore.LIGHTGREEN_EX+"💰 ",Fore.LIGHTBLACK_EX+"BOT Made:",Fore.WHITE+ str(round(bot_rich,3)),Fore.LIGHTGREEN_EX+"≈ ¥",Fore.WHITE+str(round(bot_rich*0.1096,3)),Fore.LIGHTGREEN_EX+"≈ £",Fore.WHITE+str(round(bot_rich*0.14,3)),Fore.LIGHTGREEN_EX+"≈ $")
        elif (sell == False) and (buy == True) and (array_data[count-1] > array_data[count]):
            bot_rich = bot_rich - cu5*yen
            print(Fore.LIGHTGREEN_EX+"💰 ",Fore.LIGHTBLACK_EX+"BOT Made:",Fore.WHITE+ str(round(bot_rich,3)),Fore.LIGHTGREEN_EX+"≈ ¥",Fore.WHITE+str(round(bot_rich*0.1096,3)),Fore.LIGHTGREEN_EX+"≈ £",Fore.WHITE+str(round(bot_rich*0.14,3)),Fore.LIGHTGREEN_EX+"≈ $")
        elif (sell == True) and (array_data[count-2] < array_data[count]):
            bot_rich = bot_rich - cu5*yen
            print(Fore.LIGHTGREEN_EX+"💰 ",Fore.LIGHTBLACK_EX+"BOT Made:",Fore.WHITE+ str(round(bot_rich,3)),Fore.LIGHTGREEN_EX+"≈ ¥",Fore.WHITE+str(round(bot_rich*0.1096,3)),Fore.LIGHTGREEN_EX+"≈ £",Fore.WHITE+str(round(bot_rich*0.14,3)),Fore.LIGHTGREEN_EX+"≈ $")
        elif (buy == True) and (array_data[count-1] >= array_data[count]):
            bot_rich = bot_rich - cu5*yen
            print(Fore.LIGHTGREEN_EX+"💰 ",Fore.LIGHTBLACK_EX+"BOT Made:",Fore.WHITE+ str(round(bot_rich,3)),Fore.LIGHTGREEN_EX+"≈ ¥",Fore.WHITE+str(round(bot_rich*0.1096,3)),Fore.LIGHTGREEN_EX+"≈ £",Fore.WHITE+str(round(bot_rich*0.14,3)),Fore.LIGHTGREEN_EX+"≈ $")


        count = count+1
        array_data[count] = cu5
 
    tradable = False
    first_time = first_time+1
    buy = False
    sell = False
    time.sleep(57)

print(Fore.WHITE+"\n𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡𝇡")
print(Fore.LIGHTBLACK_EX+"▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅")