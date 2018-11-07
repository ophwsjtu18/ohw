import serial
import serial.tools.list_ports
import time

def get_songs():
    f = open('songs.csv', 'r')
    songs = f.read().split('\n')
    song_lst = [song.split(',') for song in songs]
    song_dict = {song[0]:song[1:] for song in song_lst}
    #print(song_lst)
    print(song_dict)
    return song_dict

def play_single_song(ser, name, content):
    print('Song: %s' % name)
    for temp in content:
        temp = temp + 'a'
        ser.write(temp.encode())
        time.sleep(0.25)

def song_player(ser, song_dict):
    for (name, content) in song_dict.items():
        play_single_song(ser, name, content)
        time.sleep(5)

def test_com():
    print ('hello')
    ports = list(serial.tools.list_ports.comports())
    print (ports)

    for p in ports:
        print (p[1])
        if "SERIAL" in p[1] or "UART" in p[1] :
            ser=serial.Serial(port=p[0])
            return ser
        else :
            print ("No Arduino Device was found connected to the computer")

    #ser=serial.Serial(port='COM4')
    #ser=serial.Serial(port='/dev/ttymodem542')
    #wait 2 seconds for arduino board restart

def main():
    ser = test_com()
    song_dict = get_songs()
    song_player(ser, song_dict)

if __name__ == '__main__':
    main()
