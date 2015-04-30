__author__ = 'Tree'
#  TCP接收数据
from socketserver import TCPServer,ThreadingMixIn,StreamRequestHandler,UDPServer,BaseRequestHandler
import pymysql
import traceback
from DataTransform import *
from datapack import *

# class Server(ThreadingMixIn,UDPServer):pass
class Server(ThreadingMixIn,TCPServer):
    pass
class Handler(StreamRequestHandler):
    # 复写父类handle方法
    def handle(self):
        while True:
            try:
                # 读取数据
                data = self.rfile.readline()
                # 打印数据包的长度
                #print(len(data))
                #print(data)
                #m = unpack('12s12s3d1s',data)
                # 按照指定格式解析数据包
                
                m = unpack('B15s16s12d8s16s8s4d1s',data)

                #包括换行符的字符串
                #print(list(map(a,m)))
                listTemp = []#用来接收解析过的数据
                listTemp = list(map(a,m))
                listTemp.pop()#去除换行符
                print(listTemp)
                # 存入数据库
                saveAllData(listTemp)
                print('保存成功！')
                # print(type(list(map(a,m))))
                #print(data.decode(),self.client_address)
                # 回传给客户端数据
                self.wfile.write("Send Back Successfully!".encode())
                #print('dkfs')
                #Sensordatalist = data.split(',')
                # 调用saveAllData存储到数据库中
                # saveAllData(Sensordatalist)
                #print(Sensordatalist)
                #break
            	
            except:
                #traceback.print_exc()
                break



if __name__ == "__main__":
    # print('fsds')
    host = 'localhost'
    #host = '172.16.173.14'
    port = 2345
    addr = (host,port)
    server = Server(addr,Handler)
    # 创建服务器，开始循环监听
    server.serve_forever()







