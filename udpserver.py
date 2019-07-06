/*
*	Author: Carlos Henrique Cruz Salgado
*	Code adapted for my use in computer network discipline	
*
*/from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(("", serverPort))

print("the server is ready to receive")

while True:
	r = 'valor invalido'
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.decode()
	mod = modifiedMessage
	if mod == '200.126.44.20':
		result = 'ufmt.br'
	elif mod == '179.84.112.99':
		result = 'ifmt.br'
	elif mod == '210.21.10.20':
		result = 'rnp.br'
	elif mod == '189.90.100.22':
		result = 'capes.org'

	else:
		result = r 

		

	serverSocket.sendto(result.encode(), clientAddress)
