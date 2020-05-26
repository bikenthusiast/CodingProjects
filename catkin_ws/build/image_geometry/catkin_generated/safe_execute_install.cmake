execute_process(COMMAND "/home/parallels/projects/catkin_ws/build/image_geometry/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/parallels/projects/catkin_ws/build/image_geometry/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
