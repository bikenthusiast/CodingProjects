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

echo_and_run cd "/home/parallels/temporary/CodingProjects2/catkin_ws/src/third_party/vision_opencv/image_geometry"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/parallels/temporary/CodingProjects2/catkin_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/parallels/temporary/CodingProjects2/catkin_ws/install/lib/python2.7/dist-packages:/home/parallels/temporary/CodingProjects2/catkin_ws/build/image_geometry/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/parallels/temporary/CodingProjects2/catkin_ws/build/image_geometry" \
    "/usr/bin/python2" \
    "/home/parallels/temporary/CodingProjects2/catkin_ws/src/third_party/vision_opencv/image_geometry/setup.py" \
    build --build-base "/home/parallels/temporary/CodingProjects2/catkin_ws/build/image_geometry" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/parallels/temporary/CodingProjects2/catkin_ws/install" --install-scripts="/home/parallels/temporary/CodingProjects2/catkin_ws/install/bin"
