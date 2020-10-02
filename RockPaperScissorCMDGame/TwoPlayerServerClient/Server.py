# importing the pyttsx library
#import random as randint
from random import randint
import pyttsx3 
import socket

def server_program():
       # configure how many client the server can listen simultaneouslyprint("Connection from: " + str(address))
    while 1:
            host = socket.gethostname()
            port = 5000
            server_socket = socket.socket()
            server_socket.bind((host, port))
            server_socket.listen(2)
            conn, address = server_socket.accept()
            data = conn.recv(1024).decode()
            engine = pyttsx3.init() 
            if not data:
                break
            print("from connected user: " + str(data))
            player=data
            computer = randint(1,3)
            if computer==1:
                computer_ch='r'
            elif computer==2:
                computer_ch='p'
            else:
                computer_ch='s'

            print("computer choice:",computer_ch)
            if player=='r' and computer_ch=='p':
                print("computer wins")
                engine.say("computer wins")
                engine.runAndWait()
                data='computer wins'
                conn.send(data.encode())  # send data to the client
            elif player=='r' and computer_ch=='s':
                print("player win\n")
                engine.say("you win \n")
                engine.runAndWait()
                data="you win"
                conn.send(data.encode())  # send data to the client
            elif player=='p' and computer_ch=='r':
                print("player wins")
                engine.say("you win")
                engine.runAndWait()
                data="you win"
                conn.send(data.encode())  # send data to the client
            elif player=='p' and computer_ch=='s':
                print("computer wins")
                engine.say("computer wins")
                engine.runAndWait()
                data='computer wins'
                conn.send(data.encode())  # send data to the client
            elif player=='s' and computer_ch=='r':
                 print("computer wins")
                 engine.say("computer wins")
                 engine.runAndWait()
                 data='computer wins'
                 conn.send(data.encode())  # send data to the client
            elif player=='s' and computer_ch=='p':
                print("player wins")
                engine.say("you win")
                engine.runAndWait()
                data='you wins'
                conn.send(data.encode())  # send data to the client
            else:
                print("draw")
                engine.say("draw")
                engine.runAndWait()
                data='draw'
                conn.send(data.encode())  # send data to the client
            conn.close()
if __name__ == '__main__':
    server_program()
