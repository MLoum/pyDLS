
from controller import Controller
from view.gui import View
from core.FullAngleMeasurement import FullAngleMeasurement

if __name__ == "__main__":
    fullAngleMeasurement = FullAngleMeasurement()
    controller = Controller(fullAngleMeasurement)
    controller.run()