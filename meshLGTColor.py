import maya.cmds

lights = cmds.ls( selection=True )
for x in lights:
    lightName = str(x)
    coreName = lightName.split(':')
    theName = coreName[0]+":materials:colorConstant1.inColor"
    print theName
    cmds.setAttr (theName, 1.000 , 0.670, 0.481)
    