from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]


draw_line( 250, 250, 300, 275, screen, color)
draw_line( 250, 250, 300, 325, screen, color)
draw_line( 250, 250, 300, 175, screen, color)
draw_line( 250, 250, 300, 225, screen, color)
draw_line( 250, 175, 250, 325, screen, color)
draw_line( 200, 250, 300, 250, screen, color)

display(screen)
save_extension(screen, 'img.png')
