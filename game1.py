import pgzrun

music.play('song.mp3')


b = Rect((50,50),(100,50))
vx = 3
vy = 5

def draw():
    screen.fill('black')
    screen.draw.filled_rect(b, 'blue')

def update ():
    global vx, vy
    b.x += vx
    b.y += vy
    if b.right>800 or b.left <0:
        vx = -vx
    if b.bottom >600 or b.top <0:
        vy = -vy


#outside of all function
pgzrun.go()