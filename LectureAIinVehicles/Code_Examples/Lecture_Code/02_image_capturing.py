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

import pyzed.camera as zcam
import pyzed.defines as sl
import pyzed.types as tp
import pyzed.core as core
import cv2


def main():
    print("\n\n\n############################################################")
    print("Welcome to the Artificial Intelligence Lecture 2: Perception")
    print("############################################################ \n")

    print("\n **** Codeexample 2: Image Capturing  *** \n")


    print("\n1. Opening the camera by creating and Camera Object and initializing the camera:")
    # Create a PyZEDCamera object
    zed = zcam.PyZEDCamera()

    # Create a PyInitParameters object and set configuration parameters
    init_params = zcam.PyInitParameters()
    init_params.camera_resolution = sl.PyRESOLUTION.PyRESOLUTION_HD1080  # Use HD1080 video mode: VGA,HD720,HD1080,HD2k
    init_params.camera_fps = 30  # Set fps at 30: 15,30, 60,100

    # Open the camera
    err = zed.open(init_params)
    if err != tp.PyERROR_CODE.PySUCCESS:
        exit(1)

    # Capture 5 frames and stop
    i = 0
    image = core.PyMat()
    runtime_parameters = zcam.PyRuntimeParameters()
    while i < 1:
        # Grab an image, a PyRuntimeParameters object must be given to grab()
        if zed.grab(runtime_parameters) == tp.PyERROR_CODE.PySUCCESS:
            # A new image is available if grab() returns PySUCCESS
            zed.retrieve_image(image, sl.PyVIEW.PyVIEW_LEFT)
            timestamp = zed.get_timestamp(sl.PyTIME_REFERENCE.PyTIME_REFERENCE_CURRENT)  # Get the timestamp at the time the image was captured
            print("Image resolution: {0} x {1} || Image timestamp: {2}\n".format(image.get_width(), image.get_height(),
                  timestamp))
            cv2.imwrite('Pictures/Image_1.png',image.get_data())

            i = i + 1


    # Close the camera
    zed.close()

if __name__ == "__main__":
    main()
