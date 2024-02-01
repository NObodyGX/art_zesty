# coding:utf-8

from win32.lib import win32con
from win32.win32api import SendMessage
from win32.win32gui import ReleaseCapture

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QEvent, Signal
from PySide6.QtGui import QResizeEvent
from framework.button.b_button import GTCheckButton

from framework.data import GSize
from framework.button.b_button import (
    GTitleButton,
    GTMinButton,
    GTMaxButton,
    GTOffButton,
)
from framework.label import GTitleLabel
from framework.utils import UWorker


class GTitleBar(QWidget):
    def __init__(self, parent, title=""):
        self.p = parent
        super().__init__(parent)
        self.resize(1360, self.default_height())
        self._setup_ui()
        self.setMinimumWidth(200)
        self.setFixedHeight(self.default_height())
        self.setAttribute(Qt.WA_StyledBackground)
        self.window().installEventFilter(self)
        # self.balance_position()
        self.set_title(title)

    def _setup_ui(self):
        self.ico_button = GTitleButton(self)
        self.ico_button.setFixedWidth(32)
        self.tit_label_ = GTitleLabel(self, "")
        self.tit_label_.setFixedHeight(self.default_height())
        self.tit_label_.setAlignment(Qt.AlignCenter)
        self.min_button = GTMinButton(self)
        self.min_button.setFixedWidth(32)
        self.max_button = GTMaxButton(self)
        self.max_button.setFixedWidth(32)
        self.off_button = GTOffButton(self)
        self.off_button.setFixedWidth(32)

        self.ico_button.setText("👑")
        self.min_button.setText("🟡")
        self.min_button.clicked.connect(self.window().showMinimized)
        self.max_button.setText("🟢")
        self.max_button.clicked.connect(self.__switch_max_window)
        self.off_button.setText("🔴")
        self.off_button.clicked.connect(self.window().close)
        layout = UWorker.hlayout()
        layout.addWidget(self.ico_button)
        layout.addWidget(self.tit_label_)
        layout2 = UWorker.hlayout()
        layout2.addWidget(self.min_button)
        layout2.addWidget(self.max_button)
        layout2.addWidget(self.off_button)
        layout.addLayout(layout2)
        self.setLayout(layout)

    def default_height(self):
        return GSize.title_icon_h_w

    def balance_position(self):
        w = GSize.title_icon_h_w
        ww = self.width()
        self.ico_button.move(0, 0)
        self.off_button.move(ww - w, 0)
        self.max_button.move(ww - 2 * w, 0)
        self.min_button.move(ww - 3 * w, 0)

    def set_icon(self, icon):
        self.ico_button.setText(icon)

    def set_title(self, text):
        self.title_width = UWorker.font_width(text, self.tit_label_.font())

        self.tit_label_.setText(text)

    def title(self):
        return self.tit_label_.text()

    def eventFilter(self, obj, e):
        if obj is self.window():
            if e.type() == QEvent.WindowStateChange:
                self.max_button.set_max_state(self.window().isMaximized())
                return False
        return super().eventFilter(obj, e)

    # def resizeEvent(self, e: QResizeEvent):
    #     """尺寸改变时移动按钮"""
    #     self.balance_position()

    def mouseDoubleClickEvent(self, event):
        """双击最大化窗口"""
        self.__switch_max_window()

    def mousePressEvent(self, event):
        if self.is_drag_region(event.pos()):
            ReleaseCapture()
            SendMessage(
                self.window().winId(),
                win32con.WM_SYSCOMMAND,
                win32con.SC_MOVE + win32con.HTCAPTION,
                0,
            )
            event.ignore()

    def __switch_max_window(self, _=None):
        if self.window().isMaximized():
            self.window().showNormal()
        else:
            self.window().showMaximized()

    def is_drag_region(self, pos) -> bool:
        """检查鼠标按下的点是否属于允许拖动的区域"""
        w = GSize.title_icon_h_w
        return w < pos.x() < self.width() - w * 3


class GDialogTitleBar(GTitleBar):
    def __init__(self, title="", parent=None):
        self.title_width = int(100 / 4)
        super().__init__(title=title, parent=parent)
        self.setAttribute(Qt.WA_StyledBackground)

    def init_widgets(self):
        super().init_widgets()
        self.min_button.setHidden(True)
        self.max_button.setHidden(True)
        self.top_button.setHidden(True)

    def balance_position(self):
        h = GSize.title_icon_h_w
        self.ico_button.move(0, 0)
        self.off_button.move(self.width() - h, 0)
        if self.width() < h * 2 + self.title_width:
            self.tit_label_.setHidden(True)
        else:
            self.tit_label_.setHidden(False)
            self.tit_label_.setFixedWidth(self.width() - h * 2)
            self.tit_label_.move(h, 0)

    def is_drag_region(self, pos) -> bool:
        w = GSize.title_icon_h_w
        return w < pos.x() < self.width() - w * 2

    def mouseDoubleClickEvent(self, event):
        pass
