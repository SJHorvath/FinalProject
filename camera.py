from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
 
class Camera:
 
        def __init__(self, startX=0, startY=0, startZ=0, startXrot=0, startYrot=0, startZrot=0):
                self.x = startX
                self.y = startY
                self.z = startZ
                self.xRot = startXrot
                self.yRot = startYrot
                self.zRot = startZrot
 
 
        def moveForward(self, amount):
                self.moveZDirection(amount, self.yRot, self.xRot)
                print self.xRot, " x"
 
 
        def moveBack(self, amount):
                self.moveZDirection(amount, self.yRot+180, self.xRot+180)
 
 
        def strafeRight(self, amount):
                self.moveDirection(amount, self.yRot + 90)
 
         
        def strafeLeft(self, amount):
                self.moveDirection(amount, self.yRot - 90)
 
   
        def moveDirection(self, amount, angle):
                angle = math.radians(angle)
 
                forwardComponent = -(math.cos(angle) * amount)
                sidewaysComponent = -(math.sin(angle) * amount)
         
                self.z += forwardComponent
                self.x += sidewaysComponent
 
        def moveZDirection(self, amount, angle, vertical):
                self.moveDirection(amount, angle)
                angle = math.radians(angle)
                vertical = math.radians(vertical)
                verticalComponent = (math.sin(vertical) * amount)
                self.y += verticalComponent
 
 
        def moveUp(self, amount):
                self.y += amount
 
         
        def moveDown(self, amount):
                self.y -= amount
 
 
        def rotateHorizontal(self, amount):
                self.yRot += amount
 
         
        def rotateVertical(self, amount):
                self.xRot += amount
 
         
        def render(self):
                glRotatef(-self.xRot, 1.0, 0.0, 0.0)
                glRotatef(-self.yRot, 0.0, 1.0, 0.0)
                glRotatef(-self.zRot, 0.0, 0.0, 1.0)
                glTranslatef(-self.x, -self.y, -self.z)
