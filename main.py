import pygame
import socket
# 初始化所有导入的pygame模块
pygame.init()
# 初始化手柄
pygame.joystick.init()
# 在没有手柄时退出
if pygame.joystick.get_count() < 1:
    print("No joystick detected.")
    quit()
# 获取第一个手柄
joystick = pygame.joystick.Joystick(0)
joystick.init()
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
tcp=Tcp_client("192.168.204.129", 8080)
try:
    while True:
        # 处理事件队列
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP and pygame.JOYBUTTONDOWN == True:
                # 打印按钮的输入
                #x
                if event.button==14:
                    tcp.sendpose('TraX+')
                if event.button==13:
                    tcp.sendpose('TraX-')
                #y
                if event.button==11:
                    tcp.sendpose('TraY+')
                if event.button==12:
                    tcp.sendpose('TraY-')
                #z
                if event.button==9:
                    tcp.sendpose('TraZ+')
                if event.button==10:
                    tcp.sendpose('TraZ-')
                #rotatex
                if event.button==1:
                    tcp.sendpose('RotX+')
                if event.button==2:
                    tcp.sendpose('RotX-')
                #rotatey
                if event.button==3:
                    tcp.sendpose('RotY+')
                if event.button==0:
                    tcp.sendpose('RotY-')
                #rotatez
                if event.button==8:
                    tcp.sendpose('RotZ+')
                if event.button==7:
                    tcp.sendpose('RotZ-')
                #MoveToStart
                if event.button ==6:
                    tcp.sendpose('MoveToStart')
                #print(f"Joystick {event.joy}, button {event.button}, down {event.type == pygame.JOYBUTTONDOWN}")
except KeyboardInterrupt:
    print("Exiting...")
finally:
    pygame.quit()
