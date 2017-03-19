#!/usr/bin/env python
"""A Python3 module for the betterment of developers everywhere.  Linted 10/10"""

from time import sleep

YEARS = 20
WAR_WOUNDS = 111
RELEASES = 9001

class Dev(object):
    """The developer"""
    weekend = False
    experience = None
    weather = "0"

    def __init__(self, experience):
        self.experience = experience

    def set_weekend(self, weekend):
        """set that weekend"""
        self.weekend = weekend

    def set_weather(self, temp):
        """Set that weather"""
        self.weather = str(temp)

    def input(self, drink):
        """Input that drink"""

        print("A", drink['beverage'], "with a", drink['garnish']['fruit'],
              drink['garnish']['shape'] + ". ", end='')

        for _ in range(1, 5):
            print("Glug..", end='', flush=True)
            sleep(1)

        print("ahhhh. Perfect in", self.weather, "degrees. ", end='')

        if self.weekend:
            print("It prepares my mind for the next week of coding. ", end='')
        else:
            print("It makes the coding go faster during the week. ", end='')

        print("With", self.experience['war_wounds'], "war wounds, I need another.")

def main():
    """main, because I like to script"""

    dev = Dev({'years':YEARS, 'war_wounds':WAR_WOUNDS, 'releases':RELEASES})
    dev.set_weekend(True)
    dev.set_weather(32)
    drink = {'beverage':"corona", 'garnish':{'fruit':"lime", 'shape':'wedge'}}
    while True:
        dev.input(drink)

if __name__ == "__main__":
    # execute only if run as a script
    main()
