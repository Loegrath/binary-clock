"""Binary Clock Display Wrapper"""
import numpy as np
from datetime import datetime

class clock_display():
    def __init__(self):
        """Initialize a clock display.
        
        Each column in the array has values that correspond to
        whether or not that value is activated or not.
        
        The clock is initialized to have all displays set to off.
        """
        self.time = datetime.today()
        self.col_hours = np.zeros(4, dtype=int)
        self.col_mins = np.zeros(4, dtype=int)
        self.col_min_incs = np.zeros(4, dtype=int)
        self.meridiem = False

    def cols_reset(self):
        """Reset all display columns to 0s."""
        self.col_hours = np.zeros(4, dtype=int)
        self.col_mins = np.zeros(4, dtype=int)
        self.col_min_incs = np.zeros(4, dtype=int)

    def cols_update(self):
        """Update display columns so they correctly
        represent the current time."""
        translate_hours = [1, 2, 4, 8]
        translate_mins = [1, 2, 4, 8]
        translate_min_incs = [15, 30, 45, 60]
        
        self.cols_reset()

        hour = self.time.hour
        if hour == 0:
            hour = 12
        if hour > 12:
            hour -= 12

        for i in range(len(translate_hours) - 1, -1, -1):
            if hour >= translate_hours[i]:
                self.col_hours[i] = 1
                hour -= translate_hours[i]

        minutes = self.time.minute
        for i in range(len(translate_min_incs) - 1, -1, -1):
            if minutes >= translate_min_incs[i]:
                self.col_min_incs[i] = 1
                minutes -= translate_min_incs[i]
        for i in range(len(translate_mins) - 1, -1, -1):
            if minutes >= translate_mins[i]:
                self.col_mins[i] = 1
                minutes -= translate_mins[i]

    def __repr__(self):
        """Set repr to return the display of the binary clock."""
        # Insert code here.