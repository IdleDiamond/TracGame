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
        """ Initializes all face images, sets starting face to 1, rolling to False and dice placement on canvas
        is dependent on which dice number it is, either 1 or 2 there's no 3rd dice

        @param dice_number: Number of the actual dice (Not face value)
        """
        super().__init__()
        dice_1 = pygame.image.load('art/dice/dice_1.png').convert_alpha()
        dice_2 = pygame.image.load('art/dice/dice_2.png').convert_alpha()
        dice_3 = pygame.image.load('art/dice/dice_3.png').convert_alpha()
        dice_4 = pygame.image.load('art/dice/dice_4.png').convert_alpha()
        dice_5 = pygame.image.load('art/dice/dice_5.png').convert_alpha()
        dice_6 = pygame.image.load('art/dice/dice_6.png').convert_alpha()

        self._diceFace = 0
        self.diceNumber = dice_number
        self.isRolling = False
        self.frames = (dice_1, dice_2, dice_3, dice_4, dice_5, dice_6)
        self.image = self.frames[self._diceFace]

        if self.diceNumber == 1:
            self.rect = self.image.get_rect(midbottom=(FIRST_DICE_X, DICES_Y))
        else:
            self.rect = self.image.get_rect(midbottom=(SECOND_DICE_X, DICES_Y))

    def show(self):
        """ Sets self.image to frame representing the correct dice value

        @return: None
        """
        self.image = self.frames[self._diceFace]

    def roll(self):
        """ Random result for rolling the dice, change diceFace value

        @return: None
        """
        self._diceFace = randint(0, 5)

    @property
    def diceFace(self):
        """ Returns dice value for game: adds 1 to diceFace to get correct dice value (diceFace is from  0 to 5)

        @return: Integer
        """
        return self._diceFace + 1

    @diceFace.setter
    def diceFace(self, number):
        """ Sets diceFace value: must be from 0 to 5
        This method is only used by __init__

        @param number: Inter
        @return: None
        """
        self._diceFace = number

    def update(self):
        """ If isRolling True, then self.image will be set to different faces to mimic rolling, if not then
        will just show the current face of dice
        Overrides method in Sprite class

        @return: None
        """
        if self.isRolling:
            rolling_face = randint(0, 5)
            self.image = self.frames[rolling_face]
        else:
            self.show()
