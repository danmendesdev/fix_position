from enum import Enum


class OrdStatus(Enum):
    New = '0'
    Partially_filled = '1'
    Filled = '2'
    Done_for_day = '3'
    Canceled = '4'
    Replaced_Removed_or_Replaced = '5'
    Pending_Cancel = '6'
    Stopped = '7'
    Rejected = '8'
    Suspended = '9'
    Pending_New = 'A'
    Calculated = 'B'
    Expired = 'C'
    Accepted_for_bidding = 'D'
    Pending_Replace = 'E'
