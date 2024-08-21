#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 21:50:13 2024

@author: joaking

Player pixelart from "Puddin - 8 Bit Personalized Alphabet (Only Letters)"

"""

import pygame, copy

PLAYER_X_POS = 35
PLAYER_Y_POS = 30


class Player(pygame.sprite.Sprite):

    ACTIVE = 0
    INACTIVE = 1
    ELIMINATED = 2

    def __init__(self, player_num):
        """ Player instance: Starting frame is "inactive", position is determined using parameter player_num
        Attributes
        - playerNumber : Integer - Numerical number of player
        - penalty : Integer - Player penalty amount
        - isReducedDice : Boolean - if playing with fewer dices
        - isActivePlayer : Boolean - if player is currently active
        - isEliminated : Boolean - if player is eliminated from game
        - playerFrame : List - List of possible images for player (active, inactive, eliminated)
        - image : Image from Sprite class
        - rect : Rectangle from Sprite class

        @param player_num: Integer
        """
        super().__init__()
        self.playerNumber = player_num
        self.penalty = 0
        self.isReducedDice = False
        self.isActivePlayer = False
        self.isEliminated = False
        player_active = pygame.image.load(f"art/player/player{self.playerNumber}.png").convert_alpha()
        player_inactive = pygame.image.load(f"art/player/player{self.playerNumber}inactive.png").convert_alpha()
        player_eliminated = pygame.image.load(f"art/player/player{self.playerNumber}eliminated.png").convert_alpha()
        self.playerFrame = (player_active, player_inactive, player_eliminated)
        self.image = self.playerFrame[1]
        self.rect = self.image.get_rect(midleft=(PLAYER_X_POS + (155 * (self.playerNumber - 1)), PLAYER_Y_POS))

    @classmethod
    def surface_copy_player(cls, args):
        """ Will return a copy of received player argument, but only copies the player number and penalty amount

        @param args: Player to copy
        @return: New player instance (copies only player number and penalty amount)
        """
        x = cls(args.playerNumber)
        x.penalty = args.penalty
        return x


    def status(self):
        """ Will return an int if player is active(0), inactive(1) or eliminate(2)

        @return: Integer
        """
        if self.isActivePlayer:
            return Player.ACTIVE
        elif self.isEliminated:
            return Player.ELIMINATED
        else:
            return Player.INACTIVE

    # def get_player_number(self):
    #     return self.playerNumber
    #
    # def get_score(self):
    #     return self.score
    #
    # def get_is_reduced_dice(self):
    #     return self.isReducedDice
    #
    # def get_is_eliminated(self):
    #     return self.isEliminated

    def activate(self):
        """ This will change the status of the player to active

        @return: None
        """
        self.isActivePlayer = True

    def deactivate(self):
        """ This will change the status of the player to inactive

        @return: None
        """
        self.isActivePlayer = False

    def eliminated(self):
        """ This will change the status of the player to eliminated

        @return: None
        """
        self.isEliminated = True

    def add_penalty(self, penalty_amount):
        """ Will add value to the current penalty of the player

        @param penalty_amount: Integer
        @return: None
        """
        self.penalty += penalty_amount

    def update(self):
        """ Will determine the status of the player and pick the correct frame from the playerFrame[]
        Overrides method in Sprite class

        @return: None
        """
        self.image = self.playerFrame[self.status()]
