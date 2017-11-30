"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Brian Whitacre.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    #two_circles()
    #circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    windows = rg.RoseWindow()

    circle1radi = 100
    circle2radi = 50

    circle1pos = rg.Point(200,20)
    circle2pos = rg.Point(100, 100)

    circle1 = rg.Circle(circle1pos,circle1radi)
    circle2 = rg.Circle(circle2pos, circle2radi)

    circle1.fill_color = 'Green'
    circle2.fill_color = 'Blue'

    circle1.attach_to(windows)
    circle2.attach_to(windows)

    windows.render()

    windows.close_on_mouse_click()
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    window = rg.RoseWindow()
    circle1x = 90
    circle1y = 100
    circle1pos = rg.Point(circle1x,circle1y)
    circle1color = 'blue'
    circle1radi = 50
    circle1thick = 1
    rectangle1x = 150
    rectangle1y = 10
    rectangle1point1 = rg.Point(rectangle1y,rectangle1x)
    rectangle1point2 = rg.Point(200,200)
    circle1 = rg.Circle(circle1pos,circle1radi)
    rectangle1 = rg.Rectangle(rectangle1point1,rectangle1point2)

    circle1.fill_color = circle1color

    circle1.attach_to(window)
    rectangle1.attach_to(window)

    window.render()
    print(circle1.outline_thickness)
    print(circle1.fill_color)
    print(circle1.center)
    print(circle1x)
    print(circle1y)

    print(rectangle1.outline_thickness)
    print(rectangle1.fill_color)
    print(rectangle1._upper_left_corner)
    print(rectangle1x)
    print(rectangle1y)

    window.close_on_mouse_click()
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """

    window= rg.RoseWindow()

    line1x = (30,50)
    line1y = (50,70)
    line2x = (100,60)
    line2y = (1000,80)

    line1 = rg.Line(line1x,line1y)
    line2 = rg.Line(line2x,line2y)

    line1.attach_to(window)
    line2.attach_to(window)
    window.render()
    window.close_on_mouse_click()
    # ------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
