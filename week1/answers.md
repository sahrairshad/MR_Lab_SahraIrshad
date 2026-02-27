Define: node, topic, package, workspace.

Node:
A node is an executable process in ROS 2 that performs a specific task, such as reading sensor data, controlling a motor, or publishing messages.

Topic:
A topic is a named communication channel used to exchange messages between nodes using a publisher–subscriber model.Package:
A package is a structured folder that contains ROS 2 code, configuration files, dependencies, and build information.

Workspace:
A workspace is a directory that contains one or more ROS 2 packages and allows them to be built and installed together.

2️⃣ Explain why sourcing is required. What happens if you do not source a workspace?

Sourcing is required to set environment variables so that the system can find ROS 2 packages, executables, and dependencies.

When we run:

source install/setup.bash

it updates the environment so ROS 2 knows where our built packages are located.

If we do not source the workspace:

ROS 2 cannot detect our package

ros2 pkg list will not show our package

ros2 run will give “package not found” error

3️⃣ What is the purpose of colcon build? What folders does it generate?

colcon build compiles and builds all packages inside the src folder of the workspace.

It generates the following folders:

build/ → Contains intermediate build files

install/ → Contains installed executables and setup files

log/ → Contains build logs

Without running colcon build, the package cannot be executed.

4️⃣ In your own words, explain what the entry_points console script does in setup.py.

The entry_points console script connects a command name to a Python function.

For example:

'simple_node = my_first_pkg.simple_node:main'

This means:

When we run

ros2 run my_first_pkg simple_node

ROS 2 executes the main() function inside simple_node.py.

So, entry_points allows ROS 2 to know which Python file and function should run when we type a specific command.
