#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 21:50:13 2024

@author: joaking

"""

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, playerNum):
        super().__init__()
        self.playerNumber = playerNum
        self.score = 0
        self.reducedDice = False
        self.image = pygame.image.load(f"art/player/player{self.playerNumber}.png").convert_alpha()
        self.rect = self.image.get_rect(midleft = (20,50))

    def update(self):
        pass
