import turtle 

t = turtle.Turtle()
turtle.bgcolor("black")

t.speed(100)

for i in range(240): 
  t.color('cyan') 
  t.circle(i)
  t.left(5)

turtle.done()
