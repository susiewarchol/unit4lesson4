from turtle import *
triangle = Turtle()
circle = Turtle()

triangle.color('green')
triangle.pensize(5)
triangle.speed(3)
triangle.shape('turtle')

circle.color('yellow')
circle.pensize(5)
circle.speed(3)
circle.shape('turtle')


triangle.forward(100)
triangle.left(120)
triangle.forward(100)
triangle.left(120)
triangle.forward(100)
triangle.left(120)

circle.circle(50)



mainloop()