"""
My Calendar II

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendarTwo class:

MyCalendarTwo() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

"""


class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlaps = []
        

    def book(self, start: int, end: int) -> bool:
        for start_idx, end_idx in self.overlaps:
            if start < end_idx and end > start_idx:
                return False
        for start_idx, end_idx in self.calendar:
            if start < end_idx and end > start_idx:
                self.overlaps.append((max(start, start_idx), min(end, end_idx)))
        self.calendar.append((start, end))
        return True
            
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)