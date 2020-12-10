from hardware.Laser import Laser


class DummyLaser(Laser):
    def __init__(self, main_ui):
        super().__init__(main_ui)

    def set_on_off(self, is_on):
        pass

    def set_power(self, power):
        pass

    def get_power(self):
        pass

    def stop(self):
        self.set_on_off(is_on=False)

    def load_device(self, params=None):
        self.initialized = True
        return True

