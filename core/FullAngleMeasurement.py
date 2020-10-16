
from core.SingleAngleMeasurement import SingleAngleMeasurement

class FullAngleMeasurement():
    def __init__(self):
        self.single_angle_measurements = []


    def add_single_angle_measurement(self, angle, raw_data, is_analyze_in_own_thread=True):
        single_angle_measurement = SingleAngleMeasurement(self, angle, raw_data)
        self.single_angle_measurements.append(single_angle_measurement)
        if is_analyze_in_own_thread:
            pass
        pass
