import tkinter as tk
from tkinter import ttk

class ParamArea():
    def __init__(self, master_frame, view, controller):
        self.master_frame = master_frame
        self.view = view
        self.controller = controller

    def populate(self):

        self.frame_exp_params = tk.LabelFrame(self.master_frame, text="Exp Params",
                                           borderwidth=1)

        ttk.Label(self.frame_exp_params, text='Main Exp name:').grid(row=0, column=0)
        self.main_exp_name_sv = tk.StringVar(value="15")
        e = ttk.Entry(self.frame_exp_params, width=50, justify=tk.CENTER, textvariable=self.main_exp_name_sv)
        e.grid(row=0, column=1)

        ttk.Label(self.frame_exp_params, text='Angle Start:').grid(row=1, column=0)
        self.angle_start_sv = tk.StringVar(value="15")
        e = ttk.Entry(self.frame_exp_params, width=12, justify=tk.CENTER, textvariable=self.angle_start_sv)
        e.grid(row=1, column=1)

        ttk.Label(self.frame_exp_params, text='Angle Stop:').grid(row=2, column=0)
        self.angle_stop_sv = tk.StringVar(value="150")
        e = ttk.Entry(self.frame_exp_params, width=12, justify=tk.CENTER, textvariable=self.angle_stop_sv)
        e.grid(row=2, column=1)

        ttk.Label(self.frame_exp_params, text='Nb Angle:').grid(row=3, column=0)
        self.angle_nb_sv = tk.StringVar(value="10")
        e = ttk.Entry(self.frame_exp_params, width=12, justify=tk.CENTER, textvariable=self.angle_nb_sv)
        e.grid(row=3, column=1)

        ttk.Label(self.frame_exp_params, text='Time per point (s):').grid(row=4, column=0)
        self.time_per_point_sv = tk.StringVar(value="10")
        e = ttk.Entry(self.frame_exp_params, width=12, justify=tk.CENTER, textvariable=self.time_per_point_sv)
        e.grid(row=4, column=1)


        ttk.Label(self.frame_exp_params, text='Nb Photons per point:').grid(row=5, column=0)
        self.nb_photon_per_point_sv = tk.StringVar(value="1000000")
        e = ttk.Entry(self.frame_exp_params, width=12, justify=tk.CENTER, textvariable=self.nb_photon_per_point_sv)
        e.grid(row=5, column=1)

        self.frame_exp_params.pack(side=tk.LEFT, fill="both", expand=True)

        self.frame_exp_cmd = tk.LabelFrame(self.master_frame, text="Exp commands",
                                           borderwidth=1)

        # TODO Séparer DLS and SLS
        b = ttk.Button(self.frame_exp_cmd, text="Start", width=15, command=self.start_exp)
        b.grid(row=0, column=0)

        b = ttk.Button(self.frame_exp_cmd, text="Stop", width=15, command=self.stop_exp)
        b.grid(row=0, column=1)

        self.frame_exp_cmd.pack(side=tk.LEFT, fill="both", expand=True)

    def start_exp(self):

        exp_param = {}
        exp_param["theta_nb_step"] = int(self.angle_nb_sv.get())
        exp_param["exp_name"] = self.main_exp_name_sv.get()
        exp_param["theta_start"] = float(self.angle_start_sv.get())
        exp_param["theta_end"] = float(self.angle_stop_sv.get())

        self.controller.set_exp_param(exp_param)
        self.controller.launch_DLS_Measurement()

    def stop_exp(self):
        #TODO
        pass