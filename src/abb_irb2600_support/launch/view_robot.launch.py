
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory
import xacro


def get_xacro_to_doc(xacro_file_path):
    doc = xacro.parse(open(xacro_file_path))
    xacro.process_doc(doc)
    return doc


def generate_launch_description():

    robot_model = 'irb2600_12_165'
    xacro_file = get_package_share_directory(
        'abb_irb2600_support') + '/urdf/' + robot_model + '.xacro'
    doc = get_xacro_to_doc(xacro_file)
    # RViz
    rviz_config_file = get_package_share_directory('abb_irb2600_support') + "/rviz/view_config.rviz"
    rviz_node = Node(package='rviz2',
                     executable='rviz2',
                     name='rviz2',
                     output='log',
                     arguments=['-d', rviz_config_file])

    # Robot State Publisher
    robot_state_publisher = Node(package='robot_state_publisher',
                                 executable='robot_state_publisher',
                                 name='robot_state_publisher',
                                 output='both',
                                 parameters=[{'robot_description': doc.toxml()
                                              }])

    # Joint State Publisher
    joint_state_publisher_gui = Node(package='joint_state_publisher_gui',
                                     executable='joint_state_publisher_gui',
                                     output='screen',
                                     name='joint_state_publisher_gui')

    return LaunchDescription([robot_state_publisher, joint_state_publisher_gui, rviz_node])
