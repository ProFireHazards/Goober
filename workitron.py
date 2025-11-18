import pygame
import math
import os
import time
import random
import sys
time.sleep(3)
import pyttsx3
import msvcrt
#from goobersim import *
engine = pyttsx3.init()
tick = 0

pygame.init()
back = (192,192,192)

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('Workitron')
screen.fill(back)
clock = pygame.time.Clock()
music = pygame.mixer.music.load("sounds/tick.midi")
background = pygame.image.load("sprites\s00.png")
dial = pygame.image.load("sprites\s01.png")
boss = pygame.image.load("sprites\s09.png")
talk = False
def set_text(string, coordx, coordy, fontSize): #Function to set text

    font = pygame.font.Font('8-bit Arcade In.ttf', fontSize) 
    #(0, 0, 0) is black, to make black text
    text = font.render(string, True, (0, 0, 0)) 
    textRect = text.get_rect()
    textRect.center = (coordx, coordy) 
    return (text, textRect)

def speak(str):
    engine.say(str)
    engine.runAndWait()
        
def speaktask():
    global task
    global x
    x = random.randint(1, 10)
    tasks = ["Spin around", "Collect the orbs", "Walk forward", "Stand still", "Jump around", "Walk backward", "Strafe to the left", "Strafe to the right"]
    task = random.choice(tasks)
    background = pygame.image.load("sprites\s00.png")
    dial = pygame.image.load("sprites\s01.png")
    boss = pygame.image.load("sprites\s09.png")
def speakangry():
    global task
    x = random.randint(5, 10)
    tasks = ["That's a demotion", "I am lowering your paygrade", "You have dissapointed me", "I am mad at you", f"That's so bad you outta pay me ${x}"]
    task = random.choice(tasks)
    background = pygame.image.load("sprites\s00.png")
    dial = pygame.image.load("sprites\s01.png")
    boss = pygame.image.load("sprites\s09.png")
running = True
tick = 10
tick2 = 0
timefortask = False
showclock = False
w = False
task = "None"
def taskcheck():
    key = lastkeypressed
    print(f'{key}')
    if task == 'Spin around':
        if f"{key}" == "b'a'":
            win = True
        else:
            win = False
    if task == 'Jump around':
        if f"{key}" == "b' '":
            win = True
        else:
            win = False
    if task == 'Strafe to the left':
        if f"{key}" == "b'j'":
            win = True
        else:
            win = False
    if task == 'Strafe to the right':
        if f"{key}" == "b'l'":
            win = True
        else:
            win = False
    if task == 'Walk forward':
        if f"{key}" == "b'w'":
            win = True
        else:
            win = False
    if task == 'Walk backward':
        if f"{key}" == "b's'":
            win = True
        else:
            win = False
    if task == 'Spin around':
        if f"{key}" == "b'a'":
            win = True
        else:
            win = False
    if task == 'Stand still':
        if f"{key}" == "b'a'" or f"{key}" == "b's'" or f"{key}" == "b'd'" or f"{key}" == "b'w'" or f"{key}" == "b'j'" or f"{key}" == "b'l'" or f"{key}" == "b' '":
            win = False
        else:
            win = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if tick == 8 and showclock == True:
        pygame.mixer.music.play(2)
        dial = pygame.image.load("sprites\s01.png")
    if tick == 7 and showclock == True:
        pygame.mixer.music.play(2)
        dial = pygame.image.load("sprites\s02.png")
    if tick == 6 and showclock == True:
        pygame.mixer.music.play(2)
        dial = pygame.image.load("sprites\s03.png")
    if tick == 5 and showclock == True:
        pygame.mixer.music.play(2)
        dial = pygame.image.load("sprites\s04.png")
    if tick == 4 and showclock == True:
        pygame.mixer.music.play(2)
        dial = pygame.image.load("sprites\s05.png")
    if tick == 3 and showclock == True:
        pygame.mixer.music.play(2)
        dial = pygame.image.load("sprites\s06.png")
    if tick == 2 and showclock == True:
        pygame.mixer.music.play()
        dial = pygame.image.load("sprites\s07.png")
    if tick == 1 and showclock == True:
        pygame.mixer.music.play()
        dial = pygame.image.load("sprites\s08.png")
    if talk == False:
        boss = pygame.image.load("sprites\s09.png")
    if talk == True:
        boss = pygame.image.load("sprites\s10.png")
    talk = False
    screen.blit(background, (-200, -300))
    tick += 1
    tick2 += 1
    if tick2 >=1 and tick2 <=8 and w == True:
        showclock = True
    else:
        task = "None"
        w = False
        showclock = False
    if tick2 > 16:
        showclock = False
        timefortask = True
        tick2 = 0
        tick = 7
    if tick > 8:
        if timefortask == True:
            w = True
            showclock = True
            boss = pygame.image.load("sprites\s10.png")
            speaktask()
            speak(task)
            timefortask = False
        tick = 1
    totalText = set_text(task, 500, 250, 30)
    screen.blit(boss, (-200, -300))
    screen.blit(dial, (-200, -300))
    screen.blit(totalText[0], totalText[1])
    pygame.display.update()
    pygame.display.update()
    time.sleep(0.5)
screen.fill(back)
pygame.display.update()
screen.blit(background, (-200, -300))
boss = pygame.image.load("sprites\s10.png")
task = "Goodbye Goober"
totalText = set_text(task, 500, 250, 30)
screen.blit(boss, (-200, -300))
screen.blit(dial, (-200, -300))
screen.blit(totalText[0], totalText[1])
pygame.display.update()
speak(task)
pygame.quit()
quit()
            
