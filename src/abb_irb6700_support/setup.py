from setuptools import setup
import os
from glob import glob


package_name = 'abb_irb6700_support'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch','*.py'))),
        (os.path.join('share', package_name, 'rviz'), glob(os.path.join('rviz','*.rviz'))),

        (os.path.join('share', package_name, 'urdf'), glob(os.path.join('urdf','*.xacro'))),

        (os.path.join('share', package_name, 'meshes', 'irb6700', 'collision'), glob(os.path.join('meshes','irb6700', 'collision','*.stl'))),
        (os.path.join('share', package_name, 'meshes', 'irb6700', 'visual'), glob(os.path.join('meshes','irb6700', 'visual','*.stl'))),

        (os.path.join('share', package_name, 'meshes', 'irb6700_200_260', 'collision'), glob(os.path.join('meshes','irb6700_200_260', 'collision','*.stl'))),
        (os.path.join('share', package_name, 'meshes', 'irb6700_200_260', 'visual'), glob(os.path.join('meshes','irb6700_200_260', 'visual','*.stl'))),

        (os.path.join('share', package_name, 'meshes', 'irb6700_235_265', 'collision'), glob(os.path.join('meshes','irb6700_235_265', 'collision','*.stl'))),
        (os.path.join('share', package_name, 'meshes', 'irb6700_235_265', 'visual'), glob(os.path.join('meshes','irb6700_235_265', 'visual','*.stl'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rajesh',
    maintainer_email='rajesh.pachaikani@spotless.ai',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
