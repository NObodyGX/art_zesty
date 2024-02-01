from PySide6.QtWidgets import QColorDialog
from PySide6.QtCore import Signal
from PySide6.QtGui import QColor, QPainter

from framework.label.b_label import GBLabel


class GColorLabel(GBLabel):
    color_changed_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.current_color = QColor("#fefefe")
        self.setFixedWidth(8)

    def set_color(self, color: QColor):
        self.current_color = color

    def paintEvent(self, _=None) -> None:
        painter = QPainter(self)
        painter.fillRect(self.rect(), self.current_color)

    def select_color(self, _=None):
        color_dialog = QColorDialog(self)
        color_dialog.setCurrentColor(self.current_color)
        color_dialog.setOptions(QColorDialog.ShowAlphaChannel)
        color_dialog.setOptions(QColorDialog.NoButtons)
        col = QColorDialog.getColor()
        if not QColor.isValid(col):
            return
        self.color_changed_signal.emit(col.name())
        self.set_color(col)

    def mouseDoubleClickEvent(self, event) -> None:
        self.select_color()
