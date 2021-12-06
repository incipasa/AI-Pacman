# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from node import Node
import sys
import math
import searchAgents

""" fringe = utils.Queue()
    fringe.push(problem.getStartState() --->  crear el Node)
    while True:
        if fringe.empty(): raise Exception
        n:= fringe.pop()
        if problem.isGoalState(n.state):
            return n.total_path()
        
        for state, action, cost in problem.getSuccessors()
            Node()
            
            
    
    bfs(problem : Search Problem)
        """


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    n = Node(problem.getStartState())
    if problem.isGoalState(problem.getStartState()):
        return n.total_path()
    fringe = util.Stack()
    fringe.push(n)
    generated = set()

    while not fringe.isEmpty():
        n = fringe.pop()
        generated.add(n.state)

        for state, action, cost in problem.getSuccessors(n.state):
            ns = Node(state, n, action, n.cost + cost)
            if ns.state not in generated:
                if problem.isGoalState(ns.state):
                    return ns.total_path()
                fringe.push(ns)
                generated.add(ns.state)


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the s
    earch tree first."""
    n = Node(problem.getStartState())
    if problem.isGoalState(problem.getStartState()):
        return n.total_path()
    fringe = util.Queue()
    fringe.push(n)
    generated = set()

    while not fringe.isEmpty():
        n = fringe.pop()
        generated.add(n.state)

        for state, action, cost in problem.getSuccessors(n.state):
            ns = Node(state, n, action, n.cost + cost)
            if ns.state not in generated:
                if problem.isGoalState(ns.state):
                    return ns.total_path()
                fringe.push(ns)
                generated.add(ns.state)


def uniformCostSearch(problem:SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    
    n = Node(problem.getStartState())
    if problem.isGoalState(problem.getStartState()):
        return n.total_path()
    
    fringe = util.PriorityQueue()
    generated = {}
    fringe.push(n, 0) # 0 -> n.heuristic manhattan(n.state, problem)
    generated[n.state] = ("F", 0) # 0 -> n.heuristic
    
    while not fringe.isEmpty():
        n = fringe.pop()
        if problem.isGoalState(n.state):
            return n.total_path()
        
        if generated[n.state][0] == "E":
            #node has been expanded, continue
            continue
        generated[n.state] = ("E", n.cost) # n.cost + n.heurisrtic WRONG
        for s, a, c in problem.getSuccessors(n.state):
            ns = Node(s, n, a, n.cost + c) # n.cost + n.heurisrtic
            if ns.state not in generated:
                fringe.push(ns, ns.cost)
                generated[ns.state] = ("F", ns.cost)
            
            elif generated[ns.state][0] == "F" and generated[ns.state][1] > ns.cost:
                fringe.update(ns, ns.cost)
                generated[ns.state] = ("F", ns.cost)
    
    print("No solution")
    sys.exit(-1) 
    
    
    """
    n = Node(problem.getStartState())
    if problem.isGoalState(problem.getStartState()):
        return n.total_path()

    fringe = util.PriorityQueue()
    generated = {}
    fringe.push(n, 0)
    generated[n.state] = ("F", 0)

    while not fringe.isEmpty():
        n = fringe.pop()
        if problem.isGoalState(n.state):
            return n.total_path()
        if generated[n.state][0] == "E":
            continue

        generated[n.state] = ("E", n.cost)
        for state, action, cost in problem.getSuccessors(n.state):  # cost = action cost     n.cost = total cost parent node
            ns = Node(state,n, action, n.cost + cost)  # ns.cost = n.cost + cost
            if ns.state not in generated:
                fringe.push(ns, ns.cost)
                generated[ns.state] = ("F", ns.cost)
            elif generated[ns.state][0] == "F" and generated[ns.state][1] > ns.cost:
                fringe.update(ns,ns.cost)
                generated[ns.state] = ("F", ns.cost)


    print("No solution")
    sys.exit(-1)    
    """
    


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


#def manhattanHeuristic(state, problem):
#    goal_state = problem.isGoalState()
#    x, y = state.startingPosition
#    _x, _y = goal_state.startingPosition
#    return abs(x -_x) + abs(y -_y)

#def euclidianHeuristic (state, problem):
#    goal_state = problem.isGoalState()
#    x, y = state.startingPosition
#    _x, _y = goal_state.startingPosition
    
#    return math.hypot(abs(x -_x), abs(y -_y))
    
def manhattanHeuristic(position, problem, info={}):
    "The Manhattan distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.goal
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])


def euclideanHeuristic(position, problem, info={}):
    "The Euclidean distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.goal
    return ((xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2) ** 0.5

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    
    n = Node(problem.getStartState())
    if problem.isGoalState(problem.getStartState()):
        return n.total_path()
    
    fringe = util.PriorityQueue()
    generated = {}
    fringe.push(n, heuristic(n.state, problem)) # 0 -> n.heuristic manhattan(n.state, problem)
    generated[n.state] = ("F", heuristic(n.state, problem)) # 0 -> n.heuristic
    
    while not fringe.isEmpty():
        n = fringe.pop()
        if problem.isGoalState(n.state):
            return n.total_path()
        
        if generated[n.state][0] == "E":  
            #node has been expanded, continue
            continue
        generated[n.state] = ("E", n.cost + heuristic(n.state, problem)) ##
        for s, a, c in problem.getSuccessors(n.state):
            ns = Node(s, n, a, n.cost + c) #edited
            if ns.state not in generated:
                fringe.push(ns, ns.cost + heuristic(n.state, problem)) # 
                generated[ns.state] = ("F", ns.cost + heuristic(n.state, problem))
            
            elif generated[ns.state][0] == "F" and generated[ns.state][1] > ns.cost:
                fringe.update(ns, ns.cost + heuristic(n.state, problem))
                generated[ns.state] = ("F", ns.cost + heuristic(n.state, problem))
    
    print("No solution")
    sys.exit(-1) 


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
