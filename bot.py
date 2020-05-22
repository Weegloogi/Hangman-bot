import socket
import re
from time import sleep
import Solver
import traceback

NICK, PASS, CHANNEL = open('Login Details.txt', 'r').readlines()

s = socket.socket()
s.connect(("irc.twitch.tv", 6667))
s.send(f"PASS {PASS}\r\n".encode())
s.send(f"NICK {nick}\r\n".encode())
s.send(f"JOIN #{CHANNEL}\r\n".encode())

Loading = True
while Loading:
    readBuffer = s.recv(1024).decode()
    temp = readBuffer.split("\n")
    
    for line in temp:
        print(line)
        if "/NAMES" in line:
            Loading = False

def sendMessage(message):
    s.send(f'PRIVMSG #{CHANNEL}: {message}\r\n'.encode())
    
hangman = False
while True:
    readBuffer += s.recv(1024).decode()
    temp = readBuffer.split("\n")
    readBuffer = temp.pop()


    for line in temp:
        
        if line.startswith("PING"):
            s.send(b"PONG :tmi.twitch.tv\r\n")
            print("SENT PONG")
            
        else:
            try:
                user = line.split("!")[1].split("@")[0]
            except:
                # print the debug, but continue the program
                traceback.print_exc()
                print(line)
                continue

            if user == "robthebot115":
                message = line.split(':')[2][:-1]
                
                if hangman:
                    if "got it correct" in message:
                        hangman = False
                        solver = ""

                    elif message.startswith("@{NICK} was incorrect!"):
                        hangman = False
                        solver = ""

                    elif "_" not in message:
                        continue

                    else:
                        hint = message.replace(" ", "").replace("_", ".").replace("/", " ")

                        a = solver.feed(hint) # returns the pokemon if 1 is left, else returns None

                        if a != None:
                            sendMessage("Hangman Bot knows the Answer")
                            solver = ""
                            hangman=False
                        

                else:
                    if message.startswith("Alright, the category this time is "):

                        category = message.split("Alright, the category this time is ")[1].split("! Good Luck!")[0]
                        
                        if category == "Pokemon Name":
                            solver = Solver.resolver("pokemon")
                        elif category == "Pokemon City/Town":
                            solver = Solver.resolver("city")
                        elif category == "Pokemon Move":
                            solver = Solver.resolver("move")
                        elif category == "Pokemon Ability":
                            solver = Solver.resolver("ability")
                        elif category == "Pokemon Location":
                            solver = manual.resolver("location")
                        elif category == "Pokemon Key Item":
                            solver = Solver.resolver("item")
                        elif category == "Pokemon Spinoff Location":
                            solver = Solver.resolver("side")
                        else:
                            continue

                        hangman = True
