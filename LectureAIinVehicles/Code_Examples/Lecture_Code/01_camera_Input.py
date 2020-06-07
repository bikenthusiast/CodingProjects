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
import pyzed.types as tp
import pyzed.core as core
import pyzed.defines as sl


def main():
    print("\n\n\n############################################################")
    print("Welcome to the Artificial Intelligence Lecture 2: Perception")
    print("############################################################ \n")

    print("\n **** Codeexample 1: Acessing the Camera  *** \n")

    print("\n1. Opening the camera by creating and Camera Object and initializing the camera:")
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

def print_camera_information(cam):
    print("\n2. Show Camera Information:")

    print("Camera Type: ZED Stereo Camera")
    print("Serial number: {0}.".format(cam.get_camera_information().serial_number))
    print("Firmware: {0}. \n".format(cam.get_camera_information().firmware_version))

    print("\n3. Show Camera Specifications:")
    print("Resolution: {0}, {1}.".format(round(cam.get_resolution().width, 2), cam.get_resolution().height))
    print("Camera FPS: {0}.\n\n\n".format(cam.get_camera_fps()))

if __name__ == "__main__":
    main()
