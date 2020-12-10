import tkinter as tk
from tkinter import ttk
from view.InterractiveGraph import InteractiveGraph
from view.AngleTreeview import AngleTreeview

class ResultArea():
    def __init__(self, master_frame, view, controller):
        self.master_frame = master_frame
        self.view = view
        self.controller = controller

    def populate(self):
        # self.frame_results = tk.LabelFrame(self.master_frame, text="Results",
        #                                    borderwidth=1)
        self.frame_results = tk.Frame(self.master_frame)
        # self.frame_result_text.grid(row=0, column=0)
        self.frame_results.pack(side=tk.TOP, fill="both", expand=True)

        self.frame_angle_tree_view = tk.Frame(self.frame_results)
        self.frame_angle_tree_view.pack(side=tk.TOP, fill="both", expand=True)
        self.angle_tree_view = AngleTreeview(self.frame_angle_tree_view, self.view, self.controller)

        self.frame_global_results = tk.LabelFrame(self.frame_results, text="Global results",
                                                  borderwidth=1)
        self.frame_global_results.pack(side=tk.TOP, fill="both", expand=True)

        self.frame_global_results_cumulant = tk.LabelFrame(self.frame_global_results, text="Cumulants",
                                                           borderwidth=1)
        self.frame_global_results_cumulant.pack(side=tk.LEFT, fill="both", expand=True)

        ttk.Label(self.frame_global_results_cumulant, text='Mean size (nm) :').grid(row=0, column=0)
        self.global_mean_size_cumulant_sv = tk.StringVar(0)
        e = ttk.Entry(self.frame_global_results_cumulant, width=12, justify=tk.CENTER,
                      textvariable=self.global_mean_size_cumulant_sv)
        e.grid(row=0, column=1)

        ttk.Label(self.frame_global_results_cumulant, text='µ2 / % :').grid(row=1, column=0)
        self.global_mu2_cumulant_sv = tk.StringVar(0)
        e = ttk.Entry(self.frame_global_results_cumulant, width=12, justify=tk.CENTER,
                      textvariable=self.global_mu2_cumulant_sv)
        e.grid(row=1, column=1)

        self.frame_global_results_contin = tk.LabelFrame(self.frame_global_results, text="CONTIN",
                                                         borderwidth=1)
        self.frame_global_results_contin.pack(side=tk.LEFT, fill="both", expand=True)

        self.frame_graph_evol_result_angle = tk.LabelFrame(self.frame_results, text="results vs Angle",
                                                           borderwidth=1)
        self.frame_graph_evol_result_angle.pack(side=tk.TOP, fill="both", expand=True)

        self.frame_graph_SLS_intensity = tk.Frame(self.frame_graph_evol_result_angle)
        self.frame_graph_SLS_intensity.pack(side=tk.TOP, fill="both", expand=True)
        self.graph_intensity = InteractiveGraph(self.frame_graph_SLS_intensity, self, self.controller, figsize=(2, 2),
                                                dpi=100)

        self.frame_graph_chi_beta = tk.Frame(self.frame_graph_evol_result_angle)
        self.frame_graph_chi_beta.pack(side=tk.TOP, fill="both", expand=True)
        self.graph_chi_beta = InteractiveGraph(self.frame_graph_chi_beta, self, self.controller, figsize=(2, 2),
                                               dpi=100)

        self.frame_graph_Gamma_Mu2 = tk.Frame(self.frame_graph_evol_result_angle)
        self.frame_graph_Gamma_Mu2.pack(side=tk.TOP, fill="both", expand=True)
        self.graph_Gamma_Mu2 = InteractiveGraph(self.frame_graph_Gamma_Mu2, self, self.controller, figsize=(2, 2),
                                                dpi=100)