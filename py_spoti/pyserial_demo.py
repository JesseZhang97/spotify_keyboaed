import serial
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep


# connect right serial port
def build_connection_ready_for_cmd():
    # TODO connect filed notify
    # TODO auto detect port feat
    ser = serial.Serial('/dev/cu.usbmodem1301')
    pprint(ser.name)

    pprint(listening_port_cmd(ser))
    # filteredCmdStr = inputCmdStr.strip().decode('UTF-8')


def listening_port_cmd(ser):
    while (True):
        # Check if incoming bytes are waiting to be read from the serial input
        # buffer.
        # NB: for PySerial v3.0 or later, use property `in_waiting` instead of
        # function `inWaiting()` below!
        cmd_str = ''
        if (ser.inWaiting() > 0):
            # read the bytes and convert from binary array to ASCII
            cmd_str = ser.read(ser.inWaiting()).decode('ascii')
            # print the incoming string without putting a new-line
            # ('\n') automatically after every print()
            print(cmd_str, end='')

        # Put the rest of your code you want here
        command_distribution(cmd_str)

        # Optional, but recommended: sleep 10 ms (0.01 sec) once per loop to let
        # other threads on your PC run during this time.
        sleep(0.01)


def get_device_state(sp):
    return [item for item in sp.get('devices') if item.get('id') == mac_device_id][0]


def play_pause(cmd):
    pprint('play/pause')
    sp = spotify_auth()
    device_state = get_device_state(sp)
    is_active = device_state.get('is_active')
    # if device is not active -> play [playlist]j
    if (not is_active):
        sp.start_playback(context_uri='spotify:playlist:4RHTIRJNFKPuF9wcmXEHD4',
                          device_id='7b552a49a23bfb184d001ea9e8ec560abfede93b')

    # if device is acticr but not playing -> resume play
    # if device is active and playing -> pause play
    sp.start_playback()


def next_previous(cmd):
    sp = spotify_auth()
    device_state = get_device_state(sp)
    # if cmd == 'next' -> play next
    if cmd == 'next':
        sp.next_track()
        pprint('next')
    # if cmd == 'previous' -> play previous
    if cmd == 'previous':
        sp.previous_track()
        pprint('previous')


def volume_change(cmd):
    sp = spotify_auth()
    device_state = get_device_state(sp)
    current_volume = device_state.get('volume_percent')
    # get current volume and ++
    if cmd == 'volume_up':
        sp.volume(current_volume + 10)
        pprint('volume_up')
    # get current volume and --
    if cmd == 'volume_down':
        sp.volume(current_volume - 10)
        pprint('volume_down')
    # mute and unmute
    if cmd =='volume_mute_unmute':
        if current_volume == 0:
            sp.volume(50)
            pprint('volume_mute_unmute')
        else:
            sp.volume(0)


def command_distribution(cmd):
    match cmd:
        case 'play_pause':
            play_pause(cmd)
            return
        case 'next' | 'previous':
            next_previous(cmd)
            return
        case 'volume_up' | 'volume_down' | 'mute':
            volume_change(cmd)
            return

        case _:
            return pprint('command not support')

# GET TOKEN


def spotify_auth():
    scope = "user-read-playback-state,user-modify-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='b0749846ac1845bea752201825e7787c',
                         client_secret='d1311ac290484889b47c2ea2b16b1e83', redirect_uri='http://localhost', scope=scope))

    # Shows playing devices
    res = sp.devices()
    pprint(res)
    return sp


if __name__ == '__main__':
    # spotify_auth()
    mac_device_id = '7b552a49a23bfb184d001ea9e8ec560abfede93b'
    build_connection_ready_for_cmd()

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
