from hardware.RotationStanda import RotationStanda
from hardware.fpga_nist import FPGA_nist
from hardware.Laser import Laser

from core.SingleAngleMeasurement import SingleAngleMeasurement
from core.FullAngleMeasurement import FullAngleMeasurement

import threading

import numpy as np

class Controller():
    def __init(self, view, full_angle_measurements):
        self.view = view
        self.full_angle_measurements = full_angle_measurements
        self.rotation_stage = RotationStanda(self.view)
        self.couting_card = FPGA_nist(self.view)
        self.laser = Laser(self.view)
        # FIXME ? Dans le core ?
        self.exp_param = {}

    def launch_DLS_Measurement(self):
        self.thread_DLS_Measurement = threading.Thread(name='FGPA record', target=self.DLS_Measurement)
        # self.thread_monitor = threading.Thread(name='FGPA monitor', target=self.monitor)
        self.thread_DLS_Measurement.start()
        # self.thread_monitor.start()

    def stop_experiment(self):
        self.rotation_stage.stop()
        self.couting_card.stop()
        self.laser.stop()
        if self.thread_DLS_Measurement.is_alive():
            self.thread_DLS_Measurement.join(timeout=0.5)
            # self.thread_monitor.join(timeout=0.5)

    def DLS_Measurement(self):
        nb_step = self.exp_param["theta_nb_step"]
        main_exp_name = self.exp_param["exp_name"]
        theta_start, theta_end = self.exp_param["theta_start"], self.exp_param["theta_end"]
        step_angle = (self.exp_param["theta_end"] - theta_start)/nb_step

        angles = np.linspace(theta_start, theta_end, nb_step)

        for theta in angles:
            self.rotation_stage.move_absolute(theta)
            self.rotation_stage.wait_for_device()

            self.laser.set_on_off(is_on=True)

            file_name = main_exp_name + "_d" + str(int(theta)) + ".ttt"
            self.couting_card.set_time_tag_file(file_name)
            self.couting_card.time_tag()
            self.couting_card.wait_for_device()

            self.laser.set_on_off(is_on=False)

            # Gather data and start analizing it in another thread
            self.full_angle_measurements.add_single_angle_measurement(is_analyze_in_own_thread=True)

    def DLS_Measurement(self):
        pass
        """
        Envoyer des impulsions de la platine sur la quatrièeme voie de la carte pour connaitre la position angulaire ?
        the controller can output synchronization pulse each time it moves a certain distance        
        """
