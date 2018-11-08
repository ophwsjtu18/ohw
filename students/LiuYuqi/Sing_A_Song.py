import serial
import serial.tools.list_ports
import time

songs_name = ['countducks','skycity','hometown','littleapple']

def get_song(name):
    f = open(name,'r')
    data = f.read()
    data = data.split('\n')
    new_data = []
    whole_new_data = []
    for each in data:
        each = each.split(',')
        new_data.append(each)     #一句
        whole_new_data.append(new_data) #一整首
        new_data = []
    return whole_new_data

def sing(count):
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

    songs = {}
    for song_name in songs_name:
        new_data = get_song(song_name + '.csv')
        songs[song_name] = new_data

    #ser=serial.Serial(port='COM4')
    #ser=serial.Serial(port='/dev/ttymodem542')
    #wait 2 seconds for arduino board restart
    time.sleep(2)

    '''
    action = "empty"
    while action != "q":
        print ('q for quit,others for command')
        action = input("> ")
            for each in songs[str(action)]:
    '''

    for each in songs[songs_name[count]]:
        for item in each:
            for i in item:
                ser.write(i.encode())
                ser.write('a'.encode())
                time.sleep(0.25) # 每个音符间0.25
            time.sleep(0.5) # 每句歌词 0.5
