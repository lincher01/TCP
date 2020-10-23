#!/usr/bin/python
from socket import *
import os
import sys

## line 2,9,11,12,13,14,15,31 from computer networking by Kurose and ross
serverPort = int(sys.argv[1])
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(1)
print("The server is ready to recieve")
while True:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024).decode()

	substring = '>'
	if substring in sentence:
		## given a file
		found = sentence[sentence.find('>')+1:]
		os.system(sentence)


	## if there is no file
	else:
		
		os.system(sentence + ' > TCPresults.txt')
		found = "TCPresults.txt"

	connectionSocket.send(found.encode())
	connectionSocket.close()