# Mecanum Simulator

A repository containing a simulator for a Mecanum wheeled robot.

## Features

- Uses ordinary differential equations (ODEs) for the physics simulation.
- Utilizes actual motor data for realistic performance.
- Provides a graphical interface for visualizing the robot's movement.

## Status

- `systemgame.py` is runnable.
- `goalfinder.py` is only runnable once a model has been trained using `ml_trainer.py`
- `motorcurvefitter.py` is used to calculate the motor constants. It is runnable.

## Credit

`GoBilda-MotorCurve-Combined.csv` is adapted from the following sources:

- <https://motors.vex.com/other-motors/modern-robotics-12vdc>
- <https://link.vex.com/motors/modern-robotics/motor-curve-data-4v>
- <https://link.vex.com/motors/modern-robotics/motor-curve-data-6v>
- <https://link.vex.com/motors/modern-robotics/motor-curve-data-8v>
- <https://link.vex.com/motors/modern-robotics/motor-curve-data-10v>
- <https://link.vex.com/motors/modern-robotics/motor-curve-data-12v>

## Notes

- I formatted this code with Black on a whim. I'm not entirely sure that I like it yet.
- This code could do with more comments and modularization.
