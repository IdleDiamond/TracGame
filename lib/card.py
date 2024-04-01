#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 22:31:31 2024

@author: joaking

Card pixelart from Andrew Tidey andrewtidey.blogspot.co.uk
"""

# pylint: disable=invalid-name

import pygame

CARD_X_POS = 21
CARD_Y_POS = 190


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
        card_index = 10-value
        self.rect = self.image.get_rect(midleft=(CARD_X_POS+(110*(card_index-1)), CARD_Y_POS))

    def get_is_selected(self):
        return self.isSelected

    def set_is_selected(self, value):
        self.isSelected = value

    def is_clicked(self):
        if not self.isUsed:
            if self.isSelected:
                self.isSelected = False
            else:
                self.isSelected = True

    def get_is_used(self):
        return self.isUsed

    def set_is_used(self, value):
        self.isUsed = value

    def get_value(self):
        return self.value

    def card_animation(self):
        if self.isUsed:
            self.image = self.card_frame[2]
        elif self.isSelected:
            self.image = self.card_frame[1]
        else:
            self.image = self.card_frame[0]

    def check_collision(self, pos):
        return self.rect.collidepoint(pos)

    def update(self):
        self.card_animation()
