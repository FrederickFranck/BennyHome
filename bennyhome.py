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

# GPIO PINS LADEN UIT DE CONFIG
CONFIG = toml.load('config.toml')
BUTTON_PINS = CONFIG.get("GPIO").get("Buttons")
RELAY_PINS = CONFIG.get("GPIO").get("Relays")

# LISTS
buttons = []
relays = []

# Maak een lijst aan met buttons en stelt de event handler functie in
def initialize_buttons():
    global buttons
    for pin in BUTTON_PINS:
        buttons.append(Button(pin=pin))
        press_count.append(0)


# Maak een lijst aan met Relays
def initialize_relays():
    global relays
    for pin in RELAY_PINS:
        relays.append(DigitalOutputDevice(pin=pin, active_high=True,
                                          initial_value=False))


# Geeft de staat van de button terug
def check_button(index):
    button = buttons[index]
    relay = relays[index]
    if(check_button(button)):
        toggle_relay(relay)


# Geeft de staat van de relay terug
def check_button(button):
    return button.value


# Zet de relay uit als hij aanstaat en aan als hij uitstaat
def toggle_relay(relay):
    relay.off() if relay.value else relay.on()

# Gaat voor elke knop nakijken of er gedrukt is
# en bestuurt de relays volgens de flowchart
def loop():
    while True:
        for index in range(len(buttons)):
            check_button(index)

# Main functie
def main():
    try:
        initialize_buttons()
        initialize_relays()
        loop()
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    main()
