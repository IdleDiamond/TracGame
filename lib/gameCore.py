#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 Created on Wed Aug 28 12:25 2024

 @author: joaking

 OOP for game core structure. This class object will be created and used by tracGame.py

"""

import pygame

from card import Card
from dice import Dice
from player import Player

class GameCore (pygame.sprite.Sprite):

    def __init__(self, nb_player):
        """ Initialize main game instance. Receives number of players

        @param nb_player: Integer
        """
        super.__init__()
        self.nb_player = nb_player

        # Create both dices, sprite group
        self.dice_group = pygame.sprite.Group()
        self.dice_group.add(Dice(1))
        self.dice_group.add(Dice(2))

        # Create player sprite group
        self.player_group = pygame.sprite.Group()
        self.playerPenalty = []

        for p in range(self.nb_player):
            self.player_group.add(Player(p + 1))
            self.playerPenaltyplayerPenalty.append(0)

        # 9 Cards, create card group sprite
        self.card_group = pygame.sprite.Group()
        for i in range(9, 0, -1):
            self.card_group.add(Card(i))

        # Create iteration for player list
        self.listPlayer = iter(self.player_group)
        self.currPlayer = next(self.listPlayer)
        self.currPlayer.activate()

    def process_events(self):
        """ Process all game events

        @return: Boolean
        """

        return None

    def display_frame(self, screen):
        """

        @param screen: Screen from pygame to display game
        @return: None
        """
        pass


    def update(self):
        pass

