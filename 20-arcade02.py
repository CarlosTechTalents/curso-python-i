# Import module
import arcade
 
#Specify Parameters
Width = 500
Height = 700
Title = "Welcome to Arcade"
Radius = 200
 
# Open the window
arcade.open_window(Width, Height, Title)
 
# Set the background color
arcade.set_background_color(arcade.color.BLACK)
 
# start drawing
arcade.start_render()
 
# Draw a BLUE circle
arcade.draw_circle_filled(
    Width/2 , Height/2 , Radius , arcade.color.BLUE
)
 
# Draw a Red circle
arcade.draw_circle_filled(
    Width/2 , Height , Radius , arcade.color.RED
)
 
# Finish drawing
arcade.finish_render()
# Display everything
arcade.run()