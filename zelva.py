from turtle import *
import random



def spiral():
    speed(0)
    for steps in range(100):
        for c in ('blue', 'red', 'green'):
            color(c)
            forward(steps)
            right(30)

def tma_konec_tunelu():    
    speed(0)
    for i in range(0, 362):
        angle = 1
        forward(1000)
        home()
        right(angle * i)
        
    delay(2000)

def kresli_kruhy_v_kruzich():
    speed(0)
    pocet_kruhu = 10
    zakladni_polomer = 15
    krok = 20
    
    penup()  
    goto(0, -zakladni_polomer)
    pendown()
    
    for i in range(pocet_kruhu):
        circle(zakladni_polomer + i * krok)
        penup()
        goto(0, -(zakladni_polomer + (i + 1) * krok))
        pendown()

def chase():
    speed(0)
    penup()
    goto(-400, 0)
    pendown()
    right(89) 
    for i in range(1, 200):
        forward((5 * i)) 
        if i % 2 == 0:
            right(178) 
        else:
            left(178)

def cisteni():
    Screen().clear()
