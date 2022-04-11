import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def arbre (px,py):
    arcade.draw_lrtb_rectangle_filled(px, 20+px, 140+py, py, arcade.csscolor.BROWN)
    arcade.draw_circle_filled(10+px, 160+py, 60, arcade.csscolor.DARK_GREEN)

def dibuixaArbres (nombre, py):
    max = SCREEN_WIDTH
    espai = max / nombre
    print(espai)
    x = 0 - 100
    for i in range(nombre):
        x += espai
        print("x",x)
        arbre(x,py)

def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x, 190 + y, 5, arcade.color.ORANGE)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    draw_grass()
    draw_snow_person(150, 140)
    draw_snow_person(450, 180)
    dibuixaArbres(6, 200)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()