import serial
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep


# TODO auto detect port feat
# connect right serial port
def serail_connection():
    ser = serial.Serial('/dev/cu.usbmodem1301')
    pprint(ser.name)
    inputCmdStr = ser.readline()
    pprint(inputCmdStr)
# eg cmd -> b'Play\r\n'
    filteredCmdStr = inputCmdStr.strip().decode('UTF-8')
# 'Play'
    pprint(filteredCmdStr)
# read cmd from board
# inputStr = ser.read_all()
# inputStr = ser.read_until()


# get token
scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='b0749846ac1845bea752201825e7787c',
                     client_secret='d1311ac290484889b47c2ea2b16b1e83', redirect_uri='http://localhost', scope=scope))

# Shows playing devices
res = sp.devices()
pprint(res)


def resume_pause(cmd):
    pprint('play/pause')


def next_previous(cmd):
    pprint('next')
    pprint('previous')


def volume_change(cmd):
    pprint('volume_up')
    pprint('volume_down')


def command_distribution(cmd):
    match cmd:
        case 'play' | 'pause':
            resume_pause(cmd)
            return
        case 'next' | 'previous':
            next_previous(cmd)
            return
        case 'volume_up' | 'volume_down':
            volume_change(cmd)
            return

        case _:
            return pprint('command not support')

# TODO CONTROL PLAYING STATUS BY CMD
# FIXME detect playing status
    # pprint(res['devices'][0]['is_active'])
    # rs = sp.current_playback()
    # pprint(rs)
    # sp.start_playback()
    # sp.pause_playback()


# pause playing
# sp.pause_playback()
# sp.start_playback()
# Change track
# sp.start_playback(uris=['spotify:track:6gdLoMygLsgktydTQ71b15'])

# Change volume
# sp.volume(100)
# sleep(2)
# sp.volume(100)
# sleep(2)
# sp.volume(100)
