Humanoid
========

A humanoid using OpenGL with Python.

I have divided the whole module into different SubModules corresponding to each body Part so as to provide speciality (in terms of size, colour and lighting) to each and every part. The different Sub-Modules are as follows:
1. TORSO:
This module defines the abdomen portion of the Humanoid. This is the root of the Hierarchy used in this model as all the other body parts are drawn with respect to this part. So, if this part rotates, all the body parts rotate.
Its size is defined as follows:
TORSO_RADIUS=0.1 # This variable contains the radius of the torso. TORSO_HEIGHT=0.4 # This variable contains the Height of the torso.
The function used for drawing this Torso is:
glPushMatrix()
# We rotate the torso by -90 to make it look vertical as the humanoid will be standing initially.
glRotatef(-90.0, 1.0, 0.0, 0.0)
#We translate the torso by 0.2 units in ‘Z’ direction.
glTranslatef(0.0,0.0,0.2)
#Now we scale the torso (cube) in terms of its dimensions so as to make it look good.
glScalef(0.2, 0.1 , 0.4)
# Our torso is nothing but a cube. So we draw the cube now.
glutSolidCube(1.2) glPopMatrix()
The Lighting used for drawing this part is:
torso_amb = 1.0, 0.0, 0.0, 1.0 torso_diff = 0.67, 0.45, 0.21, 1.0 torso_spec = 0.2, 0.4, 0.3, 1.0
   
torso_shin = 1.8
Using the key ‘d’ and ‘D’ one can rotate the torso clockwise and Anticlockwise repectively.
2. ARMS:
They are drawn with respect to the Torso, i.e. , Torso is their parent. They are drawn using simple cubes by scaling them and then translating them to match the desired location. They have been divided into two sub-modules -> Upper Arm and Lower Arm. Their corresponding dimensions are as follows:
UPPER_ARM_HEIGHT=0.2 UPPER_ARM_WIDTH=0.07
LOWER_ARM_HEIGHT=0.2 LOWER_ARM_WIDTH=0.05
They are drawn using the following Algorithm:
Both the arms are kept in different positions initially. Hence their
Rotational variable are defined differently.
We scaled the cubes used for drawing the arms to a length
corresponding to the Arm’s height and width defined above. Then we simply draw the cube.
   
  Using the key ‘s’ and ‘f’ one can rotate the Left/Right upperArm and key ‘a’ and ‘g’ one can rotate the Left/Right LowerArm.
3. LEGS:
Even the legs are divided into two sub-modules -> Lower leg and Upper leg so as to make the humanoid look more real.
They are drawn using the following algorithm:
They are drawn using simple cubes. So, initially both the legs are in
default position.
Then the cubes used are translated with respect to the Torso so as to
get to them to the desired position.
Then the cubes are scaled to fit the dimensions that are defined
above in the code.
Using the key ‘x’ and ‘c’ one can rotate the Left/Right upperLeg and key ‘z’ and ‘v’ can rotate the Left/Right LowerLeg.
   
4. FACE:
The face is also drawn using cube. On the face there are three spheres drawn to serve the purpose of two eyes and one nose. The face is drawn with respect to the Torso whereas the Eyes and the nose are drawn with respect to the Face.
Using the key ‘r’ and ‘R’ one can rotate the face clockwise and Anticlockwise repectively.
Hence, As a whole the Humanoid is build only using two primitive-> glutSolidCube and glutSolidSphere and it looks like:
