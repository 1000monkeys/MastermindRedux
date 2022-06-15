from enum import Enum


class SettingsEnum(Enum):
    class Language(Enum):
        NL = 0
        EN = 1
    
    class AmountGameRounds(Enum):
        ONE = 0
        TWO = 1
        THREE = 2
        FOUR = 3
        FIVE = 4
        TEN = 5
    
    class TimeGuess(Enum):
        NONE = 0
        FIFTEEN = 1
        THIRTY = 2
        SIXTY = 3

    class RepeatingColors(Enum):
        NO = 0
        YES = 1

    class EmptyPins(Enum):
        NO = 0
        YES = 1
    
    class Difficulty(Enum):
        EASY = 0
        NORMAL = 1
        HARD = 2
