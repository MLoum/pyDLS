from hardware.Device import Device
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import time

class RotationStage(Device):
    def __init__(self, main_ui):
        super().__init__(main_ui)
        self.frame_name = "Rotation Stage"
        self.angle_deg = 0  # Current position
        self.step_angle = 0
        self.angle_speed = 10
        self.load_device()
        if self.initialized:
            pass

    def get_position(self):
        pass

    def move_absolute(self, angle_deg):
        pass

    def move_relative(self, angle_deg):
        #TODO negative angle means  anti-clockwise
        pass

    def move(self, mode, angle_deg):

        if self.is_busy():
            #ignore command
            threading.Thread(target=self.blinkLED_ignored).start()
            return

        if mode == "absolute":
            self.angle_deg = angle_deg
            self.move_absolute(angle_deg)

        elif mode == "relative":
            self.move_relative(angle_deg)
            self.angle_deg += angle_deg

        self.label_led_moving.configure(image=self.tkimageLEDGreenOn)
        self.wait_for_device()
        self.label_led_moving.configure(image=self.tkimageLEDGreenOff)


    def blinkLED_ignored(self):
        self.label_led_ignored.configure(image=self.tkimageLEDRedOn)
        time.sleep(0.2)
        self.label_led_ignored.configure(image=self.tkimageLEDRedOff)

    def wait_for_device(self):
        pass

    def set_home(self, angle_deg):
        pass

    def go_home(self):
        pass

    def set_speed(self):
        pass

    def get_speed(self):
        pass

    def stop(self):
        pass

    def launch_move(self, mode, angle_deg):
        """
        THREAD !!
        """
        self.move_thread = threading.Thread(name='Rotation_stage', target=self.move, args=(mode, angle_deg))
        self.move_thread.start()

    def move_left(self, angle_deg):
        self.launch_move(mode="relative", angle_deg=-self.step_angle)

    def move_right(self, angle_deg):
        self.launch_move(mode="relative", angle_deg=self.step_angle)

    def create_GUI(self, frame):
        self.frame = tk.LabelFrame(frame, text=self.frame_name,
                                   borderwidth=1)

        label = ttk.Label(self.frame, text='Current Position (°))')
        label.grid(row=0, column=0)
        self.current_angle_sv = tk.StringVar()
        #TODO bold
        e = ttk.Entry(self.frame, textvariable=self.current_angle_sv, justify=tk.CENTER, width=12)
        e.bind('<Return>', lambda e: self.get_GUI_params())
        e.grid(row=0, column=1)
        e.config(state=tk.DISABLED)
        self.current_angle_sv.set('0.5')

        img = Image.open("./Ressource/flecheLeft.png")
        self.tkimageLeftArrow = ImageTk.PhotoImage(img)
        b = tk.Button(self.frame, image=self.tkimageLeftArrow, command=self.move_left)
        b.config(width="40", height="40")
        b.grid(row=1, column=0)

        img = Image.open("./Ressource/flecheRight.png")
        self.tkimageRightArrow = ImageTk.PhotoImage(img)
        b = tk.Button(self.frame, image=self.tkimageRightArrow, command=self.move_right)
        b.config(width="40", height="40")
        b.grid(row=1, column=1)

        label = ttk.Label(self.frame, text='Step (°) : ')
        label.grid(row=1, column=2)
        self.step_angle_sv = tk.StringVar()
        e = ttk.Entry(self.frame, textvariable=self.step_angle_sv, justify=tk.CENTER, width=7)
        e.bind('<Return>', lambda e: self.get_GUI_params())
        e.grid(row=1, column=3)
        self.step_angle_sv.set('0.5')

        ttk.Button(self.frame, text="Go to", width=15, command=self.goto_angle).grid(row=2, column=0)

        self.angle_goto_sv = tk.StringVar(value="0")
        e = ttk.Entry(self.frame, width=12, justify=tk.CENTER, textvariable=self.angle_goto_sv)
        e.grid(row=2, column=1)

        label = ttk.Label(self.frame, text='Speed (°/s)')
        label.grid(row=4, column=0)
        self.speed_angle_sv = tk.StringVar()
        e = ttk.Entry(self.frame, textvariable=self.speed_angle_sv, justify=tk.CENTER, width=7)
        e.bind('<Return>', lambda e: self.get_GUI_params())
        e.grid(row=4, column=1)
        self.speed_angle_sv.set('10')

        img = Image.open("./Ressource/led-green-off.png")
        self.tkimageLEDGreenOff = ImageTk.PhotoImage(img)
        img = Image.open("./Ressource/led-green-on.png")
        self.tkimageLEDGreenOn = ImageTk.PhotoImage(img)

        img = Image.open("./Ressource/led-red-off.png")
        self.tkimageLEDRedOff = ImageTk.PhotoImage(img)
        img = Image.open("./Ressource/led-red-on.png")
        self.tkimageLEDRedOn = ImageTk.PhotoImage(img)

        self.label_led_moving = ttk.Label(self.frame, image=self.tkimageLEDGreenOff)
        self.label_led_moving.grid(row=5, column=0)

        self.label_led_ignored = ttk.Label(self.frame, image=self.tkimageLEDGreenOff)
        self.label_led_ignored.grid(row=5, column=1)

        #TODO Stop sign
        b = tk.Button(self.frame, text="STOP !", command=self.stop)
        b.grid(row=6, column=0)

    def get_GUI_params(self):
        self.step_angle = float(self.step_angle_sv.get())
        self.angle_speed = float(self.speed_angle_sv.get())

    def goto_angle(self):
        angle = float(self.angle_goto_sv.get())
        self.launch_move(mode="absolute", angle_deg=angle)

