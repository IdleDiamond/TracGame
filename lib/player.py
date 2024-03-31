#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 21:50:13 2024

@author: joaking

"""

import pygame

PLAYER_X_POS = 35
PLAYER_Y_POS = 30

class Player(pygame.sprite.Sprite):
    def __init__(self, playerNum):
        super().__init__()
        self.playerNumber = playerNum
        self.score = 0
        self.isReducedDice = False
        self.isActivePlayer = False
        self.isEliminated = False
        playerActive = pygame.image.load(f"art/player/player{self.playerNumber}.png").convert_alpha()
        playerInactive = pygame.image.load(f"art/player/player{self.playerNumber}inactive.png").convert_alpha()
        self.playerFrame = (playerInactive, playerActive)
        self.image = self.playerFrame[1]
        self.rect = self.image.get_rect(midleft = (PLAYER_X_POS + (155 * (self.playerNumber -1 )), PLAYER_Y_POS))

    def getPlayerNumber(self):
        return self.playerNumber

    def getScore(self):
        return self.score

    def getIsReducedDice(self):
        return self.isReducedDice

    def getIsActivePlayer(self):
        return self.isActivePlayer

    def getIsEliminated(self):
        return self.isEliminated

    def activate(self):
        self.isActivePlayer = True

    def deactivate(self):
        self.isActivePlayer = False

    def eliminated(self):
        self.isEliminated = True

    def addScore(self, scoreValue):
        self.score += scoreValue


    def update(self):
        self.image = self.playerFrame[self.isActivePlayer]
        return

