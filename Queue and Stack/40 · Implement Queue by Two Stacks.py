class MyQueue:
    
    def __init__(self):
        # do intialization if necessary

        self.stack_1 = []
        self.stack_2 = []

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        self.stack_1.append(element)

    """
    @return: An integer
    """

    def pop(self):
        temp = 0
        while len(self.stack_1) != 0:
            self.stack_2.append(self.stack_1.pop())
        temp = self.stack_2.pop()

        while len(self.stack_2) != 0:
            self.stack_1.append(self.stack_2.pop())
        return temp
        

    """
    @return: An integer
    """

    def top(self):
        temp = 0
        while len(self.stack_1) != 0:
            self.stack_2.append(self.stack_1.pop())
        temp = self.stack_2.pop()
            
        self.stack_1.append(temp)

        while len(self.stack_2) != 0:
            self.stack_1.append(self.stack_2.pop())
            
        return temp