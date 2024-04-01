#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 22:32:42 2024

@author: joaking

Dice pixelart by JamesWhite
"""

# pylint: disable=invalid-name

from random import randint
import pygame

FIRST_DICE_X = 160
SECOND_DICE_X = 220
DICES_Y = 410


class Dice(pygame.sprite.Sprite):
    def __init__(self, dice_number):
        super().__init__()
        dice_1 = pygame.image.load('art/dice/dice_1.png').convert_alpha()
        dice_2 = pygame.image.load('art/dice/dice_2.png').convert_alpha()
        dice_3 = pygame.image.load('art/dice/dice_3.png').convert_alpha()
        dice_4 = pygame.image.load('art/dice/dice_4.png').convert_alpha()
        dice_5 = pygame.image.load('art/dice/dice_5.png').convert_alpha()
        dice_6 = pygame.image.load('art/dice/dice_6.png').convert_alpha()

        self.diceFace = 0
        self.diceNumber = dice_number
        self.isRolling = False
        self.frames = (dice_1, dice_2, dice_3, dice_4, dice_5, dice_6)
        self.image = self.frames[self.diceFace]

        if self.diceNumber == 1:
            self.rect = self.image.get_rect(midbottom=(FIRST_DICE_X, DICES_Y))
        else:
            self.rect = self.image.get_rect(midbottom=(SECOND_DICE_X, DICES_Y))

    def show(self):
        self.image = self.frames[self.diceFace]

    def roll(self):
        # Result from rolling the dice
        self.diceFace = randint(0, 5)

    def get_dice_face(self):
        return self.diceFace + 1

    def set_dice_face(self, value):
        self.diceFace = value - 1

    def dice_animation(self):
        if self.isRolling:
            rolling_face = randint(0, 5)
            self.image = self.frames[rolling_face]
        else:
            self.show()

    def set_rolling(self, rolling):
        self.isRolling = rolling

    def get_is_rolling(self):
        return self.isRolling

    def get_dice_number(self):
        return self.diceNumber

    def update(self):
        self.dice_animation()
