#clock module 
import turtle as t

# time data
hours = 4
minutes = 55
seconds = 5

c_radius = 300

#print the time
def printTime():
    print(f"{hours:02}:{minutes:02}:{seconds:02}" )  #template string

def drawClock():
    drawClockCircle()
    drowClockHours()
    drowClockMinutes()
    drawClockCircle()
    
# draw clock with turtle
def drawClockCircle():
    t.speed(0)
    t.penup()
    t.setposition(0, -c_radius)
    t.pendown()
    t.circle(100)

# hours indicator
def drowClockHours():
    t.penup()
    t.setposition(0,0)
    t.pensize(5)    
    t.pendown()    
    t.setheading(90 + hours * -30)    
    t.forward(c_radius * 0.7)  

# minutes indicator
def drowClockMinutes():
    t.penup()
    t.setposition(0,0)
    t.pensize(2)    
    t.pendown()    
    t.setheading(90 + minutes * -6)    
    t.forward(c_radius * 0.8)

# seconds indicator
def drowClockSeconds():
    t.penup()
    t.setposition(0,0)
    t.pensize(1)    
    t.pendown()    
    t.setheading(90 + seconds * -6)    
    t.forward(c_radius * 0.9)    