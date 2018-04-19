from socket import *
serverip = input("Write your server's ip")
sunucuAd = serverip
sunucuPort = 12345
istemciSocket = socket(AF_INET,SOCK_DGRAM)
name = input("Write your nickname = ")
while True:
    mesaj = input("input : ")
    istemciSocket.sendto(name.encode()+" == ".encode()+mesaj.encode(),(sunucuAd,sunucuPort))
    yenimesaj,SunucuAdres = istemciSocket.recvfrom(4096)
    print(yenimesaj)
istemciSocket.close()