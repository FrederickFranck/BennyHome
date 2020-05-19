#!/usr/bin/env python3

'''
Rapsi code voor huisje
'''

__author__ = "Frédèrick Franck"
__version__ = "1.0.0"
__license__ = "MIT"

from gpiozero import DigitalOutputDevice
from gpiozero import Button
import toml
import time

# GPIO PINS LADEN UIT DE CONFIG
CONFIG = toml.load('config.toml')
RELAY_PINS = CONFIG.get("GPIO").get("Relays")

# LISTS
relays = []
buttons = []






def initialize_buttons():
    global buttons
    for pin in BUTTON_PINS:
        buttons.append(Button(pin=pin))


# Maak een lijst aan met Relays
def initialize_relays():
    global relays
    for pin in RELAY_PINS:
        relays.append(DigitalOutputDevice(pin=pin, active_high=True,
                                          initial_value=False))

# Zet de relay uit als hij aanstaat en aan als hij uitstaat
def toggle_relay(relay):
    if(relay.value):
        relay.off()
    else:
        relay.on()

def test():
    global buttons
    for i in range(1,27):
        buttons.append(Button(pin=i))
    for btn in buttons:
        btn.when_pressed = button_is_pressed

# Event handler functie voor als de knop ingedrukt wordt
def button_is_pressed(button):
    print(button.pin)


def loop():
    while True:
        continue


# Main functie
def main():
    #initialize_relays()
    test()
    loop()


if __name__ == "__main__":
    main()
