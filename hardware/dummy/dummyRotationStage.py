from hardware.RotationStage import RotationStage


class DummyRotationStage(RotationStage):
    def __init__(self, main_ui):
        super().__init__(main_ui)

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

    def load_device(self, params=None):
        self.initialized = True
        return True
