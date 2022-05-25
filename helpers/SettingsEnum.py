from enum import Enum


class SettingsEnum(Enum):
    class Language(Enum):
        NL = 0
        EN = 1
    
    class AmountGameRounds(Enum):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        TEN = 10
    
    class TimeGuess(Enum):
        NONE = 0
        FIFTEEN = 15
        THIRTY = 30
        SIXTY = 60

    class RepeatingColors(Enum):
        NO = 0
        YES = 1

    class EmptyPins(Enum):
        NO = 0
        YES = 1
    
    class Difficulty(Enum):
        EASY = 0
        NORMAL = 1
        DIFFICULT = 2
