import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Dimensions for the Torso(Abdomen).
TORSO_RADIUS=0.1
TORSO_HEIGHT=0.4

# Dimensions for the Head.
HEAD_RADIUS = 0.1

# Dimensions for Arms (Lower as well as upper)
UPPER_ARM_HEIGHT=0.2
UPPER_ARM_WIDTH=0.07

LOWER_ARM_HEIGHT=0.2
LOWER_ARM_WIDTH=0.05

# Dimensions for Legs.
UPPER_LEG_HEIGHT=0.2
UPPER_LEG_WIDTH=0.08

LOWER_LEG_HEIGHT=0.2
LOWER_LEG_WIDTH=0.06

# Dimensions for Shoulder and Jips.
SHOLDER_WIDTH = 0.2
HIP_WIDTH = 0.2


HEADX=0.1
HEADY=TORSO_HEIGHT

LUAX=-1.0 * SHOLDER_WIDTH / 2
RUAX=SHOLDER_WIDTH / 2
LUAY=RUAY=TORSO_HEIGHT
LLAY=RLAY=LOWER_ARM_HEIGHT

LULX=-1.0 * HIP_WIDTH / 2
RULX=HIP_WIDTH / 2
LULY=RULY=0
LLLY=RLLY=LOWER_LEG_HEIGHT

# Initial position(in terms of Roatation) of the different body parts
t0=0.0
t1=0.0
t2=0.0
t3=90.0
t4=-90.0
t5=50.0
t6=0.0
t7=180.0
t8=0.0
t9=180.0
t10=0.0

# The display function that will draw all the parts.
def display():
  glEnable(GL_DEPTH_TEST)
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(20, 1.0, 1.0, 100.0)
  
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluLookAt(2.0, 2.0, 2.0, 0.0, 0.2, 0.0, 0.0, 1.0, 0.0)

  #TORSO
  materials(torso_amb, torso_diff, torso_spec, torso_shin)
  glRotatef(t0, 0.0, 1.0, 0.0)
  torso()
  glPushMatrix()

  #HEAD
  materials(face_amb, face_diff, face_spec, face_shin)
  glTranslatef(0.0, HEADX, 0.0)
  glRotatef(t1, 1.0, 0.0, 0.0)
  glRotatef(t2, 0.0, 1.0, 0.0)
  glTranslatef(0.0, HEADY, 0.0)
  head()

  #nose
  glTranslatef(0.0, 0.0, HEAD_RADIUS)
  #glRotatef(0, 1.0, 0.0, 0.0)
  nose()

  #eyes
  glTranslatef(HEAD_RADIUS/2, HEAD_RADIUS/2, 0.0)
  #glRotatef(0, 1.0, 0.0, 0.0)
  eyes()

  glTranslatef(-HEAD_RADIUS, 0.0, 0.0)
  #glRotatef(0, 1.0, 0.0, 0.0)
  eyes()
  
  #LEFT UPPER ARM
  glPopMatrix()
  materials(uparm_amb, uparm_diff, uparm_spec, uparm_shin)
  glPushMatrix()
  glTranslatef(LUAX, LUAY, 0.0)
  glRotatef(t3, 1.0, 0.0, 0.0)
  upper_arm()

  #LEFT LOWER ARM
  materials(face_amb, face_diff, face_spec, face_shin)
  glTranslatef(0.0, LLAY, 0.0)
  glRotatef(t4, 1.0, 0.0, 0.0)
  lower_arm()

  #RIGHT UPPER ARM
  glPopMatrix()
  materials(uparm_amb, uparm_diff, uparm_spec, uparm_shin)
  glPushMatrix()
  glTranslatef(RUAX, RUAY, 0.0)
  glRotatef(t5, 1.0, 0.0, 0.0)
  upper_arm()

  #RIGHT LOWER ARM
  materials(face_amb, face_diff, face_spec, face_shin)
  glTranslatef(0.0, RLAY, 0.0)
  glRotatef(t6, 1.0, 0.0, 0.0)
  lower_arm()

  #LEFT UPPER LEG
  glPopMatrix()
  materials(brass_amb, brass_diff, brass_spec, brass_shin)
  glPushMatrix()
  glTranslatef(LULX, LULY, 0.0)
  glRotatef(t7, 1.0, 0.0, 0.0)
  upper_leg()

  #LEFT LOWER LEG
  glTranslatef(0.0, LLLY, 0.0)
  glRotatef(t8, 1.0, 0.0, 0.0)
  lower_leg()

  #RIGHT UPPER LEG
  glPopMatrix()
  glPushMatrix()
  glTranslatef(RULX, RULY, 0.0)
  glRotatef(t9, 1.0, 0.0, 0.0)
  upper_leg()

  #RIGHT LOWER LEG
  glTranslatef(0.0, RLLY, 0.0)
  glRotatef(t10, 1.0, 0.0, 0.0)
  lower_leg()
  glPopMatrix()
  #glutSwapBuffers()
  glFlush()

# These are the specific methods for specific Body parts.
def torso():
  glPushMatrix()
  glRotatef(-90.0, 1.0, 0.0, 0.0)
  glTranslatef(0.0,0.0,0.2)
  glScalef(0.2, 0.1 , 0.4)
  glutSolidCube(1.2)
  glPopMatrix()

def head():
  glPushMatrix()
  glRotatef(-90.0, 1.0, 0.0, 0.0)
  glutSolidCube(0.18)
  glPopMatrix()
  
def upper_arm():
  glPushMatrix()
  glTranslatef(0.0, 0.5*UPPER_ARM_HEIGHT, 0.0)
  glScalef(UPPER_ARM_WIDTH, UPPER_ARM_HEIGHT, UPPER_ARM_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

def lower_arm():
  glPushMatrix()
  glTranslatef(0.0, 0.5*UPPER_ARM_HEIGHT, 0.0)
  glScalef(LOWER_ARM_WIDTH, LOWER_ARM_HEIGHT, LOWER_ARM_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

def upper_leg():
  glPushMatrix()
  glTranslatef(0.0, 0.5*LOWER_ARM_HEIGHT, 0.0)
  glScalef(UPPER_LEG_WIDTH, UPPER_LEG_HEIGHT, UPPER_LEG_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

def lower_leg():
  glPushMatrix()
  glTranslatef(0.0, 0.5*LOWER_ARM_HEIGHT, 0.0)
  glScalef(LOWER_LEG_WIDTH, LOWER_LEG_HEIGHT, LOWER_LEG_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

def nose():
  glPushMatrix()  
  glRotatef(-90.0, 1.0, 0.0, 0.0)
  glutSolidSphere(HEAD_RADIUS/5, 10, 10)
  glPopMatrix()

def eyes():
  glPushMatrix()
  materials(eye_amb, eye_diff, eye_spec, eye_shin)
  glRotatef(-90.0, 1.0, 0.0, 0.0)
  glutSolidSphere(HEAD_RADIUS/5, 10, 10)
  glPopMatrix() 

# This function defines functionality for pressing different keys on the keyboard.  
def mykey(key, x, y):
  global t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10
  if key=='d': # TORSO
    t0 = t0 + 10.0
  elif key=='D':
    t0 = t0 - 10.0
  elif key=='r': # HEAD 2
    t2 = t2 + 10.0
  elif key=='R':
    t2 = t2 - 10.0
  elif key=='s': # LUA
    t3 = t3 + 10.0
  elif key=='S':
    t3 = t3 - 10.0
  elif key=='a': # LLA
    t4 = t4 + 10.0
  elif key=='A':
    t4 = t4 - 10.0
  elif key=='f': # RUA
    t5 = t5 + 10.0
  elif key=='F':
    t5 = t5 - 10.0
  elif key=='g': # RLA
    t6 = t6 + 10.0
  elif key=='G':
    t6 = t6 -10.0
  elif key=='x': # LUL
    t7 = t7 + 10.0
  elif key=='X':
    t7 = t7 - 10.0
  elif key=='z': # LLL
    t8 = t8 + 10.0
  elif key=='Z':
    t8 = t8 -10.0
  elif key=='c': # RUL
    t9 = t9 + 10.0
  elif key=='C':
    t9 = t9 - 10.0
  elif key=='v': # RLL
    t10 = t10 + 10.0
  elif key=='V':
    t10 = t10 - 10.0
  elif key=='q':
    sys.exit()

  glutPostRedisplay()

# This function provides the Lighting to the model.
def materials(amb, diff, spec, shin):
  glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, amb)
  glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, diff)
  glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, spec)
  glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, shin)
  
glutInit( sys.argv )
#glutInitDisplayMode( GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH )
glutInitDisplayMode( GLUT_RGBA | GLUT_SINGLE | GLUT_DEPTH )
glutInitWindowSize( 500, 500 )
glutInitWindowPosition(0,0)
glutCreateWindow( 'robot' )
glutDisplayFunc( display )
glutKeyboardFunc(mykey)

glEnable(GL_DEPTH_TEST)
glEnable(GL_CULL_FACE)
glCullFace(GL_BACK)

glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)

light0_pos = 10.0, 10.0, 0.0, 0.0
diffuse0 = 0.5, 0.5, 0.5, 1.0
specular0 = 0.5, 0.5, 0.5, 1.0
ambient0 = 0.8, 0.8, 0.8, 1.0

glMatrixMode(GL_MODELVIEW)
glLightfv(GL_LIGHT0, GL_POSITION, light0_pos)
glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse0)
glLightfv(GL_LIGHT0, GL_SPECULAR, specular0)
glLightfv(GL_LIGHT0, GL_AMBIENT, ambient0)

p=gluNewQuadric()
gluQuadricDrawStyle(p, GLU_FILL)
gluQuadricNormals(p, GLU_SMOOTH)

# Colour scheme for Pants!!..
brass_amb = 0.0, 0.0, 1.0, 1.0
brass_diff = 0.67, 0.45, 0.21, 1.0
brass_spec = 0.2, 0.4, 0.3, 1.0
brass_shin = 1.8

# Color Scheme for Shirts (Torso)
torso_amb = 1.0, 0.0, 0.0, 1.0
torso_diff = 0.67, 0.45, 0.21, 1.0
torso_spec = 0.2, 0.4, 0.3, 1.0
torso_shin = 1.8

# Color Scheme for UpperArm
uparm_amb = 0.5, 0.5, 0.0, 1.0
uparm_diff = 0.67, 0.45, 0.21, 1.0
uparm_spec = 0.2, 0.4, 0.3, 1.0
uparm_shin = 1.8

# Color scheme for Face!!..
face_amb = 0.42, 0.21, 0.03, 0.0
face_diff = 0.78, 0.57, 0.11, 1.0
face_spec = 0.99, 0.91, 0.81, 1.0
face_shin = 27.8

# Color scheme for Eyes!!..
eye_amb = 0.0, 0.0, 0.0, 1.0
eye_diff = 0.78, 0.57, 0.11, 1.0
eye_spec = 0.99, 0.91, 0.81, 1.0
eye_shin = 27.8

p_amb = 0.3, 0.0, 0.0, 1.0
p_diff = 0.6, 0.0, 0.0, 1.0
p_spec = 0.8, 0.6, 0.6, 1.0
p_shin = 32.8

glutMainLoop()
