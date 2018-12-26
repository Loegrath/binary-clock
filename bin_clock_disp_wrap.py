"""Binary Clock Display Wrapper"""
import numpy as np

class clock_display():
    def __init__(self):
        """Initialize a clock display.
        
        Each column in the array has values that correspond to
        whether or not that value is activated or not.
        
        The clock is initialized to have all displays set to off.
        """
        self.time = "Time not set."
        self.col_hours = np.zeros(4, dtype=int)
        self.col_mins = np.zeros(4, dtype=int)
        self.col_min_incs = np.zeros(4, dtype=int)

    def time_read(self):
        # Code here

    def time_set(self, time_str):
        """Take an input and set the display to the correct time.
        
        Function should take inputs as "HH:DD"
        """
        # Code here