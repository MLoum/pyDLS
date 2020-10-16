from hardware.Device import Device


class RotationStage(Device):
    def __init__(self, main_ui):
        super(self).__init__(main_ui)

    def get_position(self):
        pass

    def move_absolute(self, angle_deg):
        pass

    def move_relative(self, angle_deg):
        pass

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

