#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/parallels/Coding/CodingProjects/slam_catkin_ws/src/vision_opencv/cv_bridge"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/parallels/Coding/CodingProjects/slam_catkin_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/parallels/Coding/CodingProjects/slam_catkin_ws/install/lib/python2.7/dist-packages:/home/parallels/Coding/CodingProjects/slam_catkin_ws/build/cv_bridge/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/parallels/Coding/CodingProjects/slam_catkin_ws/build/cv_bridge" \
    "/usr/bin/python2" \
    "/home/parallels/Coding/CodingProjects/slam_catkin_ws/src/vision_opencv/cv_bridge/setup.py" \
    egg_info --egg-base /home/parallels/Coding/CodingProjects/slam_catkin_ws/build/cv_bridge \
    build --build-base "/home/parallels/Coding/CodingProjects/slam_catkin_ws/build/cv_bridge" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/parallels/Coding/CodingProjects/slam_catkin_ws/install" --install-scripts="/home/parallels/Coding/CodingProjects/slam_catkin_ws/install/bin"
