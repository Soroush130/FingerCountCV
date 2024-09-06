def calculate_bisector(point1, point2):
    # Unpack the coordinates of the two points
    x1, y1 = point1.x, point1.y
    x2, y2 = point2.x, point2.y

    # Calculate the midpoint (bisector)
    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2

    return (midpoint_x, midpoint_y)
