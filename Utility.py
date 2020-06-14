"""
This Python Module Is A Utility Library Which Other Classes Use.
"""

import math

class Color:
    """
    A Utility Class Which Holds All The RGB Values For Different Color's
    """

    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

class Operations:
    """
    A Utility Class Which Perform Certain User Defined Mathematical Operations
    """

    @staticmethod
    def Distance(coor_1, coor_2):
        """
        Returns The Distance Between Two Points, Used Internally To Find Which Block Was Clicked With Reference
        To The Clicked Pos ANd Centroid Of Block Distance
        :Param coor_1 : Co-ordinate 1, (x1, y1)
        :Param coor_2 : Co-ordinate 2, (x2, y2)
        """

        return math.sqrt(((coor_1[0] - coor_2[0]) ** 2) + ((coor_1[1] - coor_2[1]) ** 2))

    @staticmethod
    def TTTCentroid(width, height):
        """
        Returns An Array Of Centroid's Co-ordinate For Each Block In The TicTacToe Board.
        :Param width : Width In Terms Of Pixels Of The DISPLAY SCREEN
        :Param height : Height In Terms Of Pixels Of The DISPLAY SCREEN
        """

        centroid = []
        for i in range(1, 7, 2):
            y_coor = round(100 + (i * ((height - 100) / 6)), 2)
            for j in range(1, 7, 2):
                centroid.append((round(j * (width / 6), 2), y_coor))

        return centroid