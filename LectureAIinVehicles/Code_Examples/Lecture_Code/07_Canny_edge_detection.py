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
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
########################################################################

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
    print("In todays Lecture we will see how to process Images\n")



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

    print("\n2. Now we will grey and blur the image and do a canny edge detection")
    key = ''
    while key != 113:  # for 'q' key
        err = cam.grab(runtime)
        if err == tp.PyERROR_CODE.PySUCCESS:
            cam.retrieve_image(image, sl.PyVIEW.PyVIEW_LEFT)

            #Process the Image
            gray_image = cv2.cvtColor(image.get_data(), cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray_image, (7, 7), 1.5)
            edges = cv2.Canny(blur, 0, 23)

            #rescale the images
            gray_image2 = cv2.resize(gray_image, (0, 0), None, .70, .70)
            blur2 = cv2.resize(blur, (0, 0), None, .70, .70)
            edges2 = cv2.resize(edges, (0, 0), None, .70, .70)

            # Put all images in one numpy stack
            numpy_horizontal = np.hstack((gray_image2, blur2, edges2))

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
