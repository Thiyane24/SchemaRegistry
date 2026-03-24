from enum import Enum, auto

class ChangeType(Enum):
    BREAKING = "breaking"
    NON_BREAKING = "non_breaking"
    NO_CHANGE = "no_change"