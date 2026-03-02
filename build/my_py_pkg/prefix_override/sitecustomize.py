import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/samruddhi/ros2_ws/src/my_py_pkg/install/my_py_pkg'
