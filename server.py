from socket import *
hostname = input("Write your local ip adress(cmd->ipconfig for Windows Users,terminal-> ifconfig for Linux)= ")
sunucuAd = hostname
sunucuPort = 12345
sunucuSocket = socket(AF_INET,SOCK_DGRAM)
sunucuSocket.bind((sunucuAd,sunucuPort))
name = input("Write your nickname = ")


while 1:
    mesaj, istemciAdres = sunucuSocket.recvfrom(4096)
    print(mesaj)
    if mesaj == 'bitir'.encode():
        break
    xmesaj = input("input = ")
    sunucuSocket.sendto(name.encode()+" == ".encode()+xmesaj.encode(),istemciAdres)
sunucuSocket.close()
print("sunucu kapandı.")