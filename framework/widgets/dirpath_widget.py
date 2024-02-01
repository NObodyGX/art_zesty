from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLineEdit, QWidget, QPushButton, QFileDialog
import os

from framework.utils.u_worker import UWorker


class DirPathEdit(QLineEdit):
    def __init__(self, parent=None):
        self.p = parent  # type: GDirPathWidget
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setPlaceholderText("请输入目录路径")
        self.textChanged.connect(self.on_text_changed)

    def dragEnterEvent(self, event):
        fullpath = event.mimeData().urls()[0].toLocalFile()
        if not os.path.exists(fullpath):
            return
        text = fullpath
        if os.path.isfile(fullpath):
            text = os.path.dirname(fullpath)
        self.set_text(text)
        event.accept()

    def dropEvent(self, event):
        # 把原有的取消掉
        pass

    def set_text(self, v: str):
        v = os.path.normpath(v)
        self.setText(v)
        self.on_text_changed(v)

    def on_text_changed(self, v):
        self.p.dir_changed.emit(v)


class GDirPathWidget(QWidget):
    dir_changed = Signal(str)

    def __init__(self, parent: None):
        super().__init__(parent)

        self._setup_ui()
        self._setup_fn()

    def _setup_ui(self):
        self.w_center = DirPathEdit(self)
        self.w_updown = QPushButton("🔙")
        self.w_choice = QPushButton("📂")

        # 减去上下线宽度
        self.w_updown.setFixedHeight(self.w_center.height() - 2)
        self.w_updown.setFixedWidth(self.w_center.height() - 2)
        self.w_choice.setFixedHeight(self.w_center.height() - 2)
        self.w_choice.setFixedWidth(self.w_center.height() - 2)

        layout = UWorker.hlayout()
        layout.addWidget(self.w_center)
        layout.addWidget(self.w_updown)
        layout.addWidget(self.w_choice)
        self.setLayout(layout)

    def _setup_fn(self):
        self.w_updown.clicked.connect(self._on_back_clicked)
        self.w_choice.clicked.connect(self._on_cdir_clicked)

    def _on_back_clicked(self):
        cdir = self.v()
        ndir = os.path.dirname(cdir)
        if not ndir:
            return
        self.w_center.set_text(ndir)

    def _on_cdir_clicked(self):
        ndir = "." if not self.v() else self.v()
        cdir = QFileDialog.getExistingDirectory(
            self, "选择文件路径", ndir, QFileDialog.DontUseNativeDialog
        )
        if not cdir:
            return
        self.w_center.set_text(cdir)

    def v(self) -> str:
        cdir = self.w_center.text()
        return os.path.normpath(cdir)
