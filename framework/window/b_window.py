# coding:utf-8
from ctypes import cast
from ctypes.wintypes import LPRECT, MSG

from win32 import win32gui
from win32.lib import win32con

from framework.effect import LPNCCALCSIZE_PARAMS, WindowEffect
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout

from framework.titlebar.titlebar import GTitleBar
from framework.utils.win_worker import Taskbar, WinWorker
from framework.utils.u_worker import UWorker


class GBaseWindow(QWidget):
    """Frameless window for Windows system"""

    BORDER_WIDTH = 5

    def __init__(self, parent=None, titlebar="normal"):
        super().__init__(parent=parent)
        self.windowEffect = WindowEffect(self)
        self.title_bar = GTitleBar(parent=self)
        self._isResizeEnabled = True

        # remove window border
        self.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.WindowSystemMenuHint
            | Qt.WindowMinimizeButtonHint
            | Qt.WindowMaximizeButtonHint
        )
        # 添加阴影和窗口动画

        # add DWM shadow and window animation
        self.windowEffect.addWindowAnimation(self.winId())
        self.windowEffect.addShadowEffect(self.winId())

        # solve issue #5
        self.windowHandle().screenChanged.connect(self.__onScreenChanged)

        self.resize(1260, 720)
        self.title_bar.raise_()
        self._setup_ui()

    def _setup_ui(self):
        layout = UWorker.vlayout()
        layout.addWidget(self.title_bar)
        layout.addLayout(self.center_layout())
        self.setLayout(layout)

    def center_layout(self):
        layout = UWorker.hlayout()
        return layout

    def set_title(self, title: str):
        self.title_bar.set_title(title)
        self.setWindowTitle(title)

    def setResizeEnabled(self, isEnabled: bool):
        """set whether resizing is enabled"""
        self._isResizeEnabled = isEnabled

    def resizeEvent(self, e):
        super().resizeEvent(e)
        # self.title_bar.resize(self.width(), self.title_bar.height())

    def nativeEvent(self, eventType, message):
        """Handle the Windows message"""
        msg = MSG.from_address(message.__int__())
        if not msg.hWnd:
            return super().nativeEvent(eventType, message)

        if msg.message == win32con.WM_NCHITTEST and self._isResizeEnabled:
            pos = QCursor.pos()
            xPos = pos.x() - self.x()
            yPos = pos.y() - self.y()
            w, h = self.width(), self.height()

            bw = (
                0
                if WinWorker.is_maximized(msg.hWnd)
                or WinWorker.is_full_screen(msg.hWnd)
                else self.BORDER_WIDTH
            )
            lx = xPos < bw
            rx = xPos > w - bw
            ty = yPos < bw
            by = yPos > h - bw
            if lx and ty:
                return True, win32con.HTTOPLEFT
            elif rx and by:
                return True, win32con.HTBOTTOMRIGHT
            elif rx and ty:
                return True, win32con.HTTOPRIGHT
            elif lx and by:
                return True, win32con.HTBOTTOMLEFT
            elif ty:
                return True, win32con.HTTOP
            elif by:
                return True, win32con.HTBOTTOM
            elif lx:
                return True, win32con.HTLEFT
            elif rx:
                return True, win32con.HTRIGHT
        elif msg.message == win32con.WM_NCCALCSIZE:
            if msg.wParam:
                rect = cast(msg.lParam, LPNCCALCSIZE_PARAMS).contents.rgrc[0]
            else:
                rect = cast(msg.lParam, LPRECT).contents

            isMax = WinWorker.is_maximized(msg.hWnd)
            isFull = WinWorker.is_full_screen(msg.hWnd)

            # adjust the size of client rect
            if isMax and not isFull:
                ty = WinWorker.get_resize_border_thickness(msg.hWnd, False)
                rect.top += ty
                rect.bottom -= ty

                tx = WinWorker.get_resize_border_thickness(msg.hWnd, True)
                rect.left += tx
                rect.right -= tx

            # handle the situation that an auto-hide taskbar is enabled
            if (isMax or isFull) and Taskbar.isAutoHide():
                position = Taskbar.getPosition(msg.hWnd)
                if position == Taskbar.LEFT:
                    rect.top += Taskbar.AUTO_HIDE_THICKNESS
                elif position == Taskbar.BOTTOM:
                    rect.bottom -= Taskbar.AUTO_HIDE_THICKNESS
                elif position == Taskbar.LEFT:
                    rect.left += Taskbar.AUTO_HIDE_THICKNESS
                elif position == Taskbar.RIGHT:
                    rect.right -= Taskbar.AUTO_HIDE_THICKNESS

            result = 0 if not msg.wParam else win32con.WVR_REDRAW
            return True, result

        return super().nativeEvent(eventType, message)

    def __onScreenChanged(self):
        hWnd = int(self.windowHandle().winId())
        win32gui.SetWindowPos(
            hWnd,
            None,
            0,
            0,
            0,
            0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_FRAMECHANGED,
        )
