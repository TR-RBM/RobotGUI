#!/usr/bin/python
# -*- coding: UTF-8 -*-

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
        self.init_global_variablesx(screen_x, screen_y, win, log)
        if self.log == True:
            print("__init__:                    "+str(win))
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
                self.h5y = int(_screen_y/5*5)

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

            self.position = self.get_current_position()
            self.current_position = self.check_current_position()

            if self.current_position == 2: # Wenn User macht den Ersten klick in ein Feld.
                self.first_position = self.position
                self.draw_current_spot()

            elif self.current_position == 3: # Wenn User macht ein Klick ein anderes Feld was nicht das gleiche ist wie zuvor.
                self.goal = self.current_position
                self.KI_path_finder()
            elif self.current_position == 4:
                self.draw_current_spot()



            #self.draw_message()

        # Name: init_global_variablesx( %%Hier alle localen Variablen die in Globale umgewandelt werden sollen)
        # Funktion: Initiert alle Variablen die von allen Funtkionen innerhalb der Klasse genutz werden sollen.
    def init_global_variablesx(self, screen_x, screen_y, win, log):
        if log == True:
            _init_vars_time_start = time.time() #* 1000.0
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.win = win
        self.log = log
        self.first_run = True
        self.position = ""
        self.old_position = ""
        self.first_position = ""
        self.current_position = ""
        self.first_klick = True
        self.generate_vars = True
        self.spots=["A1" ,"A2" , "A3", "A4", "A5","B1", "B2", "B3", "B4", "B5","C1", "C2", "C3", "C4", "C5","D1", "D2", "D3", "D4", "D5","E1" ,"E2" ,"E3" ,"E4" ,"E5","F1", "F2", "F3", "F4" ,"F5" ,"G1" ,"G2" ,"G3" , "G4", "G5"]
        for i in self.spots:
            if i[0] == "A":
                execute_string = "self."+i+" =\"1"+i[1]+"\""
            if i[0] == "B":
                execute_string = "self."+i+" =\"2"+i[1]+"\""
            if i[0] == "C":
                execute_string = "self."+i+" =\"3"+i[1]+"\""
            if i[0] == "D":
                execute_string = "self."+i+" =\"4"+i[1]+"\""
            if i[0] == "E":
                execute_string = "self."+i+" =\"5"+i[1]+"\""
            if i[0] == "F":
                execute_string = "self."+i+" =\"6"+i[1]+"\""
            if i[0] == "G":
                execute_string = "self."+i+" =\"7"+i[1]+"\""
            exec(execute_string)
        if self.log == True:
            _init_vars_time_end = time.time() #* 1000.0
            print(_init_vars_time_start, "\n", _init_vars_time_end)
            _init_vars_time = _init_vars_time_end - _init_vars_time_start
            print("init_global_variablesx:      Job done in", _init_vars_time, "ms")
            del _init_vars_time, _init_vars_time_end, _init_vars_time_start

    # name: get_current_position( float: self.xm , float: self.ym)
    # Funktion: liest Mausklick und gibt zurück in welches feld geklickt wurde.
    def get_current_position(self):
                    position = self.win.getMouse()
                    self.xm = position.getX()
                    self.ym = position.getY()
                    if self.xm > self.v7x or self.ym > self.h5y :
                        _out ="0"
                    elif self.v1x >= self.xm >= 0 and  self.h1y >= self.ym >= 0:
                        _out = "A1"
                    elif self.v1x >= self.xm >= 0 and self.h2y >= self.ym >= self.h1y:
                        _out = "A2"
                    elif self.v1x >= self.xm >= 0 and self.h3y >= self.ym >= self.h2y:
                        _out = "A3"
                    elif self.v1x >= self.xm >= 0 and self.h4y >= self.ym >= self.h3y:
                        _out = "A4"
                    elif self.v1x >= self.xm >= 0 and self.h5y >= self.ym >= self.h4y:
                        _out = "A5"
                    elif self.v2x >= self.xm >= self.v1x and self.h1y >= self.ym >= 0:
                        _out = "B1"
                    elif self.v2x >= self.xm >= self.v1x and self.h2y >= self.ym >= self.h1y:
                        _out = "B2"
                    elif self.v2x >= self.xm >= self.v1x and self.h3y >= self.ym >= self.h2y:
                        _out = "B3"
                    elif self.v2x >= self.xm >= self.v1x and self.h4y >= self.ym >= self.h3y:
                        _out = "B4"
                    elif self.v2x >= self.xm >= self.v1x and self.h5y >= self.ym >= self.h4y:
                        _out = "B5"
                    elif self.v3x >= self.xm >= self.v2x and self.h1y >= self.ym >= 0:
                        _out = "C1"
                    elif self.v3x >= self.xm >= self.v2x and self.h2y >= self.ym >= self.h1y:
                        _out = "C2"
                    elif self.v3x >= self.xm >= self.v2x and self.h3y >= self.ym >= self.h2y:
                        _out = "C3"
                    elif self.v3x >= self.xm >= self.v2x and self.h4y >= self.ym >= self.h3y:
                        _out = "C4"
                    elif self.v3x >= self.xm >= self.v2x and self.h5y >= self.ym >= self.h4y:
                        _out = "C5"
                    elif self.v4x >= self.xm >= self.v3x and self.h1y >= self.ym >= 0:
                        _out = "D1"
                    elif self.v4x >= self.xm >= self.v3x and self.h2y >= self.ym >= self.h1y:
                        _out = "D2"
                    elif self.v4x >= self.xm >= self.v3x and self.h3y >= self.ym >= self.h2y:
                        _out = "D3"
                    elif self.v4x >= self.xm >= self.v3x and self.h4y >= self.ym >= self.h3y:
                        _out = "D4"
                    elif self.v4x >= self.xm >= self.v3x and self.h5y >= self.ym >= self.h4y:
                        _out = "D5"
                    elif self.v5x >= self.xm >= self.v4x and self.h1y >= self.ym >= 0:
                        _out = "E1"
                    elif self.v5x >= self.xm >= self.v4x and self.h2y >= self.ym >= self.h1y:
                        _out = "E2"
                    elif self.v5x >= self.xm >= self.v4x and self.h3y >= self.ym >= self.h2y:
                        _out = "E3"
                    elif self.v5x >= self.xm >= self.v4x and self.h4y >= self.ym >= self.h3y:
                        _out = "E4"
                    elif self.v5x >= self.xm >= self.v4x and self.h5y >= self.ym >= self.h4y:
                        _out = "E5"
                    elif self.v6x >= self.xm >= self.v5x and self.h1y >= self.ym >= 0:
                        _out = "F1"
                    elif self.v6x >= self.xm >= self.v5x and self.h2y >= self.ym >= self.h1y:
                        _out = "F2"
                    elif self.v6x >= self.xm >= self.v5x and self.h3y >= self.ym >= self.h2y:
                        _out = "F3"
                    elif self.v6x >= self.xm >= self.v5x and self.h4y >= self.ym >= self.h3y:
                        _out = "F4"
                    elif self.v6x >= self.xm >= self.v5x and self.h5y >= self.ym >= self.h4y:
                        _out = "F5"
                    elif self.v7x >= self.xm >= self.v6x and self.h1y >= self.ym >= 0:
                        _out = "G1"
                    elif self.v7x >= self.xm >= self.v6x and self.h2y >= self.ym >= self.h1y:
                        _out = "G2"
                    elif self.v7x >= self.xm >= self.v6x and self.h3y >= self.ym >= self.h2y:
                        _out = "G3"
                    elif self.v7x >= self.xm >= self.v6x and self.h4y >= self.ym >= self.h3y:
                        _out = "G4"
                    elif self.v7x >= self.xm >= self.v6x and self.h5y >= self.ym >= self.h4y:
                        _out = "G5"
                    if self.log == True:
                        print("get_current_position:        Es wurde:", _out , "gedrückt")
                    return _out

    # name: check_current_position()
    # Funktion: Gibt zurück ob das gleiche Feld wie vorher gedrückt wurde oder ob ein anderes feld gedrückt wurde.
    def check_current_position(self):
        if self.position == "0":
            if self.log == True:
                print("check_current_position:      1 - Klick ist außerhalb des Bereiches.")
            return 1 # Wenn außerhalb des Bereiches.
        elif self.old_position == "":
            self.old_position = self.position
            if self.log == True:
                print("check_current_position:      2 - Erster klick in einem Feld wurde erkannt.")
            return 2 # Wenn erster klick in ein bereich
        elif self.position == self.old_position :
            if self.log == True:
                print("check_current_position:      3 - Das gleiche Feld wurde gedrückt.")
            return 3 # Wenn klick auf das gleiche feld wie vorher
        elif self.position != self.old_position :
            self.old_position = self.position
            if self.log == True:
                print("check_current_position:      4 - Es wurde auf ein neues Feld gedrückt.")
            return 4 # Wenn klick auf ein neues Feld.

    def KI_path_finder(self):
        if self.current_position == self.goal:
            if self.log == True:
                print("KI_path_finder:              Ziel ist gelich wie aktuelle Position")

    def draw_current_spot(self):
        for i in self.spots:
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
                if self.log == True:
                    print("draw_current_spot:           "+str(i)+" wurde ROT makiert")
                execute_string = "self.pint"+str(i)+".setFill(\"red\")"
                exec(execute_string)
            else:
                execute_string = "self.pint"+str(i)+".setFill(\"white\")"
                exec(execute_string)
        self.generate_vars = False

    #def draw_message(self):
        #if message != "" :
        #    message.undraw(self.win)
    #    msg1="Außerhalb des Breiches."
    #    msg2=str(self.position)+" ist die aktuelle start Position."
    #    msg3="Der gewünschte Platz ist bereits die aktuelle Position."+str(self.old_position)
    #    msg4=str(self.old_position)+"ist die aktuelle Position."
    #    msg5=str(self.position)+"wurde gedückt."
    #    print(self.check_current_position())
    #    if self.check_current_position() == 1 :
    #        message = Text(Point(self.screen_x/100*90,60), msg1)
    #    elif self.check_current_position() == 2 :
    #        message = Text(Point(self.screen_x/100*90,60), msg2)
    #    elif self.check_current_position() == 3 :
    #        message = Text(Point(self.screen_x/100*90,60), msg3)
    #    elif self.check_current_position() == 4 :
    #        message = Text(Point(self.screen_x/100*90,60), msg4 + msg5)
    #    message.draw(self.win)


# Name: read_resolution ( int:STANDART_X_POS , int:STANDART_Y_POS, str: POS x/y/xy, log)
# Nutzen: Liest die Bildschirmgröße
def read_resolution(default_x, default_y, pos, log):
    if platform.system() == "Windows":
        if log == True:
            print("read_resolution:             Windows System Detected")
        try:
            user32 = ctypes.windll.user32
            screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
            screen_x = screensize[0]
            screen_y = screensize[1]
        except:
            if log == True:
                print("read_resolution:         Error while trying to get screensize")
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
            print("Es gab einen Fehler beim Lesen der Bildschirmgröße,\nin der Funktion read_resolution().\nEs werden Standard Werte verwendet!")

    if pos == "x":
        if log == True:
            print("read_resolution:             Detected Monitor X:",screen_x)
        return screen_x
    elif pos == "y":
        if log == True:
            print("read_resolution:             Detected Monitor Y:",screen_y)
        return screen_y
    elif pos == "xy":
        return screen_x, screen_y
    else:
        print("\nEin unbekannter Fehler ist aufgetrerten.\nDer Fehler ist in read_resolution() und trat wärend des versuches auf,\n die Bildschirmgröße zu lesne.\nBitte Melden Sie dies den Entwicklern des Programmes.")
        time.sleep(10)
        exit()


def main():
    screen_x = int(int(read_resolution(default_x, default_y, "x", log))/100*90)
    screen_y = int(int(read_resolution(default_x, default_y, "y", log))/100*90)
    win = GraphWin(programm_name, screen_x, screen_y)
    main_window = window(win,screen_x,screen_y, log)


if __name__ == "__main__":
    main()
