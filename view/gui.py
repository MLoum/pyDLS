import tkinter as tk
from tkinter import ttk
from view.AngleTreeview import AngleTreeview
from view.InterractiveGraph import InteractiveGraph

from view.hardwareArea import HardwareArea
from view.logArea import LogArea
from view.ParamArea import ParamArea
from view.resultArea import ResultArea

class View():
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.exp_widget = [] # List of widget related to the experiment (hardware, param etc)

        self.root.protocol("WM_DELETE_WINDOW",
                           self.on_quit)  # Exit when x pressed, notice that its the name of the function 'self.handler' and not a method call self.handler()


    def on_quit(self):
        # paramFile = open('param.ini', 'w')
        # paramFile.write(self.saveDir)
        self.root.destroy()
        self.root.quit()

    def pressed_key_shortcut(self):
        pass

    def create_architecture(self):
        """:arg
        Top level etc
        """
        # 1 Menu, param, and hardware
        # self.frame_param_and_hardware = tk.LabelFrame(self.root, text="Status", borderwidth=1)
        self.frame_param_and_hardware = tk.Frame(self.root)
        self.frame_param_and_hardware.pack(side=tk.TOP, fill="both", expand=True)
        self.frame_param_and_hardware.bind("<Key>", self.pressed_key_shortcut)

        self.frame_param = tk.Frame(self.frame_param_and_hardware)
        self.frame_param.pack(side=tk.TOP, fill="both", expand=True)
        self.param_area = ParamArea(self.frame_param_and_hardware, self, self.controller)
        self.param_area.populate()

        self.frame_hardware = tk.Frame(self.frame_param_and_hardware)
        self.frame_hardware.pack(side=tk.TOP, fill="both", expand=True)
        self.hardware_area = HardwareArea(self.frame_hardware, self, self.controller)
        self.hardware_area.populate()

        self.frame_param_and_hardware.pack(side="top", fill="both", expand=True)

        # Results
        self.top_level_Results = tk.Toplevel(self.root)
        self.top_level_Results.bind("<Key>", self.pressed_key_shortcut)
        self.top_level_Results.title("Results")
        # self.frame_results = tk.LabelFrame(self.top_level_Results, text="Results",
        #                                       borderwidth=1)
        self.frame_results = tk.Frame(self.top_level_Results)
        self.result_area = ResultArea(self.frame_results, self, self.controller)
        self.result_area.populate()
        self.frame_results.pack(side="top", fill="both", expand=True)

        self.top_level_log = tk.Toplevel(self.root)
        self.top_level_log.bind("<Key>", self.pressed_key_shortcut)
        self.frame_log = tk.LabelFrame(self.top_level_log, text="Log", borderwidth=1)
        self.log_area = LogArea(self.frame_log, self, self.controller)
        self.log_area.populate()
        self.frame_log.pack(side="top", fill="both", expand=True)

    def create_widget(self):
        pass
        # self.create_exp_setup_widget()
        self.angle_treeview = AngleTreeview(self.root)
        # self.create_results_widget()

    def create_exp_setup_widget(self):
        pass

    def create_results_widget(self):
        pass


    def add_angle(self):
        # TODO
        pass


    def display_angle_selection(self):
        """
        Faire un graphe de la (les) courbe de corrélation avec le fit et les résidus
        Mettre le chi² du fit et les paramètres du fit report.
        Mettre le CONTIN de/des angles.
        :return:
        """
        pass

    def update_global_measuremnt(self):
        """
        Display la moyenne des contin / ou autre technique
        Display les résultats du global cumulant. Mettre en rouge si mu2 est trop grand.
        Est-ce qu'il y  a mieux comme technique
        :return:
        """
        pass