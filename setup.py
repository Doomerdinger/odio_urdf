from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['odio_urdf'],
    scripts=[],
    package_dir={'odio_urdf':'odio_urdf'},
)

setup(**d)
