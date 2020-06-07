########################################################################
#
# Copyright (c) 2017, STEREOLABS.
#
# All rights reserved.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE########################################################################

"""
    Live camera sample showing the camera information and video in real time and allows to control the different
    settings.
"""

import cv2
import pyzed.camera as zcam
import pyzed.types as tp
import pyzed.core as core
import pyzed.defines as sl
import numpy as np
from timeit import default_timer as timer
from matplotlib import pyplot as plt

camera_settings = sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_BRIGHTNESS
str_camera_settings = "BRIGHTNESS"
step_camera_settings = 1


" This is the  main code which is running the camera"

def main():
    print("\n############################################################")
    print("Welcome to the Artificial Intelligence Lecture 2: Perception")
    print("############################################################ \n")

    print("\n **** Codeexample 4: Live Color Spaces *** \n")

    print("\n1. We will acces the camera and  see the camera Paramters:")

    # Create a PyZEDCamera object
    cam = zcam.PyZEDCamera()

    # Create a PyInitParameters object and set configuration parameters
    init = zcam.PyInitParameters()

    # Open the camera
    if not cam.is_opened():
        print("Opening Camera...")
    status = cam.open(init)
    if status != tp.PyERROR_CODE.PySUCCESS:
        print(repr(status))
        exit()

    runtime = zcam.PyRuntimeParameters()

    #Define the image as ZED Python Wrapper format
    image= core.PyMat()

    # Extract the current Camera paramters and camera Information
    print_camera_information(cam)

    print("\n2. We will start with displaying a live stream from the camera")
    key = ''

    while key != 113:  # for 'q' key
        err = cam.grab(runtime)
        if err == tp.PyERROR_CODE.PySUCCESS:
            cam.retrieve_image(image, sl.PyVIEW.PyVIEW_LEFT)


            #Process the Image
            gray_image = cv2.cvtColor(image.get_data(), cv2.COLOR_BGR2GRAY)
            gray_image2 = cv2.resize(gray_image, (0, 0), None, .70, .70)
            cv2.imshow("ZED Live Stream", image.get_data())

            key = cv2.waitKey(5)
        else:
            key = cv2.waitKey(5)

    print("\n3. Now we will turn the image into a greyscale image")
    key = ''

    while key != 113:  # for 'q' key
        err = cam.grab(runtime)
        if err == tp.PyERROR_CODE.PySUCCESS:
            cam.retrieve_image(image, sl.PyVIEW.PyVIEW_LEFT)

            # Process the Image
            gray_image = cv2.cvtColor(image.get_data(), cv2.COLOR_BGR2GRAY)
            cv2.imshow("ZED Live Stream", gray_image)

            key = cv2.waitKey(5)
        else:
            key = cv2.waitKey(5)

    print("\n4. We are in the RGB Color space so we can display just the RED, Blue and Green values")
    key = ''

    while key != 113:  # for 'q' key
        err = cam.grab(runtime)
        if err == tp.PyERROR_CODE.PySUCCESS:
            cam.retrieve_image(image, sl.PyVIEW.PyVIEW_LEFT)

            # Extract the different colors from one image
            image2 = image.get_data()

            r = image2.copy()
            r[:, :, 0] = 0  # set blue and green channels to 0
            r[:, :, 1] = 0  # set blue and green channels to 0
            Red = r

            g = image2.copy()
            g[:, :, 0] = 0  # set blue and red channels to 0
            g[:, :, 2] = 0  # set blue and red channels to 0
            Green = g

            b = image2.copy()
            b[:, :, 1] = 0  # set green and red channels to 0
            b[:, :, 2] = 0  # set green and red channels to 0
            Blue = b

            # rescale the images
            Red2= cv2.resize(Red, (0, 0), None, .60, .60)
            Green2 = cv2.resize(Green, (0, 0), None, .60, .60)
            Blue2 = cv2.resize(Blue, (0, 0), None, .60, .60)

            # Put all images in one numpy stack
            numpy_horizontal = np.hstack((Red2, Green2, Blue2))
            cv2.imshow("ZED Live Stream", numpy_horizontal)

            key = cv2.waitKey(5)
        else:
            key = cv2.waitKey(5)

    print("\n4. We are now Changing the ColorSpace from RGB to HSV")
    key = ''
    while key != 113:  # for 'q' key
        err = cam.grab(runtime)
        if err == tp.PyERROR_CODE.PySUCCESS:
            cam.retrieve_image(image, sl.PyVIEW.PyVIEW_LEFT)

            # Change the color space in the image
            image2 = image.get_data()
            hsv_image = cv2.cvtColor(image2, cv2.COLOR_RGB2HSV)
            cv2.imshow("ZED Live Stream", hsv_image)


            key = cv2.waitKey(5)
        else:
            key = cv2.waitKey(5)

    print("\n5. Now we are splitting the HSV image into three images presenting H, S and V values")
    key = ''
    while key != 113:  # for 'q' key
        err = cam.grab(runtime)
        if err == tp.PyERROR_CODE.PySUCCESS:
            cam.retrieve_image(image, sl.PyVIEW.PyVIEW_LEFT)

            # Change the color space in the image
            image2 = image.get_data()
            hsv_image = cv2.cvtColor(image2, cv2.COLOR_RGB2HSV)

            h = hsv_image.copy()
            Hue = h[:, :, 0]

            s = hsv_image.copy()
            Saturation = s[:, :, 1]

            v = hsv_image.copy()
            Value= v[:, :, 2]

            # rescale the images
            Hue2 = cv2.resize(Hue, (0, 0), None, .60, .60)
            Saturation2 = cv2.resize(Saturation, (0, 0), None, .60, .60)
            Value2 = cv2.resize(Value, (0, 0), None, .60, .60)

            # Put all images in one numpy stack
            numpy_horizontal = np.hstack((Hue2, Saturation2, Value2))
            cv2.imshow("ZED Live Stream", numpy_horizontal)

            key = cv2.waitKey(5)
        else:
            key = cv2.waitKey(5)

    cv2.destroyAllWindows()

    cam.close()
    print("\nFINISH")


def print_camera_information(cam):
    print("Camera Type: ZED Stereo Camera")
    print("Serial number: {0}.\n".format(cam.get_camera_information().serial_number))
    print("Firmware: {0}.".format(cam.get_camera_information().firmware_version))
    print("Resolution: {0}, {1}.".format(round(cam.get_resolution().width, 2), cam.get_resolution().height))
    print("Camera FPS: {0}.".format(cam.get_camera_fps()))


if __name__ == "__main__":
    main()
