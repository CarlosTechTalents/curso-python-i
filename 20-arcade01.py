
# Import module
import arcade
 
# Specify Parameters
Width = 500
Height = 700
Title = "Welcome to Arcade"
Radius = 100
 
# Open the window
arcade.open_window(Width, Height, Title)
 
# Set the background color
arcade.set_background_color(arcade.color.BLUE)
 
# start drawing
arcade.start_render()
 
# Draw a Pink circle
arcade.draw_circle_filled(
    Width/2 , Height/2 , Radius , arcade.color.PINK
)
# Finish drawing
arcade.finish_render()
 
# Display everything
arcade.run()