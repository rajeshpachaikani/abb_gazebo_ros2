import os

from ament_index_python.packages import get_package_share_directory

from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription, RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
import xacro



def get_xacro_to_doc(xacro_file_path):
    doc = xacro.parse(open(xacro_file_path))
    xacro.process_doc(doc)
    return doc


def generate_launch_description():

    robot_model = "irb6700_200_260"
    #   <include file="$(find gazebo_ros)/launch/empty_world.launch">
    #     <arg name="world_name" value="worlds/empty.world"/>
    #     <arg name="gui" value="true"/>
    #     <arg name="paused" value="$(arg paused)"/>
    #   </include>

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch'), '/gazebo.launch.py']),
    )

    
    xacro_file = get_package_share_directory(
        'abb_irb6700_gazebo') + '/urdf/' + robot_model + '.xacro'

    doc = xacro.parse(open(xacro_file))
    xacro.process_doc(doc)
    params = {'robot_description': doc.toxml()}

    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params]
    )

    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'abb_robot'],
                        output='screen')

    # Start Gazebo with my empty world
    world_file_name = 'my_empty_world.world'
    world = os.path.join(get_package_share_directory('abb_irb6700_gazebo'), 'worlds', world_file_name)
    gazebo_node = ExecuteProcess(cmd=['gazebo', '--verbose', world, '-s', 'libgazebo_ros_factory.so'], output='screen')

    return LaunchDescription([node_robot_state_publisher, spawn_entity, gazebo_node])
