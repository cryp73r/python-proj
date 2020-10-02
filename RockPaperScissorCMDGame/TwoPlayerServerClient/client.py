# importing the pyttsx library
#import random as randint
from random import randint
import pyttsx3 
import socket


def client_program():
    engine = pyttsx3.init()
    print("WELCOME TO ROCK PAPER SCISSOR Game")
    engine.say("WELCOME TO ROCK PAPER SCISSOR Game")
    print("Here are some rules of Game")
    engine.say("Here are some rules of Game")
    print("Press r for rock")
    engine.say("Press r for rock")
    print("press p for paper")
    engine.say("press p for paper")
    print("press s for scissor")
    engine.say("press s for scissor")
    engine.runAndWait()
   
    while 1:
         host = socket.gethostname()  # as both code is running on same pc
         port = 5000  # socket server port number

         client_socket = socket.socket()  # instantiate
         client_socket.connect((host, port))  # connect to the server
         
         message = input(" -> ")  # take input
         client_socket.send(message.encode())  # send message
         data = client_socket.recv(1024).decode()  # receive response
         print('Received from server: ' + data)  # show in terminal
        
         client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
