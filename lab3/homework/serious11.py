def is_inside(point, rectangle):

    if (rectangle[2] + rectangle[0]) >= point[0] >= rectangle[0] and (rectangle[3] + rectangle[1]) >= point[1] >= rectangle[1]:
        print("True")
    else:
        print("False")

is_inside([100, 120], [140, 60, 0, 0	])
is_inside([200, 120], [140, 60, 100, 200])

    



