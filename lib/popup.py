#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 2 12:21:00 2024

@author: joaking

"""

import tkinter as tk
from tkinter import ttk


class WindowNbPlayer:

    def set_player(self, p_value):
        self.nb_player = p_value

    def close_popup(self):
        self.main.destroy()

    def __init__(self):
        self.nb_player = 1
        self.show_popup()

    def show_popup(self):
        self.main = tk.Tk()
        width_window = 300
        height_window = 125
        width_monitor = self.main.winfo_screenmmwidth()
        height_monitor = self.main.winfo_screenheight()

        x_win = int((height_monitor / 1.35))
        y_win = int((width_monitor / 2) + height_window)

        self.main.geometry(f"{width_window}x{height_window}+{x_win}+{y_win}")
        self.main.overrideredirect(True)

        title_bar = tk.Frame(self.main, bg='gray', relief='raised', bd=2)
        title_bar.pack(fill=tk.X)

        title_label = tk.Label(title_bar, text="Trac Game", bg='gray', fg='white')
        title_label.pack(side=tk.LEFT, padx=10)

        def move_window(event):
            self.main.geometry(f'+{event.x_root}+{event.y_root}')

        title_bar.bind('<B1-Motion>', move_window)

        tk.Label(self.main, text="How many player?").pack()

        v_list = [1, 2, 3, 4, 5, 6]
        combo = ttk.Combobox(self.main, values=v_list)
        combo.set("1")
        combo.pack(padx=10, pady=5)

        tk.Button(self.main, text="Play", command=lambda: [self.set_player(combo.get()),
                                                           self.close_popup()]).pack(padx=10, pady=10)

        self.main.mainloop()
