



from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys, random, math
import Camera
 
NAME = 'Snowmen!'
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
 
#Create a "blank" camera that can be accessed by all functions... this is probably the wrong way to do it...
myCamera = Camera.Camera(0,.5,2)
 
#Global variables to track the mouse's last coordinates in the window - we'll say it starts at the center of the screen:
mouseLastX = WINDOW_WIDTH / 2
mouseLastY = WINDOW_HEIGHT / 2
 
#List of currently-pressed keys, allowing OpenGL to process multiple keypresses:
keyQueue = []

SIM_WIDTH = 15
 
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

        global_ambient = ( 0.5, 0.5, 0.5, 1.0 );
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, global_ambient);
 
 
def initLighting():
 	'''Sets up the lighting under which the scene is viewed.'''

		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glEnable(GL_DEPTH_TEST)
		glEnable(GL_LIGHT1)
		glShadeModel(GL_SMOOTH)

		ambientLight = ( 0.2, 0.2, 0.2, 1.0 );
		diffuseLight = ( 0.8, 0.8, 0.8, 1.0 );
		specularLight = ( 0.5, 0.5, 0.5, 1.0 );
		position = ( -1.5, 1.0, -4.0, 1.0 );

		glLightfv(GL_LIGHT0, GL_AMBIENT, ambientLight);
		glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuseLight);
		glLightfv(GL_LIGHT0, GL_SPECULAR, specularLight);
		glLightfv(GL_LIGHT0, GL_POSITION, position)	

		glEnable(GL_COLOR_MATERIAL);
		glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE);



		specReflection = ( 0.6, 0.6, 0.6, 1.0 )
		glMaterialfv(GL_FRONT, GL_SPECULAR, specReflection);
		glMateriali(GL_FRONT, GL_SHININESS, 96);


 
 
 
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
                        myCamera.strafeRight(.1)
                if 'd' in keyQueue:
                        myCamera.strafeLeft(.1)
                if 'w' in keyQueue:
                        myCamera.moveForward(.1)
                if 's' in keyQueue:
                        myCamera.moveBack(.1)
                if ' ' in keyQueue:
                        myCamera.moveUp(.1)
 
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

def pacMan(size):
        glPushMatrix()
        glRotate(1, 23, 1, 23)
        glColor(1, 1, 0)
        glutSolidSphere(size+.02, 15, 15)
        #glColor(.0, .0, .0)
       
        glRotate(190, 1, 1, 1)
    #back endcap
        glBegin(GL_TRIANGLES)
        glColor(0, 0, 0)
        glVertex3f(size, 0, 0)
        glVertex3f(0, -size, 0)
        glVertex3f(0, -size, 0)
        glEnd()

        # front endcap
        glBegin(GL_TRIANGLES)
        glColor(0, 0, 0)
        glVertex3f(size, 0, size)
        glVertex3f(0, 0, size)
        glVertex3f(0, -size , size)
        glEnd()

        #bottom
        glBegin(GL_QUADS)
        glColor(0, 0, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(size, 0, 0)
        glVertex3f(size, 0, size)
        glVertex3f(0, 0, size)
        glEnd()

        #back
        #glBegin(GL_QUADS)
        #glColor(0, 0, 0)
        #glVertex3f(0, 0, 0)
        #glVertex3f(0, -size, 0)
        #glVertex3f(0, -size, size)
        #glVertex3f(0, 0, size)
        #glEnd()

        #top
        glBegin(GL_QUADS)
        glColor(0, 0, 0)
        glVertex3f(0, -size, 0)
        glVertex3f(size, 0, 0)
        glVertex3f(size, 0, size)
        glVertex3f(0, -size, size)
        glEnd()

        glRotate(-190, 1, 1, 1)

        glTranslate(size*.6 , size*.6, size*.6)
        glutSolidSphere(size*.2, 5, 6)
        glTranslate(-size*.6, -size*.6, -size*.6)
        glTranslate(-size*.6, size*.6, size*.6)
        glutSolidSphere(size*.2, 5, 6)
        glTranslate(size*.6, -size*.6, -size*.6)            

        #glTranslate(size*.6 , size*.6, size*.6)
        glPopMatrix()

def Cone():
        glTranslate(0, 0, 0)
        glColor(0.82, 0.41, 0.12)
        glRotate(90,1,0,0)
        glutSolidCone(.15, .25, 10, 10)

        glTranslate(0, 0, -.15)
        glColor(1, 0.41, 0.71)
        glutSolidSphere(.2, 8, 10)

def Block():
        glColor3f(0.421, 0.480, 0.542)
        glutSolidCube(1)
 
 
def drawScene():
        '''Draws the entire scene to be viewed, consisting of three snowmen of different sizes and a grey floor.'''
   
 
        for i in range(-10,10):
                for j in range(-10,10):
                        glPushMatrix()
                        #glMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE , (.2*i, .2*j, .2));
                        glTranslatef(i*1.05,0,j * 1.05)
 
                        if i == 2:
                                Block()
                        elif j == 3:
                                Cone()
                        else:
                                pacMan(.2)
                        glPopMatrix()
       
        #Draw the ground... adapted from C++ code found at http://www.lighthouse3d.com/opengl/picking/index.php3?color1
   
        glTranslate(0,-0.5,0)
        glColor3f(0.1,0.9,0.1)

        glBegin(GL_QUADS)
        glVertex3f(-SIM_WIDTH, 0, -SIM_WIDTH)
        glVertex3f(-SIM_WIDTH, 0,  SIM_WIDTH)
        glVertex3f( SIM_WIDTH, 0,  SIM_WIDTH)
        glVertex3f( SIM_WIDTH, 0, -SIM_WIDTH)
        glEnd()
        #It's [slate] grey!
        glPushMatrix()
        glTranslate(-10,0.01,-10)
        glColor3f(0.421, 0.480, 0.542)
  

        glBegin(GL_LINES);
        for i in range(-2,22):
            if i <= 0:
                glColor3f(.6,.3,.3); 
            else:
                glColor3f(.75,.75,.75);         
            glVertex3f(i,0,0);
            glVertex3f(i,0,22);
            if i==0: 
                glColor3f(.3,.3,.6); 
            else:
                glColor3f(.75,.75,.75);
                glVertex3f(0,0,i);
                glVertex3f(22,0,i);
        glEnd()
        glPopMatrix()
 
   
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
