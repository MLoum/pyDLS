
from core.SingleAngleMeasurement import SingleAngleMeasurement

class FullAngleMeasurement():
    def __init__(self):
        #FIXME


        # Area for fit the data. E.g. ignore afterpulsing
        #FIXME
        self.correlation_fit_time_start = 0
        self.correlation_fit_time_end = -1

        #FIXME
        self.fitting_method1 = "Nelder"
        self.fitting_method2 = "lst"

        # Correlation calculation parameters
        #FIXME User selectable
        self.nb_of_point_per_cascade_aka_B = 10
        self.max_correlation_time_in_tick = 1E6
        #FIXME should be set by the couting card here it is determined by the FPGA NIST card.
        self.tick_duration_micros = 1.0/48.0
        self.correlation_algo = "Whal"
        #FIXME should be based on nb of core.
        self.correlation_nb_of_workers = 4
        #FIXME User selectable
        self.is_cross_correlation = False

        self.single_angle_measurements = []


    def add_single_angle_measurement(self, angle, raw_data, is_analyze_in_own_thread=True):
        single_angle_measurement = SingleAngleMeasurement(self, angle, raw_data)
        self.single_angle_measurements.append(single_angle_measurement)
        if is_analyze_in_own_thread:
            single_angle_measurement.correlate_raw_data()
        pass

    def open_measurements(self, file_path, filename):
        pass