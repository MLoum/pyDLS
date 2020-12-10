from hardware.Device import Device
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk


class CountingCard(Device):
    def __init__(self, main_ui):
        super().__init__(main_ui)
        self.frame_name = "Counting Card"

    def set_time_tag_file(self, file_path):
        pass

    def time_tag(self):
        pass

    def stop(self):
        pass

    def clear(self):
        pass

    def select_time_tag_file(self):
        pass

    def start(self):
        pass


    def create_GUI(self, frame):
        self.frame = tk.LabelFrame(frame, text=self.frame_name,
                                   borderwidth=1)

        img = Image.open("./Ressource/OffSmall.png")
        self.tkimage_off = ImageTk.PhotoImage(img)
        img = Image.open("./Ressource/OnSmall.png")
        self.tkimage_on = ImageTk.PhotoImage(img)
        img = Image.open("./Ressource/chooseFile.png")
        self.tkimage_open = ImageTk.PhotoImage(img)

        ttk.Label(self.frame, text='File Path').grid(row=0, column=0)

        self.file_path_sv = tk.StringVar(value="test.ttt")
        e = ttk.Entry(self.frame, textvariable=self.file_path_sv, justify=tk.CENTER, width=7).grid(row=0, column=1)
        # e.configure(state='readonly')

        tk.Button(self.frame, text='Open', image=self.tkimage_open, command=self.select_time_tag_file).grid(row=0, column=2)

        tk.Button(self.frame, text='Clear', command=self.clear).grid(row=0, column=3)
        tk.Button(self.frame, text='Start', command=self.start).grid(row=0, column=4)
        tk.Button(self.frame, text='Stop', command=self.stop).grid(row=0, column=5)

        self.label_LED_busy = ttk.Label(self.frame, image=self.tkimage_off)
        self.label_LED_busy.grid(row=0, column=6)
