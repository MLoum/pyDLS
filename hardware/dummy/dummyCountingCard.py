from hardware.CountingCard import CountingCard


class DummyCountingCard(CountingCard):
    def __init__(self, main_ui):
        super().__init__(main_ui)

    def set_time_tag_file(self, file_path):
        pass

    def time_tag(self):
        pass

    def stop(self):
        pass
