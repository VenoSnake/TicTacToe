"""
This Python Module Carries Out The Respective Operations Required In A TicTacToe Game.
(Ex: Play A Move, Declare Winner.. etc)
"""

import numpy as np
from enum import Enum

class GameState(Enum):
    """
    This Class Holds The State Of The Game (i.e Won, Lost, Tie, In Progress ?)
    """

    NOT_FINISHED = 0
    NAUGHT_WIN   = 1
    CROSS_WIN    = 2
    DRAW         = 3

EMPTY  = 0  # State Of A Particular Block = 0, If Empty
NAUGHT = 1  # State Of A Particular Block = 1, If O
CROSS  = 2  # State Of A Particular Block = 2, If X

BOARD_DIMENSION = 3
BOARD_SIZE      = 9

class TicTacToe:
    """
    This Class Ensure's All The Rules Of The Game Are Followed, The Progression Of The Game
    Also Takes Place Through This Class.
    """

    WIN_CHECK_DIRECTORY = {0: [(1, 1), (1, 0), (0, 1)],
                           1: [(1, 0)],
                           2: [(1, 0), (1, -1)],
                           3: [(0, 1)],
                           6: [(0, 1)]}

    def __init__(self, s = None):   # Constructor Initializes New TicTacToe Board
        """
        Creates A New Board
        :Param s: If A Existing Board's State Has Been Passed We Use That, Else New Board
        """

        if s is None:
            self.state = np.array([0] * BOARD_SIZE)
            self.reset()

        else:
            self.state = s.copy()

    @staticmethod
    def NextTurn(side):  # Returns Who Has To Play Next

        if side == EMPTY:
            raise ValueError('Empty Has No Other Side/NextTurn')

        elif side == NAUGHT:
            return CROSS

        elif side == CROSS:
            return NAUGHT

        else:
            raise ValueError('{} Is Not Valid Side'.format(side))

    @staticmethod
    def ConvertToPosition(coor):
        """
        Converts A 2D Location Of A Block In A GameState To A 1D Location
        :Param coor : A List/Tuple (row, column)
        """

        return coor[0] * BOARD_DIMENSION + coor[1]

    @staticmethod
    def ConvertToCoordinate(pos):
        """
        Converts A 1D Position To A 2D Coordinate (row, column)
        :Param pos : A 1D number Indicating Pos Of Block
        """

        return pos // BOARD_DIMENSION, pos % BOARD_DIMENSION

    def reset(self):
        """
        Resets the TicTacToe board. All fields are set to be EMPTY.
        """
        self.state.fill(EMPTY)

    def NumberOfEmptySpots(self):
        """"
        Returns Number Of Empty Blocks Left In The Board
        """

        return np.count_nonzero(self.state == EMPTY)

    def RandomEmptySpot(self):
        """
        Returns A Random Position (1D) On The Board
        """
        choice = int(np.random.choice(np.array([i for i in range(9) if self.state[i] == 0]), 1))
        return choice

    def LegalMove(self, pos):
        """
        Checks Whether A Given Position(1D) Is EMPTY (i.e, Can Be Played)
        :Param pos: 1D Block Number
        """

        return (0 <= pos <= BOARD_SIZE) and (self.state[pos] == EMPTY)

    def PlayerMove(self, position, side):
        """"
        Places A Piece Of Player Move (Of A Particular Side (i.e Either X or O)) At Position 'position',
        Raises A Value Exception If Position Is Not Empty
        :Param position : Location Of Move (1D)
        :Param side : Whose Turn ? (Naught or Cross)
        :Returns : The Game State After The move, The Game Result After The Move, Whether The Move Finished The Game.
        """

        if self.state[position] != EMPTY:
            raise ValueError('Invalid Move')

        self.state[position] = side

        if self.CheckWin():
            return self.state, GameState.CROSS_WIN if side == CROSS else GameState.NAUGHT_WIN, True

        if self.NumberOfEmptySpots() == 0:
            return self.state, GameState.DRAW, True

        return self.state, GameState.NOT_FINISHED, False

    @staticmethod
    def ApplyDirection(pos, direction):
        """
        Returns a 1D Position Of (When A Given Position Is Moved To The Given Direction),
        Returns -1 If A Position Is Not Valid On Board.
        :Param pos: Initial Position
        :Param direction: 2D Final Position Of The Block (i.e, (Row, Column)
        """

        row = pos // 3
        col = pos % 3

        row += direction[0]

        if row < 0 or row > 2:
            return -1

        col += direction[1]

        if col < 0 or col > 2:
            return -1

        return int(row * 3 + col)

    def CheckWinInDirection(self, pos, direction):
        """
        Checks And Returns Whether There Are Three Pieces Of Same Side In A Row (ReturnType = Boolean)
        :Param pos : The Position in 1D To Check If We Have 3 In A Row
        :Param direction : The Direction In 2D In Which To Check 3 In A Row
        """

        block_owner = self.state[pos]

        if block_owner == EMPTY:
            return False

        pos_1 = self.ApplyDirection(pos, direction)     # Moving To Next Position (1D)
        pos_2 = self.ApplyDirection(pos_1, direction)   # Moving To Next Position (1D)

        if pos_1 == -1 or pos_2 == -2:  # -2 Will Be Max Because You Have To Check With Three Strick-Throughs
            return False

        if block_owner == self.state[pos_1] and block_owner == self.state[pos_2]:  # Check If There's A StrickThrough
            return True

        return False

    def CheckWin(self):
        """
        Checks Whether If Any Side (i.e Cross Or Naught) Has Won The Game. (Return Type = Boolean)
        """

        for start_pos in self.WIN_CHECK_DIRECTORY:

            if self.state[start_pos] != EMPTY:
                for direction in self.WIN_CHECK_DIRECTORY[start_pos]:
                    result = self.CheckWinInDirection(start_pos, direction)

                    if result:
                        return True

        return False