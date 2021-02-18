#Statemachine til beskrivelse af livets gang
#from gpiozero import LED
#from time import sleep

#NSred=LED(13)
#NSgul=LED(19)
#NSgreen=LED(26)
#EVred=LED(21)
#EVgul=LED(20)
#EVgreen=LED(16)


print("Test!")
EVred.on()
sleep(1)
EVgreen.on()
sleep(1)
EVgul.on()
sleep(1)
NSred.on()
sleep(1)
NSgreen.on()
sleep(1)
NSgul.on()
sleep(1)
EVred.off()
EVgreen.off()
EVgul.off()
NSred.off()
NSgreen.off()
NSgul.off()

def redred(x):# Udgangs punkt for lyskrydset
    if x=="NS": #Hvis lyskrydset kommer fra NS skal den gå til EV
        x="EV"
        print("NS RED   EV RED")
        NSred.on()
        EVred.on()
        sleep(2)
        return EV(x)
    elif x=="EV": #Hvis lyskrydset kommer fra EV skal den gå til NS
        x="NS"
        print("NS red   EV red")
        NSred.on()
        EVred.on()
        sleep(2)
        return NS(x)

def NS():
    NSred.on()
    EVred.on()
    sleep(2)
    return NS_gul()

def NS_green():
    NSgreen.on()
    EVred.on()
    sleep(10)
    return redred()

def NS_gul():
    NSred.on()
    NSgul.on()
    Evred.on()
    sleep(1)
    return NS_green()

def EV():
    EVred.on()
    NSred.on()
    sleep(2)
    return EV_gul()

def EV_green():
    EVgreen.on()
    NSred.on()
    sleep(10)
    return redred()

def EV_gul():
    EVred.on()
    EVgul.on()
    NSred.on()
    sleep(1)
    return EV_green()

state=redred(x="EV")
while state: state=redred(x="EV")
