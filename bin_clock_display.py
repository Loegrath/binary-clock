"""
Binary Clock Display.

This file should just be used to contain
the clock_display() class. The class should
accept inputs to activate its update method,
outputting a display on the __repr__ call.
"""
import numpy as np
from datetime import datetime


class clock_display():
    """
    Binary clock display class.

    This class should be used as an object to represent
    datetime inputs according to the readme on the following
    github repository: https://github.com/Loegrath/binary-clock
    """

    def __init__(self):
        """
        Initialize a clock display.

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

    def cols_update(self, time):
        """
        Update display columns so they correctly
        represent the current time.
        """
        self.time = time

        translate_hours = [8, 4, 2, 1]
        translate_mins = [8, 4, 2, 1]
        translate_min_incs = [60, 45, 30, 15]

        self.cols_reset()

        hour = self.time.hour
        if hour >= 12:
            self.meridiem = True
            if hour != 12:
                hour -= 12
        elif hour < 12:
            self.meridiem = False
            if hour == 0:
                hour = 12

        for i in range(len(translate_hours)):
            if hour >= translate_hours[i]:
                self.col_hours[i] = 1
                hour -= translate_hours[i]

        minutes = self.time.minute
        for i in range(len(translate_min_incs)):
            if minutes >= translate_min_incs[i]:
                self.col_min_incs[i] = 1
                minutes -= translate_min_incs[i]
        for i in range(len(translate_mins)):
            if minutes >= translate_mins[i]:
                self.col_mins[i] = 1
                minutes -= translate_mins[i]

    def __repr__(self):
        """Set repr to return the display of the binary clock."""
        # If time is in PM, use thick border.
        if self.meridiem:
            print("=========")
            for i in range(len(self.col_hours)):
                print("||{0} {1} {2}||".format(self.col_hours[i],
                                               self.col_mins[i],
                                               self.col_min_incs[i]))
            return "========="

        # If time is in AM, use thin border.
        else:
            print(" -------")
            for i in range(len(self.col_hours)):
                print(" |{0} {1} {2}|".format(self.col_hours[i],
                                              self.col_mins[i],
                                              self.col_min_incs[i]))
            return " -------"
