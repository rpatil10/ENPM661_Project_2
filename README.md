# Project 2: Implementation of Dijkstra algorithm for a Point Robot
## _ENPM661_
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Author
Rohit M Patil

Email ID: rpatil10@umd.edu

## Description
Implemention of Dijkstra’s Algorithm to find a path between start and end point on a given map for a point robot (radius = 0; clearance = 5 mm). Checks the feasibility of all inputs/outputs (if user gives start and goal nodes that are in the obstacle space they will be informed by a message and they should try again). Code outputs an animation/video of optimal path generation between start and goal point on the map. It shows both the node exploration as well as the optimal path generated.

![Work space](/outputs/workspace.jpg?raw=true)
## Dependencies

| Plugin | 
| ------ |
| time | 
| numpy | 
| cv2 | 
| queue | 
| math | 
| ast | 

## Instructions to run
Clone or download the project repository and open the folder,
Open terminal in the project folder and type below command:
```bash
python Dijkstra-pathplanning-rohit-patil.py
```
or
```bash
python3 Dijkstra-pathplanning-rohit-patil.py
```
Terminal asks for user input for start and goal location:
Input start location as shown in below fashion, **x-coordinate** _space_ **y-coordinate**
```sh
Enter start location point[x,y](eg: if (5,5), then enter: 10 10): 25 30
```
Input goal location as shown in below fashion, **x-coordinate** _space_ **y-coordinate**
```sh
Enter goal location point[x,y](eg: if (5,5), then enter: 115 185): 120 190
```
## Output
**Test case 1:**
Start location: 10 10
Goal location: 115 185
. Visualization video: [Test case 1](https://youtu.be/vwKUfesqk9k).
![Optimal_path_testcase1](/outputs/Optimal_path_testcase1.png?raw=true)


**Test case 2:**
Start location: 20 50
Goal location: 395 245
. Visualization video: [Test case 2](https://youtu.be/W2lts-Yb6SI).
![Optimal_path_testcase2](/outputs/Optimal_path_testcase2.png?raw=true)

