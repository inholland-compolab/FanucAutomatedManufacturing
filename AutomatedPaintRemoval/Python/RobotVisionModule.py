"""
This module handle the vision algorithm.
It consists of 2 parts, the paint detector and the path creator.

It also contains a few utility files like the HSV value picker
that thresholds different parts of an image based on HSV sliders.
This way u can more accurately pick colors.
"""

import cv2
import numpy as np
from Image import Image, EImageType, ImageConverter

from PathPoint import PathPoint, ESandingDirection

DEBUG = True

max_value = 255
max_value_H = 360 // 2
low_H = 0
low_S = 0
low_V = 0

high_H = 180
high_S = 32
high_V = 255

radius = 24.5  # mm
ignorable_radius = 12  # mm

# These are the object values as how they appear in the image
objectLength = 250  # mm
objectWidth = 140  # mm

window_detection_name = "Processed image"
window_radius_name = "Path image"


def on_low_hue_thresh_trackbar(val):
    global low_H
    global high_H
    low_H = val
    low_H = min(high_H - 1, low_H)
    cv2.setTrackbarPos("Low H", window_detection_name, low_H)


def on_high_hue_thresh_trackbar(val):
    global low_H
    global high_H
    high_H = val
    high_H = max(high_H, low_H + 1)
    cv2.setTrackbarPos("High H", window_detection_name, high_H)


def on_low_saturation_thresh_trackbar(val):
    global low_S
    global high_S
    low_S = val
    low_S = min(high_S - 1, low_S)
    cv2.setTrackbarPos("Low S", window_detection_name, low_S)


def on_high_saturation_thresh_trackbar(val):
    global low_S
    global high_S
    high_S = val
    high_S = max(high_S, low_S + 1)
    cv2.setTrackbarPos("High S", window_detection_name, high_S)


def on_low_value_thresh_trackbar(val):
    global low_V
    global high_V
    low_V = val
    low_V = min(high_V - 1, low_V)
    cv2.setTrackbarPos("Low V", window_detection_name, low_V)


def on_high_value_thresh_trackbar(val):
    global low_V
    global high_V
    high_V = val
    high_V = max(high_V, low_V + 1)
    cv2.setTrackbarPos("High V", window_detection_name, high_V)


def on_radius_trackbar(val):
    global radius
    radius = val
    cv2.setTrackbarPos("Radius in mm", window_radius_name, radius)


def run_procedure(captured_image):
    """
    This function contains the algorithms to find the paint on the object

    :param captured_image: numpy image
    :return: points, image
    """
    if DEBUG:
        # load debug image
        img = cv2.imread('images\\image_smudge1.jpg')
    else:
        # change te image format to BGR
        tempimg = np.copy(captured_image)
        img = cv2.cvtColor(tempimg, cv2.COLOR_RGB2BGR)

    if img is None:
        print("Error opening image!")

    # show_debug_image('image', img, 640, 480)

    # blur the image, removing some of the sharper edges.
    blur = cv2.blur(img, (5, 5))
    # show_debug_image('blurred image', blur, 640, 480)
    # Convert image format to HSV
    hsv_image = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # HSVValuePicker(hsv_image)

    # threshold the image based on the hsv color
    threshold_image = cv2.inRange(hsv_image, (low_H, low_S, low_V), (high_H, high_S, high_V))
    # show_debug_image('threshold image', threshold_image, 640, 480)

    # erode the image, removing some small speckles in the image.
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(threshold_image, kernel, iterations=2)

    # show_debug_image('Erode image', erosion)

    # Label the different parts of the image and return the stats
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(erosion, 8, cv2.CV_32S)

    sizes = stats[1:, -1]
    num_labels = num_labels - 1

    new_image = erosion

    # check if the blob has a smaller area then specified
    for i in range(0, num_labels):
        if sizes[i] < 400:
            # remove it
            new_image[labels == i + 1] = 0

    # show_debug_image("new image", new_image)

    # call the function to create a simple path with the labeled
    # image and original image
    points = create_simple_path(img, new_image)

    # Change image format back to original and convert to Image
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    image = Image(img.data, img.shape[1], img.shape[0], EImageType.IMAGE_TYPE_RGB888)

    # return pointlist and original image
    return points, image
    # showDebugImage('color image', img)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def show_debug_image(window_name, image, window_width=640, window_height=480):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, window_width, window_height)
    cv2.imshow(window_name, image)


def hsv_value_picker(hsv_image):
    cv2.namedWindow(window_detection_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_detection_name, 640, 480)

    cv2.createTrackbar("Low H", window_detection_name, low_H, max_value_H, on_low_hue_thresh_trackbar)
    cv2.createTrackbar("High H", window_detection_name, high_H, max_value_H, on_high_hue_thresh_trackbar)
    cv2.createTrackbar("Low S", window_detection_name, low_S, max_value, on_low_saturation_thresh_trackbar)
    cv2.createTrackbar("High S", window_detection_name, high_S, max_value, on_high_saturation_thresh_trackbar)
    cv2.createTrackbar("Low V", window_detection_name, low_V, max_value, on_low_value_thresh_trackbar)
    cv2.createTrackbar("High V", window_detection_name, high_V, max_value, on_high_value_thresh_trackbar)

    while True:
        threshold_image = cv2.inRange(hsv_image, (low_H, low_S, low_V), (high_H, high_S, high_V))
        cv2.imshow(window_detection_name, threshold_image)

        key = cv2.waitKey(30)
        if key == ord('q') or key == 27:
            cv2.destroyAllWindows()
            break


def create_simple_path(img, labels):
    """
    This function creates the path from the vision algorithm.
    For a more detailed explanation of how this function works
    check the .md file of the same name as the module.

    :param img: original image
    :param labels: labeled image
    :return PathPoint: points
    """
    points = []

    # To calculate realworld distance based on pixel distance we need to
    # divide the largest fov the width by the same real value lengte
    height, width, channels = img.shape
    # print(height / objectWidth)
    # print(width / objectLength)

    pixels_per_mm = width / objectLength
    radius_in_pixels = int(radius * pixels_per_mm)
    ignorable_radius_in_pixels = int(ignorable_radius * pixels_per_mm)

    check_radius = radius_in_pixels - ignorable_radius_in_pixels

    # Make sure that the check radius in uneven
    if check_radius % 2 == 0:
        check_radius += 1

    print(check_radius)

    # create kernel for checkable radius
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (check_radius * 2, check_radius * 2))

    starting_point_x = radius_in_pixels
    starting_point_y = radius_in_pixels

    on_allowed_sanding_path = True

    # Create ROI of sanding device
    roi = labels[starting_point_y - check_radius: starting_point_y + check_radius,
          starting_point_x - check_radius: starting_point_x + check_radius]

    if (roi * kernel).sum() == 0:
        on_allowed_sanding_path = True
    elif (roi * kernel).sum() != 0:
        on_allowed_sanding_path = False

    end_point_x = starting_point_x
    end_point_y = height - radius_in_pixels

    # append the first point to the list
    points.append(PathPoint(starting_point_x / pixels_per_mm, starting_point_y / pixels_per_mm,
                            allowed_to_sand=on_allowed_sanding_path))

    started_top = True
    step_size = 1

    while True:
        """This for loop handles all movements from top to bottom and vice
        versa"""
        for y in np.arange(starting_point_y, end_point_y, step_size):
            # adjust the ROI on the labeled image.
            roi = labels[y - check_radius: y + check_radius, starting_point_x - check_radius: starting_point_x + check_radius]
            # Check whether the kernel is on top of material
            if (roi * kernel).sum() == 0:
                # if it isn't, check whether the previous iteration was on
                # an allowed sanding path
                if not on_allowed_sanding_path:
                    # if it wasn't, Create a new point and set the on_allowed_sanding_path
                    # to true
                    points.append(
                        PathPoint(starting_point_x / pixels_per_mm, (y + step_size) / pixels_per_mm,
                                  allowed_to_sand=False))

                    img[y, starting_point_x - 2:starting_point_x + 2] = [255, 0, 0]

                    on_allowed_sanding_path = True
                else:
                    # If it was, continue
                    img[y, starting_point_x - 2:starting_point_x + 2] = [255, 0, 0]
            elif (roi * kernel).sum() != 0:
                # if it is, check whether the previous iteration was not
                # on an allowed sanding path
                if on_allowed_sanding_path:
                    # If it was, end path here by adding the point to the
                    # list and setting on_allowed_sanding_path to true.
                    points.append(
                        PathPoint(starting_point_x / pixels_per_mm, (y + step_size) / pixels_per_mm,
                                  allowed_to_sand=True))

                    img[y, starting_point_x - 2:starting_point_x + 2] = [0, 0, 255]

                    on_allowed_sanding_path = False
                else:
                    # If it wasn't, continue
                    img[y, starting_point_x - 2:starting_point_x + 2] = [0, 0, 255]

        # this is the end point for the top to bottom movement or vice versa
        points.append(
            PathPoint(end_point_x / pixels_per_mm, end_point_y / pixels_per_mm, allowed_to_sand=on_allowed_sanding_path,
                      sanding_direction=ESandingDirection.Down if step_size == 1 else ESandingDirection.Up))

        # this statement checks whether or not we can go sideways
        if end_point_x + (3 * radius_in_pixels) <= width:
            # starting point are the old end points
            starting_point_x = end_point_x
            starting_point_y = end_point_y

            end_point_x = end_point_x + (2 * radius_in_pixels)

            """This for loop handles all movement from left to right"""
            for x in np.arange(starting_point_x, end_point_x):
                roi = labels[starting_point_y - check_radius: starting_point_y + check_radius,
                      x - check_radius: x + check_radius]
                # This part is identical to the previous one but then sideways
                if (roi * kernel).sum() == 0:
                    if not on_allowed_sanding_path:
                        points.append(
                            PathPoint((x - 1) / pixels_per_mm, starting_point_y / pixels_per_mm, allowed_to_sand=False,
                                      sanding_direction=ESandingDirection.Right))

                        img[starting_point_y - 2:starting_point_y + 2, x] = [255, 0, 0]

                        on_allowed_sanding_path = True
                    else:
                        img[starting_point_y - 2:starting_point_y + 2, x] = [255, 0, 0]
                elif (roi * kernel).sum() != 0:
                    if on_allowed_sanding_path:
                        points.append(
                            PathPoint((x - 1) / pixels_per_mm, starting_point_y / pixels_per_mm, allowed_to_sand=True,
                                      sanding_direction=ESandingDirection.Right))

                        img[starting_point_y - 2:starting_point_y + 2, x] = [0, 0, 255]

                        on_allowed_sanding_path = False
                    else:
                        img[starting_point_y - 2:starting_point_y + 2, x] = [0, 0, 255]

            # this is the end point for left to right movement
            points.append(
                PathPoint(end_point_x / pixels_per_mm, end_point_y / pixels_per_mm,
                          allowed_to_sand=on_allowed_sanding_path,
                          sanding_direction=ESandingDirection.Right))

            # start point is old end point
            starting_point_x = end_point_x
            starting_point_y = end_point_y

            # Determine whether the for loop needs to be reversed, because
            # of the path direction.
            if started_top:
                end_point_y = radius_in_pixels
                step_size = -1
                started_top = False
            else:
                end_point_y = height - radius_in_pixels
                step_size = 1
                started_top = True

        else:
            break

    # showDebugImage('gray_image', gray_image)
    # showDebugImage('color_image', img)

    return points
