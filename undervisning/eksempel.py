import turtle

# Start skilpadden
t = turtle.Turtle()

# Tegn en linje
t.forward(100)

# Løft pennen (ingen tegning nå)
t.penup()
t.forward(50)

# Sett pennen ned igjen
t.pendown()
t.forward(100)

# Avslutt
turtle.done()