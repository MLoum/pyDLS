import tkinter as tk
from tkinter import ttk
from view.AngleTreeview import AngleTreeview

class View():
    def __init__(self):
        self.root = tk.Tk()
        self.create_widget()

        self.exp_widget = [] # List of widget related to the experiment (hardware, param etc)
        self.root.protocol("WM_DELETE_WINDOW",
                           self.on_quit)  # Exit when x pressed, notice that its the name of the function 'self.handler' and not a method call self.handler()

    def on_quit(self):
        # paramFile = open('param.ini', 'w')
        # paramFile.write(self.saveDir)
        self.root.destroy()
        self.root.quit()

    def create_widget(self):
        self.create_exp_setup_widget()
        self.angle_treeview = AngleTreeview(self.root)
        self.create_results_widget()

    def create_exp_setup_widget(self):
        self.frame_exp_setup = tk.LabelFrame(self.root, text="Exp setup",
                                               borderwidth=1)
        # self.frame_result_text.grid(row=0, column=0)
        self.frame_exp_setup.pack(side=tk.TOP, fill="both", expand=True)
        self.frame_exp_param = tk.LabelFrame(self.frame_exp_setup, text="Exp setup",
                                               borderwidth=1)

        ttk.Label(self.frame_exp_param, text='Angle Start:').grid(row=0, column=0)
        self.angle_start_sv = tk.StringVar(15)
        e = ttk.Entry(self.frame_exp_param, width=12, justify=tk.CENTER, textvariable=self.angle_start_sv)
        e.grid(row=0, column=1)
        self.exp_widget.append(e)

        ttk.Label(self.frame_exp_param, text='Angle Stop:').grid(row=1, column=0)
        self.angle_stop_sv = tk.StringVar(150)
        e = ttk.Entry(self.frame_exp_param, width=12, justify=tk.CENTER, textvariable=self.angle_stop_sv)
        e.grid(row=1, column=1)
        self.exp_widget.append(e)

        ttk.Label(self.frame_exp_param, text='Nb Angle:').grid(row=2, column=0)
        self.angle_nb_sv = tk.StringVar(10)
        e = ttk.Entry(self.frame_exp_param, width=12, justify=tk.CENTER, textvariable=self.angle_nb_sv)
        e.grid(row=2, column=1)
        self.exp_widget.append(e)

        ttk.Label(self.frame_exp_param, text='Time per point (s):').grid(row=0, column=3)
        self.time_per_point_sv = tk.StringVar(10)
        e = ttk.Entry(self.frame_exp_param, width=12, justify=tk.CENTER, textvariable=self.time_per_point_sv)
        e.grid(row=0, column=4)
        self.exp_widget.append(e)

        ttk.Label(self.frame_exp_param, text='Nb Photons per point:').grid(row=1, column=3)
        self.nb_photon_per_point_sv = tk.StringVar(1000000)
        e = ttk.Entry(self.frame_exp_param, width=12, justify=tk.CENTER, textvariable=self.nb_photon_per_point_sv)
        e.grid(row=1, column=4)
        self.exp_widget.append(e)

        self.frame_exp_param.pack(side=tk.LEFT, fill="both", expand=True)

        self.frame_exp_cmd = tk.LabelFrame(self.frame_exp_setup, text="Exp commands",
                                               borderwidth=1)

        b = ttk.Button(self.frame_exp_cmd, text="Start", width=15, command=self.start_exp)
        b.grid(row=0,column=0)
        self.exp_widget.append(b)
        b = ttk.Button(self.frame_exp_cmd, text="Stop", width=15, command=self.stop_exp)
        b.grid(row=0,column=1)
        self.exp_widget.append(b)

        self.frame_exp_cmd.pack(side=tk.LEFT, fill="both", expand=True)

        # Hardware configuration
        self.frame_hardware = tk.LabelFrame(self.root, text="Hardware", borderwidth=1)
        self.frame_hardware.pack(side=tk.TOP, fill="both", expand=True)

        self.frame_rotation_stage = tk.LabelFrame(self.frame_hardware, text="Rotation Stage",
                                               borderwidth=1)
        self.frame_rotation_stage.pack(side=tk.LEFT, fill="both", expand=True)

        ttk.Label(self.frame_rotation_stage, text='Current Angle :').grid(row=0, column=0)
        self.current_angle_sv = tk.StringVar(0)
        e = ttk.Entry(self.frame_rotation_stage, width=12, justify=tk.CENTER, textvariable=self.current_angle_sv)
        e.grid(row=0, column=1)
        self.exp_widget.append(e)

        ttk.Label(self.frame_rotation_stage, text='Speed (unit) :').grid(row=1, column=0)
        self.speed_angle_sv = tk.StringVar(1)
        e = ttk.Entry(self.frame_rotation_stage, width=12, justify=tk.CENTER, textvariable=self.speed_angle_sv)
        e.grid(row=1, column=1)
        self.exp_widget.append(e)

        self.frame_couting_card = tk.LabelFrame(self.frame_hardware, text="Couting card",
                                               borderwidth=1)
        self.frame_couting_card.pack(side=tk.LEFT, fill="both", expand=True)

        ttk.Label(self.frame_couting_card, text='Current Angle :').grid(row=0, column=0)
        self.current_angle_sv = tk.StringVar(0)
        e = ttk.Entry(self.frame_rotation_stage, width=12, justify=tk.CENTER, textvariable=self.current_angle_sv)
        e.grid(row=0, column=1)
        self.exp_widget.append(e)

        self.frame_detectors = tk.LabelFrame(self.frame_hardware, text="Detectors",
                                               borderwidth=1)
        self.frame_detectors.pack(side=tk.LEFT, fill="both", expand=True)

        self.frame_laser = tk.LabelFrame(self.frame_hardware, text="Laser",
                                               borderwidth=1)
        self.frame_laser.pack(side=tk.LEFT, fill="both", expand=True)

    def create_results_widget(self):
        self.frame_results = tk.LabelFrame(self.root, text="Exp setup",
                                             borderwidth=1)
        # self.frame_result_text.grid(row=0, column=0)
        self.frame_results.pack(side=tk.TOP, fill="both", expand=True)

        self.frame_global_results = tk.LabelFrame(self.frame_results, text="Global results",
                                             borderwidth=1)
        self.frame_global_results.pack(side=tk.LEFT, fill="both", expand=True)

        self.frame_global_results_cumulant = tk.LabelFrame(self.frame_global_results, text="Cumulants",
                                             borderwidth=1)
        self.frame_global_results_cumulant.pack(side=tk.LEFT, fill="both", expand=True)

        ttk.Label(self.frame_global_results_cumulant, text='Mean size (nm) :').grid(row=0, column=0)
        self.global_mean_size_cumulant_sv = tk.StringVar(0)
        e = ttk.Entry(self.frame_rotation_stage, width=12, justify=tk.CENTER, textvariable=self.global_mean_size_cumulant_sv)
        e.grid(row=0, column=1)

        ttk.Label(self.frame_global_results_cumulant, text='µ2 / % :').grid(row=0, column=0)
        self.global_mu2_cumulant_sv = tk.StringVar(0)
        e = ttk.Entry(self.frame_rotation_stage, width=12, justify=tk.CENTER, textvariable=self.global_mu2_cumulant_sv)
        e.grid(row=0, column=1)



        self.frame_global_results_contin = tk.LabelFrame(self.frame_global_results, text="CONTIN",
                                             borderwidth=1)

    def start_exp(self):
        pass

    def stop_exp(self):
        pass

    def add_angle(self):
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