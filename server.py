"""This module is meant to be ran on the host device, which is the device with the keyboard"""
import socket
import keyboard
import parse_p

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", parse_p.parse_port('server.cfg')))

server.listen(0)
while True:
    client, addr = server.accept()
    print(f"{addr[0]} has joined you.")
    # Continue logic later
