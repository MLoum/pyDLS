import tkinter as tk
from tkinter import ttk




class AngleTreeview():
    def __init__(self, root):
        self.root = root
        self.create_angle_treeview()


    def create_angle_treeview(self):
        self.frame_tree_view = tk.LabelFrame(self.root, text="Angle browser",
                                             borderwidth=1)
        self.frame_tree_view.pack(side="top", fill="both", expand=True)

        # https://riptutorial.com/tkinter/example/31885/customize-a-treeview
        self.tree_view = ttk.Treeview(self.frame_tree_view)
        self.tree_view["columns"] = (
        "Angle", "Nb of tick", "Intensity", "Mean size", "µ2", "µ3", "µ4", "beta", "t_start_µs",
        "t_end_µs")
        # remove first empty column with the identifier
        # self.tree_view['show'] = 'headings'
        # tree.column("#0", width=270, minwidth=270, stretch=tk.NO) tree.column("one", width=150, minwidth=150, stretch=tk.NO) tree.column("two", width=400, minwidth=200) tree.column("three", width=80, minwidth=50, stretch=tk.NO)
        self.tree_view.column("#0", width=25, stretch=tk.NO)
        self.tree_view.column("Angle", width=300, stretch=tk.YES, anchor=tk.CENTER)
        self.tree_view.column("Nb of tick", width=75, stretch=tk.YES, anchor=tk.CENTER)
        self.tree_view.column("Intensity", width=300, stretch=tk.YES, anchor=tk.CENTER)
        self.tree_view.column("Mean size", width=75, stretch=tk.YES, anchor=tk.CENTER)
        self.tree_view.column("µ2", width=75, stretch=tk.YES, anchor=tk.CENTER)
        self.tree_view.column("µ3", width=75, stretch=tk.YES, anchor=tk.CENTER)
        self.tree_view.column("µ4", width=75, stretch=tk.YES, anchor=tk.CENTER)
        self.tree_view.column("beta", width=600, stretch=tk.YES, anchor=tk.CENTER)
        self.tree_view.column("t_start_µs", width=50, stretch=tk.YES, anchor=tk.CENTER)
        self.tree_view.column("t_end_µs", width=50, stretch=tk.YES, anchor=tk.CENTER)

        self.tree_view.heading("Angle", text="Angle")
        self.tree_view.heading("Nb of tick", text="Nb of tick")
        self.tree_view.heading("Intensity", text="Intensity")
        self.tree_view.heading("Mean size", text="Mean size")
        self.tree_view.heading("µ2", text="µ2")
        self.tree_view.heading("µ3", text="µ3")
        self.tree_view.heading("µ4", text="µ4")
        self.tree_view.heading("beta", text="beta")
        self.tree_view.heading("t_start_µs", text="t_start_µs")
        self.tree_view.heading("t_end_µs", text="t_end_µs")

        ysb = ttk.Scrollbar(self.frame_tree_view, orient='vertical', command=self.tree_view.yview)
        self.tree_view.grid(row=0, column=0, sticky='nsew')
        ysb.grid(row=0, column=1, sticky='ns')
        self.tree_view.configure(yscroll=ysb.set)

        self.tree_view.bind('<<TreeviewSelect>>', self.treeview_angle_select)

        self.tree_view.grid(row=0, column=0)

    def treeview_angle_select(self):
        pass

    def insert_angle_treeview(self):
        pass

    def del_angle_treeview(self):
        pass

    def clear_tree_view(self):
        pass
