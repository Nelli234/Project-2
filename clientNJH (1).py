#Nelson Hucklebridge
#100614680
#12/12/2023
#TPRG 2131
from pathlib import Path
import sys
import os, io 
import json, time
import PySimpleGUI as sg
import socket
from time import sleep as sl
def Get_Volts():# for vcgencmd volts
    v = os.popen('vcgencmd measure_volts ain1').readline()
    return float(v.split('=')[1][:-3]), "volts"
def Get_Core_temp():# for vcgencmd core temp
    core = os.popen('vcgencmd measure_temp').readline()
    return float(core.split('=')[1][:-3])
def Get_Mem_Arm():# for vcgencmd mem_arm
    mem_arm = os.popen('vcgencmd get_mem arm').readline()
    return float(mem_arm.split('=')[1][:-3])
def Get_IO_Volts():# for vcgencmd IO volts
    IO = os.popen('vcgencmd measure_volts sdram_i').readline()
    return float(IO.split('=')[1][:-3])
def Get_PixelClock():# for vcgencmd pixel clock
    pix = os.popen('vcgencmd measure_clock pixel').readline()
    return float(pix.split('=')[1][:-7])

IS_RPI = Path("/etc/rpi-issue").exists()# checks if on pi
print(IS_RPI)

if (IS_RPI):
    print("Correct Hardware")
    try:
       s = socket.socket()
       address = '10.150.6.58'
       #host = 127.0.0.1 for local
       port = 4000
    except socket.error as err:# if not on pi
        print('Socket error because of %s' %(err))
    
    sg.theme('Light Brown 4')

    CIRCLE = '\u26AB'#unicode
    CIRCLE_OUTLINE = '\u26AA'#unicode
    #for the GUI shows if connection is stable
    def LED(color, key):
        return sg.Text(CIRCLE_OUTLINE, text_color=color, key=key)
    layout = [ [sg.Text('connection '), LED('Green', '-LED0-') ],
               [sg.Button('Exit')]]
    window = sg.Window('Window Title', layout, font='Any 16')

    while True:
        event, values = window.read(timeout=200)
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            break
        window[f'-LED{0}-'].update(CIRCLE if s.connect  else CIRCLE_OUTLINE)
        
    
        
    try:
        s.connect((address, port))
        for i in range(50):
            V = Get_Volts()
            core = Get_Core_temp()
            mem_arm = Get_Mem_Arm()
            IO = Get_IO_Volts()
            pix = Get_PixelClock()
            time.sleep(2)
            jsonResult = {"volts":V, "temp-core":core, "memory-arm":mem_arm, "input-output volts":IO, "pixel clock":pix, "it=":i}  
            jsonResult = json.dump(jsonResult)
        
            jsonbyte = bytearray(jsonResult, "utf-8")#turns into utf 8
            print("this Json byte, sent ->", jsonbyte)
        
            #s.send(jsonResult)
            s.send(jsonbyte)
            time.sleep(2)
    except socket.gaierror:# for errors
        print('there be an error here')
        sock.close()
    finally:
        print("sorry lost thy connection")
        exit()