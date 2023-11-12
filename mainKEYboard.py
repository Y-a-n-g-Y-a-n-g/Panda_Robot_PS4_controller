import pygame
import socket
import keyboard
class Tcp_client():
    def __init__(self, server_ip, server_port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 连接服务器
        server_address = (server_ip, server_port)
        self.sock.connect(server_address)
        print(f"Connecting to {server_ip}:{server_port}")
    def sendpose(self,pose):
        try:
            # 发送数据
            print(f"Sending message: {pose}")
            self.sock.send(str(pose).encode())
        except:
            print("Closing connection")
            self.sock.close()


def key_callback(e):
    keys = ['w', 'a', 's', 'd','+','-','j','k','l', 'up', 'down', 'left', 'right']
    if e.name in keys and e.event_type == keyboard.KEY_DOWN:
        print(f"'{e.name}' 键被按下")
        if e.name == "w":
            tcp.sendpose('TraX+')
        if e.name == "s":
            tcp.sendpose('TraX-')
        # y
        if e.name == "a":
            tcp.sendpose('TraY+')
        if e.name == "d":
            tcp.sendpose('TraY-')
        # z
        if e.name == "+":
            tcp.sendpose('TraZ+')
        if e.name == "-":
            tcp.sendpose('TraZ-')
        # rotatex
        if e.name == "up":
            tcp.sendpose('RotX+')
        if e.name == "down":
            tcp.sendpose('RotX-')
        # rotatey
        if e.name == "left":
            tcp.sendpose('RotY+')
        if e.name == "right":
            tcp.sendpose('RotY-')
        # rotatez
        if e.name == "j":
            tcp.sendpose('RotZ+')
        if e.name == "k":
            tcp.sendpose('RotZ-')
        # MoveToStart
        if e.name == "l":
            tcp.sendpose('MoveToStart')

tcp=Tcp_client("127.0.0.1", 8080)
print("开始监听键盘输入...")
keyboard.hook(key_callback)
keyboard.wait('esc')

