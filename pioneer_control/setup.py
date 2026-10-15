from setuptools import setup

package_name = 'pioneer_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='student@example.com',
    description='Teleop and ultrasonic visualization for Pioneer 3-DX in CoppeliaSim',
    license='MIT',
    entry_points={
        'console_scripts': [
            'teleop_node = pioneer_control.teleop_node:main',
            'sensor_viz_node = pioneer_control.sensor_viz_node:main',
        ],
    },
)
