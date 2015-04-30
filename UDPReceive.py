__author__ = 'Tree'
#  UDP接收数据
from socketserver import TCPServer,ThreadingMixIn,StreamRequestHandler,UDPServer,BaseRequestHandler
import pymysql
import traceback
from DataTransform import *
import socket

class Handler(BaseRequestHandler):
    # 复写父类handle方法
    def handle(self):
        while True:
            try:
                print('接收数据了!')

                data,s = self.request
                print(self.client_address,data.decode(),end='')
                '''
                s2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                s2.sendto("dtfs".encode(),('localhost',1111))
                print('send data success!')
                '''
                #s2.sendto("dfsf".encode())
                # data2 = data.decode()
                # print(data2)
                #self.request.sendto(self.data.upper(),addr)
                #Sensordatalist = data.split(',')
                # 调用saveAllData存储到数据库中
                # saveAllData(Sensordatalist)
                #print(Sensordatalist)
                break
            except:
                traceback.print_exc()
                break



if __name__ == "__main__":
    host = ''
    port = 2345
    addr = (host,port)
    server = UDPServer(addr,Handler)
    # 创建服务器，开始循环监听
    server.serve_forever()









