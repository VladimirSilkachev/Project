import turtle as t
import math
n = int(input())
def SpyralStart():
    b = 10
    t.right(90)
    t.circle(b,90)
pass

def spyral():
    t.up()
    t.setposition(0,0)
    t.down()
    a = 0
    b = 10
    t.right(90)
    t.right(90)
    for i in range(n):
        t.circle((b),90)
        c = b
        b = b+c
        a = c
pass
def SquareStart():
    b = 10
    t.backward(b)
    t.left(90)
    t.backward(b)
    t.left(90)
    t.backward(b)
    t.left(90)
    t.backward(b)
pass
def SquareSpyral():
    a = 0
    b = 10
    for i in range(1, n+1):
        t.backward(a)
        t.right(90)
        t.forward(b)
        t.left(90)
        t.forward(b)
        t.left(90)
        t.forward(b)
        c = b
        b = a + b
        a = c
pass
SquareStart()
SquareSpyral()
#SpyralStart()
spyral()
t.done()
