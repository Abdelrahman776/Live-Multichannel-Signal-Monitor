from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QSlider

class CustomSlider(QSlider):
    differenceChanged = pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.previous_value = 0
        self.sliderMoved.connect(self.calculateDifference)
        self.sliderPressed.connect(self.updatePreviousValue)

    def updatePreviousValue(self):
        self.previous_value = self.value()

    def calculateDifference(self):
        current_value = self.value()
        difference = current_value - self.previous_value
        self.differenceChanged.emit(difference)
        self.previous_value = current_value