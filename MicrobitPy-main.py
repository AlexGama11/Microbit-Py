# Imports go at the top
from microbit import *
import music
import radio
import speech


# Code in a 'while True:' loop repeats forever

SOS = False
BluetoothGroup = 1
Number2 = 0
radio.config(group=BluetoothGroup)
display.scroll("Hi!")
Number2 = 0

def Radio():
    radio.send("Hello World!")
    display.scroll("Message Sent!")

def Shapes():
    display.show(Image.SKULL)
    sleep(200)
    display.show(Image.GHOST)
    sleep(200)
    display.show(Image.CHESSBOARD)
    sleep(200)
    display.show(Image.PITCHFORK)
    sleep(200)

def SOSRadioGroup():
    global BluetoothGroup
    radio.config(group=BluetoothGroup)
    BluetoothGroup += 1
    if BluetoothGroup == 20:
        BluetoothGroup = 0

while True:
    if not (SOS):
        Number2 += 1
        display.scroll(Number2)
        message = radio.receive()
        if message:
            display.clear()
            display.show(message)
        if button_a.is_pressed() and button_b.is_pressed():
            tune = ["C5:4", "B", "A", "G", "G", "A", "B", "C5"]
            #music.play(tune)
            #speech.say("Hello World", speed=200)
            speech.pronounce(' /HEHLOW WERLD')
        elif button_a.was_pressed():
            display.clear()
            Radio()
            Number2 = 0
        elif button_b.was_pressed():
            display.clear()
            Shapes()
            Number2 = 0
    if display.read_light_level() <= 30:
        SOS = True
        radio.send("SOS")
        #speech.say("S", speed=120)
        #speech.say("O", speed=120)
        #speech.say("S", speed=120)
        display.show(Image(
        "00900:"
        "00900:"
        "00900:"
        "00000:"
        "00900"
        ))
        sleep(200)
        display.clear()
        sleep(200)
        SOSRadioGroup()
        if display.read_light_level() > 30:
            SOS = False
            radio.send("Safe!")
    



