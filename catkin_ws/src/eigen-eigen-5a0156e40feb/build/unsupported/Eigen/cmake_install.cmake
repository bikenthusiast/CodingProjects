# Install script for directory: /home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xDevelx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/eigen3/unsupported/Eigen" TYPE FILE FILES
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/AdolcForward"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/AlignedVector3"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/ArpackSupport"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/AutoDiff"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/BVH"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/EulerAngles"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/FFT"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/IterativeSolvers"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/KroneckerProduct"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/LevenbergMarquardt"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/MatrixFunctions"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/MoreVectorization"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/MPRealSupport"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/NonLinearOptimization"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/NumericalDiff"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/OpenGLSupport"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/Polynomials"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/Skyline"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/SparseExtra"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/SpecialFunctions"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/Splines"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xDevelx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/eigen3/unsupported/Eigen" TYPE DIRECTORY FILES "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/unsupported/Eigen/src" FILES_MATCHING REGEX "/[^/]*\\.h$")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/build/unsupported/Eigen/CXX11/cmake_install.cmake")

endif()

