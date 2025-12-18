Project's Title:
- 777-300ER Flight Simulator using Python

Why I programmed the flight simulator and what I learnt through this flight simulator:
- I want to deepen my understanding of the four principles of flight (lift, weight, thrust, drag).
- I developed an understanding of how all four principles of flight and angle of attack interact, and how reduced airspeed reduces climb performance and stall margins.
- I learnt how iterative testing, where I tested each new function, can reduce the complexity of debugging when a problem is found.

Project Description:
- I use aerodynamic equations and joystick inputs (may use keyboard & mouse instead) to model aircraft behaviour across three primary control surfaces.
- I use the Pygame module, which is a 2D game library for Python, as it is simpler to programme than a 3D game engine (Ursina).
- The flight simulator works by moving the background, which consists of two rectangles that represent the sky and ground. This creates a sense that the aircraft is rolling and pitching.
- I need to calculate the coordinates of the four corners for each rectangle.
- Initially, I struggled to find the correct equation to calculate all four coordinates of the rectangles, so I drew a scale diagram on paper to help solve this geometric problem.

Assumptions & Future Improvements:
- This program assumes an angle of attack above 20 degrees will stall the aircraft.
- I would like to create a runway and infrastructure to allow the aircraft to land.
- I also hope to be able to calculate an accurate angle of attack based on the program's current data.
- The program's variables also grow exponentially over time when altitude or airspeed is too high (likely numerical instability), which needs further debugging.

How to run the flight simulator:
- Download and open VS Code / Visual Studio
- Download a Python interpreter online
- pip install pygame
- (Optional) Connect a joystick to your computer
- Click Run

How to use the flight simulator:
Joystick:
- Move the joystick left/right for roll movement
- Move the joystick up/down for pitch movement
- Twist the joystick for yaw movement

Keyboard:
- Move the cursor left/right for roll movement
- Move the cursor up/down for pitch movement
- Click and hold the key 'w' to throttle up
- Click and hold the key 's' to throttle down