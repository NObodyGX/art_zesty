# coding:utf-8
import os
import stat
import sys
from ctypes import Structure, byref, c_int, sizeof, windll
from ctypes.wintypes import DWORD, HWND, LPARAM, RECT, UINT

import win32api
import win32con
import win32file
import win32gui
import win32print
from PySide6.QtCore import QOperatingSystemVersion
from PySide6.QtGui import QGuiApplication
from win32comext.shell import shellcon


def catch_error(error_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except error_type as e:
                print(f"[ERROR] {error_type.__name__}: {str(e)}")

        return wrapper

    return decorator


class WinWorker(object):
    @staticmethod
    def is_readonly(fullname: str):
        attrs = win32file.GetFileAttributes(fullname)
        return attrs & win32file.FILE_ATTRIBUTE_READONLY > 0

    @catch_error(Exception)
    @staticmethod
    def set_readonly(fullname: str, readonly: bool):
        if not readonly:
            attrs = win32file.GetFileAttributes(fullname)
            win32file.SetFileAttributes(
                fullname, attrs & ~win32file.FILE_ATTRIBUTE_READONLY
            )
            return
        attributes = os.stat(fullname).st_file_attributes
        os.chmod(fullname, attributes | stat.S_IREAD)

    @catch_error(Exception)
    @staticmethod
    def set_hide(fullname: str, hide: bool):
        if not hide:
            win32api.SetFileAttributes(fullname, win32con.FILE_ATTRIBUTE_NORMAL)
            return
        win32api.SetFileAttributes(fullname, win32con.FILE_ATTRIBUTE_HIDDEN)

    @staticmethod
    def is_maximized(hwnd):
        windowPlacement = win32gui.GetWindowPlacement(hwnd)
        if not windowPlacement:
            return False

        return windowPlacement[1] == win32con.SW_MAXIMIZE

    @staticmethod
    def is_full_screen(hwnd):
        if not hwnd:
            return False

        hwnd = int(hwnd)
        winRect = win32gui.GetWindowRect(hwnd)
        if not winRect:
            return False

        monitorInfo = WinWorker.get_monitor_info(
            hwnd, win32con.MONITOR_DEFAULTTOPRIMARY
        )
        if not monitorInfo:
            return False

        monitorRect = monitorInfo["Monitor"]
        return all(i == j for i, j in zip(winRect, monitorRect))

    @staticmethod
    def get_monitor_info(hWnd, dwFlags):
        monitor = win32api.MonitorFromWindow(hWnd, dwFlags)
        if not monitor:
            return
        return win32api.GetMonitorInfo(monitor)

    @staticmethod
    def is_composition_enabled():
        """detect if dwm composition is enabled"""
        bResult = c_int(0)
        windll.dwmapi.DwmIsCompositionEnabled(byref(bResult))
        return bool(bResult.value)

    @staticmethod
    def get_resize_border_thickness(hWnd, horizontal=True):
        """get resize border thickness of widget

        Parameters
        ----------
        hWnd: int or `sip.voidptr`
            window handle

        dpiScale: bool
            whether to use dpi scale
        """
        window = WinWorker.find_window(hWnd)
        if not window:
            return 0

        frame = win32con.SM_CXSIZEFRAME if horizontal else win32con.SM_CYSIZEFRAME
        result = WinWorker.get_system_metrics(
            hWnd, frame, horizontal
        ) + WinWorker.get_system_metrics(hWnd, 92, horizontal)

        if result > 0:
            return result

        thickness = 8 if WinWorker.is_composition_enabled() else 4
        return round(thickness * window.devicePixelRatio())

    @staticmethod
    def get_system_metrics(hWnd, index, horizontal):
        """get system metrics"""
        if not hasattr(windll.user32, "GetSystemMetricsForDpi"):
            return win32api.GetSystemMetrics(index)

        dpi = WinWorker.get_dpi_for_window(hWnd, horizontal)
        return windll.user32.GetSystemMetricsForDpi(index, dpi)

    @staticmethod
    def get_dpi_for_window(hWnd, horizontal=True):
        """get dpi for window

        Parameters
        ----------
        hWnd: int or `sip.voidptr`
            window handle

        dpiScale: bool
            whether to use dpi scale
        """
        if hasattr(windll.user32, "GetDpiForWindow"):
            return windll.user32.GetDpiForWindow(hWnd)

        hdc = win32gui.GetDC(hWnd)
        if not hdc:
            return 96

        dpiX = win32print.GetDeviceCaps(hdc, win32con.LOGPIXELSX)
        dpiY = win32print.GetDeviceCaps(hdc, win32con.LOGPIXELSY)
        win32gui.ReleaseDC(hWnd, hdc)
        if dpiX > 0 and horizontal:
            return dpiX
        elif dpiY > 0 and not horizontal:
            return dpiY

        return 96

    @staticmethod
    def find_window(hWnd):
        """find window by hWnd, return `None` if not found

        Parameters
        ----------
        hWnd: int or `sip.voidptr`
            window handle
        """
        if not hWnd:
            return

        windows = QGuiApplication.topLevelWindows()
        if not windows:
            return

        hWnd = int(hWnd)
        for window in windows:
            if window and int(window.winId()) == hWnd:
                return window

    @staticmethod
    def is_greater_equal_version(version):
        """determine if the windows version ≥ the specifics version

        Parameters
        ----------
        version: QOperatingSystemVersion
            windows version
        """
        return QOperatingSystemVersion.current() >= version

    @staticmethod
    def is_greater_equal_win8_1():
        """determine if the windows version ≥ Win8.1"""
        return WinWorker.is_greater_equal_version(QOperatingSystemVersion.Windows8_1)

    def is_greater_equal_win10():
        """determine if the windows version ≥ Win10"""
        return WinWorker.is_greater_equal_version(QOperatingSystemVersion.Windows10)

    def is_greater_equal_win11():
        """determine if the windows version ≥ Win10"""
        return (
            WinWorker.is_greater_equal_version(QOperatingSystemVersion.Windows10)
            and sys.getwindowsversion().build >= 22000
        )


class APPBARDATA(Structure):
    _fields_ = [
        ("cbSize", DWORD),
        ("hWnd", HWND),
        ("uCallbackMessage", UINT),
        ("uEdge", UINT),
        ("rc", RECT),
        ("lParam", LPARAM),
    ]


class Taskbar(object):
    LEFT = 0
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    NO_POSITION = 4

    AUTO_HIDE_THICKNESS = 2

    @staticmethod
    def isAutoHide():
        """detect whether the taskbar is hidden automatically"""
        appbarData = APPBARDATA(sizeof(APPBARDATA), 0, 0, 0, RECT(0, 0, 0, 0), 0)
        taskbarState = windll.shell32.SHAppBarMessage(
            shellcon.ABM_GETSTATE, byref(appbarData)
        )

        return taskbarState == shellcon.ABS_AUTOHIDE

    @classmethod
    def getPosition(cls, hWnd):
        """get the position of auto-hide task bar

        Parameters
        ----------
        hWnd: int or `sip.voidptr`
            window handle
        """
        if WinWorker.is_greater_equal_win8_1():
            monitorInfo = WinWorker.get_monitor_info(
                hWnd, win32con.MONITOR_DEFAULTTONEAREST
            )
            if not monitorInfo:
                return cls.NO_POSITION

            monitor = RECT(*monitorInfo["Monitor"])
            appbarData = APPBARDATA(sizeof(APPBARDATA), 0, 0, 0, monitor, 0)
            positions = [cls.LEFT, cls.TOP, cls.RIGHT, cls.BOTTOM]
            for position in positions:
                appbarData.uEdge = position
                if windll.shell32.SHAppBarMessage(11, byref(appbarData)):
                    return position

            return cls.NO_POSITION

        appbarData = APPBARDATA(
            sizeof(APPBARDATA),
            win32gui.FindWindow("Shell_TrayWnd", None),
            0,
            0,
            RECT(0, 0, 0, 0),
            0,
        )
        if appbarData.hWnd:
            windowMonitor = win32api.MonitorFromWindow(
                hWnd, win32con.MONITOR_DEFAULTTONEAREST
            )
            if not windowMonitor:
                return cls.NO_POSITION

            taskbarMonitor = win32api.MonitorFromWindow(
                appbarData.hWnd, win32con.MONITOR_DEFAULTTOPRIMARY
            )
            if not taskbarMonitor:
                return cls.NO_POSITION

            if taskbarMonitor == windowMonitor:
                windll.shell32.SHAppBarMessage(
                    shellcon.ABM_GETTASKBARPOS, byref(appbarData)
                )
                return appbarData.uEdge

        return cls.NO_POSITION


class WindowsMoveResize:
    """Tool class for moving and resizing Mac OS window"""

    @staticmethod
    def startSystemMove(window, globalPos):
        """resize window

        Parameters
        ----------
        window: QWidget
            window

        globalPos: QPoint
            the global point of mouse release event
        """
        win32gui.ReleaseCapture()
        win32api.SendMessage(
            int(window.winId()),
            win32con.WM_SYSCOMMAND,
            win32con.SC_MOVE | win32con.HTCAPTION,
            0,
        )
