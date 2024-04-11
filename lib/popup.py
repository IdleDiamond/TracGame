#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 2 12:21:00 2024

@author: joaking

"""

import tkinter as tk
from tkinter.ttk import *


class Popup:
    def __init__(self):
        self.main = tk.Tk()
        self.frame = Frame(self.main)

    def number_players(self):

        self.main.title("Trac Game")
        self.main.resizable(0, 0)
        self.main.geometry('200x200')
        # main.overrideredirect(1)

        self.frame.destroy()
        self.frame = Frame(self.main)

        tk.Label(self.main, text="How many player?").pack(expand = True)

        self.main.mainloop()



