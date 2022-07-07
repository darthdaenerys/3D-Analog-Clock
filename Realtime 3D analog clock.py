# import libraries and packages
from vpython import *
import time
import winsound
import numpy as np

# vpython canvas
canvas(width=1320,height=680)

# beep parameters
frequency=5000
duration=500

# trignometric parameters
theta=np.pi

# otherparameters
boxsmallL=.1
boxlargeL=.2
boxsmallwidth=0.02
boxlargewidth=0.04
boxcolor=color.black
minutehandlength=1.5
secondhandlength=1.7
hourhandlength=1

# back plate
innerplate=cylinder(
    axis=vector(0,0,1),
    length=.2,
    radius=2.2,
    texture=textures.metal,
    color=vector(207/255, 252/255, 236/255)
)
outerplate=cylinder(
    axis=vector(0,0,1),
    length=.2,
    radius=2.4,
    pos=vector(0,0,-.02),
    color=vector(204/255, 41/255, 41/255),
    texture=textures.wood
)
cylinder(radius=.07,color=color.black,axis=vector(0,0,1),length=.34)
for i in range(0,359,6):
    if i%30==0:
        box(
            axis=vector(boxlargeL*np.cos(theta*i/180),boxlargeL*np.sin(theta*i/180),0),
            size=vector(boxlargeL,boxlargewidth,.1),
            pos=vector(2*np.cos(theta*i/180),2*np.sin(theta*i/180),0.2),
            color=boxcolor
        )
    else:
        box(
            axis=vector(boxsmallL*np.cos(theta*i/180),boxsmallL*np.sin(theta*i/180),0),
            size=vector(boxsmallL,boxsmallwidth,.1),
            pos=vector(2*np.cos(theta*i/180),2*np.sin(theta*i/180),0.2),
            color=boxcolor
        )

# adjusting the time from time module
    second=time.localtime()[5]
    minute=time.localtime()[4]
    hour=time.localtime()[3]

# converting time to angles
    secondangle=-6*second+90
    minuteangle=-6*minute+90
    hourangle=-6*hour+90

# hour,minute and second hand
hourhand=arrow(
    length=hourhandlength,
    shaftwidth=.07,
    axis=vector(hourhandlength*hourangle,hourhandlength*hourangle,0),
    pos=vector(0,0,0.28),
    color=vector(20/255,20/255,20/255)
)
minutehand=arrow(
    length=minutehandlength,
    shaftwidth=.04,
    axis=vector(minutehandlength*minuteangle,minutehandlength*minuteangle,0),
    pos=vector(0,0,0.25),
    color=vector(20/255,20/255,20/255)
)
secondhand=arrow(
    length=secondhandlength,
    shaftwidth=.025,
    axis=vector(secondhandlength*secondangle,secondhandlength*secondangle,0),
    pos=vector(0,0,0.22),
    color=vector(20/255,20/255,20/255)
)
attach_light(hourhand)
attach_light(minutehand)
attach_light(secondhand)

# Putting a label
mylabel=text(
    text='Current Time',
        align='center',
        color=color.cyan,
        height=.5,
        pos=vector(0,2.6,0),
        depth=0
        )
attach_light(mylabel)

# Adding Numbers
j=3
for i in range(0,331,30):
    text(
        text=str(j),
        align='center',
        color=color.black,
        height=0.4,
        pos=vector(1.05*minutehandlength*np.cos(theta*(i/180)),1.05*minutehandlength*np.sin(theta*(i/180))-0.2,.17),
        depth=0.05
    )
    j-=1
    if j==0:
        j=12

while True:
    rate(30)

    # adjusting the time from time module
    second=time.localtime()[5]
    minute=time.localtime()[4]
    hour=time.localtime()[3]
    if hour>=13:
        hour-=12
    orgminuteangle=-6*minute+90
    orghourangle=-30*(hour-3)

    # converting second to angles(in degrees)
    secondangle=-6*second+90
    minuteangle=(secondangle-90)/60+orgminuteangle
    hourangle=(minuteangle+90)/14+orghourangle-15

    # updating the axis of second, minute and hour hands
    secondhand.axis=vector(secondhandlength*np.cos(theta*secondangle/180),secondhandlength*np.sin(theta*secondangle/180),0)
    minutehand.axis=vector(minutehandlength*np.cos(theta*(minuteangle/180)),minutehandlength*np.sin(theta*(minuteangle/180)),0)
    hourhand.axis=vector(hourhandlength*np.cos(theta*(hourangle/180)),hourhandlength*np.sin(theta*(hourangle/180)),0)

    # beep sound on every hour
    if hourangle%30==0 and minuteangle==90 and secondangle==90:
        winsound.Beep(frequency, duration)