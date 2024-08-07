#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Created on Thu Feb  1 12:53:48 2024

 @author: joaking

 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science

"""
import types

# pylint: disable=invalid-name
# pylint: disable=no-member

import pygame
from lib.dice import Dice
from lib.card import Card
from lib.player import Player
from lib.windowNbPlayer import WindowNbPlayer


def check_turn_end():
    # Checks if with dice result the game is still possible

    POSSIBILITY_DICT = {12: [{9, 3}, {9, 2, 1}, {8, 4}, {8, 3, 1}, {7, 5}, {7, 3, 2}, {7, 4, 1}, {6, 5, 1}, {6, 4, 2},
                             {6, 3, 2, 1}, {5, 4, 3}],
                        11: [{9, 2}, {8, 3}, {8, 2, 1}, {7, 4}, {7, 3, 1}, {6, 5}, {6, 4, 1}, {6, 3, 2}, {5, 4, 2},
                             {5, 3, 2, 1}],
                        10: [{9, 1}, {8, 2}, {7, 3}, {7, 2, 1}, {6, 4}, {6, 3, 1}, {5, 4, 1}, {5, 3, 2}, {4, 3, 2, 1}],
                        9: [{9}, {8, 1}, {7, 2}, {6, 3}, {6, 2, 1}, {5, 4}, {5, 3, 1}, {4, 3, 2}],
                        8: [{8}, {7, 1}, {6, 2}, {5, 3}, {5, 2, 1}, {4, 3, 1}],
                        7: [{7}, {6, 1}, {5, 2}, {4, 3}, {4, 2, 1}],
                        6: [{6}, {5, 1}, {4, 2}, {3, 2, 1}],
                        5: [{5}, {4, 1}, {3, 2}],
                        4: [{4}, {3, 1}],
                        3: [{3}, {2, 1}],
                        2: [{2}],
                        1: [{1}]}

    is_turn_impossible = True
    pos_list = POSSIBILITY_DICT[diceResult]

    for countT, setPos in enumerate(pos_list):

        if setPos.issubset(set(cardsInPlay)):
            is_turn_impossible = False

    return is_turn_impossible


def turn_ending_get_score():
    turn_score = 0

    for countTE1, cardTE1 in enumerate(cardsInPlay):
        turn_score += cardTE1

    for countTE2, cardTE2 in enumerate(card_group):
        cardTE2.set_is_used(False)
        cardTE2.set_is_selected(False)

    cardsInPlay.clear()

    return turn_score


# Define message constants
MSG_TYPE = types.SimpleNamespace()
MSG_TYPE.NO_MSG = 0
MSG_TYPE.SPACE_ROLL_DICE = 1
MSG_TYPE.DICE_RESULT = 2
MSG_TYPE.PERFECT_TURN = 3
MSG_TYPE.PERFECT_GAME = 4
MSG_TYPE.PRESS_TO_CONTINUE = 5

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Constant position
MSG_POS_XY = (380, 335)
MSG_BLOCK_XY = (350, 325)
INFO_BOX_XY = (995, 30)

# Booleans
isFirstRoll = True
isDiceRolling = False
isGameDone = False
isPlayerTurn = False
isPerfectTurn = False

# variables
msgToDisplay = MSG_TYPE.SPACE_ROLL_DICE
diceResult = 0
cardsInPlay = [9, 8, 7, 6, 5, 4, 3, 2, 1]
playerScores = []
# Used for perfect turn: diceResTest[]
diceResTest = [9, 8, 7, 6, 5, 4, 3, 2, 1]


pygame.init()

# title_font = pygame.font.Font(None, 80)
msg_font = pygame.font.SysFont("garamond", 28)
score_font = pygame.font.Font('font/Pixeltype.ttf', 80)

# Set the width and height of the screen [width, height]
size = (1025, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Trac Game')
bg_surf = pygame.image.load("art/card_table.jpg").convert_alpha()
bg_surf = pygame.transform.smoothscale(bg_surf, size)

# info button
info_box = pygame.image.load("art/info_box.png").convert_alpha()
info_box_rect = info_box.get_rect(center=INFO_BOX_XY)

# Game blue message board
msg_blue_block = pygame.image.load("art/msg_block.png").convert_alpha()
msg_blue_block_rect = msg_blue_block.get_rect(topleft=MSG_BLOCK_XY)

# Groups dice
dice_group = pygame.sprite.Group()
dice_group.add(Dice(1))
dice_group.add(Dice(2))

# Call tk popup to know how many players
windowNbPlayer = WindowNbPlayer()

# Group player
player_group = pygame.sprite.Group()

for p in range(int(windowNbPlayer.nb_player)):
    player_group.add(Player(p+1))
    playerScores.append(0)

"""
#For testing only
player_group.add(Player(1))
playerScores.append(0)
player_group.add(Player(2))
playerScores.append(0)
# player_group.add(Player(3))
# playerScores.append(0)
# player_group.add(Player(4))
# playerScores.append(0)
# player_group.add(Player(5))
# playerScores.append(0)
# player_group.add(Player(6))
# playerScores.append(0)
"""

# 9 Cards, create card group sprite
card_group = pygame.sprite.Group()
for i in range(9, 0, -1):
    card_group.add(Card(i))


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Setup timers
rollTimer = pygame.USEREVENT + 1
perfectTurnTimer = pygame.USEREVENT + 2

listPlayer = iter(player_group)
currPlayer = next(listPlayer)
currPlayer.activate()

# -------- Main Program Loop ---------------------
while not isGameDone:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameDone = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not isPerfectTurn:
            if not isPlayerTurn:
                if not isDiceRolling:
                    # player press SPACE to roll dices
                    if isFirstRoll:
                        isFirstRoll = False

                    pygame.time.set_timer(rollTimer, 1000, 1)
                    isDiceRolling = True
                    isPlayerTurn = True
                    for dice in dice_group:
                        dice.set_rolling(True)
                        dice.roll()

        if event.type == rollTimer:

            # stop rolling dices
            isDiceRolling = False
            diceResult = 0
            for dice in dice_group:
                dice.set_rolling(False)
                diceResult += dice.get_dice_face()

            # Block used to create perfect turn
            # if diceResTest:
            #     diceResult = diceResTest.pop()

            msgToDisplay = MSG_TYPE.DICE_RESULT

            if check_turn_end():

                currentTurnScore = turn_ending_get_score()
                currPlayer.add_score(currentTurnScore)
                playerScores[currPlayer.get_player_number() - 1] = currPlayer.get_score()
                cardsInPlay = [9, 8, 7, 6, 5, 4, 3, 2, 1]

                print(currPlayer.get_score())

                msgToDisplay = MSG_TYPE.SPACE_ROLL_DICE
                isPlayerTurn = False

                # todo 31 just for testing
                if currPlayer.get_score() >= 31:
                    currPlayer.eliminated()
                    print(f"Player {currPlayer.get_player_number()} is eliminated")

                    checkActivePlayer = []

                    # Check if there's a winner
                    for countP, playerRem in enumerate(player_group):
                        if not playerRem.get_is_eliminated():
                            checkActivePlayer.append(playerRem)

                    if len(checkActivePlayer) == 0:
                        print("Game over")
                        isGameDone = True
                        # todo ask to replay
                        break

                    elif len(checkActivePlayer) == 1:
                        print(f"Winner is Player {checkActivePlayer[0].get_player_number()}!!")

                currPlayer.deactivate()

                # Activate next player that is not eliminated
                while True:
                    try:
                        currPlayer = next(listPlayer)

                    except StopIteration:
                        listPlayer = iter(player_group)
                        currPlayer = next(listPlayer)

                    if not currPlayer.get_is_eliminated():
                        break

                currPlayer.activate()

        if event.type == perfectTurnTimer:

            isPerfectTurn = False
            msgToDisplay = MSG_TYPE.PRESS_TO_CONTINUE
            isPlayerTurn = False
            pygame.time.set_timer(rollTimer, 1, 1)

        if event.type == pygame.MOUSEBUTTONDOWN and not isPerfectTurn:
            if not isDiceRolling:
                if info_box_rect.collidepoint(pygame.mouse.get_pos()):
                    # put code in method that reset all game information
                    # isFirstRoll = True
                    # todo info box to complete
                    pass

            if isPlayerTurn:
                for count, card in enumerate(card_group, 1):
                    if card.check_collision(pygame.mouse.get_pos()):
                        card.is_clicked()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and not isPerfectTurn:

            if isPlayerTurn and not isDiceRolling:
                cardSelection = []
                sumSelected = 0
                for count, card in enumerate(card_group):
                    if not card.get_is_used():
                        if card.get_is_selected():
                            # print(f"Value {card.get_value()}")
                            cardSelection.append(card)
                            sumSelected += card.get_value()

                if sumSelected == diceResult:
                    # print("same amount")
                    for count, card in enumerate(cardSelection):
                        card.set_is_used(True)
                        cardsInPlay.remove(card.get_value())

                    isPlayerTurn = False
                    diceResult = 0
                    msgToDisplay = MSG_TYPE.SPACE_ROLL_DICE
                    print(cardsInPlay)

                    # Is perfect turn
                    if not cardsInPlay:
                        isPerfectTurn = True
                        msgToDisplay = MSG_TYPE.PERFECT_TURN
                        pygame.time.set_timer(perfectTurnTimer, 4000, 1)

    # --- Drawing code should go here

    # table background
    screen.blit(bg_surf, (0, 0))

    dice_group.update()
    card_group.update()
    player_group.update()
    dice_group.draw(screen)
    card_group.draw(screen)
    player_group.draw(screen)

    # Display player score on board
    for countS, score in enumerate(playerScores):
        score_surf = score_font.render(f'{score}', False, (200, 200, 0))
        score_rect = score_surf.get_rect(center=(100 + (155 * countS), 85))
        screen.blit(score_surf, score_rect)

    match msgToDisplay:
        case MSG_TYPE.NO_MSG:
            pass
        case MSG_TYPE.SPACE_ROLL_DICE:
            msg_board = msg_font.render(f"Player {currPlayer.get_player_number()} press space to roll dices", False, BLACK)
            msg_board_rect = msg_board.get_rect(topleft=MSG_POS_XY)
        case MSG_TYPE.DICE_RESULT:
            msg_board = msg_font.render(f"{diceResult}", False, BLACK)
            msg_board_rect = msg_board.get_rect(topleft=MSG_POS_XY)
        case MSG_TYPE.PERFECT_TURN:
            msg_board = msg_font.render(f"Perfect Turn from player {currPlayer.get_player_number()}", False, BLACK)
            msg_board_rect = msg_board.get_rect(topleft=MSG_POS_XY)
        case MSG_TYPE.PRESS_TO_CONTINUE:
            msg_board = msg_font.render("Press space to continue", False, BLACK)
            msg_board_rect = msg_board.get_rect(topleft=MSG_POS_XY)
        case MSG_TYPE.PERFECT_GAME:
            pass

    # Display msg board, info box and message on board
    screen.blit(msg_blue_block, msg_blue_block_rect)
    screen.blit(info_box, info_box_rect)
    screen.blit(msg_board, msg_board_rect)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

    if isGameDone:
        break

# Close the window and quit.
pygame.quit()
