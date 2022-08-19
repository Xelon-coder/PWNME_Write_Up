import socket
from math import *

s = socket.socket()
level = 2 #GridSize

def init():
	HOST = "prog.pwnme.fr"
	PORT = 7001

	s.connect((HOST, PORT))

def parser(buff,level):
	index = 1
	tab = []
	for k in range(0,level):
		array = []
		for j in range(0,level):
			line = []
			for i in buff[index]:
				line.append(i)
			index = index + 1
			array.append(line)
		index = index + 1
		tab.append(array)
	return tab

def read(level):
	recv = s.recv(8000).decode('utf-8')
	if(level > 13):
		recv = recv+ s.recv(8000).decode('utf-8')
	print(recv)
	readbuffer = (recv.split('\n'))
	return parser(readbuffer,level)

def solveGrid(entry,exit,cpt,data):
	while(entry[1] < exit[1]):
		cpt = cpt + 1
		entry = (entry[0], entry[1]+1, entry[2])
		data = data + "y-;"
	while(entry[1] > exit[1]):
		cpt = cpt + 1
		entry = (entry[0], entry[1]-1, entry[2])
		data = data + "y+;"
	while(entry[2] < exit[2]):
		cpt = cpt + 1
		entry = (entry[0], entry[1], entry[2]+1)
		data = data + "x+;"
	while(entry[2] > exit[2]):
		cpt = cpt + 1
		entry = (entry[0], entry[1], entry[2]-1)		
		data = data + "x-;"
	return (data,cpt)

def allGrid(level):
	for number in range(0,16):

		tableau = read(level)

		Ecoo = (0,0,0)
		Scoo = (0,0,0)

		cpt = 0
		data = ""

		for i in range(0,level):
			for j in range(0,level):
				for k in range(0,level):
					if(tableau[i][j][k] == 'E'):
						Ecoo = (i,j,k)
					if(tableau[i][j][k] == 'S'):
						Scoo = (i,j,k)

		diff = Ecoo[0] - Scoo[0]

		if(diff < 0):
			for i in range(0,abs(diff)):
				data = data + "z+;"
		elif(diff > 0):
			for i in range(0,abs(diff)):
				data = data + "z-;"

		(data,cpt) = solveGrid(Ecoo,Scoo,cpt,data)

		cpt = str(cpt) + '\n'

		data = data[:-1] + '\n'
		print(data)
		
		s.send(data.encode())

		level = level + 1

if __name__ == '__main__':
	init()
	allGrid(level)
	print(s.recv(1024).decode('utf-8'))
