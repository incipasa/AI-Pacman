class Node:
    def __init__(self, _state, _parent=None, _action=None, _cost=0):
        self.state = _state
        self.parent = _parent
        self.action = _action
        self.cost = _cost

    def total_path(self):
        path_actions = []
        node = self
        
        while node.parent is not None:
            path_actions.append(node.action)
            node = node.parent
        
        path_actions.reverse()
        return path_actions
        
    def __str__(self):
        # TODO implement, default behaviour:
        return super().__str__()


