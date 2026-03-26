from enum import Enum

class ChangeType(Enum):
    BREAKING = "BREAKING"
    NON_BREAKING = "NON_BREAKING"
    NO_CHANGE = "NO_CHANGE"