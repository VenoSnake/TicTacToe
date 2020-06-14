"""
This Python Module Is The Main Function Which Handles All Events And Calls Other Methods Of Their Respective Classes.
"""

import sys
import pygame
import Utility as U
from Screen import Screen
from TicTacToe import TicTacToe, NAUGHT, CROSS

def PlayGame(ScreenObj, TTTObj):

    game_over = False
    centroids = U.Operations.TTTCentroid(ScreenObj.width, ScreenObj.height)
    turn = CROSS
    game_state = None
    result = None

    while not game_over:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                dist = []
                for val in centroids:
                    dist.append(U.Operations.Distance(val, event.pos))
                block_pos = dist.index(min(dist))

                if turn == CROSS:
                    ScreenObj.DrawCross(centroids[block_pos])

                if turn == NAUGHT:
                    ScreenObj.DrawNaught(centroids[block_pos])

                game_state, result, game_over = TTTObj.PlayerMove(block_pos, turn)
                turn = TTTObj.NextTurn(turn)

        ScreenObj.ShowBoard()

    return result

if __name__ == "__main__":

    pygame.init()
    display = Screen()
    game = TicTacToe()
    Winner = PlayGame(display, game)
    print('\n Winner : ', Winner)