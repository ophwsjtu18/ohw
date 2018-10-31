import serial
import serial.tools.list_ports
import time

def song():
    print ('hello')
    ports = list(serial.tools.list_ports.comports())
    print (ports)


    # 遍历串口，若名称里带‘serial’或者’uart’就打开
    for p in ports:
        print (p[1])
        if "SERIAL" in p[1] or "UART" in p[1]:
    	    ser=serial.Serial(port=p[0])
        else :
    	    print ("No Arduino Device was found connected to the computer")

    f = open('xiaopingguo.csv','r')
    data = f.read()
    data = data.split('\n')
    new_data = []
    for each in data:
        each = each.split(',')
        new_data.append(each)

    songs = {
        'xiaopingguo':new_data

    }
    #ser=serial.Serial(port='COM4')
    #ser=serial.Serial(port='/dev/ttymodem542')
    #wait 2 seconds for arduino board restart
    time.sleep(2)

    def run():
        '''
        action = "empty"
        while action != "q":
            print ('q for quit,others for command')
            action = input("> ")
                for each in songs[str(action)]:
        '''
        for each in songs['xiaopingguo']:
            for item in each:
                ser.write(item.encode())
                ser.write('a'.encode())
                time.sleep(0.25)

    run()
