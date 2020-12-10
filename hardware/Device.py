class Device(object):
    def __init__(self, main_ui):
        self.root = main_ui.root
        self.main_ui = main_ui
        self.frame_name = "Device"

        self.initialized = False
        self.is_busy_ = False

    def create_GUI(self):
        pass

    def load_device(self, params=None):
        pass

    def close_device(self, params=None):
        pass

    def is_busy(self):
        pass

    def wait_for_device(self):
        pass