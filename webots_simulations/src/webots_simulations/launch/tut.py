import os
import launch
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.substitutions.path_join_substitution import PathJoinSubstitution
from launch import LaunchDescription
from launch_ros.actions import Node
from webots_ros2_driver.webots_launcher import WebotsLauncher
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from webots_ros2_core.webots_launcher import WebotsLauncher

def generate_launch_description():
    webots = WebotsLauncher(
        world=os.path.join(
            get_package_share_directory('webots_simulations'),
            'worlds',
            'tut.wbt'
        )
    )

    return LaunchDescription([
        webots,
        Node(
            package='webots_ros2_core',
            executable='webots_node',
            output='screen'
        )
    ])