#Nelson Hucklebridge
#100614680
#12/12/2023
#TPRG 2131
#rough draft
#from pathlib import Path
import sys
import os, io 
import json, time
#import PySimpleGUI as sg
#import socket
#from time import sleep as sl
'''
IS_RPI = Path("/etc/rpi-issue").exists()
print(IS_RPI)
if (IS_RPI):
    print("Correct Hardware")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('10.150.4.8', 8000))
    except socket.error as err:
        print('Socket error because of %s' %(err))

sg.theme('Light Brown 4')

CIRCLE = '\u26AB'
CIRCLE_OUTLINE = '\u26AA'
    
def LED(color, key):
    return sg.Text(CIRCLE_OUTLINE, text_color=color, key=key)
layout = [ [sg.Text('status 1 '), LED('Green', '-LED0-') ],
           [sg.Button('Exit')]]
window = sg.Window('Window Title', layout, font='Any 16')

while True:
    event, values = window.read(timeout=200)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    window[f'-LED{0}-'].update(CIRCLE if s.connect  else CIRCLE_OUTLINE)
window.close()

'''
def Get_Volts():
    v = os.popen('vcgencmd measure_volts ain1').readline()
    return float(v.split('=')[1][:-3]), "volts"
def Get_Core_temp():
    core = os.popen('vcgencmd measure_temp').readline()
    return float(core.split('=')[1][:-3])
def Get_Mem_Arm():
    mem_arm = os.popen('vcgencmd get_mem arm').readline()
    return float(mem_arm.split('=')[1][:-3])
def Get_IO_Volts():
    IO = os.popen('vcgencmd measure_volts sdram_i').readline()
    return float(IO.split('=')[1][:-3])
def Get_PixelClock():
    pix = os.popen('vcgencmd measure_clock pixel').readline()
    return float(pix.split('=')[1][:-7])

for i in range(50):
    V = Get_Volts()
    core = Get_Core_temp()
    mem_arm = Get_Mem_Arm()
    IO = Get_IO_Volts()
    pix = Get_PixelClock()
    time.sleep(2)
    jsonResult = {"volts":V, "temp-core":core, "memory-arm":mem_arm, "input-output volts":IO, "pixel clock":pix, "it=":i}
    print(jsonResult)   
    #jsonResult = json.dump(jsonResult)
        
    #jsonbyte = bytearray(jsonResult,"UTF-8")
    #print("this Json byte, sent ->", jsonbyte)
        
    #print(v, " it= ",i, " ",core)
    #sock.send(jsonResult)
    #s.send(jsonbyte)
    #time.sleep(2)