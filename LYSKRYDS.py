from random import random
from time import sleep
x=1

def Rød_ØV():
    print('\x1b[6;30;41m' + "Rød!" + '\x1b[0m')

def Rød_NS():
    print('\x1b[6;30;41m' + "Rød!" + '\x1b[0m')

def Gul_ØV():
    print('\x1b[6;30;43m' + "Gul!" + '\x1b[0m')

def Gul_NS():
    print('\x1b[6;30;43m' + "Gul!" + '\x1b[0m')

def Grøn_ØV():
    print('\x1b[6;30;42m' + "Grøn!" + '\x1b[0m')

def Grøn_NS():
    print('\x1b[6;30;42m' + "Grøn!" + '\x1b[0m')

def state0(x):
    if x=="NS":
        x="ØV"
        Rød_NS()
        Rød_ØV()
        print()
        sleep(2)
        return state1()
    elif x=="ØV":
        x="NS"
        Rød_ØV()
        Rød_NS()
        print()
        sleep(2)
        return state4()

def state1():
    Rød_ØV()
    Rød_NS()
    Gul_NS()
    print()
    sleep(1)
    return state2()

def state2():
    Rød_ØV()
    Grøn_NS()
    print()
    sleep(10)
    return state3()

def state3():
    Rød_ØV()
    Gul_NS()
    print()
    sleep(2)
    return state0("ØV")

def state4():
    Rød_NS()
    Rød_ØV()
    Gul_ØV()
    print()
    sleep(1)
    return state5()

def state5():
    Rød_NS()
    Grøn_ØV()
    print()
    sleep(10)
    return state6()

def state6():
    Rød_NS()
    Gul_ØV()
    print()
    sleep(2)
    return state0("NS")

state=state0(x="NS")
while state: state=state("NS")
print ("Done with states")
