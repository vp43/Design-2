
# Time Complexity : O(1) for all operations Amortized time Complexity for pop - 0(1) 
# Space Complexity : 0(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

#Approach - push to stack_in always. if stack out is empty then transfer all elements from 
#in to out and pop from out.

class MyQueue:
    
    def __init__(self):
        
        #Initialize your data structure here.
        
        self.stack_in = []
        self.stack_out = []
        
    def push(self, x: int) -> None:
        #Push element x to the back of queue.
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.stack_out.pop()
        
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack_in and not self.stack_out 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()