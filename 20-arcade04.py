"""
Example "Arcade" library code.

Showing how to do nested loops.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.nested_loops_box
"""

# Library imports
import arcade

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 110
BOTTOM_MARGIN = 110

# Open the window and set the background
arcade.open_window(400, 400, "Complex Loops - Box")

arcade.set_background_color(arcade.color.WHITE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

y = 300

# Loop1 for each row
x = 0 * COLUMN_SPACING + LEFT_MARGIN
arcade.draw_circle_filled(x, y, 7, arcade.color.AO)

# Loop1 for each row
x = 1 * COLUMN_SPACING + LEFT_MARGIN
arcade.draw_circle_filled(x, y, 7, arcade.color.AO)

# Loop1 for each row
x = 2 * COLUMN_SPACING + LEFT_MARGIN
arcade.draw_circle_filled(x, y, 7, arcade.color.AO)

# Loop1 for each row
x = 3 * COLUMN_SPACING + LEFT_MARGIN
arcade.draw_circle_filled(x, y, 7, arcade.color.AO)


# Finish the render.
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()