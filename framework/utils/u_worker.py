from PySide6.QtGui import QFont, QFontMetrics, QGuiApplication
from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout


class UWorker(object):
    @staticmethod
    def vlayout(space=0, left=0, top=0, right=0, bottom=0, total=0):
        if total != 0:
            space = space if space else total
            left = left if left else total
            top = top if top else total
            right = right if right else total
            bottom = bottom if bottom else total
        layout = QVBoxLayout()
        layout.setSpacing(space)
        layout.setContentsMargins(left, top, right, bottom)
        return layout

    @staticmethod
    def hlayout(space=0, left=0, top=0, right=0, bottom=0, total=0):
        if total != 0:
            space = space if space else total
            left = left if left else total
            top = top if top else total
            right = right if right else total
            bottom = bottom if bottom else total
        layout = QHBoxLayout()
        layout.setSpacing(space)
        layout.setContentsMargins(left, top, right, bottom)
        return layout

    @staticmethod
    def glayout(space=0, left=0, top=0, right=0, bottom=0, total=0):
        if total != 0:
            left = left if left else total
            top = top if top else total
            right = right if right else total
            bottom = bottom if bottom else total
        layout = QGridLayout()
        layout.setSpacing(space)
        layout.setContentsMargins(left, top, right, bottom)
        return layout

    @staticmethod
    def font_width(text: str, font: QFont):
        fm = QFontMetrics(font)
        width = fm.boundingRect(text).width()
        return width

    @staticmethod
    def font_height(font):
        metrics = QFontMetrics(font)
        height = metrics.height()
        return height

    @staticmethod
    def avail_geometry(pos):
        geo = QGuiApplication.screenAt(pos).availableGeometry()
        return geo
