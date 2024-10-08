from turtle import *
import random

speed(0)

def spiral():
    for steps in range(100):
        for c in ('blue', 'red', 'green'):
            color(c)
            forward(steps)
            right(30)

    mainloop()
    
    
def tma_konec_tunelu():    
    for i in range(0, 362):
        angle = 1
        forward(1000)
        home()
        right(angle * i)
        
    delay(2000)



def kresli_kruhy_v_kruzich():
    pocet_kruhu=10
    zakladni_polomer=15
    krok=20
    
    penup()  
    goto(0, -zakladni_polomer)
    pendown()
    
    for i in range(pocet_kruhu):
        circle(zakladni_polomer + i * krok)
        penup()
        goto(0, -(zakladni_polomer + (i + 1) * krok))
        pendown()

    mainloop()


def chase():
    penup()
    goto(-400,0)
    pendown()
    right(89) 
    for i in range(1, 300):
        forward((5 * i)) 
        if i % 2 == 0:
            right(178) 
        else:
            left(178)
        
    mainloop()

 