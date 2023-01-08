import numpy as np
from matplotlib.pyplot import plot, show

class HeadTail:
    
    def __init__(self, sequence, head_size=100, tail_size=25):
        
        self.head_size = head_size
        self.tail_size = tail_size
        
        self.sequence = sequence
        
        self.head = sequence[:self.head_size]
        self.tail = sequence[-self.tail_size:]
   
    def show_plot(
        self, head=True, tail=True, window_show=True, head_color='g', tail_color='r',):
        """
        # colors:
        # ‘b’ blue,   ‘g’ green, ‘r’ red
        # ‘c’ cyan,   ‘m’ magenta
        # ‘y’ yellow, ‘k’ black, ‘w’ white
        
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
        if window_show:
            show()
if __name__ == '__main__':
    pass