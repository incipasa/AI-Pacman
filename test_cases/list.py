def cornersHeuristic(state, problem):
    """
    A heuristic for the CornersProblem that you defined.

      state:   The current search state
               (a data structure you chose in your search problem)

      problem: The CornersProblem instance for this layout.

    This function should always return a number that is a lower bound on the
    shortest path from the state to a goal of the problem; i.e.  it should be
    admissible (as well as consistent).
    """
  
    
    corners = problem.corners  # These are the corner coordinates
    walls = problem.walls  # These are the walls of the maze, as a Grid (game.py)

    min_cost = 1000000
    for i in range(4):
        cost  = manhattanDistance(state[0],corners[i])
        if cost < min_cost:
            min_cost = cost
            nearest = i   
 
    
    h_c = min_cost

    if nearest == 0:
        h_c = h_c + manhattanDistance(corners[nearest],corners[1])
        h_c = h_c + manhattanDistance(corners[1],corners[3])
        h_c = h_c + manhattanDistance(corners[3],corners[2])
    
    if nearest == 1:
        h_c = h_c + manhattanDistance(corners[nearest],corners[0])
        h_c = h_c + manhattanDistance(corners[0],corners[2])
        h_c = h_c + manhattanDistance(corners[2],corners[3])

    if nearest == 2:
        h_c = h_c + manhattanDistance(corners[nearest],corners[3])
        h_c = h_c + manhattanDistance(corners[3],corners[1])
        h_c = h_c + manhattanDistance(corners[1],corners[0])

    if nearest == 3:
        h_c = h_c + manhattanDistance(corners[nearest],corners[2])
        h_c = h_c + manhattanDistance(corners[2],corners[0])
        h_c = h_c + manhattanDistance(corners[0],corners[1])                
        

    return h_c # Default to trivial solution

###################################################################

def cornersHeuristic(state, problem):
    """
    A heuristic for the CornersProblem that you defined.

      state:   The current search state
               (a data structure you chose in your search problem)

      problem: The CornersProblem instance for this layout.

    This function should always return a number that is a lower bound on the
    shortest path from the state to a goal of the problem; i.e.  it should be
    admissible (as well as consistent).
    """
  
    
    corners = problem.corners  # These are the corner coordinates
    walls = problem.walls  # These are the walls of the maze, as a Grid (game.py)
    
    food_length = 4
    actual_food_length = food_length - 1
    min_cost = 1000000
    c_list = list(corners)
    
    for i in range(4):
        cost  = manhattanDistance(state[0],c_list[i])
        if cost < min_cost:
            min_cost = cost
            nearest = i   
 
    h_c = min_cost
    nearest_point = c_list[nearest]
    c_list.pop(nearest) 

    while len(c_list) > 0:
        min_cost = 1000000
        for i in range(actual_food_length):
            cost  = manhattanDistance(nearest_point,c_list[i])
            if cost < min_cost:
                min_cost = cost
                nearest = i   
                nearest_point = c_list[nearest]
        h_c = h_c + min_cost
        c_list.pop(nearest)            
        actual_food_length = actual_food_length - 1    

    return h_c # Default to trivial solution