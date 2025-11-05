This project demonstrates a custom DIY game controller combining physical pushbuttons on an Arduino and computer vision via OpenCV to control in-game actions in Battlefield 2. It’s a fusion of hardware interfacing, real-time vision processing, and Python automation, showcasing a hands-on approach to interactive gaming systems.

Core Features

Physical Button Inputs (Arduino)

Two pushbuttons wired to the Arduino trigger standard in-game actions:

Button 1 → Jump (space)

Button 2 → Fire (left mouse click)

Arduino communicates button presses via serial communication, read by Python in real-time.

Computer Vision Gestures (OpenCV)

A webcam detects a red-colored object (e.g., glove or marker) to trigger additional in-game actions:

Red object detected → Throw Grenade (g)

Real-time contour detection ensures fast and accurate gesture recognition even under variable lighting.

Python Integration

PyAutoGUI simulates keyboard and mouse events based on Arduino input and OpenCV detection.

A single Python script reads Arduino serial input, processes camera feed, and maps all events to game actions.

Multithreading ensures simultaneous reading from Arduino and camera, providing a seamless user experience.

Real-Time Gameplay Control

The hybrid controller allows real-time interaction with Battlefield 2:

Physical pushbuttons for essential actions like jump and fire.

Gestural input for secondary actions like grenades, providing a more immersive and customizable gameplay experience.

Modular and Expandable

Easily add more buttons or gestures for additional game actions (reload, crouch, melee, etc.).

OpenCV detection can track multiple colors or even head movements for advanced camera control.

Technical Highlights

Arduino Uno: Pushbutton inputs and serial communication.

Python 3: Handles integration between Arduino, OpenCV, and PyAutoGUI.

OpenCV: Real-time image processing for gesture recognition.

PyAutoGUI: Sends keyboard and mouse events directly to the game.

Multithreading: Ensures non-blocking input handling from both hardware and computer vision.
