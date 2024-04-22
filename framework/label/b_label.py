from PySide6.QtWidgets import QLabel, QColorDialog, QWidget, QLineEdit
from PySide6.QtCore import Signal
from PySide6.QtGui import Qt, QColor, QPainter
from framework.button.b_button import GButton

from framework.data import GSize
from framework.utils import UWorker


class GBLabel(QLabel):
    pass


class GTitleLabel(GBLabel):
    def __init__(self, parent=None, text=""):
        super().__init__(text, parent)
        self.resize(GSize.title_icon_h_w, GSize.title_icon_h_w)


class GLineNameLabel(GBLabel):
    pass


class GLineLabel(QWidget):
    refresh_text_signal = Signal(str)

    def __init__(self, text="", parent=None):
        super().__init__(parent)

        layout = UWorker.vlayout()
        self.label = GLineNameLabel(text)
        self.editor = QLineEdit()
        self.editor.setHidden(True)
        self.button_ok = GButton()
        self.button_ok.setHidden(True)
        edit_layout = UWorker.hlayout()
        edit_layout.addWidget(self.editor)
        edit_layout.addWidget(self.button_ok)
        layout.addWidget(self.label)
        layout.addLayout(edit_layout)
        self.setLayout(layout)

        self.label.mouseDoubleClickEvent = self.editing_start
        self.button_ok.clicked.connect(self.editing_finish)

    def switch_visiable(self, show_label=True):
        self.label.setHidden(not show_label)
        self.editor.setHidden(show_label)
        self.button_ok.setHidden(show_label)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.editing_finish()
        elif event.key() == Qt.Key_Escape:
            self.editing_cancel()
        else:
            super().keyPressEvent(event)

    def editing_start(self, event=None):
        self.editor.setText(self.label.text())
        self.switch_visiable(show_label=False)
        self.editor.setFocus(Qt.MouseFocusReason)

    def editing_finish(self):
        text = self.editor.text()
        self.label.setText(text)
        self.switch_visiable(show_label=True)
        self.refresh_text_signal.emit(text)

    def editing_cancel(self):
        self.switch_visiable(show_label=True)

    def resizeEvent(self, e) -> None:
        h = self.height()
        self.label.setFixedHeight(h)
        self.label.setMaximumWidth(self.width())
        self.editor.setFixedHeight(h)
        self.editor.setFixedWidth(self.width() - h)
        self.button_ok.setFixedSize(h, h)
        return super().resizeEvent(e)
