#Nelson Hucklebridge
#100614680
#12/14/2023
#TPRG 2131
import socket
import json, time
import PySimpleGUI as sg
from pathlib import Path
IS_RPI = Path("/etc/rpi-issue").exists()# checks to see if on raspberry pi
print(IS_RPI)
if (IS_RPI):# if on raspberry pi use local host client is on
    print("ON RPI")
    sock = socket.socket()
    print("socket created")
    sock.bind(('127.0.0.1', port))
    sock.listen(5)
else:# if on pc use local host
    print("ON PC")
    sock = socket.socket()
    host = '' # Localhost
    port = 4000#port being used
    sock.bind((host, port))
    sock.listen(5)

print('socket is listening')
c, addr = sock.accept()
print('got connection from', addr)
# the main
def main():
    while True:
        jsonRecieved = c.recv(1024)# recieve json
        print("Json recieved (byte type)-->", jsonRecieved)
        if jsonRecieved == b'':#if this exit program
            print("whoopsie")
            exit()
        data = json.loads(jsonRecieved)
        ret = json.dumps(data, indent=4)
        ret1 = data["volts"]
        ret2 = data["temp-core"]
        ret3 = data["memory-arm"]
        ret4 = data["input-output volts"]
        ret5 = data["pixel clock"]
        ret6 = data["it="]
    print(ret1, ret2, ret3, ret4, ret5, ret6) #print results
        
if __name__ == '__main__':#simple main guard 
    try:
        main()
    except KeyboardInterrupt:
        print("bye...")
        exit()