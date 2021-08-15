#!/bin/python3

from gui import Gui
from setup import SetUp
from sensor_fake import Sensor
#from sensor import Sensor
from gui_style import GuiStyle

class App(SetUp, Gui, Sensor): pass

if __name__ == '__main__':
    app = App()
    GuiStyle(app.root)
    app.root.mainloop()
