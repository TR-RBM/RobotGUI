#!/usr/bin/python
# -*- coding: UTF-8 -*-

# RobotGUI
# von Tim Richter

# Todo: Lite 100 -> init cords


# Bibliotheken Importieren ##
from graphics import *
import subprocess as sp
import re, math, time, platform
try:
    import ctypes
except:
    print("Error while importing win32api..")

#
default_x = 480
default_y = 320
# Programm name
programm_name = "RobotGUI"
log = True
###############

class window:
    def __init__(self, win, screen_x, screen_y, log):
        print(win, screen_x, screen_y)
        self.win = win
        first_run = True
        while True:

            # Set background and draw grid
            if first_run == True:
                self.win.setBackground("white")
                # v =vertikal / h = horizontal

                _oberer_abstand = 0
                _laenge_nach_unten = 80
                _linker_abstand = 0
                _laenge_nach_rechts = 80

                _screen_x = (screen_x/100*80)
                _screen_y = (screen_y/100*80)

                vobabst = int(_screen_y/100*_oberer_abstand)    # Vertikaler oberer abstand
                vlnu   = int(screen_y/100*_laenge_nach_unten)   # Vertikale länge nach unten
                hliabst = int(_screen_x/100*_linker_abstand)    # horizontaler linker abstand

                v1x = int(_screen_x/7*1)
                v2x = int(_screen_x/7*2)
                v3x = int(_screen_x/7*3)
                v4x = int(_screen_x/7*4)
                v5x = int(_screen_x/7*5)
                v6x = int(_screen_x/7*6)
                v7x = int(_screen_x)

                h1y = int(_screen_y/5*1)
                h2y = int(_screen_y/5*2)
                h3y = int(_screen_y/5*3)
                h4y = int(_screen_y/5*4)
                h5y = int(_screen_y)

                v1 = Line(Point(v1x, vobabst), Point(v1x, vlnu))
                v2 = Line(Point(v2x, vobabst), Point(v2x, vlnu))
                v3 = Line(Point(v3x, vobabst), Point(v3x, vlnu))
                v4 = Line(Point(v4x, vobabst), Point(v4x, vlnu))
                v5 = Line(Point(v5x, vobabst), Point(v5x, vlnu))
                v6 = Line(Point(v6x, vobabst), Point(v6x, vlnu))
                v7 = Line(Point(v7x, vobabst), Point(v7x, vlnu))

                h1 = Line(Point(hliabst, h1y), Point(_screen_x, h1y))
                h2 = Line(Point(hliabst, h2y), Point(_screen_x, h2y))
                h3 = Line(Point(hliabst, h3y), Point(_screen_x, h3y))
                h4 = Line(Point(hliabst, h4y), Point(_screen_x, h4y))
                h5 = Line(Point(hliabst, h5y), Point(_screen_x, h5y))

                v1.draw(self.win)
                v2.draw(self.win)
                v3.draw(self.win)
                v4.draw(self.win)
                v5.draw(self.win)
                v6.draw(self.win)
                v7.draw(self.win)
                h1.draw(self.win)
                h2.draw(self.win)
                h3.draw(self.win)
                h4.draw(self.win)
                h5.draw(self.win)

                # Liste mit allen Koordinaten, die in der for schleife zu richtigen variablen werden
                cord = [] # Deklariere Cords um dort späte die richtigen variablen zu speichern.
                a1 = [[0,0], [v1x, h1y]]
                a2 = []
                a3 = []
                a4 = []
                a5 = []
                a6 = []
                a7 = []
                b1 = []
                b2 = []
                b3 = []
                b4 = []
                b5 = []
                b6 = []
                b7 = []
                c1 = []
                c2 = []
                c3 = []
                c4 = []
                c5 = []
                c6 = []
                c7 = []
                d1 = []
                d2 = []
                d3 = []
                d4 = []
                d5 = []
                d6 = []
                d7 = []
                e1 = []
                e2 = []
                e3 = []
                e4 = []
                e5 = []
                e6 = []
                e7 = []

                print()
                # for i in range(int(_screen_x)):
                #     if i <= (_screen_x/7):
                #         a1.append(i)
                #         print(a1)

                del v1, v2 ,v3, v4, v5, v6 ,v7, h1 ,h2 ,h3 ,h4, h5 # Lösche variablen die nicht mehr gebraucht werden
                del vobabst, vlnu, hliabst, _screen_x, screen_y, _oberer_abstand, _laenge_nach_unten, _linker_abstand, _laenge_nach_rechts
                message = Text(Point(screen_x/100*88,50), "Bitte wähle einen Startpunkt\n indem du mit der Maus auf ein Feld drückst.")
                message.draw(self.win)
                first_run = False

            position = self.win.getMouse()
            xm = position.getX()
            ym = position.getY()
            #print ("xm" , xm)
            #print ("ym" , ym)
            if xm > 1345 or ym > 780 :
                print("außerhalb den breich")
            else :
                print("Point", xm , ym)


# Name: read_resolution ( int:STANDART_X_POS , int:STANDART_Y_POS, str: POS x/y/xy, log)
# Nutzen: Liest die Bildschirmgröße
def read_resolution(default_x, default_y, pos, log):
    if platform.system() == "Windows":
        if log == True:
            print("Windows System Detected")
        try:
            user32 = ctypes.windll.user32
            screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
            screen_x = screensize[0]
            screen_y = screensize[1]
        except:
            if log == True:
                print("Error while trying to get screensize")
        if log == True:
            print("Detected Monitor:",screen_x,"x",screen_y)

    else:
        print(platform.system())
        try:
            screen_resolution = sp.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=sp.PIPE).communicate()[0]
            screen_resolution = re.findall(r"\d+", str(screen_resolution))
            screen_x = int(screen_resolution[0])
            screen_y = int(screen_resolution[1])
        except:
            screen_x = default_x
            screen_y = default_y
            print("Es gab einen Fehler beim Lesen der Bildschirmgröße,\nbitte den Entwickler (Tim Richter) informieren\n\nDie standart Bildschirmgröße wurde auf 480x320 festgelegt,\ndie Größe kann am anfang in dem script geändert werden.")
            time.sleep(5)

    if pos == "x":
        return screen_x
    elif pos == "y":
        return screen_y
    elif pos == "xy":
        return screen_x, screen_y
    else:
        print("Unknown error while trying to output screen resolution.")
        time.sleep(5)

def main():
    screen_x = int(int(read_resolution(default_x, default_y, "x", log))/100*90)
    screen_y = int(int(read_resolution(default_x, default_y, "y", log))/100*90)
    win = GraphWin(programm_name, screen_x, screen_y)
    main_window = window(win,screen_x,screen_y, log)






if __name__ == "__main__":
    main()
