# Install script for directory: /home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/eigen3/Eigen" TYPE FILE FILES
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/Cholesky"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/CholmodSupport"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/Core"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/Dense"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/Eigen"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/Eigenvalues"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/Geometry"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/Householder"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/IterativeLinearSolvers"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/Jacobi"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/LU"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/MetisSupport"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/OrderingMethods"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/PaStiXSupport"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/PardisoSupport"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/QR"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/QtAlignedMalloc"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/SPQRSupport"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/SVD"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/Sparse"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/SparseCholesky"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/SparseCore"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/SparseLU"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/SparseQR"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/StdDeque"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/StdList"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/StdVector"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/SuperLUSupport"
    "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/UmfPackSupport"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xDevelx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/eigen3/Eigen" TYPE DIRECTORY FILES "/home/parallels/Coding/CodingProjects/catkin_ws/src/eigen-eigen-5a0156e40feb/Eigen/src" FILES_MATCHING REGEX "/[^/]*\\.h$")
endif()

