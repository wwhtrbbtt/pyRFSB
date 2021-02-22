from scripts.message_formats import message_formats
from scripts.parse_message import parse
from scripts.commands import commands
from scripts.utils import clear

import websocket
from threading import Thread
import time

m = 0
DEBUG = 0
SIGNATURE = 0
TOKEN = 0
LOG = 0

def change_signature(new):
    global SIGNATURE
    SIGNATURE = " " + new

def toggle_log():
    global LOG
    LOG = not LOG
    print(f"[+] logging: {LOG}")

def toggle_debug():
    global DEBUG
    DEBUG = not DEBUG
    print(f"[+] debug: {DEBUG}")

def pingThread(ws):
    global DEBUG
    """
    We have to ping the server every once in a while to 
    keep the connection running
    """
    while 1:
        ws.send(m.ping())
        if DEBUG:
            print("ping")
        time.sleep(20)

def run(ws):
        global DEBUG
        global SIGNATURE
        global m

        # sleep 1 second before sending any packets
        time.sleep(1)

        # sending a few packets to establish a good connection
        for x in m.start_sequence():
            if DEBUG:
                print(f"⬆️ {x}")

            ws.send(x)
        # let the user know were connected
        print("[+] Connected")

        # the main loop: wait for input,
        # execute if command, send the message if otherwise
        while 1:
            msg = input()
            try:
                if msg[0] == "/":
                    commands(msg)
                else:
                    format = m.send_message(msg + SIGNATURE)
                    ws.send(format)
            except IndexError:
                print("[!] cant send empty message")

def on_message(ws, message):
    global LOG
    global DEBUG
    """
    whenever we receive a packet from raidforums.
    Only 1 type of packet gets parsed ATM: messages from users
    """
    global oldTime
    if DEBUG:
        print(f"⬇️ packet")
    parse(message, LOG, DEBUG=DEBUG)


def on_error(ws, error):
    """
    If there should be an error, never occured to me in testing
    """
    print(f"⬇️ {error}")


def on_close(ws):
    """
    When the connection gets closed
    """
    print("### closed ###")


def on_open(ws):
    global DEBUG
    global SIGNATURE
    global m
    """
    When we first open the connection
    """
    # start the two threads, kinda important
    Thread(target=run, args=[ws]).start()
    Thread(target=pingThread, args=[ws]).start()


def main(nDEBUG, nSIGNATURE, nTOKEN, nLOG):
    global DEBUG
    global SIGNATURE
    global TOKEN
    global LOG
    global m

    DEBUG = nDEBUG
    SIGNATURE = nSIGNATURE
    TOKEN = nTOKEN
    LOG = nLOG
    m = message_formats(TOKEN)

    # clear the screen
    clear()

    # open the connection with all the settings
    ws = websocket.WebSocketApp(m.url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
