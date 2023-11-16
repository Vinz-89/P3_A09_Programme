# Imports go at the top
from microbit import *
import microbit
import radio
import music

radio.on()
radio.config(group=23)



state = ["endormi", "agité", "très agité"]

image = Image.HAPPY
def update_image(image):
    if image == Image.HAPPY:
        image = Image.SAD
    elif image == Image.SAD:
        image = Image.HAPPY

    display.show(image)
    return image

state_b = state[0]
def update_state(state):
    state_b = state


def send_message(type, longueur, contenu):
    message = type + "|" + longueur + "|" + contenu


    radio.send(message)

    receive_message(message)
    
    return message

def receive_message(message):
    message_item = message.split("|")
    
    if(message_item[0] == "sound"):
        audio.play(Sound.HAPPY)
    
    
    
    return message_item

def sound_Detected():
    lightsOn = not lightsOn
    if lightsOn:
        display.show(Image.HEART)
    else:
        display.clear()

    

# Code in a 'while True:' loop repeats forever
steps=0
lightsOn = False

while True:
    if microbit.button_a.is_pressed():
        image = update_image(image)



        sleep(500)
    elif microbit.button_b.is_pressed():
        send_message("sound", "5", "Test Message")
        
        sleep(500)

    

    if microphone.was_event(SoundEvent.LOUD):
        sound_Detected()
        
        sleep(500)
    

    message = radio.receive()
    if message:
        display.scroll(message)
