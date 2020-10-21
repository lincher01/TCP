#!/usr/bin/python
from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)
IP = input('Enter server name or IP addres:')
port = input('Enter port: ')

if (int(port)<0) | (int(port)>65535):
	print("Invalid port number")
	clientSocket.close()
	exit()

command = input('Enter command: ')
clientSocket.connect((IP, int(port)))
clientSocket.send(command.encode())
modifiedSentence = clientSocket.recv(2048)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()