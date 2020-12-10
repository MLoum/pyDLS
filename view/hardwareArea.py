import tkinter as tk
from tkinter import ttk

class HardwareArea():
    def __init__(self, master_frame, view, controller):
        self.master_frame = master_frame
        self.view = view
        self.controller = controller

    def populate(self):
        # Hardware configuration
        self.controller.rotation_stage.create_GUI(self.master_frame)
        self.controller.rotation_stage.frame.pack(side=tk.LEFT, fill="both", expand=True)

        self.controller.laser.create_GUI(self.master_frame)
        self.controller.laser.frame.pack(side=tk.LEFT, fill="both", expand=True)

        # TODO counting card, detectors