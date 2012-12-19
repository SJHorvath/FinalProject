from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys, random, math
import Camera
 
NAME = 'Snowmen!'
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
 
#Create a "blank" camera that can be accessed by all functions... this is probably the wrong way to do it...
myCamera = Camera.Camera(0,.5,2)
 
#Global variables to track the mouse's last coordinates in the window - we'll say it starts at the center of the screen:
mouseLastX = WINDOW_WIDTH / 2
mouseLastY = WINDOW_HEIGHT / 2
 
#List of currently-pressed keys, allowing OpenGL to process multiple keypresses:
keyQueue = []
 
def main():
        '''Initiates the window and GL system, then starts the program's main loop.'''
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        glutCreateWindow(NAME)
   
        glutKeyboardFunc(keyPressed)
        glutKeyboardUpFunc(keyReleased)
        glutPassiveMotionFunc(mouseMoved)
 
        glutDisplayFunc(display)
        glutIdleFunc(display)
   
        initGL(WINDOW_WIDTH, WINDOW_HEIGHT)
        initLighting()
 
        glutMainLoop()
 
 
def initGL(Width, Height):
        '''Defines the perspective used to view 3D elements.'''
 
        # This Will Clear The Background Color To Black
        glClearColor(0.0, 0.0, 0.0, 0.0)
        # Enables Clearing Of The Depth Buffer
        glClearDepth(1.0)
 
        # The Type Of Depth Test To Do
        glDepthFunc(GL_LESS)
        # Enables Depth Testing
        glEnable(GL_DEPTH_TEST)
 
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
 
        # Calculate The Aspect Ratio Of The Window
        gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
 
 
def initLighting():
        '''Sets up the lighting under which the scene is viewed.'''
   
        light_diffuse = (.5, .5, .5, .5)
        light_position = (.05, .1, -.5, 1)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
 
        light_ambient = (.5, .5, .5, 1)
        light_position = (0, 0, 1, 0)
        glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient)
        glLightfv(GL_LIGHT1, GL_POSITION, light_position)
 
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys, random, math
import Camera
 
NAME = 'Snowmen!'
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
 
#Create a "blank" camera that can be accessed by all functions... this is probably the wrong way to do it...
myCamera = Camera.Camera(0,.5,2)
 
#Global variables to track the mouse's last coordinates in the window - we'll say it starts at the center of the screen:
mouseLastX = WINDOW_WIDTH / 2
mouseLastY = WINDOW_HEIGHT / 2
 
#List of currently-pressed keys, allowing OpenGL to process multiple keypresses:
keyQueue = []
 
def main():
        '''Initiates the window and GL system, then starts the program's main loop.'''
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        glutCreateWindow(NAME)
   
        glutKeyboardFunc(keyPressed)
        glutKeyboardUpFunc(keyReleased)
        glutPassiveMotionFunc(mouseMoved)
 
        glutDisplayFunc(display)
        glutIdleFunc(display)
   
        initGL(WINDOW_WIDTH, WINDOW_HEIGHT)
        initLighting()
 
        glutMainLoop()
 
 
def initGL(Width, Height):
        '''Defines the perspective used to view 3D elements.'''
 
        # This Will Clear The Background Color To Black
        glClearColor(0.0, 0.0, 0.0, 0.0)
        # Enables Clearing Of The Depth Buffer
        glClearDepth(1.0)
 
        # The Type Of Depth Test To Do
        glDepthFunc(GL_LESS)
        # Enables Depth Testing
        glEnable(GL_DEPTH_TEST)
 
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
 
        # Calculate The Aspect Ratio Of The Window
        gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
 
 
def initLighting():
        '''Sets up the lighting under which the scene is viewed.'''
   
        light_diffuse = (.5, .5, .5, .5)
        light_position = (.05, .1, -.5, 1)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
 
        light_ambient = (.5, .5, .5, 1)
        light_position = (0, 0, 1, 0)
        glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient)
        glLightfv(GL_LIGHT1, GL_POSITION, light_position)
        glEnable(GL_COLOR_MATERIAL);
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHT1)
        glShadeModel(GL_SMOOTH)
 
 
 
def keyPressed(key, x, y):
        '''Handles when a key is pressed.'''
   
        global keyQueue
 
        #Convert letters to lowercase, so the Shift and Capslock keys don't prevent them from working
        key = key.lower()
 
        #Add key to list if it isn't already there, to be processed later by handleKeys
        if not key in keyQueue:
                keyQueue.append(key)
 
 
def keyReleased(key, x, y):
        '''Handles when a key is released.'''
 
        #Remove the key from the list of currently-pressed keys
        global keyQueue
 
        keyQueue.remove(key.lower())
 
 
def handleKeys():
        '''Moves the camera based on which keys are currently held down.  The camera is moved by W, A, S, and D.'''
   
        global keyQueue
 
        if keyQueue:
        #Process any keys that might be currently pressed:
                if 'a' in keyQueue:
                        myCamera.strafeRight(.02)
                if 'd' in keyQueue:
                        myCamera.strafeLeft(.02)
                if 'w' in keyQueue:
                        myCamera.moveForward(.02)
                if 's' in keyQueue:
                        myCamera.moveBack(.02)
 
        #Ideally, the amount we move should be calculated by (framerate / distance we want to move per second), because this function is called at every step
 
 
def mouseMoved(mouseX, mouseY):
        '''Handles the mouse's position changing by rotating the camera accordingly.'''
 
        global mouseLastX
        global mouseLastY
 
        #Calculate the mouse's change in position by finding the difference between its current and most recent positions:
        xChange = mouseX - mouseLastX
        yChange = mouseY - mouseLastY
 
        myCamera.rotateHorizontal(-xChange * .6)
        myCamera.rotateVertical(-yChange * .2)
 
        #Now we use the current coordinates of the mouse as the most recent coordinates.
        mouseLastX = mouseX
        mouseLastY = mouseY
 
 
def Snowman(radius):
 
        glMaterial(GL_FRONT, GL_AMBIENT, (1, 0, 1))
        glTranslate(0, radius, 0)
        glutSolidSphere(.15, 15, 15)
        glTranslate(0, radius, 0)
        glutSolidSphere(.1, 15, 15)
        glTranslate(0, radius-.05, 0)
        glutSolidSphere(.05, 15, 15)
        glTranslate(0, -3*radius+.15, 0)
 
 
def drawScene():
        '''Draws the entire scene to be viewed, consisting of three snowmen of different sizes and a grey floor.'''
   
 
        for i in range(-5,5):
                for j in range(-5,5):
                        glPushMatrix()
            #glMaterial(GL_FRONT, GL_AMBIENT, (.2*i, .2*j, .2));
                        glTranslatef(i*1.05,0,j * 1.05)
 
                        glColor3f(0.4*+i, 0.3*+j,0.3);
                        if i == 2:
                                Snowman(.1)
                        elif j == 3:
                                Snowman(.13)
                        else:
                                Snowman(.17)
                        glPopMatrix()
       
        #Draw the ground... adapted from C++ code found at http://www.lighthouse3d.com/opengl/picking/index.php3?color1
   
        #It's [slate] grey!
        glColor3f(0.421, 0.480, 0.542)
   
        glBegin(GL_QUADS)
        glVertex3f(-100, 0, -100)
        glVertex3f(-100, 0,  100)
        glVertex3f( 100, 0,  100)
        glVertex3f( 100, 0, -100)
        glEnd()
 
   
def display(x=0, y=0):
        '''Main display function - clears the screen, moves the camera according to any keys that are currently pressed, transforms the scene based on the camera's position and angle, and draws the entire scene.'''
   
        #Clear the display
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
 
        #We need to be constantly checking what keys are currently pressed, and moving the camera accordingly:
        handleKeys()
   
        #Now, position the view according to the camera
        myCamera.render()
 
        #Draw everything
        drawScene()
   
        #Make sure all drawing functions have been called.
        glFlush()
 
 
if __name__ == '__main__':
        main()
        # glEnable(GL_LIGHT1)
        glShadeModel(GL_SMOOTH)
 
 
 
def keyPressed(key, x, y):
        '''Handles when a key is pressed.'''
   
        global keyQueue
 
        #Convert letters to lowercase, so the Shift and Capslock keys don't prevent them from working
        key = key.lower()
 
        #Add key to list if it isn't already there, to be processed later by handleKeys
        if not key in keyQueue:
                keyQueue.append(key)
 
 
def keyReleased(key, x, y):
        '''Handles when a key is released.'''
 
        #Remove the key from the list of currently-pressed keys
        global keyQueue
 
        keyQueue.remove(key.lower())
 
 
def handleKeys():
        '''Moves the camera based on which keys are currently held down.  The camera is moved by W, A, S, and D.'''
   
        global keyQueue
 
        if keyQueue:
        #Process any keys that might be currently pressed:
                if 'a' in keyQueue:
                        myCamera.strafeRight(.02)
                if 'd' in keyQueue:
                        myCamera.strafeLeft(.02)
                if 'w' in keyQueue:
                        myCamera.moveForward(.02)
                if 's' in keyQueue:
                        myCamera.moveBack(.02)
 
        #Ideally, the amount we move should be calculated by (framerate / distance we want to move per second), because this function is called at every step
 
 
def mouseMoved(mouseX, mouseY):
        '''Handles the mouse's position changing by rotating the camera accordingly.'''
 
        global mouseLastX
        global mouseLastY
 
        #Calculate the mouse's change in position by finding the difference between its current and most recent positions:
        xChange = mouseX - mouseLastX
        yChange = mouseY - mouseLastY
 
        myCamera.rotateHorizontal(-xChange * .6)
        myCamera.rotateVertical(-yChange * .2)
 
        #Now we use the current coordinates of the mouse as the most recent coordinates.
        mouseLastX = mouseX
        mouseLastY = mouseY
 
 
def Snowman(radius):
 
        glMaterial(GL_FRONT, GL_AMBIENT, (1, 0, 1))
        glTranslate(0, radius, 0)
        glutSolidSphere(.15, 15, 15)
        glTranslate(0, radius, 0)
        glutSolidSphere(.1, 15, 15)
        glTranslate(0, radius-.05, 0)
        glutSolidSphere(.05, 15, 15)
        glTranslate(0, -3*radius+.15, 0)


 
 
def drawScene():
        '''Draws the entire scene to be viewed, consisting of three snowmen of different sizes and a grey floor.'''
   
 
        for i in range(-5,5):
                for j in range(-5,5):
                        glPushMatrix()
            #glMaterial(GL_FRONT, GL_AMBIENT, (.2*i, .2*j, .2));
                        glTranslatef(i*1.05,0,j * 1.05)
 
                        glColor3f(0.9, 0.1,0.3);
                        if i == 2:
                                Snowman(.1)
                        elif j == 3:
                                Snowman(.13)
                        else:
                                Snowman(.17)
                        glPopMatrix()
       
        #Draw the ground... adapted from C++ code found at http://www.lighthouse3d.com/opengl/picking/index.php3?color1
   
        #It's [slate] grey!
        glColor3f(0.421, 0.480, 0.542)
   
        glBegin(GL_QUADS)
        glVertex3f(-100, 0, -100)
        glVertex3f(-100, 0,  100)
        glVertex3f( 100, 0,  100)
        glVertex3f( 100, 0, -100)
        glEnd()
 
   
def display(x=0, y=0):
        '''Main display function - clears the screen, moves the camera according to any keys that are currently pressed, transforms the scene based on the camera's position and angle, and draws the entire scene.'''
   
        #Clear the display
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
 
        #We need to be constantly checking what keys are currently pressed, and moving the camera accordingly:
        handleKeys()
   
        #Now, position the view according to the camera
        myCamera.render()
 
        #Draw everything
        drawScene()
   
        #Make sure all drawing functions have been called.
        glFlush()
 
 
if __name__ == '__main__':
        main()