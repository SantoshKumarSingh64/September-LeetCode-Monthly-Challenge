'''
Question Description :-

Robot Bounded In Circle


On an infinite plane, a robot initially stands at (0, 0) and faces north.  
The robot can receive one of three instructions:
        "G": go straight 1 unit;
        "L": turn 90 degrees to the left;
        "R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.
Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 
Example 1:
        Input: "GGLLGG"
        Output: true
        Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
                    When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example 2:
        Input: "GG"
        Output: false
        Explanation: The robot moves north indefinitely.

Example 3:
    Input: "GL"
    Output: true
    Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
 

Note:
        1.   1 <= instructions.length <= 100
        2.   instructions[i] is in {'G', 'L', 'R'}
'''
def isRobotBounded(instructions):

    next_move = [0,1]
    current_state = [0,0]

    for _ in range(4):
        for x in instructions:

            if x == "G":
                current_state[0] += next_move[0]
                current_state[1] += next_move[1]
            elif x == "L":
                next_move = [-next_move[1],next_move[0]]
            elif x == "R":
                next_move = [next_move[1],-next_move[0]]

    return current_state == [0,0]

print(isRobotBounded("GL"))

'''
Optimal Solution :-

def isRobotBounded(instructions):
    
    go = {'N':(0,1), 'S':(0,-1), 'W':(-1,0), 'E':(1,0)}
    left = {'N':'W', 'W':'S', 'S':'E', 'E':'N'}
    right = {'N':'E', 'E':'S', 'S':'W', 'W':'N'}
    current = [0, 0]
    direction = 'N'
        
    for i in instructions:
        if i == 'G':
            x, y = go[direction]
            current[0] += x
            current[1] += y
        elif i == 'L':
            direction = left[direction]
        else:
            direction = right[direction]
        
    if current == [0,0] or direction != 'N':
        return True
    else:
        return False
'''