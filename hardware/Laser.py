from hardware.Device import Device


class Laser(Device):
    def __init__(self, main_ui):
        super(self).__init__(main_ui)

    def set_on_off(self, is_on):
        pass

    def set_power(self, power):
        pass

    def stop(self):
        self.set_on_off(is_on=False)

