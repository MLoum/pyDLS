from hardware.Device import Device
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk


class Detectors(Device):
    def __init__(self, main_ui):
        super().__init__(main_ui)
        self.frame_name = "Detectors"

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

    def create_GUI(self):
        pass
