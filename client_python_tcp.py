#!/usr/bin/python
from socket import *
import os

clientSocket = socket(AF_INET, SOCK_STREAM)
IP = input('Enter server name or IP addres: ')
port = input('Enter port: ')

## check if port is good
if (int(port)<0) | (int(port)>65535):
	print("Invalid port number")
	clientSocket.close()
	exit()

## check if IP is good
try:
	clientSocket.connect((IP, int(port)))
except:
	print("Could not connect to server")
	exit()

command = input('Enter command: ')
clientSocket.send(command.encode())
modifiedSentence = clientSocket.recv(2048)
result_file = modifiedSentence.decode()
print("File "+ result_file + " saved")
clientSocket.close()