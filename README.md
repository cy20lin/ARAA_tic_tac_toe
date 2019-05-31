# ARAA Tic-Tac-Toe
This is the final project for the course, `Advanced Robotics and Automation Applications`, at `National Taipei University of Technology`. 
This project started at May 2019.

## Project Layout

This project contains following packages, each is responsable for specific job.

| Package          | Description                              |
|------------------|------------------------------------------|
| araa_manipulator | Manipulator controls for moving chess    |
| araa_dip         | Image processing on the chessboard       |
| araa_algorithm   | Algorithms for Computer Player           |
| araa_ui          | User Interface for user to play the game |
| araa_demo        | Demo for the Tic-Tac-Toe game            |

## Development Environment Setup

To develop this project, fellow the instructions below to have your environment setup.

### Ensure ROS is installed

If not, fellow the installation instructions for ROS, [here](http://wiki.ros.org/ROS/Installation).

It is not restricted to install which ROS distribution, though `ROS melodic` distribution is preferred.

### Build this project

To build this project, go through following commands to setup the workspace.

```bash
  # Assume ROS workspace is at ~/ws
  cd ~
  mkdir -p ~/ws/src
  cd ~/ws/src
  catkin_init_workspace
  git clone https://github.com/cy20lin/ARAA_tic_tac_toe
  cd ~/ws
  catkin_make
```

### Test and Run (optional)

If you want to test and run the project, do following steps.

```bash
  cd ~/ws
  source ~/ws/devel/setup.bash
  roslaunch araa_demo demo.launch
```

