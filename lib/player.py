#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 21:50:13 2024

@author: joaking
"""

import pygame

class Player(pygame.sprite.Sprite):
    def __inti__(self, playerNum):
        super().__init__()
        self.playerNumber = playerNum
        self.score = 0
        self.diceInPlay = 2
