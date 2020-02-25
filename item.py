class Item:
    
    def __init__(self, name, description=" "):
        self.name = name
        self.description = description
    
    def __str__(self):
        raise NotImplementedError
    
class Task(Item):

    def __init__(self, name, state=0, importance=5, difficulty=5, description=" "):
        super().__init__(name, description=description)
        self.state = state
        self.importance = importance
        self.difficulty = difficulty
    
    @staticmethod
    def get_state_short(state):

        if state is 0:
            return "NS"
        elif state is 1:
            return "IP"
        elif state is 2:
            return "UT"
        elif state is 3:
            return "FN"
        elif state is 4:
            return "CN"
        elif state is 5:
            return "DE"
        else:
            raise ValueError(f"Invalid state {state}")

    @staticmethod
    def get_state_long(state):

        if state is 0:
            return "Not Started"
        elif state is 1:
            return "In Progress"
        elif state is 2:
            return "Untested"
        elif state is 3:
            return "Finished"
        elif state is 4:
            return "Canceled"
        elif state is 5:
            return "Delayed"
        else:
            raise ValueError(f"Invalid state {state}")

    def __str__(self):
        '''Return the formatted output of the Task'''
        
        msg = ""

        msg += f"{self.get_state_short(self.state)} ({self.importance}|{self.difficulty}) - {self.name}"
        if self.description != "":
            msg += f"\n  {self.description}"
        
        return msg

class Group(Item):

    def __init__(self, name, children=[], description=" "):
        super().__init__(name, description=description)
        self.children = children
    
    def __str__(self):
        '''Return the formatted output of the Group'''
        
        msg = ""


        msg += f"{self.name}:"
        if self.description != "":
            msg += f"\n  {self.description}"
        
        msg += "\n" +  "-" * max(len(self.name), len(self.description) + 2)
        
        for child in self.children:
            msg += f"\n    {child}"
        
        return msg
    
    def add_child(self, item_to_add):
        
        if not isinstance(item_to_add, Item):
            raise TypeError(f"{item_to_add} not an Item (Type={type(item_to_add)})")
        
        self.children = self.children + [item_to_add]

    def remove_child(self, item_to_remove):

        try:
            self.children.remove(item_to_remove)
        except:
            raise ValueError("Item not a child")