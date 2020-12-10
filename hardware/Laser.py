from hardware.Device import Device
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

class Laser(Device):
    def __init__(self, main_ui):
        super().__init__(main_ui)
        self.frame_name = "Laser"
        self.is_on = False
        self.load_device()
        if self.initialized:
            pass

    def set_on_off(self, is_on):
        self.is_on = is_on

    def set_power(self, power):
        pass

    def get_power(self):
        pass

    def stop(self):
        self.set_on_off(is_on=False)

    def create_GUI(self, frame):
        self.frame = tk.LabelFrame(frame, text=self.frame_name,
                                   borderwidth=1)

        img = Image.open("./Ressource/OffSmall.png")
        self.tkimageOff = ImageTk.PhotoImage(img)
        img = Image.open("./Ressource/OnSmall.png")
        self.tkimageOn = ImageTk.PhotoImage(img)

        self.lb_on_off = ttk.Label(self.frame, image=self.tkimageOff)
        #self.lbOnOff.config(width="40", height="40")
        self.lb_on_off.bind('<Button-1>', lambda e: self.on_button_on_off())
        self.lb_on_off.grid(row=0, column=0)


        ttk.Label(self.frame, text='Power (mW)').grid(row=1, column=0)
        self.laser_power_sv = tk.StringVar(value="1")
        e = ttk.Entry(self.frame, width=12, justify=tk.CENTER, textvariable=self.laser_power_sv)
        e.config(state=tk.DISABLED)
        e.grid(row=1, column=1)

        #TODO set Power

    def on_button_on_off(self):
        if self.is_on == False:
            self.set_on_off(is_on=True)
            self.lb_on_off.configure(image=self.tkimageOn)
        else:
            self.set_on_off(is_on=False)
            self.lb_on_off.configure(image=self.tkimageOff)
