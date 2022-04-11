'''
DIBUIXANT ELEMENTS
'''
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

#fons
arcade.draw_lrtb_rectangle_filled(0, 599, 100, 0, arcade.csscolor.GREEN)

#cos
arcade.draw_circle_filled(100, 100, 60, arcade.color.WHITE)
arcade.draw_circle_filled(100, 170, 50, arcade.color.WHITE)
arcade.draw_circle_filled(100, 240, 40, arcade.color.WHITE)

#ulls i nas
arcade.draw_circle_filled(80, 250, 5, arcade.color.BLACK)
arcade.draw_circle_filled(120, 250, 5, arcade.color.BLACK)
arcade.draw_circle_filled(100, 230, 5, arcade.color.ORANGE)

#botons
arcade.draw_circle_filled(100, 100, 5, arcade.color.BROWN)
arcade.draw_circle_filled(100, 140, 5, arcade.color.BROWN)
arcade.draw_circle_filled(100, 180, 5, arcade.color.BROWN)

#bufanda
arcade.draw_lrtb_rectangle_filled(60, 140, 215, 200, arcade.csscolor.PINK)
arcade.draw_lrtb_rectangle_filled(125, 140, 215, 150, arcade.csscolor.PINK)

#capell
arcade.draw_lrtb_rectangle_filled(70, 130, 300, 260, arcade.csscolor.BLACK)
arcade.draw_lrtb_rectangle_filled(50, 150, 270, 260, arcade.csscolor.BLACK)

#Rectangles: 
arcade.draw_lrtb_rectangle_filled(265, 285, 160,100, arcade.csscolor.BROWN)

#Triangles: 
arcade.draw_triangle_filled(280, 450, 170, 160, 380, 160, arcade.csscolor.GREEN)
arcade.draw_triangle_filled(280, 450, 180, 220, 370, 220, arcade.csscolor.GREEN)
arcade.draw_triangle_filled(280, 450, 190, 280, 360, 280, arcade.csscolor.GREEN)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()