#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 22:31:31 2024

@author: joaking

Card pixelart from Andrew Tidey andrewtidey.blogspot.co.uk
"""

#pylint: disable=invalid-name

import pygame

CARD_X_POS = 21
CARD_Y_POS = 180

class Card(pygame.sprite.Sprite):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.isSelected = False
        self.isUsed = False
        card = pygame.image.load(f'art/cards/{value}.png').convert_alpha()
        card_selected = pygame.image.load(f'art/cards/{value}sel.png').convert_alpha()
        card_used = pygame.image.load('art/cards/used.png').convert_alpha()
        self.card_frame = (card, card_selected, card_used)
        self.image = self.card_frame[0]
        cardIndex = 10-value
        self.rect = self.image.get_rect(midleft = (CARD_X_POS+(110*(cardIndex-1)),CARD_Y_POS))


    def getIsSelected(self):
        return self.isSelected

    #not used yet
    def setIsSelected(self, value):
        self.isSelected = value

    def isClicked(self):
        if not self.isUsed:
            if self.isSelected:
                self.isSelected = False
            else:
                self.isSelected = True


    def getIsUsed(self):
        return self.isUsed

    def setIsUsed(self, value):
        self.isUsed = value

    def getValue(self):
        return self.value

    def cardAnimation(self):
        if self.isUsed:
            self.image = self.card_frame[2]
        elif self.isSelected:
            self.image = self.card_frame[1]
        else:
            self.image = self.card_frame[0]

    def checkCollision(self, pos):
        return self.rect.collidepoint(pos)

    def update(self):
        self.cardAnimation()
