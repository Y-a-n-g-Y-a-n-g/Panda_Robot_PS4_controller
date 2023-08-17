
import socket
import time


# 初始化所有导入的pygame模块
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
tcp=Tcp_client("192.168.31.150", 8080)

for i in range(1,80):
    tcp.sendpose('TraY-')
    time.sleep(5)
for i in range(1,13):
    tcp.sendpose('TraX+')
    time.sleep(5)
for i in range(1,90):
    tcp.sendpose('TraY+')
    time.sleep(5)

