from functools import partial
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QWheelEvent, QCursor
from PySide6.QtWidgets import QDialog, QGridLayout, QPushButton
from framework.data.size import GSize

from framework.label.b_label import GBLabel
from framework.theme.worker import GThemeWorker
from framework.utils.u_worker import UWorker
from framework.button.b_button import GGridLabelButton, GOffButton


class NumDialog(QDialog):
    value_changed = Signal(int)

    def __init__(self, max_v=60):
        super().__init__()
        self.max_v = max_v
        self.resize(320, 240 if max_v == 60 else 80)
        self.setWindowFlags(
            Qt.Window
            | Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
        )
        self._setup_ui()

    def _setup_ui(self):
        layout = UWorker.glayout()
        self.buttons = []
        self.close_button = GOffButton()
        self.close_button.setFixedWidth(self.width())
        self.close_button.setFixedHeight(GSize.grid_button_w_h)
        self.close_button.clicked.connect(lambda: self.close())
        layout.addWidget(self.close_button, 0, 0, 1, 10)
        for i in range(self.max_v):
            button = GGridLabelButton(str(i))
            button.setFixedSize(GSize.grid_button_w_h, GSize.grid_button_w_h)
            self.buttons.append(button)
            x = i / 10 + 1
            y = i % 10
            layout.addWidget(button, x, y)
            button.clicked.connect(partial(self.on_clicked, i))

        self.setLayout(layout)

    def on_clicked(self, v: int):
        self.value_changed.emit(v)
        self.close()


class GNumberLabel(GBLabel):
    number_changed_signal = Signal(str)

    def __init__(self, min_v=0, max_v=100, step=1):
        super().__init__()
        self._min_v = min_v
        self._max_v = max_v
        self._step = step
        self.cur_v = min_v

    @property
    def cur_v(self):
        return self._current_v

    @cur_v.setter
    def cur_v(self, v: int):
        v = int(v)
        if v > self._max_v:
            v = self._max_v
        if v < self._min_v:
            v = self._min_v
        self._current_v = int(v)
        self.setText(str(self._current_v))

    def mouseDoubleClickEvent(self, event) -> None:
        self.show_pick_dialog()

    def show_pick_dialog(self):
        dialog = NumDialog(self._max_v)
        dialog.value_changed.connect(self._on_value_changed)
        x = QCursor.pos().x() - dialog.size().width() // 2
        y = QCursor.pos().y() - dialog.size().height() // 2
        dialog.move(x, y)
        GThemeWorker.apply(dialog, theme="default")
        dialog.show()
        dialog.show()

    def _on_value_changed(self, v):
        self.cur_v = int(v)

    def wheelEvent(self, event: QWheelEvent) -> None:
        # QWheelEvent中的一个用法就是angleDelta().y()
        # 其中 angleDelta() 表述返回一个 Qpoint，x代表滚轮方向和步数，y是滚轮垂直方向上的偏移
        degree = event.angleDelta().y() / 8
        step = degree / 15
        self.cur_v += self._step * step
