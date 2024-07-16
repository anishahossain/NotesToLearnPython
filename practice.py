import turtle as t
tur = t.Turtle()
tur.shape('arrow')
x, y = 0, 0
tur.setpos(x, y)
for c in range(4):
    tur.pendown()
    tur.circle(60)
    x += 30
    tur.penup()
    tur.setpos(x, y)
