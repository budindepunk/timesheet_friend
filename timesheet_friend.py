from tkinter import *
from tkinter import simpledialog
from datetime import datetime
import calendar
from os.path import exists

root = Tk()
root.withdraw()

now = datetime.now()
hour = now.hour
day =  calendar.day_name[now.weekday()]
date = now.day

# popup
message = "qué estuviste haciendo entre " + str(hour-1) + " y " + str(hour) + "? (¡docket!)"
input = simpledialog.askstring("input", message)
message_log = day + "| " + str(hour-1) + " - " + str(hour) + ": " + input

# this is supposed to just create a new file every week. it is friday as i write this so next week will be week 1
week_number = datetime.now().isocalendar()[1]
nombre_txt = "week " + str(week_number) + ".txt"

def new_day():
    file.write("\n \n---- " + day + " " + str(date) + "\n")

# open the file or create it
if not exists(nombre_txt):
    open(nombre_txt, 'w')

file = open(nombre_txt, "r+")
lines = []
lines = file.readlines()
# check if its a new week
if len(lines) == 0: 
    new_day()
else:
    last_line = lines[-1]
    # check if its the beginning of a day (hourly logs end with line breaks)
    if last_line != "\n":
        new_day()

# create hourly log and save file
file.write(message_log + "\n")
if hour == 18 or hour == 19:
    file.write("EOD")

file.close()

# quit TK
root.quit()
root.destroy()