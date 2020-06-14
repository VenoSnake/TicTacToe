"""
This Python Module Handles All Graphical User Interface For The TicTacToe Game.
"""

import pygame
import Utility as U

class Screen:
    """
    Used To Instantiate A GUI Screen On Which Game Is Played
    """

    def __init__(self, width = 800, height = 800, background_color = U.Color.WHITE):
        """
        Useful Initializations Of GUI Screen Parameters Through Constructor
        :Param width : Width Of The GUI Screen
        :Param height : Height Of The GUI Screen
        :Param background_color : Background Color Of GUI Screen
        """

        self.width = width
        self.height = height
        self.background_color = background_color
        self.screen = pygame.display.set_mode((width, height))
        self.offset = self.width / 12.7

    def RefreshBackground(self):
        """
        Refreshes Background, Although At Present There Is No Particular Use, I Used It For Some Debugging Process.
        """

        self.screen.fill(self.background_color)

    def DrawBackground(self):
        """
        Draws The Empty Board Sub-Background Layer
        """

        pygame.draw.line(self.screen, U.Color.WHITE, (0, (self.height - 100)/3 + 100), (self.width, (self.height - 100)/3 + 100))
        pygame.draw.line(self.screen, U.Color.WHITE, (0, 2 * ((self.height - 100)/3) + 100), (self.width, 2 * ((self.height - 100)/3) + 100))
        pygame.draw.line(self.screen, U.Color.WHITE, (self.width/3, 100), (self.width/3, self.height))
        pygame.draw.line(self.screen, U.Color.WHITE, (2 * (self.width/3), 100), (2 * (self.width/3), self.height))

    def DrawCross(self, block_pos):
        """
        Draws A Cross When A X-Player Picks A Move On The GUI
        :Param block_pos : Centroid Of The Block Clicked
        """

        pygame.draw.line(self.screen, U.Color.WHITE, (block_pos[0] + (self.width / 6) - self.offset, block_pos[1] - ((self.height - 100) / 6) + self.offset), (block_pos[0] - (self.width / 6) + self.offset, block_pos[1] + ((self.height - 100) / 6) - self.offset), 2)
        pygame.draw.line(self.screen, U.Color.WHITE, (block_pos[0] - (self.width / 6) + self.offset, block_pos[1] - ((self.height - 100) / 6) + self.offset), (block_pos[0] + (self.width / 6) - self.offset, block_pos[1] + ((self.height - 100) / 6) - self.offset), 2)

    def DrawNaught(self, block_pos):
        """
        Draws A Cross When A O-Player Picks A Move On The GUI
        :Param block_pos : Centroid Of The Block Clicked
        """

        pygame.draw.circle(self.screen, U.Color.WHITE, block_pos, (self.width / 6) - self.offset, 2)

    def ShowBoard(self):
        """
        Updates The GUI After Every Move, Holds The Background
        """

        self.DrawBackground()
        pygame.display.update()