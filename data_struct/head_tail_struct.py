import numpy as np
from matplotlib.pyplot import plot, show

class HeadTail:
    
    def __init__(self, sequence, head_size=100, tail_size=25, change_value=0.00001):
        
        self.head_size = head_size
        self.tail_size = tail_size
        
        self.sequence = sequence
        
        self.head = sequence[:self.head_size]
        self.tail = sequence[-self.tail_size:]
        
        self.change_value = change_value
    
    @property
    def tail_conclusion(self):
        """
        the result of the behavior of the tail relative to the end of the head
        (growth, fall or unchanged)
        growth    : 1
        fall      : 0
        unchanged : None
        """
        if abs(self.tail[-1] - self.tail[0]) < self.change_value:
            return None
        if self.tail[-1] - self.tail[0] >= self.change_value:
            return 1
        if self.tail[-1] - self.tail[0] <= (-1)*self.change_value:
            return 0

    def set_change_value(self, change_value):
        """
        set the threshold value for the final result 
        (growth, fall or unchanged)
        """
        self.change_value = change_value
        
    @property
    def get_change_value(self):
        return self.change_value
   
    def show_plot(
        self, head=True, tail=True, head_color='g', tail_color='r',):
        """
        # colors:
        # 'b' blue,   'g' green, 'r' red
        # 'c' cyan,   'm' magenta
        # 'y' yellow, 'k' black, 'w' white
        
        """
        if head:
            plot(np.arange(0, self.head_size), 
                 self.head, 
                 color=head_color)
        if tail:
            plot(
                np.arange(self.head_size - 1, self.head_size + self.tail_size), 
                self.sequence[self.head_size - 1 : self.head_size + self.tail_size],
                color=tail_color)
        show()
            
            
if __name__ == '__main__':
    pass