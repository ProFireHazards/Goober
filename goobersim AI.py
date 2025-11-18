import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import random
import sys
import time
import numpy as np
import sounddevice as sd
import random
import threading, pyttsx3
import prompt
import threading

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def drawText(x, y, text):                                                
    textSurface = font.render(text, True, (238, 238, 119, 255), (0, 0, 170, 255))
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    glWindowPos2d(x, y)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)
def play_happy_beep():
    frequency = random.uniform(800, 1200)  # Adjust the frequency range for a happy vibe
    duration = random.uniform(0.15, 0.2)    # Adjust the duration for a faster sound

    t = np.linspace(0, duration, int(44100 * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    sd.play(wave, samplerate=44100)
    sd.wait()
def play_neutral_beep():
    frequency = random.uniform(400, 800)  # Adjust the frequency range for a happy vibe
    duration = random.uniform(0.15, 0.2)    # Adjust the duration for a faster sound

    t = np.linspace(0, duration, int(44100 * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    sd.play(wave, samplerate=44100)
    sd.wait()


def play_sad_beep():
    frequency = random.uniform(200, 300)  # Adjust the frequency range for a sad vibe
    duration = random.uniform(0.4, 0.8)    # Adjust the duration for a slower sound

    t = np.linspace(0, duration, int(44100 * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    sd.play(wave, samplerate=44100)
    sd.wait()
def play_grumpy_beep():
    frequency = random.uniform(100, 200)  # Adjust the frequency range for a grumpy vibe
    duration = random.uniform(0.20, 0.12)    # Adjust the duration for a slower sound

    t = np.linspace(0, duration, int(44100 * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    sd.play(wave, samplerate=44100)
    sd.wait()
def play_curious_beep():
    frequency = random.uniform(800, 900)  # Adjust the frequency range for a grumpy vibe
    duration = random.uniform(0.16, 0.17)    # Adjust the duration for a slower sound

    t = np.linspace(0, duration, int(44100 * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    sd.play(wave, samplerate=44100)
    sd.wait()
def say1(text, emotion='happy'):
    sys.stdout.write(" ")
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        if emotion == 'happy':
            play_happy_beep()
        elif emotion == "neutral":
            play_neutral_beep()
        elif emotion == 'sad':
            play_sad_beep()
        elif emotion == "grumpy":
            play_grumpy_beep()
        elif emotion == "curious":
            play_curious_beep()
def sayemotion(text):
    sys.stdout.write(" ")
    if "." in text:
        emotion = "neutral"
    if "!" in text:
        emotion = 'happy'
    if "!!" in text:
        emotion = 'grumpy'
    if "..." in text:
        emotion = 'sad'
    if "?" in text:
        emotion = "curious"
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        if emotion == 'happy':
            play_happy_beep()
        elif emotion == "neutral":
            play_neutral_beep()
        elif emotion == 'sad':
            play_sad_beep()
        elif emotion == "grumpy":
            play_grumpy_beep()
        elif emotion == "curious":
            play_curious_beep()
points = 1
def reputation(text):
    if points == 0:
        text = text + "."
    if points == 1:
        text = text + "!"
    if points == -1:
        text = text + "?"
    if points == -2:
        text = text + "..."
    if points == -3:
        text = text + "!!"
    return text
def say(str):
    sayemotion(reputation(str))
    drawText(400, 300, str)
    

gooberlines = [
"Where am I?",
"Please help me, I don’t know where I’m going.",
"I’m lost, can someone guide me?",
"Everything feels unfamiliar… where am I?",
"Is anyone out there? I can’t find my way.",
"Am I the only one who’s completely lost?",
"I thought I knew where I was, but now everything’s changed.",
"I can’t seem to find the way back.",
"Is there a way out of this maze?",
"I don’t know which direction to go anymore.",
"I’m starving, can’t think of anything else right now.",
"Why does my stomach feel like it’s eating itself?",
"All I can think about is food.",
"I’m so hungry, I could eat a whole buffet.",
"Is it normal to feel this hungry? Like, all the time?",
"My stomach is growling like it’s about to start a riot.",
"I’m craving anything at this point.",
"I’m not just hungry, I’m hangry.",
"Food is all that’s on my mind right now.",
"Can we just eat already? I’m losing focus here.",
"I’m so thirsty, I could drink an ocean.",
"Is there any water around here? I’m parched.",
"My mouth feels like the desert right now.",
"I need a drink, like, yesterday.",
"I can’t think straight, I’m so thirsty.",
"Please, just a sip of water… I’m dying here.",
"I feel like I could drink a whole river and still be thirsty.",
"Thirst is taking over, I need something cold.",
"Why does thirst always hit at the worst time?",
"I’m not just thirsty, I’m desperate for a drink.",
"Why am I overthinking this?", "Am I going the right way?", "What’s the point of all this?", "Wait, did I already think that?", "Am I making this harder than it needs to be?", "Is anyone else as confused as I am?", "Why does my brain do this to me?", "Can I just take a break from myself for a minute?", "Is it normal to forget where you’re going?", "Why does it always feel like I’m chasing something I can’t catch?",
"Why does my mind always wander at the worst times?", "Am I supposed to be doing something right now?", "What if I just turned around and went back?", "Is it weird that I can’t remember the last thing I thought about?", "Maybe I’m just overthinking everything?", "Why is everything so loud in my head?", "Am I even sure of what I want?", "Does everyone else feel this lost sometimes?", "Why do I always second-guess myself?", "How do I keep ending up here again?"
]


# Global variables
person_x = 0
person_z = 0
person_rotation = 0
jump_height = 0.8
jump_speed = 0.1
current_jump_height = 0
is_jumping = False
floor_size = 25
movspeed = 0
anger = 0
VHS = False
jwalk = False
oldschool = False
fullscreen = True
# Define colors
def colors():
    global preset
    global rannum
    global rannum2
    rannum2 = random.randint(1, 5)
    rannum = random.randint(1, 15)
    preset = "Earth"
    presets = ["Stage", "Stage2", "Stage3", "Carpet", "Backrooms", "Cafeteria", "Heaven", "Hell", "White Void", "Space", "Black Void", "Earth"]
    global topcolor
    global floor_size
    global wallcolor
    global shirtcolor
    global headcolor
    global eyecolor
    global floorcolor
    global floorcolor2
    global red, orange, yellow, green, blue, indigo, violet, black, white
    if VHS == True:
        red = (1.0 + random.uniform(-0.5, 0.5), 0.0 + random.uniform(-0.5, 0.5), 0.0 + random.uniform(-0.5, 0.5))      # Red
        orange = (1.0 + random.uniform(-0.3, 0.3), 0.5 + random.uniform(-0.3, 0.3), 0.3 + random.uniform(-0.3, 0.3))   # Orange
        yellow = (1.0 + random.uniform(-0.3, 0.3), 1.0 + random.uniform(-0.3, 0.3), 0.50 + random.uniform(-0.3, 0.3))   # Yellow
        green = (0.0 + random.uniform(-0.2, 0.2), 1 + random.uniform(-0.2, 0.2), 0.0 + random.uniform(-0.2, 0.2))    # Green
        blue = (0.0 + random.uniform(-0.2, 0.2), 0.5 + random.uniform(-0.2, 0.2), 1.0 + random.uniform(-0.2, 0.2))     # Blue
        indigo = (0.294 + random.uniform(-0.2, 0.2), 0.0 + random.uniform(-0.2, 0.2), 0.51 + random.uniform(-0.2, 0.2)) # Indigo
        violet = (0.933 + random.uniform(-0.2, 0.2), 0.51 + random.uniform(-0.2, 0.2), 0.933 + random.uniform(-0.2, 0.2)) # Violet
        black = (0.0 + random.uniform(-0.2, 0.2), 0.0 + random.uniform(-0.2, 0.2), 0.0 + random.uniform(-0.2, 0.2))    # Black
        white = (0.9 + random.uniform(-0.2, 0.2), 0.9 + random.uniform(-0.2, 0.2), 0.9 + random.uniform(-0.2, 0.2))    # White
    elif oldschool == True:
        red = (0.53, 0, 0)      # Rede
        orange = (0.86, 0.53, 0.33)   # Orange
        yellow = (0.93, 0.93, 0.46)   # Yellow
        green = (0, 0.8, 0.33)    # Green
        blue = (0, 0.53, 1)     # Blue
        indigo = (0, 0, 0.66) # Indigo
        violet = (0.8, 0.26, 0.8) # Violet
        black = (0.0, 0.0, 0.0)    # Black
        white = (1.0, 1.0, 1.0)
    else:
        red = (1.0, 0.0, 0.0)      # Red
        orange = (1.0, 0.5, 0.3)   # Orange
        yellow = (1.0, 1.0, 0.50)   # Yellow
        green = (0.0, 1, 0.0)    # Green
        blue = (0.0, 0.5, 1.0)     # Blue
        indigo = (0.294, 0.0, 0.51) # Indigo
        violet = (0.933, 0.51, 0.933) # Violet
        black = (0.0, 0.0, 0.0)    # Black
        white = (1.0, 1.0, 1.0)
    topcolor = white
    wallcolor = yellow
    shirtcolor = red
    headcolor = white
    eyecolor = black
    floorcolor = yellow
    floorcolor2 = black
    floor_size = 25
    if preset == "Seizure":
        preset = random.choice(presets)
    if preset == "Backrooms":
        floor_size = 100
        topcolor = white
        wallcolor = yellow
        floorcolor = yellow
        floorcolor2 = orange
    if preset == "Cafeteria":
        floor_size = 85
        topcolor = black
        wallcolor = yellow
        floorcolor = white
    if preset == "Carpet":
        floor_size = 25
        topcolor = yellow
        wallcolor = yellow
        floorcolor = orange
        floorcolor2 = orange
    if preset == "Stage":
        floor_size = 30
        topcolor = black
        wallcolor = red
        floorcolor = white
        floorcolor2 = black
    if preset == "Stage2":
        floor_size = 30
        topcolor = black
        wallcolor = red
        floorcolor = white
        floorcolor2 = red
    if preset == "Stage3":
        floor_size = 30
        topcolor = black
        wallcolor = red
        floorcolor = black
        floorcolor2 = red
    if preset == "Heaven":
        floor_size = 100
        topcolor = blue
        wallcolor = blue
        floorcolor = white
        floorcolor2 = yellow
    if preset == "Hell":
        floor_size = 100
        topcolor = red
        wallcolor = red
        floorcolor = orange
        floorcolor2 = black
    if preset == "White Void":
        floor_size = 50
        topcolor = white
        wallcolor = white
        floorcolor = white
        floorcolor2 = white
    if preset == "Space":
        floor_size = 100
        topcolor = black
        wallcolor = black
        floorcolor = black
        floorcolor2 = black
        headcolor = blue
        eyecolor = indigo
        shirtcolor = white
    if preset == "Black Void":
        floor_size = 50
        topcolor = black
        wallcolor = black
        floorcolor = black
        floorcolor2 = black
    if preset == "Earth":
        floor_size = 200
        topcolor = blue
        wallcolor = blue
        floorcolor = green
        floorcolor2 = orange
colors()
# Walking Animation Logic
def walk():
    global person_rotation
    rotation_speed = random.uniform(-10, 10)
    person_rotation += rotation_speed
    if person_rotation >= 360:
        person_rotation = 0

# Movement Logic
def move():
    global person_x, person_z, movspeed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        x_move = math.sin(math.radians(person_rotation)) * (0.1 + movspeed / 3)
        z_move = math.cos(math.radians(person_rotation)) * (0.1 + movspeed / 3)
        new_person_x = person_x + x_move
        new_person_z = person_z + z_move
        if -floor_size < new_person_x < floor_size and -floor_size < new_person_z < floor_size:
            person_x = new_person_x
            person_z = new_person_z
    if keys[pygame.K_s]:
        x_move = math.sin(math.radians(person_rotation)) * (0.1 + movspeed / 3)
        z_move = math.cos(math.radians(person_rotation)) * (0.1 + movspeed / 3)
        new_person_x = person_x - x_move
        new_person_z = person_z - z_move
        if -floor_size < new_person_x < floor_size and -floor_size < new_person_z < floor_size:
            person_x = new_person_x
            person_z = new_person_z
def draw_cube(length, width, height):
    # Define the vertices of the cube
    vertices = [
        (0, 0, 0), (length, 0, 0), (length, height, 0), (0, height, 0),  # Front face
        (0, 0, width), (length, 0, width), (length, height, width), (0, height, width),  # Back face
    ]

    # Define the indices of the vertices for each face
    faces = [
        (0, 1, 2, 3),  # Front face
        (4, 5, 6, 7),  # Back face
        (0, 4, 7, 3),  # Left face
        (1, 5, 6, 2),  # Right face
        (0, 1, 5, 4),  # Bottom face
        (3, 2, 6, 7),  # Top face
    ]

    # Draw the cube
    glBegin(GL_QUADS)
    for face in faces:
        for vertex_index in face:
            glVertex3fv(vertices[vertex_index])
    glEnd()

def draw_table(length, width, height):
    # Define colors for the table
    leg_color = (0.4, 0.2, 0.0)  # Brown color for the leg
    top_color = (0.5, 0.5, 0.5)  # Gray color for the tabletop
    
    # Set up the table leg
    leg_width = width / 8  # Width of the table leg
    leg_height = height  # Height of the table leg
    
    glPushMatrix()
    glTranslatef(0, -height / 2, 0)
    glRotatef(90, 1, 0, 0)  # Rotate to align the leg with the y-axi
    glColor3fv(leg_color)
    draw_cylinder(leg_width / 2, leg_height, 16)  # Draw the leg
    glPopMatrix()
    
    # Set up the tabletop
    glPushMatrix()
    glTranslatef(width - width * width, -height / 2, length - length * length)  # Position the tabletop on top of the leg
    glColor3fv(top_color)
    draw_cube(length, width, 0.1)  # Draw the tabletop
    glPopMatrix()


# Jumping Animation Logic
def jump():
    global current_jump_height, is_jumping
    if is_jumping:
        if current_jump_height < jump_height:
            current_jump_height += jump_speed
        else:
            is_jumping = False
    else:
        if current_jump_height > 0:
            current_jump_height -= jump_speed

# Drawing Functions
colors()
def draw_floor(e):
    glBegin(GL_QUADS)
    for x in range(e * -1, e):
        for z in range(e * -1, e):
            if VHS:
                # VHS madness mode with random colors
                glColor3fv(((x + z) % 2 + random.uniform(-0.2, 0.2), 
                            (x + z) % 2 + random.uniform(-0.2, 0.2), 
                            (x + z) % 2 + random.uniform(-0.2, 0.2)))
            else:
                if preset == "Backrooms":
                    if (x + z) % 2 == rannum2:
                        glColor3fv(floorcolor2)
                    else:
                        # Change this to your desired color (e.g., neon green)
                        glColor3fv(floorcolor)
                if preset == "Earth":
                    if (x + z) % rannum <= rannum2:
                        glColor3fv(floorcolor2)
                    else:
                        # Change this to your desired color (e.g., neon green)
                        glColor3fv(floorcolor)
                else:
                    if (x + z) % 2 == 0:
                        glColor3fv(floorcolor2)
                    else:
                        # Change this to your desired color (e.g., neon green)
                        glColor3fv(floorcolor)
            glVertex3f(x, -1, z)
            glVertex3f(x + 1, -1, z)
            glVertex3f(x + 1, -1, z + 1)
            glVertex3f(x, -1, z + 1)
    glEnd()

pygame.init()
if oldschool == True:
    display = (320, 200)
    font = pygame.font.Font("C64_Pro_Mono-STYLE.ttf", 8)
else:
    display = (1280, 720)
    font = pygame.font.Font("Vgafont.ttf", 16)
if fullscreen == True:
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL  | pygame.FULLSCREEN)
else:
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("Goober Simulator")
pygame.display.set_caption("Goober Simulator")
# Create an overlay surface
overlay_surface = pygame.Surface((display[0], display[1]))
overlay_surface.set_alpha(255)  # Set transparency (0: fully transparent, 255: fully opaque)

clock = pygame.time.Clock()
overlay_surface.fill((0, 0, 0))

def enable_lighting(brightness):
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)  # Enable the first light source

    # Set up the light source position and color
    light_position = [1.0, 1.0, 1.0, 0.0]  # [x, y, z, w], w=0 indicates a directional light
    light_color = [brightness, brightness, brightness, 0.0]  # [r, g, b, a], where r,g,b are RGB values and a is alpha (transparency)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color)

    # Set up the material properties of our objects
    glEnable(GL_COLOR_MATERIAL)  # Allow colors to be used for material properties
    glColorMaterial(GL_FRONT, GL_DIFFUSE)  # Set the color to be used for diffuse reflection
    # Set up the material properties of our objects
    object_color = [1.0, 1.0, 1.0, 1.0]  # Let's make them all white for now
    glMaterialfv(GL_FRONT, GL_DIFFUSE, object_color)
def draw_sphere(radius, slices, stacks):
    for j in range(0, stacks):
        lat0 = math.pi * (-0.5 + (j) / stacks)
        z0 = math.sin(lat0)
        zr0 = math.cos(lat0)

        lat1 = math.pi * (-0.5 + (j + 1) / stacks)
        z1 = math.sin(lat1)
        zr1 = math.cos(lat1)

        # Use Quad strips to draw the sphere
        glBegin(GL_QUAD_STRIP)
        for i in range(0, slices + 1):
            lng = 2 * math.pi * (i - 1) / slices
            x = math.cos(lng)
            y = math.sin(lng)

            # Define vertices for the quad strip
            glNormal3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr0 * radius, y * zr0 * radius, z0 * radius)

            glNormal3f(x * zr1, y * zr1, z1)
            glVertex3f(x * zr1 * radius, y * zr1 * radius, z1 * radius)

        glEnd()
def draw_cylinder(radius, height, slices):
    # Calculate the step angle for each slice
    step = 2 * math.pi / slices
    
    # Begin drawing the cylinder
    glBegin(GL_QUAD_STRIP)
    for i in range(slices + 1):
        # Calculate the angle for the current slice
        angle = i * step
        
        # Calculate the coordinates of the current point on the circle
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        
        # Rotate the coordinates by 90 degrees around the z-axis
        new_x = y
        new_y = -x
        
        # Draw the points on the top and bottom circles of the cylinder
        glVertex3f(new_x, new_y, 0)               # Bottom circle
        glVertex3f(new_x, new_y, height)          # Top circle
    glEnd()
    
    # Draw the top and bottom circles of the cylinder
    glBegin(GL_POLYGON)
    for i in range(slices + 1):
        angle = i * step
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(y, -x, 0)                      # Bottom circle
    glEnd()

    glBegin(GL_POLYGON)
    for i in range(slices + 1):
        angle = i * step
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(y, -x, height)                 # Top circle
    glEnd()
    glRotatef(90, 0, 0, 1)

def draw_ceiling(e, height):
    glBegin(GL_QUADS)
    for x in range(e * -1, e):
        for z in range(e * -1, e):
            glColor3fv(topcolor)
            glVertex3f(x, height, z)
            glVertex3f(x + 1, height, z)
            glVertex3f(x + 1, height, z + 1)
            glVertex3f(x, height, z + 1)
    glEnd()

def draw_person():
    glPushMatrix()  # Push the current matrix onto the stack
    if oldschool == True:
        # Draw the body (cylinder)
        glPushMatrix()
        glColor3fv(shirtcolor)  # Orange color
        glRotatef(90, 1, 0, 0)  # Rotate the body around the y-axis
        draw_cylinder(0.2, 1, 8)
        glPopMatrix()
        # Draw the head (sphere)
        glTranslatef(0, 0.20, 0)  # Move the sphere up to the head level
        glColor3fv(headcolor)  # White color
        draw_sphere(0.2, 15, 4)

        # Draw the eyes (spheres)
        glPushMatrix()  # Push the current matrix onto the stack
        glColor3fv(eyecolor)  # Blue color for eyes

        glTranslatef(-0.15, 0.1, 0.15)  # Move to left eye position
        draw_sphere(0.05, 16, 4)  # Draw left eye

        glPopMatrix()  # Pop the matrix stack to revert to the previous state

        glPushMatrix()  # Push the current matrix onto the stack
        glTranslatef(0.15, 0.1, 0.15)  # Move to right eye position
        draw_sphere(0.05, 16, 4)  # Draw right eye

        glPopMatrix()  # Pop the matrix stack to revert to the previous state

        glPopMatrix()  # Pop the matrix stack to revert to the previous state
    else:
            # Draw the body (cylinder)
        glPushMatrix()
        glColor3fv(shirtcolor)  # Orange color
        glRotatef(90, 1, 0, 0)  # Rotate the body around the y-axis
        draw_cylinder(0.2, 1, 32)
        glPopMatrix()
        # Draw the head (sphere)
        glTranslatef(0, 0.20, 0)  # Move the sphere up to the head level
        glColor3fv(headcolor)  # White color
        draw_sphere(0.2, 15, 32)

        # Draw the eyes (spheres)
        glPushMatrix()  # Push the current matrix onto the stack
        glColor3fv(eyecolor)  # Blue color for eyes

        glTranslatef(-0.15, 0.1, 0.15)  # Move to left eye position
        draw_sphere(0.05, 16, 4)  # Draw left eye

        glPopMatrix()  # Pop the matrix stack to revert to the previous state

        glPushMatrix()  # Push the current matrix onto the stack
        glTranslatef(0.15, 0.1, 0.15)  # Move to right eye position
        draw_sphere(0.05, 16, 4)  # Draw right eye

        glPopMatrix()  # Pop the matrix stack to revert to the previous state

        glPopMatrix()  # Pop the matrix stack to revert to the previous state



def perspective_setup():
    glMatrixMode(GL_PROJECTION)
    gluPerspective(30, (display[0] / display[1]), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def xyrotation(angle_of_rotation, speed):
    angle_radians = math.radians(angle_of_rotation)
    x_component = math.sin(angle_radians)
    z_component = math.cos(angle_radians)
    x_movement = x_component * speed
    z_movement = z_component * speed
    return x_movement, z_movement
def is_collision(x, z):
    # Check if the camera position is within the boundaries of the floor
    if -floor_size <= x <= floor_size and -floor_size <= z <= floor_size:
        return False  # No collision
    else:
        return True   # Collision detected
def get_random_behavior():
    return {
        "jump_chance": random.random(),       # 0.0 to 1.0
        "turn_direction": random.choice([-1, 1, 0]),  # Left, Right, or None
        "turn_strength": random.uniform(1, 5),
        "movement_style": random.choice(["forward", "backward", "none"]),
        "movement_strength": random.uniform(0.1, 0.4),
        "extra_rotation": random.uniform(-3, 3),
        "should_jump": random.random() < 0.1,  # 10% chance to jump
    }
def gooberaispeak():
    prompt.curi()
def main():
    choice = ["sounds/music/goobersong.midi","sounds/music/goobersong2.midi","sounds/music/goobersong3.midi"]
    chosen = random.choice(choice)
    if oldschool == True:
        chosen = "sounds/music/goobersong_oldschool.wav"
    music = pygame.mixer.music.load(chosen)
    pygame.mixer.music.play(-1)
    inactive = 59
    c_up = 0
    c_lr = 0
    glEnable(GL_DEPTH_TEST)  # Enable depth testing
    jump_height = 0.8
    jump_speed = 0.1
    current_jump_height = 5
    is_jumping = False
    person_x = 0
    person_z = 0
    person_rotation = 0
    movspeed = 0
    movspeed2 = 0
    floor_size = 20
    perspective_setup()
    pygame.key.get_mods()
    zoom = False
    zooml = False
    zoomr = False
    #enable_lighting(1)
    while True:
        # Create the thread
        t = threading.Thread(target=gooberaispeak)
        t.daemon = True  # This makes it a daemon thread

        # Start the thread
        t.start()
        gooberline = random.choice(gooberlines)
        global jwalk
        global VHS
        is_jumping = False
        print(person_rotation)
        decision = random.randint(1,50)
        lr = random.randint(1,50)
        turn = random.randint(1,50)
        for i in range(random.randint(1, 500)):
            behavior = get_random_behavior()

            if inactive == 0 and person_rotation != 53:
                # reset rotation
                ...

            if behavior["should_jump"] and not is_jumping and current_jump_height == 0:
                is_jumping = True

            person_rotation += behavior["turn_direction"] * behavior["turn_strength"]

            if behavior["movement_style"] == "forward":
                x_move, z_move = xyrotation(person_rotation, behavior["movement_strength"] + movspeed / 3)
                ...
            elif behavior["movement_style"] == "backward":
                x_move, z_move = xyrotation(person_rotation, behavior["movement_strength"] + movspeed / 3)
                x_move *= -1
                z_move *= -1

            person_rotation += behavior["extra_rotation"]

        for i in range(random.randint(5,100)):
            if inactive == 0 and person_rotation != 53:
                zooml = False
                zoomr = False
                rotation_speed = 1
                if person_rotation < 53:
                    person_rotation += rotation_speed
                if person_rotation > 53:
                    person_rotation -= rotation_speed
            print(inactive)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            keys = pygame.key.get_pressed()

            inactive += 2
            if 1 <= decision <= 10:
                if not is_jumping and current_jump_height == 0:
                    is_jumping = True
            if 1 <= turn <= 15:
                person_rotation += 3
            if 15 <= turn <= 25:
                person_rotation -= 3
            if 30 <= decision <= 50:
                if jwalk == True:
                    if not is_jumping and current_jump_height == 0:
                        is_jumping = True
                rotation_speed = random.uniform(-3, 3)
                person_rotation += rotation_speed
                x_move, z_move = xyrotation(person_rotation, 0.1 + movspeed / 3)
                new_person_x = person_x + x_move
                new_person_z = person_z + z_move
                if -floor_size < new_person_x < floor_size and -floor_size < new_person_z < floor_size:
                    person_x = new_person_x
                    person_z = new_person_z
            if 15<= decision <= 25:
                rotation_speed = random.uniform(-3, 3)
                person_rotation += rotation_speed
                x_move, z_move = xyrotation(person_rotation, 0.1 + movspeed / 3)
                new_person_x = person_x - x_move
                new_person_z = person_z - z_move
                if -floor_size < new_person_x < floor_size and -floor_size < new_person_z < floor_size:
                    person_x = new_person_x
                    person_z = new_person_z
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
            if keys[pygame.K_UP]:
                c_up += 1
            if keys[pygame.K_DOWN]:
                c_up -= 1
            if keys[pygame.K_q]:
                zooml = False
                zoomr = False
            # Handle left and right camera rotation collision with walls
            if zoom == True:
                if c_lr > 0:
                    c_lr -= 0.1
                if c_lr < 0:
                    c_lr += 0.1
                if c_lr == 0:
                    zoom = False
                    zooml = False
                    zoomr = False
            if keys[pygame.K_LEFT]:
                zoom = True
                zooml = True
            if zooml == True:
                zoomr = False
                new_c_lr = c_lr - 0.3
                if new_c_lr < -floor_size:
                    new_c_lr = -floor_size
                elif new_c_lr > floor_size:
                    new_c_lr = floor_size
                if not is_collision(person_x + 5, person_z + 5 + new_c_lr):
                    c_lr = new_c_lr

            if keys[pygame.K_RIGHT]:
                zoom = True
                zoomr = True
            if zoomr == True:
                zooml = False
                new_c_lr = c_lr + 0.3
                if new_c_lr < -floor_size:
                    new_c_lr = -floor_size
                elif new_c_lr > floor_size:
                    new_c_lr = floor_size
                if not is_collision(person_x + 5, person_z + 5 + new_c_lr):
                    c_lr = new_c_lr

            if 1 <= lr <= 20:
                movspeed = movspeed + 0.02
            if movspeed > 0.3:
                movspeed = 0.3
            if movspeed > 0:
                movspeed = movspeed - 0.01
            if c_up > 2:
                c_up = 2
            if c_up < 0:
                c_up = 0
            if is_jumping:
                x_move, z_move = xyrotation(person_rotation, 0.1 + movspeed / 2)
                new_person_x = person_x + x_move
                new_person_z = person_z + z_move
                if -floor_size < new_person_x < floor_size and -floor_size < new_person_z < floor_size:
                    person_x = new_person_x
                    person_z = new_person_z
                if current_jump_height < jump_height:
                    current_jump_height += jump_speed
                else:
                    is_jumping = False
            if not is_jumping:
                if current_jump_height > 0:
                    x_move, z_move = xyrotation(person_rotation, 0.1 + movspeed / 2)
                    new_person_x = person_x + x_move
                    new_person_z = person_z + z_move
                    if -floor_size < new_person_x < floor_size and -floor_size < new_person_z < floor_size:
                        person_x = new_person_x
                        person_z = new_person_z
                    current_jump_height -= jump_speed
                if current_jump_height < 0:
                    current_jump_height = 0
            person_y = current_jump_height
            movspeed2 = -movspeed
            if inactive > 600:
                inactive = 600
            elif inactive > 0:
                inactive -= 1
            # Adjust camera position based on boundaries
            camera_x = person_x + 5
            camera_z = person_z + 5
            if camera_x > floor_size:
                camera_x = floor_size
            elif camera_x < -floor_size:
                camera_x = -floor_size
            if camera_z > floor_size:
                camera_z = floor_size
            elif camera_z < -floor_size:
                camera_z = -floor_size
            
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            gluLookAt(camera_x, person_y + 3 + c_up, camera_z + c_lr,  # Camera position
                      person_x + math.sin(math.radians(person_rotation)),  # Pointing towards x direction based on rotation
                      1,  # Keep the y-coordinate constant to avoid zooming
                      person_z + math.cos(math.radians(person_rotation)),  # Pointing towards z direction based on rotation
                      0, 1, 0)  # Up vector
            glClearColor(*wallcolor, 1.0)
            draw_floor(floor_size)
            draw_ceiling(floor_size, jump_height + 5.5)
            glPushMatrix()
            glTranslatef(person_x, person_y, person_z)
            glRotatef(person_rotation, 0, 1, 0)
            draw_person()
            if person_rotation >= 360:
                person_rotation = 0
            if person_rotation <= -360:
                person_rotation = 0
            glPopMatrix()
            glPushMatrix()
            glTranslatef(0, 1, 0)  # Adjust the position of the table as needed
            glPopMatrix()
            if VHS== True:                    
                rotation_speed = random.uniform(-3, 3)
                person_rotation += rotation_speed
            drawText(0, 0, gooberline)
            if oldschool == True:
                clock.tick(10)
            else:
                clock.tick(30)
            pygame.display.flip()

main()
