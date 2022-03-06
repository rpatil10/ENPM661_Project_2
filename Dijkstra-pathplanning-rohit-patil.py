# Author: Rohit M Patil
# Date: 3/5/2022
import time
import numpy as np
import cv2
from queue import PriorityQueue
import math
import ast

begin_time = time.time()
# Blank workspace/canvas dimensions
workspace_height = 250
workspace_width = 400
# Obstacle clearance
o_clearance = 5
# Create blank canvas
blank_canvas = np.zeros((workspace_height,workspace_width,3), np.uint8)
y_flip = 250

# Function to draw all three obstacles on canvas/workspace using half planes method
def define_obstacle_geometry():
    # Function to draw circle, hexagon and arrow shaped polygon using half planes method
    canvas = draw_all_obstacles()
    #######################################################################
    #######################################################################
    # Below commented code uses OpenCV built in functions to draw obstacles 
    #######################################################################
    # canvas = blank_canvas.copy()
    # Draw clearance Circle
    # cv2.circle(canvas, (300,y_flip-185), 40 + o_clearance, (0,255,255),-1)
    # # Draw Circle
    # cv2.circle(canvas, (300,y_flip-185), 40, (0,0,255),-1)
    # # Draw clearance Hexagon
    # pts = np.array([[200,y_flip-146],[240,y_flip-123],[240,y_flip-77],[200,y_flip-54],[160,y_flip-77],[160,y_flip-123]], np.int32)
    # pts = pts.reshape((-1,1,2))
    # cv2.fillPoly(canvas,[pts],(0,255,255))
    # # Draw Hexagon
    # pts = np.array([[200,y_flip-140],[235,y_flip-120],[235,y_flip-80],[200,y_flip-60],[165,y_flip-80],[165,y_flip-120]], np.int32)
    # pts = pts.reshape((-1,1,2))
    # cv2.fillPoly(canvas,[pts],(0,0,255))
    # # Draw clearance Arrow
    # pts1 = np.array([[137,y_flip-222],[85,y_flip-178],[116,y_flip-79],[28,y_flip-188]], np.int32)
    # pts1 = pts1.reshape((-1,1,2))
    # cv2.fillPoly(canvas,[pts1],(0,255,255))
    # # Draw Arrow
    # pts1 = np.array([[115,y_flip-210],[80,y_flip-180],[105,y_flip-100],[36,y_flip-185]], np.int32)
    # pts1 = pts1.reshape((-1,1,2))
    # cv2.fillPoly(canvas,[pts1],(0,0,255))
    ########################################################################
    ########################################################################
    return canvas

# Function to draw hexagon obstacle using half planes method
def draw_hexagon():
    os_h_1 = blank_canvas.copy()
    for i in range(workspace_width):
        if(240>=i):
            os_h_1[:,i] = [0,0,255]
        if(235>=i):
            os_h_1[:,i] = [0,255,255]

    os_h_2 = blank_canvas.copy()
    for i in range(workspace_width):
        if(160<=i):
            os_h_2[:,i] = [0,0,255]
        if(165<=i):
            os_h_2[:,i] = [0,255,255]

    os_h_3 = blank_canvas.copy()
    for i in range(workspace_width):
        for j in range(workspace_height):
            if (j-(23/40)*i >= -11):
                os_h_3[j,i] = [0,0,255]
            if (j-(4/7)*i >= -(30/7)):
                os_h_3[j,i] = [0,255,255]

    os_h_4 = blank_canvas.copy()
    for i in range(workspace_width):
        for j in range(workspace_height):
            if (j+(23/40)*i <= 311):
                os_h_4[j,i] = [0,0,255]
            if (j+(4/7)*i <= (2130/7)):
                os_h_4[j,i] = [0,255,255]

    os_h_5 = blank_canvas.copy()
    for i in range(workspace_width):
        for j in range(workspace_height):
            if (j-(23/40)*i <= 81):
                os_h_5[j,i] = [0,0,255]
            if (j-(4/7)*i <= (530/7)):
                os_h_5[j,i] = [0,255,255]

    os_h_6 = blank_canvas.copy()
    for i in range(workspace_width):
        for j in range(workspace_height):
            if (j+(23/40)*i >= 219):
                os_h_6[j,i] = [0,0,255]
            if (j+(4/7)*i >= (1570/7)):
                os_h_6[j,i] = [0,255,255]

    output_h_12 = cv2.bitwise_and(os_h_2, os_h_1, mask=None)
    output_h_123 = cv2.bitwise_and(os_h_3, output_h_12, mask=None)
    output_h_1234 = cv2.bitwise_and(os_h_4, output_h_123, mask=None)
    output_h_12345 = cv2.bitwise_and(os_h_5, output_h_1234, mask=None)
    output_h = cv2.bitwise_and(os_h_6, output_h_12345, mask=None)
    return output_h

# Function to draw arrow-shaped polygon obstacle using half planes method
def draw_arrow_polygon():
    os_a_1 = blank_canvas.copy()
    for i in range(workspace_width):
        for j in range(workspace_height):
            if (j-(16/5)*i > -201):
                os_a_1[j,i] = [0,0,255]
            if (j-(16/5)*i > -186):
                os_a_1[j,i] = [0,255,255]

    os_a_2 = blank_canvas.copy()
    for i in range(workspace_width):
        for j in range(workspace_height):
            if (j+(6/7)*i < 145):
                os_a_2[j,i] = [0,0,255]
            if (j+(6/7)*i < (970/7)):
                os_a_2[j,i] = [0,255,255]

    os_a_3 = blank_canvas.copy()
    for i in range(workspace_width):
        for j in range(workspace_height):
            if (j-(85/69)*i < 28):
                os_a_3[j,i] = [0,0,255]
            if (j-(85/69)*i < (475/23)):
                os_a_3[j,i] = [0,255,255]

    os_a_4 = blank_canvas.copy()
    for i in range(workspace_width):
        for j in range(workspace_height):
            if (j+(25/79)*i > 71):
                os_a_4[j,i] = [0,0,255]
            if (j+(25/79)*i > (6035/79)):
                os_a_4[j,i] = [0,255,255]

    output_a_12 = cv2.bitwise_or(os_a_2, os_a_1, mask=None)
    output_a_34 = cv2.bitwise_and(os_a_4, os_a_3, mask=None)
    output_a = cv2.bitwise_and(output_a_34, output_a_12, mask=None)
    return output_a

# Function to draw circle obstacle using half planes method
def draw_circle():
    os_c = blank_canvas.copy()
    for i in range(workspace_width):
        for j in range(workspace_height):
            if ((i-300)**2 + (j-(y_flip-185))**2 <= (40+o_clearance)**2):
                    os_c[j,i] = [0,0,255]
            if ((i-300)**2 + (j-(y_flip-185))**2 <= (40)**2):
                    os_c[j,i] = [0,255,255]
    return os_c

# Function to merge all three obstacles using half planes method
def draw_all_obstacles():
    output_img_ah = cv2.bitwise_or(draw_arrow_polygon(), draw_hexagon(), mask=None)
    output_img_ahc = cv2.bitwise_or(draw_circle(), output_img_ah, mask=None)
    return output_img_ahc

# Class/Object that holds position, c2c(cost to come) and parent data
class Node:
    def __init__(self, position, c2c, parent):
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.c2c = c2c
        self.parent = parent

# Function to check whether given point/location/node lies in obstacle or not
def is_in_obstacle(node):
    x,y = node[0],node[1]
    b,g,r = workspace[y_flip-y-1,x-1]
    if((b==0 and g==0 and r==255) or (b==0 and g==255 and r==255)):
        return True
    else:
        return False

# Function to check whether given point/location/node lies in obstacle or not, while taking inputs from user
def is_in_obstacle_for_get_points(node):
    x,y = node[0],node[1]
    b,g,r = workspace[y-1,x-1]
    if((b==0 and g==0 and r==255) or (b==0 and g==255 and r==255)):
        return True
    else:
        return False

# Function to check whether the current point/location/node is at goal point/location/node
def goal_reached(current_node, goal_node):
    if current_node == goal_node:
        print("Goal reached and path found")
        return True
    else:
        return False

# Function to capture start point/location/node and goal point/location/node inputs from user 
def get_start_end_points():
    # Function to capture start point/location/node input from user
    while True:
        start_location_x, start_location_y = [int(i) for i in input("Enter start location point[x,y](eg: if (5,5), then enter: 10 10): ").split()]
        # Condition to check whether start location is beyond workspace/canvas or not
        if(start_location_x > workspace_width or start_location_y > workspace_height):
            print("Start location cannot be beyond workspace/canvas")
            continue
        if(start_location_y == 250):
            start_location_y = start_location_y-1
        if(start_location_x == 400):
            start_location_x = start_location_x-1
        start_location_y = y_flip - start_location_y
        start_location_node = (start_location_x, start_location_y)
        # Condition to check whether start location is within obstacle or not
        if(is_in_obstacle_for_get_points(start_location_node)):
            print("Start location cannot be within an obstacle")
            continue
        break
    # Function to capture goal point/location/node input from user
    while True:
        goal_location_x, goal_location_y = [int(i) for i in input("Enter goal location point[x,y](eg: if (5,5), then enter: 115 185): ").split()]
        # Condition to check whether goal location is beyond workspace/canvas or not
        if(goal_location_x > workspace_width or goal_location_y > workspace_height):
            print("Goal location cannot be beyond workspace/canvas")
            continue
        if(goal_location_y == 250):
            goal_location_y = goal_location_y-1
        if(goal_location_x == 400):
            goal_location_x = goal_location_x-1
        goal_location_y = y_flip - goal_location_y
        goal_location_node = (goal_location_x, goal_location_y)
        # Condition to check whether goal location is within obstacle or not
        if(is_in_obstacle_for_get_points(goal_location_node)):
            print("Goal location cannot be within an obstacle")
            continue
        break
    return start_location_x, start_location_y, goal_location_x, goal_location_y, start_location_node, goal_location_node

# Function to define robot's possible action set and it's associated c2c(cost to come)
def robot_moves(node):
    i = node.x
    j = node.y
    # Robot's possible action set
    possible_directions = [(i, j + 1), (i + 1, j), (i - 1, j), (i, j - 1), (i + 1, j + 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1)]
    possible_direction_paths = []
    for position, path in enumerate(possible_directions):
        # Robot's possible actions bound inside workspace/canvas
        if not (path[0] >= workspace_width or path[0] < 0 or path[1] >= workspace_height or path[1] < 0):
            # Robot's possible actions restricted from obstacle space
            if not (is_in_obstacle(path)):
                # c2c(determination of cost to come)
                c2c = 1.4 if position > 3 else 1
                possible_direction_paths.append([path, c2c])
    return possible_direction_paths

# Function to perform dijkstra algorithm
def dijkstra_algo(start_location_node, goal_location_node):
    # Dict to map parent child relationship
    parent = {}
    # Dict to map total cost to come to that particular point/location/node 
    total_c2c = {}
    # List to save all the visited point/location/node
    visited = []
    # initialize Priority queue
    q = PriorityQueue()
    # Loop to set c2c of all unvisited point/location/node to infinity 
    for i in range(0, workspace_width):
        for j in range(0, workspace_height):
            total_c2c[str([i, j])] = math.inf
    # Initialize parameters for first/initial point/location/node
    total_c2c[str(start_location_node)] = 0
    visited.append(str(start_location_node))
    node = Node(start_location_node, 0, None)
    parent[str(node.position)] = node
    q.put([node.c2c, node.position])
    while not q.empty():
        current_node = q.get()
        node = parent[str(current_node[1])]
        if goal_reached(current_node[1], goal_location_node):
            print("Time to reach goal location -> %s seconds" % (time.time() - begin_time))
            parent[str(goal_location_node)] = Node(goal_location_node, current_node[0], node)
            break
        for next_node, c2c in robot_moves(node):
            if not is_in_obstacle(next_node):
                if next_node[0] <= workspace_width and next_node[1] <= workspace_height:
                    if str(next_node) in visited:
                        current_cost = c2c + total_c2c[str(node.position)]
                        if current_cost < total_c2c[str(next_node)]:
                            total_c2c[str(next_node)] = current_cost
                            parent[str(next_node)].parent = node
                    else:
                        visited.append(str(next_node))
                        final_cost = c2c + total_c2c[str(node.position)]
                        total_c2c[str(next_node)] = final_cost
                        temp_node = Node(next_node, final_cost, parent[str(node.position)])
                        parent[str(next_node)] = temp_node
                        q.put([final_cost, temp_node.position])
    goal_location_node_final = parent[str(goal_location_node)]
    parent_node = goal_location_node_final.parent
    backtracking = []
    while parent_node:
        backtracking.append(parent_node.position)
        print("Location:", parent_node.position, " it's associated cost to come:", parent_node.c2c)
        parent_node = parent_node.parent
    return backtracking, visited

def visualization_and_documentation(path, map, visited, out):
    visual_map = map.copy()
    # Converts list of string tuple into list of int tuple
    visited = [ast.literal_eval(x.strip()) for x in visited]
    # To draw and document start point/location/node and exploration of new point/location/node
    file = open("Workspace_Exploration_testcase2.txt", "w+")
    for i in visited:
        visual_map[y_flip-i[1]-1, i[0]] = (255, 10, 0)
        # Draw start point/location/node
        cv2.circle(visual_map, (start_location_x, y_flip - start_location_y), radius=3, color=(0, 255, 0), thickness=-1)
        out.write(visual_map)
        file.write(str(i) + "\n")
    file.close()
    # Draw goal point/location/node
    cv2.circle(visual_map, (goal_location_x, y_flip - goal_location_y), radius=3, color=(0, 0, 255), thickness=-1)
    for i in range(1000):
        out.write(visual_map)
    # To draw and document optimal path from goal point/location/node to start point/location/node
    file = open("Optimal_path_testcase2.txt", "w+")
    for i in path:
        visual_map[y_flip-i[1]-1, i[0]-1] = (200, 255, 0)
        out.write(visual_map)
        file.write(str(i) + "\n")
    file.close()
    return visual_map

#############################################
########### Program Starts here #############
#############################################
# Define workspace/canvas with all three obstacles
workspace = define_obstacle_geometry()
# Get start point/location/node and goal point/location/node from user input
start_location_x, start_location_y, goal_location_x, goal_location_y, start_location_node, goal_location_node = get_start_end_points()
start_location_y = y_flip - start_location_y
start_location_node = (start_location_x, start_location_y)
goal_location_y = y_flip - goal_location_y
goal_location_node = (goal_location_x, goal_location_y)
# Call dijkstra algorithm using user inputs and defined workspace/canvas
optimal_path, visited = dijkstra_algo(start_location_node, goal_location_node)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('Optimal_path_using_dijkstra_for_point_robot_animation_testcase2.mp4', fourcc, 2000,(400, 250), isColor=True)
v_n_d_map = visualization_and_documentation(optimal_path, workspace, visited, out)

cv2.imwrite("Optimal_path_testcase2.png", v_n_d_map)  
cv2.imshow("Visualization", v_n_d_map)

out.release()
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()