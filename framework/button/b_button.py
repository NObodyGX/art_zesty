from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal

from framework.data.size import GSize


class GBaseButton(QPushButton):
    pass


class GPlayButton(GBaseButton):
    def __init__(self, func):
        super().__init__()
        self.setFixedSize(32, 32)
        self.clicked.connect(func)
        self.switch(True)

    def switch(self, is_playing: bool):
        self.setDown(not is_playing)


class GTitleButton(GBaseButton):
    """标题按钮"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(GSize.title_icon_h_w, GSize.title_icon_h_w)
        self.setFixedHeight(GSize.title_icon_h_w)


class GTCheckButton(GTitleButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCheckable(True)
        self.setChecked(False)


class GTMaxButton(GTitleButton):
    """标题栏最大化按钮"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_max = False

    def set_max_state(self, isMax):
        self.is_max = bool(isMax)


class GTMinButton(GTitleButton):
    """标题栏最小化按钮"""

    def __init__(self, parent=None):
        super().__init__(parent)


class GTOffButton(GTitleButton):
    """标题栏关闭按钮"""

    def __init__(self, parent=None):
        super().__init__(parent)


class GOffButton(GBaseButton):
    pass
    """通用关闭按钮"""


class GOKButton(GBaseButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(42, 24)


class GNOButton(GBaseButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(42, 24)


class GCheckButton(GBaseButton):
    state_changed_signal = Signal(bool)

    def __init__(self):
        super().__init__()
        self._check_state = False
        self.setFixedSize(24, 24)
        self.setCheckable(True)
        self.clicked.connect(self._on_clicked)

    def _on_clicked(self):
        self.setChecked(not self._check_state)

    def setChecked(self, checked: bool) -> None:
        if self._check_state != checked:
            self._check_state = checked
            self.state_changed_signal.emit(self._check_state)
        return super().setChecked(checked)


class GToggleButton(GCheckButton):
    pass


class GArrowButton(GCheckButton):
    pass


class GFontButton(GBaseButton):
    pass


class GGridLabelButton(GBaseButton):
    pass
