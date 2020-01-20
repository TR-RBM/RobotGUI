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
log = False
###############

class window:
    def __init__(self, win, screen_x, screen_y, log):
        print(win, screen_x, screen_y)
        self.win = win
        self.first_run = True
        self.old_position = ""
        self.aktuel_position = ""
        self.first_klick = True
        self.generate_vars = True
        while True:

            # Set background and draw grid
            if self.first_run == True:
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

                self.v1x = int(_screen_x/7*1)
                self.v2x = int(_screen_x/7*2)
                self.v3x = int(_screen_x/7*3)
                self.v4x = int(_screen_x/7*4)
                self.v5x = int(_screen_x/7*5)
                self.v6x = int(_screen_x/7*6)
                self.v7x = int(_screen_x/7*7)

                self.h1y = int(_screen_y/5*1)
                self.h2y = int(_screen_y/5*2)
                self.h3y = int(_screen_y/5*3)
                self.h4y = int(_screen_y/5*4)
                self.h5y = int(_screen_y)

                v1 = Line(Point(self.v1x, vobabst), Point(self.v1x, vlnu))
                v2 = Line(Point(self.v2x, vobabst), Point(self.v2x, vlnu))
                v3 = Line(Point(self.v3x, vobabst), Point(self.v3x, vlnu))
                v4 = Line(Point(self.v4x, vobabst), Point(self.v4x, vlnu))
                v5 = Line(Point(self.v5x, vobabst), Point(self.v5x, vlnu))
                v6 = Line(Point(self.v6x, vobabst), Point(self.v6x, vlnu))
                v7 = Line(Point(self.v7x, vobabst), Point(self.v7x, vlnu))

                h1 = Line(Point(hliabst, self.h1y), Point(_screen_x, self.h1y))
                h2 = Line(Point(hliabst, self.h2y), Point(_screen_x, self.h2y))
                h3 = Line(Point(hliabst, self.h3y), Point(_screen_x, self.h3y))
                h4 = Line(Point(hliabst, self.h4y), Point(_screen_x, self.h4y))
                h5 = Line(Point(hliabst, self.h5y), Point(_screen_x, self.h5y))

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

                message = Text(Point(screen_x/100*88,50), "Bitte wähle einen positionpunkt\n indem du mit der Maus auf ein Feld drückst.")
                message.draw(self.win)


            self.position = self.get_current_position(log)
            print("CORDS:", self.xm,self.ym)
            self.check_current_position()
            self.draw_current_spot()





    # name: get_current_position( float: XM , float: ym, bool: log)
    # Funktion: liest Mausklick und gibt zurück in welches feld geklickt wurde.
    def get_current_position(self, log):
                    position = self.win.getMouse()
                    self.xm = position.getX()
                    self.ym = position.getY()
                    xm = self.xm
                    ym = self.ym
                    if xm > self.v7x or ym > self.h5y :
                        _out ="0"
                    if self.v1x >= xm >= 0 and  self.h1y >= ym >= 0:
                        _out = "A1"
                    if self.v1x >= xm >= 0 and self.h2y >= ym >= self.h1y:
                        _out = "A2"
                    if self.v1x >= xm >= 0 and self.h3y >= ym >= self.h2y:
                        _out = "A3"
                    if self.v1x >= xm >= 0 and self.h4y >= ym >= self.h3y:
                        _out = "A4"
                    if self.v1x >= xm >= 0 and self.h5y >= ym >= self.h4y:
                        _out = "A5"
                    if self.v2x >= xm >= self.v1x and self.h1y >= ym >= 0:
                        _out = "B1"
                    if self.v2x >= xm >= self.v1x and self.h2y >= ym >= self.h1y:
                        _out = "B2"
                    if self.v2x >= xm >= self.v1x and self.h3y >= ym >= self.h2y:
                        _out = "B3"
                    if self.v2x >= xm >= self.v1x and self.h4y >= ym >= self.h3y:
                        _out = "B4"
                    if self.v2x >= xm >= self.v1x and self.h5y >= ym >= self.h4y:
                        _out = "B5"
                    if self.v3x >= xm >= self.v2x and self.h1y >= ym >= 0:
                        _out = "C1"
                    if self.v3x >= xm >= self.v2x and self.h2y >= ym >= self.h1y:
                        _out = "C2"
                    if self.v3x >= xm >= self.v2x and self.h3y >= ym >= self.h2y:
                        _out = "C3"
                    if self.v3x >= xm >= self.v2x and self.h4y >= ym >= self.h3y:
                        _out = "C4"
                    if self.v3x >= xm >= self.v2x and self.h5y >= ym >= self.h4y:
                        _out = "C5"
                    if self.v4x >= xm >= self.v3x and self.h1y >= ym >= 0:
                        _out = "D1"
                    if self.v4x >= xm >= self.v3x and self.h2y >= ym >= self.h1y:
                        _out = "D2"
                    if self.v4x >= xm >= self.v3x and self.h3y >= ym >= self.h2y:
                        _out = "D3"
                    if self.v4x >= xm >= self.v3x and self.h4y >= ym >= self.h3y:
                        _out = "D4"
                    if self.v4x >= xm >= self.v3x and self.h5y >= ym >= self.h4y:
                        _out = "D5"
                    if self.v5x >= xm >= self.v4x and self.h1y >= ym >= 0:
                        _out = "E1"
                    if self.v5x >= xm >= self.v4x and self.h2y >= ym >= self.h1y:
                        _out = "E2"
                    if self.v5x >= xm >= self.v4x and self.h3y >= ym >= self.h2y:
                        _out = "E3"
                    if self.v5x >= xm >= self.v4x and self.h4y >= ym >= self.h3y:
                        _out = "E4"
                    if self.v5x >= xm >= self.v4x and self.h5y >= ym >= self.h4y:
                        _out = "E5"
                    if self.v6x >= xm >= self.v5x and self.h1y >= ym >= 0:
                        _out = "F1"
                    if self.v6x >= xm >= self.v5x and self.h2y >= ym >= self.h1y:
                        _out = "F2"
                    if self.v6x >= xm >= self.v5x and self.h3y >= ym >= self.h2y:
                        _out = "F3"
                    if self.v6x >= xm >= self.v5x and self.h4y >= ym >= self.h3y:
                        _out = "F4"
                    if self.v6x >= xm >= self.v5x and self.h5y >= ym >= self.h4y:
                        _out = "F5"
                    if self.v7x >= xm >= self.v6x and self.h1y >= ym >= 0:
                        _out = "G1"
                    if self.v7x >= xm >= self.v6x and self.h2y >= ym >= self.h1y:
                        _out = "G2"
                    if self.v7x >= xm >= self.v6x and self.h3y >= ym >= self.h2y:
                        _out = "G3"
                    if self.v7x >= xm >= self.v6x and self.h4y >= ym >= self.h3y:
                        _out = "G4"
                    if self.v7x >= xm >= self.v6x and self.h5y >= ym >= self.h4y:
                        _out = "G5"

                    # Gib aus was gedückt wurde wenn log = True
                    if log == True:
                        print("Es wurde:", _out , "gedrückt")
                    return _out
    # name: check_current_position()
    # Funktion: Überprüfe ob ein Bereich mehrfach gedrückt wurde
    def check_current_position(self):
        position = self.position
        if position == "0" :
            print("Außerhalb des Breiches.")
        elif self.old_position == "" and position != self.old_position :
            print(position ,"ist die aktuelle start Position.")
            self.old_position = position
        elif position == self.old_position :
            print("Der gewünschte Platz ist bereits die aktuelle Position." , self.old_position)
        elif position != self.old_position :
            print(self.old_position, "ist die aktuelle Position.")
            print(position, "wurde gedückt.")
            self.old_position = position


    def draw_current_spot(self):
        spots=["A1" ,"A2" , "A3", "A4", "A5",
                "B1", "B2", "B3", "B4", "B5",
                "C1", "C2", "C3", "C4", "C5",
                "D1", "D2", "D3", "D4", "D5",
                "E1" ,"E2" ,"E3" ,"E4" ,"E5",
                "F1", "F2", "F3", "F4" ,"F5" ,
                "G1" ,"G2" ,"G3" , "G4", "G5"]
        for i in spots:
            if i[0] == "A":
                X1 = "0"
                X2 = "self.v1x"
                if i[1] != "1":
                    Y1 = "self.h"+str(int(i[1])-1)+"y"
                    Y2 = "self.h"+str(i[1])+"y"
                else:
                    Y1 = "0"
                    Y2 = "self.h1y"
            if i[0] == "B":
                X1 = "self.v1x"
                X2 = "self.v2x"
                if i[1] != "1":
                    Y1 = "self.h"+str(int(i[1])-1)+"y"
                    Y2 = "self.h"+str(i[1])+"y"
                else:
                    Y1 = "0"
                    Y2 = "self.h1y"
            if i[0] == "C":
                X1 = "self.v2x"
                X2 = "self.v3x"
                if i[1] != "1":
                    Y1 = "self.h"+str(int(i[1])-1)+"y"
                    Y2 = "self.h"+str(i[1])+"y"
                else:
                    Y1 = "0"
                    Y2 = "self.h1y"
            if i[0] == "D":
                X1 = "self.v3x"
                X2 = "self.v4x"
                if i[1] != "1":
                    Y1 = "self.h"+str(int(i[1])-1)+"y"
                    Y2 = "self.h"+str(i[1])+"y"
                else:
                    Y1 = "0"
                    Y2 = "self.h1y"
            if i[0] == "E":
                X1 = "self.v4x"
                X2 = "self.v5x"
                if i[1] != "1":
                    Y1 = "self.h"+str(int(i[1])-1)+"y"
                    Y2 = "self.h"+str(i[1])+"y"
                else:
                    Y1 = "0"
                    Y2 = "self.h1y"
            if i[0] == "F":
                X1 = "self.v5x"
                X2 = "self.v6x"
                if i[1] != "1":
                    Y1 = "self.h"+str(int(i[1])-1)+"y"
                    Y2 = "self.h"+str(i[1])+"y"
                else:
                    Y1 = "0"
                    Y2 = "self.h1y"
            if i[0] == "G":
                X1 = "self.v6x"
                X2 = "self.v7x"
                if i[1] != "1":
                    Y1 = "self.h"+str(int(i[1])-1)+"y"
                    Y2 = "self.h"+str(i[1])+"y"
                else:
                    Y1 = "0"
                    Y2 = "self.h1y"
            if self.generate_vars == True:
                execute_string = "self.pint"+str(i)+" = Rectangle(Point("+X1+","+Y1+"), Point("+X2+","+Y2+"))"
                exec(execute_string)
                execute_string = "self.pint"+str(i)+".setFill(\"red\")"
                exec(execute_string)
                execute_string = "self.pint"+str(i)+".draw(self.win)"
                exec(execute_string)
            if self.position == i:
                execute_string = "self.pint"+str(i)+".setFill(\"red\")"
                exec(execute_string)
            else:
                execute_string = "self.pint"+str(i)+".setFill(\"white\")"
                exec(execute_string)

        self.generate_vars = False


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
